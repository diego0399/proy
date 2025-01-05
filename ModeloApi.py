import speech_recognition as sr
import pyttsx3
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Configuración del modelo de traducción
model_path = "C:\\data\\en-es"  # Ruta local al modelo
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)



# Función de traducción
def translate_text(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# Configuración de reconocimiento y síntesis de voz
def recognize_translate_and_speak():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.8  # Pausa natural para detectar frases completas
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        # Convertimos el audio a texto completo
        text = recognizer.recognize_google(audio, language="en-US")
        print("Texto reconocido:", text)
        
        # Revisa si el usuario dice "finalizar" para detener el programa
        if "stop" in text.lower():
            print("Se ha detectado la palabra 'finalizar'. Terminando el programa.")
            engine.say("Hasta luego.")
            engine.runAndWait()
            return False  # Señal para terminar el bucle
        

        # Traducción del texto reconocido
        translated_text = translate_text(text)
        print("Texto traducido:", translated_text)
        
        # Convertimos el texto traducido a voz
        engine.say(translated_text)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("No se entendió el audio.")
        engine.say("No se entendió el audio.")
        engine.runAndWait()
    except sr.RequestError:
        print("Error con el servicio de reconocimiento de voz.")
        engine.say("Error con el servicio de reconocimiento de voz.")
        engine.runAndWait()

    return True  # Continua el bucle

# Bucle principal que termina cuando se detecta "finalizar"
while True:
    if not recognize_translate_and_speak():
        break
