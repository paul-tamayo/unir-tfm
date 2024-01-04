mport os
import openai
import gradio as gr
from gradio import Interface
#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = ""

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Cómo puedo ayudarte, escribe tu pregunta, por favor "
# Crear la interfaz de Gradio con colores personalizados


def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


#block = gr.Blocks()


with gr.Blocks(theme=gr.themes.Default(primary_hue="emerald", secondary_hue="emerald",neutral_hue="purple")) as demo:
    gr.Markdown("""<h1><center>JOBOT CHAT VER EMPLEOS</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("Enviar")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

demo.launch(debug = True,share=True)
