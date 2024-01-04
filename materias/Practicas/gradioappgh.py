import consume_api_rest
import openai
import gradio as gr
from gradio import Interface

from consume_api_rest import Usuario
from consume_api_rest import Vacante

openai.api_key = ""

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


def respuesta_generica(respuestas: list):
    respuestas.append("1. Listar vacantes de mi país de origen.")
    respuestas.append("2. Listar todas las vacantes.")
    respuestas.append("3. Listar vacantes dado el país.")


def generar_html_vacante(vacante: Vacante = None) -> str:
    return "<p><b>Puesto:</b>" + vacante.puesto + "</p>" + "<p><b>Área:</b>" + vacante.area + "</p>" + \
        "<p><b>Descripción:</b>" + vacante.descripcionPuesto + "</p>" + \
        "<a href='" + vacante.url + "' target='_blank'>Visualizar</a><hr/>"


def generador_respuesta(prompt, nombrePais: str, state):
    usuario = state[0]
    activar_respuesta = True
    respuestas = []
    html = None

    try:
        if usuario is None:
            html = "<a href='https://verempleos.com/inicio.aspx' target='_blank'>Ir a la Página Principal</a>"
            usuario = consume_api_rest.getUsuario(prompt)
            if usuario is not None and usuario.idPais != 0:
                html = ""
                state[0] = usuario
                respuestas.append(
                    "Bienvenido {} al ChatBot de VerEmpleos.".format(usuario.nombre))
            else:
                usuario = None
                activar_respuesta = False
                respuestas.append('El usuario ingresado no esta registrado.')
                respuestas.append(
                    'Revise la salida para encontrar la URL de registro.')
        elif prompt == '1':
            listado = consume_api_rest.getVacantesPorPais(str(usuario.idPais))

            html = "<div>"
            for p in listado:
                html = html + generar_html_vacante(vacante=p)
            html = html + "</div>"
        elif prompt == '2':
            listado = consume_api_rest.getTodasVacantes()

            html = "<div>"
            for p in listado:
                html = html + generar_html_vacante(vacante=p)
            html = html + "</div>"
        elif prompt == '3':
            if nombrePais is None or len(nombrePais) == 0:
                activar_respuesta = False
                respuestas.append(
                    "Debe seleccionar un país en el panel para poder revisar.")
            else:
                listado = consume_api_rest.getVacantesDadoNombrePais(
                    nombrePais=nombrePais)

                html = "<div>"
                for p in listado:
                    html = html + generar_html_vacante(vacante=p)
                html = html + "</div>"
        else:
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
            respuestas.append(response.choices[0].text)
            activar_respuesta = False
    except Exception as ex:
        print(ex)
        html=""
        respuestas.append("Se ha generado un error. Pruebe a intentar nuevamente.")

    if activar_respuesta:
        respuesta_generica(respuestas=respuestas)

    return html, respuestas


def controlador_chat(input, state, nombrePais):
    if len(state) == 0:
        state.append(None)
        state.append([])

    historial = state[1]

    primera_linea = True
    html, outputs = generador_respuesta(input, nombrePais, state)

    for o in outputs:
        if primera_linea:
            historial = historial + [(input, o)]
            primera_linea = False
        else:
            historial = historial + [(None, o)]

    state[1] = historial

    return historial, state, html, ''


with gr.Blocks(gr.themes.Default(primary_hue="emerald", secondary_hue="emerald", neutral_hue="purple")) as block:
    gr.Markdown("""<h1><center>JOBY CHAT</center></h1>""")
    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(value=[(
                None, "Bienvenido a JOBY de VerEmpleos. Para iniciar es necesario el ingreso de su nombre de usuario para una interacción personalizada.")]).style(height=390)
        with gr.Column(scale=1):
            paises_radio = gr.Radio(choices=consume_api_rest.getTodosNombrePais(),
                                    label="Países", info="Selecciona para buscar por país.")
    message = gr.Textbox(label="Ingrese su consulta aquí.")
    state = gr.State([])
    with gr.Accordion('Información Adicional:'):
        html = gr.HTML()

    submit = gr.Button("Enviar")
    submit.click(controlador_chat, inputs=[message, state, paises_radio], outputs=[
                 chatbot, state, html, message])

# darwinvinicio14_11@hotmail.com
block.launch(server_name="0.0.0.0")
