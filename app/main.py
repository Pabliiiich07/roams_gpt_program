from fastapi import FastAPI, HTTPException
from transformers import set_seed
from app.models import PromptRequest
from app.config import get_model_pipeline

app = FastAPI()

@app.post("/generate/")
async def generate_text(request: PromptRequest):
    try:
        model_pipeline = get_model_pipeline(request.model)
        set_seed(42)

        response = model_pipeline(
            request.prompt, 
            max_length=request.max_length, 
            num_return_sequences=request.num_return_sequences
        )        
        return {"prompt": request.prompt, "response": response}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al procesar la solicitud")
