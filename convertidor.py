# Importamos las bibliotecas necesarias
from newspaper import Article
from gtts import gTTS
import nltk
import re
import config
from pydub import AudioSegment

# Descargar los datos de NLTK necesarios para procesamiento de texto
nltk.download('punkt')
nltk.download('stopwords')

def limpiar_texto(texto):
    """
    Limpia el texto eliminando elementos no deseados como URLs, textos de redes sociales
    y pies de foto.
    
    Args:
        texto (str): El texto a limpiar
    Returns:
        str: Texto limpio
    """
    # Eliminar URLs
    texto = re.sub(r'http\S+|www.\S+', '', texto)
    
    # Eliminar menciones de redes sociales comunes
    texto = re.sub(r'@\w+', '', texto)
    texto = re.sub(r'#\w+', '', texto)
    
    # Eliminar texto común de redes sociales
    patrones_a_eliminar = [
        r'Síguenos en \w+',
        r'Sígueme en \w+',
        r'Follow us on \w+',
        r'Follow me on \w+',
        r'Compartir en \w+',
        r'Share on \w+',
        r'\[Foto:.*?\]',
        r'\[Imagen:.*?\]',
        r'\[Photo:.*?\]',
        r'\[Image:.*?\]',
        r'Foto:.*?\n',
        r'Imagen:.*?\n',
    ]
    
    for patron in patrones_a_eliminar:
        texto = re.sub(patron, '', texto)
    
    # Eliminar líneas que parecen pies de foto (líneas cortas entre paréntesis)
    texto = re.sub(r'\([^)]{1,50}\)\n', '', texto)
    
    # Eliminar múltiples saltos de línea
    texto = re.sub(r'\n\s*\n', '\n', texto)
    
    # Eliminar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto)
    
    return texto.strip()

def extraer_texto(url):
    """
    Extrae el contenido de texto de un artículo desde una URL y lo limpia.
    
    Args:
        url (str): La URL del artículo a procesar.
    Returns:
        str: El texto extraído y limpio del artículo.
    """
    try:
        articulo = Article(url)
        articulo.download()
        articulo.parse()
        
        # Extraer y limpiar el texto
        texto_limpio = limpiar_texto(articulo.text)
        return texto_limpio
    except Exception as e:
        print(f"Error al extraer el texto: {e}")
        return None

def texto_a_voz(texto, idioma=config.IDIOMA_VOZ, archivo=config.RUTA_ARCHIVO_AUDIO):
    """
    Convierte el texto a un archivo de audio en formato mp3 usando Google Text-to-Speech
    y ajusta la velocidad y el tono.
    
    Args:
        texto (str): El contenido de texto a convertir en voz.
        idioma (str): El código del idioma para la conversión.
        archivo (str): La ruta donde se guardará el archivo de audio mp3.
    """
    try:
        # Generar el audio con gTTS
        archivo_temporal = "temp_audio.mp3"
        tts = gTTS(text=texto, lang=idioma)
        tts.save(archivo_temporal)
        
        # Cargar el audio con pydub
        audio = AudioSegment.from_mp3(archivo_temporal)
        
        # Ajustar la velocidad (1.5x)
        audio_modificado = audio._spawn(audio.raw_data, overrides={
            "frame_rate": int(audio.frame_rate * 1.5)
        }).set_frame_rate(audio.frame_rate)
        
        # Bajar el tono (pitch) para una voz más adulta
        # Los valores negativos bajan el tono, positivos lo suben
        # -2 suele dar un buen resultado para voz adulta
        octaves = -0.6  # Prueba con valores entre -1 y -3
        new_sample_rate = int(audio_modificado.frame_rate * (2.0 ** octaves))
        
        # Aplicar el cambio de tono manteniendo la duración
        audio_modificado = audio_modificado._spawn(audio_modificado.raw_data, overrides={
            "frame_rate": new_sample_rate
        })
        audio_modificado = audio_modificado.set_frame_rate(audio.frame_rate)
        
        # Guardar el resultado final
        audio_modificado.export(archivo, format="mp3")
        print(f'Archivo de audio guardado como {archivo}')
        
        # Eliminar el archivo temporal
        import os
        os.remove(archivo_temporal)
        
    except Exception as e:
        print(f"Error al convertir texto a voz: {e}")

def main():
    """
    Flujo principal del programa: solicita una URL, extrae el texto del artículo,
    lo limpia y lo convierte en un archivo de audio en formato mp3.
    """
    url = input("Introduce la URL del artículo: ")
    texto = extraer_texto(url)
    
    if texto:
        print("Texto extraído y limpiado con éxito. Iniciando la conversión a audio...")
        texto_a_voz(texto)
        print("Conversión completada.")
    else:
        print("No se pudo extraer texto de la URL. Verifique la URL e intente nuevamente.")

if __name__ == "__main__":
    main()