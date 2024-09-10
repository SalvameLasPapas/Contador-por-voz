import speech_recognition as sr
from collections import Counter

# Inicializar el reconocimiento de voz
r = sr.Recognizer()

# Inicializar los contadores
positive_count = 0
neutral_count = 0
negative_count = 0

while True:
    try:
        # Escuchar el audio desde el micrófono
        with sr.Microphone() as source:
            print("Di algo...")
            audio = r.listen(source)

        # Transcribir el audio a texto
        text = r.recognize_google(audio, language="es-ES")
        print(f"Dijiste: {text}")

        # Actualizar los contadores
        if text.lower() == "positivo":
            positive_count += 1
        elif text.lower() == "neutral":
            neutral_count += 1
        elif text.lower() == "negativo":
            negative_count += 1

        # Mostrar la tabla de recuento
        print("\nRecuento de categorías:")
        print(f"Positivo: {positive_count}")
        print(f"Neutral: {neutral_count}")
        print(f"Negativo: {negative_count}")

    except sr.UnknownValueError:
        print("No pude entender lo que dijiste")
    except sr.RequestError as e:
        print(f"Error al solicitar resultados de Google Speech Recognition; {e}")
