# Archivo de configuración - config.py

# Configuración de idioma para la conversión de texto a voz (utilizado en gTTS)
IDIOMA_VOZ = 'es'  # Código del idioma, por ejemplo, 'es' para español, 'en' para inglés

# Ruta de almacenamiento para los archivos de audio generados
RUTA_ARCHIVO_AUDIO = 'audio/articulo.mp3'

# Configuración adicional de newspaper3k
# Definir la cantidad máxima de tiempo (en segundos) para esperar al descargar el artículo
TIEMPO_MAXIMO_DESCARGA = 10  # Tiempo en segundos para la descarga del artículo

# Configuración de procesamiento de texto
# Especificar si se desea utilizar procesamiento de lenguaje natural (NLTK) para limpiar el texto
UTILIZAR_PROCESAMIENTO_NLTK = True
