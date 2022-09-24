import gradio as gr

gdps = []

def track_gdp(gdp):
    gdps.append(gdp)
    top_gdps = sorted(gdps, reverse=True)[:3]
    return top_gdps

demo = gr.Interface(
    track_gdp, 
    gr.Number(label="gdp"), 
    gr.JSON(label="Top gdps")
)
demo.launch(quiet = True,)