# 🎧 Artículo a Audio - Conversor de Texto a Voz

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-stable-success.svg)

## 🚀 Descripción

Convierte artículos web en archivos de audio MP3 de forma instantánea. Este proyecto transforma el contenido de texto de cualquier URL en un archivo de audio reproducible, permitiéndote consumir contenido mientras realizas otras actividades. El programa incluye limpieza inteligente de texto y optimización de voz para una experiencia de escucha natural y eficiente.

### ⚡ Desarrollo Rápido con IA
Este proyecto fue desarrollado en menos de 1 hora utilizando:
- 🤖 ChatGPT 4.0 Omni
- 🧠 Claude 3.5 Sonnet

La combinación de estas herramientas de IA permitió un desarrollo ágil y eficiente, resultando en un programa totalmente funcional y probado.

## ✨ Características

| Característica | Descripción |
|----------------|-------------|
| 🎯 Conversión Texto a Voz | Genera archivos MP3 a partir de artículos web |
| 📝 Extracción Inteligente | Obtiene automáticamente el contenido relevante de las URLs |
| 🌍 Multilenguaje | Soporte para múltiples idiomas gracias a gTTS |
| 🧹 Limpieza Avanzada | Elimina automáticamente enlaces, pies de foto y contenido irrelevante |
| ⚡ Audio Optimizado | Velocidad de reproducción aumentada a 1.5x para una escucha más eficiente |
| 🎤 Voz Natural | Tono de voz ajustado para una experiencia de escucha más agradable |

## 🛠️ Tecnologías

- **📰 newspaper3k**: Extracción y procesamiento de artículos web
- **🔤 NLTK**: Procesamiento avanzado de lenguaje natural
- **🔊 gTTS**: Conversión de texto a voz utilizando la API de Google
- **🎵 pydub**: Manipulación y optimización de audio
- **🧰 FFmpeg**: Procesamiento de audio (dependencia externa)

## 📦 Instalación

### Prerrequisitos
- Python 3.x
- pip (gestor de paquetes de Python)
- FFmpeg (necesario para el procesamiento de audio)

### Instalación de FFmpeg
- **Windows**: 
  ```powershell
  # Usando Chocolatey
  choco install ffmpeg

  # O mediante PowerShell (alternativa sin Chocolatey)
  Set-ExecutionPolicy Bypass -Scope Process -Force
  [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
  iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

## 📦 Instalación

### Prerrequisitos
- Python 3.x
- pip (gestor de paquetes de Python)
- FFmpeg (necesario para el procesamiento de audio)

### Instalación de FFmpeg
- **Windows**: 
  1. Descarga FFmpeg desde la [web oficial](https://ffmpeg.org/download.html)
  2. Añade FFmpeg a las variables de entorno del sistema
- **Linux**: 
  ```bash
  sudo apt-get install ffmpeg

### Pasos de Instalación

1. Clona el repositorio:

git clone https://github.com/kigaldev/Text-to-voice-PYTHON
cd texto-a-voz

2. Instala todas las dependencias:

pip install -r requirements.txt

🚀 Uso

- Ejecuta el script principal:

python convertidor.py

Ingresa la URL del artículo cuando se te solicite

¡Espera a que se genere tu archivo de audio optimizado!

🔍 Características de Limpieza

El programa automáticamente:

Elimina URLs y enlaces
Remueve menciones de redes sociales
Limpia pies de foto y textos entre paréntesis
Elimina espacios y saltos de línea innecesarios
Optimiza el texto para una mejor experiencia de audio

⚙️ Optimización de Audio

Velocidad de reproducción aumentada a 1.5x
Mantiene la calidad del tono de voz
Formato MP3 optimizado

📝 Nota Importante
Asegúrate de tener FFmpeg instalado correctamente en tu sistema antes de ejecutar el programa. Puedes verificar la instalación ejecutando:
bashCopyffmpeg -version

🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.

📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.



Los principales cambios en el README incluyen:
1. Nueva sección sobre la instalación de FFmpeg
2. Información sobre las características de limpieza de texto
3. Detalles sobre la optimización del audio
4. Actualización de la sección de tecnologías
5. Actualización de los prerrequisitos
6. Simplificación del proceso de instalación usando requirements.txt

