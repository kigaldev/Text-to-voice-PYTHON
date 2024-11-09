# Importamos las bibliotecas necesarias
from newspaper import Article
from gtts import gTTS
import nltk
import config

# Descargar los datos de NLTK necesarios para procesamiento de texto
nltk.download('punkt')
nltk.download('stopwords')

# Función para extraer el texto de un artículo a partir de una URL
def extraer_texto(url):
    """
    Extrae el contenido de texto de un artículo desde una URL.
    Args:
        url (str): La URL del artículo a procesar.
    Returns:
        str: El texto extraído del artículo.
    """
    try:
        articulo = Article(url)
        articulo.download()
        articulo.parse()
        return articulo.text
    except Exception as e:
        print(f"Error al extraer el texto: {e}")
        return None

# Función para convertir el texto extraído en un archivo de audio en formato mp3
def texto_a_voz(texto, idioma=config.IDIOMA_VOZ, archivo=config.RUTA_ARCHIVO_AUDIO):
    """
    Convierte el texto a un archivo de audio en formato mp3 usando Google Text-to-Speech.
    Args:
        texto (str): El contenido de texto a convertir en voz.
        idioma (str): El código del idioma para la conversión (por defecto es español - 'es').
        archivo (str): La ruta donde se guardará el archivo de audio mp3.
    """
    try:
        tts = gTTS(text=texto, lang=idioma)
        tts.save(archivo)
        print(f'Archivo de audio guardado como {archivo}')
    except Exception as e:
        print(f"Error al convertir texto a voz: {e}")

# Función principal del programa que integra la extracción y conversión
def main():
    """
    Flujo principal del programa: solicita una URL, extrae el texto del artículo,
    y lo convierte en un archivo de audio en formato mp3.
    """
    url = input("Introduce la URL del artículo: ")
    texto = extraer_texto(url)
    
    if texto:
        print("Texto extraído con éxito. Iniciando la conversión a audio...")
        texto_a_voz(texto)
        print("Conversión completada.")
    else:
        print("No se pudo extraer texto de la URL. Verifique la URL e intente nuevamente.")

# Ejecuta el flujo principal si el archivo es ejecutado directamente
if __name__ == "__main__":
    main()
