from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model_config import translate_text

# Inicializar la app FastAPI
app = FastAPI()

# Modelo de datos para solicitudes de traducción
class TranslationRequest(BaseModel):
    text: str

@app.post("/translate/es-en/")
def translate_es_to_en(request: TranslationRequest):
    """
    Traduce texto de español a inglés.
    """
    try:
        translated_text = translate_text(request.text, "es-en")
        return {"input_text": request.text, "translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error durante la traducción: {str(e)}")

@app.post("/translate/en-es/")
def translate_en_to_es(request: TranslationRequest):
    """
    Traduce texto de inglés a español.
    """
    try:
        translated_text = translate_text(request.text, "en-es")
        return {"input_text": request.text, "translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error durante la traducción: {str(e)}")

@app.get("/test-translation/")
def test_translation():
    """
    Endpoint para probar la traducción directamente desde el servidor.
    """
    try:
        # Prueba de español a inglés
        test_text_es = "nos atraparon por que Carlos solto los frijoles en el interrogatorio"
        result_es_en = translate_text(test_text_es, "es-en")  # Dirección de traducción especificada

        # Prueba de inglés a español
        test_text_en = "we got caught because Carlos released the beans during the interrogation."
        result_en_es = translate_text(test_text_en, "en-es")  # Dirección de traducción especificada

        return {
            "input_text_es": test_text_es,
            "translated_text_es_en": result_es_en,
            "input_text_en": test_text_en,
            "translated_text_en_es": result_en_es,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error durante la prueba de traducción: {str(e)}")
