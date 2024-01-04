import gradio as gr
import openai
import os

# Configurar la API de OpenAI
openai.api_key = os.environ["#apideopenai"]

# Crear el modelo de ChatGPT
model_engine = "text-davinci-002"
model_prompt = "Conversa conmigo!"
chatgpt = openai.CompletionV1(
    engine=model_engine,
    prompt=model_prompt,
    temperature=0.7,
)

# Crear la función del chatbot
def chatbot(input_text):
    # Completar la entrada del usuario utilizando ChatGPT
    response = chatgpt.create(
        prompt=input_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

# Crear la interfaz de usuario del chatbot
chatbot_interface = gr.Interface(
    fn=chatbot,
    inputs=gr.inputs.Textbox(label="Escribe algo..."),
    outputs=gr.outputs.Textbox(label="Respuesta"),
    title="Chatbot con Gradio y ChatGPT",
    theme="default",
    layout="vertical",
    analytics_enabled=False,
)

# Ejecutar la interfaz de usuario del chatbot
chatbot_interface.launch()
