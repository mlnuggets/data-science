import gradio as gr
with gr.Blocks() as demo:
    with gr.Accordion("Display Details"):
        gr.Markdown("Machine Learning and Big Data")
demo.launch(quiet = True,)