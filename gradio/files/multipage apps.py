#define your first application
#!pip install gradio
import gradio as gr
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import log
def user_greeting(name):
    return "Hi! " + name + " Welcome to your multi-page application!😎"
#app 1
app =  gr.Interface(fn = user_greeting, inputs="text", outputs="text", examples = ["Zenith", "Antoinne", "Amelia", "Johanna"])

#define your second application
def gdp_change(r, year, country, smoothen):
    years = ['1850', '1900', '1950', '2000', '2050']
    m = years.index(year)
    start_day = 10* m
    final_day = 10* (m + 1)
    x = np.arange(start_day, final_day + 1)
    pop_count = {"USA": 350, "Canada": 40, "Mexico": 300, "UK": 120}
    if smoothen:
        r = log(r)
    df = pd.DataFrame({'day': x})
    df[country] = ( x ** (r) * (pop_count[country] + 1))
    fig = plt.figure()
    sns.lineplot(x = df['day'], y = df[country].to_numpy())
    plt.title("GDP in " + year)
    plt.ylabel("GDP (Millions)")
    plt.xlabel("Population Change since 1800s")
    plt.grid()
    return fig

inputs = [
        gr.Slider(1, 4, 3.2, label="R"),
        gr.Dropdown(['1850', '1900', '1950', '2000', '2050'], label="year"),
        gr.Radio(["USA", "Canada", "Mexico", "UK"], label="Countries", ),
        gr.Checkbox(label="Log of GDP Growth Rate?"),
    ]
outputs = gr.Plot()
#app 2
app2 = gr.Interface(fn=gdp_change, inputs=inputs, outputs=outputs)
#combine to create a multipage app
demo = gr.TabbedInterface([app, app2], ["Welcome page", "Visualization page"])

if __name__ == "__main__":
    demo.launch(quiet = True,)