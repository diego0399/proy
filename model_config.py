from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Rutas de los modelos locales
model_paths = {
    "es-en": "C:\\data\\es-en",  # Modelo español a inglés
    "en-es": "C:\\data\\en-es",  # Modelo inglés a español
}

# Cargar modelos y tokenizadores
models = {
    "es-en": AutoModelForSeq2SeqLM.from_pretrained(model_paths["es-en"]),
    "en-es": AutoModelForSeq2SeqLM.from_pretrained(model_paths["en-es"]),
}

tokenizers = {
    "es-en": AutoTokenizer.from_pretrained(model_paths["es-en"]),
    "en-es": AutoTokenizer.from_pretrained(model_paths["en-es"]),
}

def translate_text(text: str, model_key: str) -> str:
    """
    Traduce texto basado en la clave del modelo especificada (es-en o en-es).
    """
    # Asegurarse de que el modelo_key sea válido
    if model_key not in models:
        raise ValueError(f"Modelo no válido: {model_key}")

    # Configurar el modelo y tokenizador
    model = models[model_key]
    tokenizer = tokenizers[model_key]

    # Preparar el texto para el modelo
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    print(f"Texto traducido ({model_key}): {translated_text}")
    return translated_text
