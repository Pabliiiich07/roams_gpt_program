# roams_gpt_program

Este proyecto permite generar texto con un modelo GPT-2 a partir de un prompt cualquiera a través de peticiones POST.

# Primero tendremos que clonar el repositorio a través del comando:
- git clone https://github.com/Pabliiiich07/roams_gpt_program.git

Para ejecutar el programa seguiremos los siguientes pasos:

# 1. Preparar el entorno virtual e instalar las dependencias:
    - python -m venv venv (Crear entorno virtual)
    - .\venv\Scripts\Activate (Activar entorno virtual)
    - pip install -r requirements.txt (Instalar dependencias)

# 2. Ejecutar FastAPI a través de main.py:
    - uvicorn app.main:app --reload (Inicializa la API)

# 3. Abrir Postman y realizar peticiones POST (Adjunto ejemplo):
    - http://127.0.0.1:8000/generate/ (Endpoint)
    - { "prompt": "Once upon a time", "model": "gpt2", "max_length": 25, "num_return_sequences": 5 } (Body, poner en JSON RAW)

# 4. Ahora si todo ha ido bien recibiremos en el objeto response el prompt que hemos introducido junto a las respuestas del modelo solicitado.
    - {
    "prompt": "Once upon a time",
    "response": [
        {
            "generated_text": "Once upon a time, what seems to you that the lightest person could make a living being with that power, you felt"
        },
        {
            "generated_text": "Once upon a time, a black hole created by a black hole's mass would generate a massive tidal field and create gravity."
        },
        {
            "generated_text": "Once upon a time, the men would get together and say they'd like to know as much as we did. He'd"
        },
        {
            "generated_text": "Once upon a time, one's mind was occupied in the present. However, now the situation was different. The world was"
        },
        {
            "generated_text": "Once upon a time she had once again become her own mother.\n\nWith her young sister still reeling from their death she"
        }
    ]
}

