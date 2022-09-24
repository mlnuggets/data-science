import gradio as gr

import gradio as gr
def update_textbox(choice):
  if choice == "short":
      return gr.Textbox.update(lines=1, visible=True)
  elif choice == "long":
      return gr.Textbox.update(lines=6, visible=True)
  else:
      return gr.Textbox.update(visible=False)
gr.Interface(
  update_textbox,
  gr.Radio(
      ["short", "long", "No message"], label="What kind of message would you like to send?"
  ),
  gr.Textbox(lines=2),
  live=True,
).launch(quiet = True,)