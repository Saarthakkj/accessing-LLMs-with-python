from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import gradio as gr

model = TFAutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

def text_gen(input_string, max_length):

    input_ids = tokenizer(input_string ,  return_tensors="pt").input_ids 
    return model.generate(input_ids)

def to_gradio(): 
    demo = gr.Interface(
        fn=text_gen,
        inputs=["text", gr.Slider(0, 250)],
        outputs="text",
        title="Text Generation with Flan T5 Language Model",
        description=
        "This model takes some input text, and generates new text from Flan T5.")
    demo.launch(debug=True, share=True)

if __name__ == "__main__":
    to_gradio()