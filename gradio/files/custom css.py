import gradio as gr
with gr.Blocks(css=".gradio-container {background-color: grey}") as demo:
    with gr.Tab(label = "Button tab"):
         btn1 = gr.Button("Button 1")
         btn2 = gr.Button("Button 2")
    with gr.Tab(label = "Textbox tab"):
         text1 = gr.Textbox()
         text2 = gr.Textbox()
demo.launch(quiet = True,)
