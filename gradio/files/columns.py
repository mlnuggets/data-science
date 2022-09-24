import gradio as gr
with gr.Blocks() as demo:
    with gr.Column(scale=2):
         btn1 = gr.Button("Button 1")
         btn2 = gr.Button("Button 2")
    with gr.Column(scale=1):
         text1 = gr.Textbox()
         text2 = gr.Textbox()
demo.launch(quiet = True,)