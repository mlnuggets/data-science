import gradio as gr

blocks = gr.Blocks()

with blocks as demo:
    subject = gr.Radio(["Analyse", "Explore", "Learn"])
    verb = gr.Radio(["GDP Change", "Population Growth", "Big Data"])
    object = gr.Textbox(placeholder="region")

    with gr.Row():
        btn = gr.Button("Create sentence.")
        reverse_btn = gr.Button("Reverse sentence.")

    def sentence_maker(w1, w2, w3):
        return f"{w1} {w2} in {w3}"

    output1 = gr.Textbox(label="output 1")
    output2 = gr.Textbox(label="verb reversed")

    btn.click(sentence_maker, [subject, verb, object], output1)
    #custom JS to reverse the sentense
    reverse_btn.click(None, [subject, verb, object], output2, _js="(s, v, o) => o + ' ' + v + ' ' + s")

demo.launch(quiet = True,)