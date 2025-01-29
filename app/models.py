from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="El prompt no puede estar vacío")
    model: str = Field(..., min_length=1, description="El modelo no puede estar vacío")
    max_length: int = Field(ge=1, le=100, default=100, description="Debe ser la longitud de cada respuesta.")
    num_return_sequences: int = Field(ge=1, le=10, default=1, description="Debe ser el número de respuestas que deseas recibir por parte del modelo")
