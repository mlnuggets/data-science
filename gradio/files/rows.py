import gradio as gr
with gr.Blocks() as demo:
    with gr.Row():
        gr.Text()
        gr.Text()
demo.launch(quiet = True,)