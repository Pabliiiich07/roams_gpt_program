from transformers import pipeline
from fastapi import HTTPException
generator = pipeline('text-generation', model='gpt2')

def get_model_pipeline(model_name: str):
    try:
        if model_name is None:
            return generator
        return pipeline('text-generation', model=model_name)
    except Exception:
        raise HTTPException(status_code=400, detail=f"Error cargando el modelo {model_name}")
