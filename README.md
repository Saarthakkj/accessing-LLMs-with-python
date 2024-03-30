
# Gradio Text Generation and Synthesis Project

This project showcases an interactive web application that leverages the power of GPT-2, a state-of-the-art language model by OpenAI, to generate text based on user input. It demonstrates the use of advanced sampling techniques such as `top_k` and `top_p` sampling to fine-tune the output, offering diverse and contextually relevant text generation. Additionally, the project integrates Google's Text-to-Speech (gTTS) technology to convert the generated text into audible speech, enhancing the user experience by providing both textual and audio output. This application also experiments with Flan-T5, showcasing the versatility in integrating different language models with Gradio for varied text generation tasks. The entire project is encapsulated within a virtual environment, ensuring a contained and reproducible setup.

## Features

- **Text Generation with GPT-2**: Utilizes GPT-2 to generate text based on user input, showcasing the model's ability to create coherent and contextually relevant narratives.
- **Advanced Sampling Techniques**: Employs `top_k`, `top_p`, and `contrastive` sampling methods to fine-tune the text generation process, offering a range of outputs from deterministic to diverse and creative text.
- **Text-to-Speech Conversion**: Integrates Google's gTTS to convert generated text into speech, providing an auditory representation of the generated content.
- **Flan-T5 Integration**: Demonstrates the capability to incorporate Flan-T5, a variant of the T5 model fine-tuned for question-answering and other tasks, into the Gradio interface.
- **Interactive Web Application**: Built with Gradio, allowing users to interact with the model through a user-friendly web interface.

## Technologies Used

- **Gradio**: For creating the web interface that interacts with the models.
- **Hugging Face's Transformers**: To access pre-trained models like GPT-2 and Flan-T5.
- **Google's Text-to-Speech (gTTS)**: For converting text output to speech.
- **Python**: The core programming language used for project development.
- **Virtual Environment**: To manage dependencies and ensure project portability.

## Getting Started

To get this project up and running on your local machine, follow these steps:

1. **Clone the Repository**

```bash
git clone https://github.com/yourgithubusername/gradio-text-synthesis.git
cd gradio-text-synthesis
```

2. **Set Up a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Application**

```bash
python final_code.py
```

Navigate to the URL provided by Gradio in your terminal to interact with the application.

## How to Use

- Enter a text prompt in the input box.
- Choose the maximum length for the generated text.
- Select the generation method: `Top_k`, `Top_p`, or `Contrastive`.
- Click "Submit" to generate the text and listen to the converted speech output.

## Learning Outcomes

This project was a comprehensive learning experience, covering several key areas:

- Understanding and implementing Hugging Face's transformer models.
- Exploring advanced text generation techniques and their applications.
- Developing interactive web applications with Gradio.
- Integrating text-to-speech technology for multimodal output.
- Managing project environments with virtual environments.
