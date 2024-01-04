import gradio as gr
import random
import time
import consume_api_rest
from consume_api_rest import Empresa

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def bot(history):
        listado = consume_api_rest.getListadoEmpresasPorPais(str(history[0][0]));

        mensaje = ''
        for empresa in listado:
            mensaje = mensaje + empresa.__str__()
        bot_message = mensaje
        history[-1][1] = bot_message
        time.sleep(1)
        return history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch(share=True)
