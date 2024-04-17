from openai import OpenAI

import os
import openai
import gradio as gr

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def generate_text_gpt(input_string, max_length):
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=input_string,
                                      temperature=0,
                                      max_tokens=max_length,
                                      top_p=1,
                                      frequency_penalty=0,
                                      presence_penalty=0)
  answer = response.choices[0]['text']
  return (answer)

def to_gradio(): 
    demo = gr.Interface(
        fn=generate_text_gpt,
        inputs=["text", gr.Slider(0, 250)],
        outputs="text",
        title="Text Generation with OPENAI API's key",
        description=
        "This model takes some input text, and generates new text from Chatgpt-4")
    demo.launch(debug=True, share=True)

if __name__ == "__main__":
    to_gradio()