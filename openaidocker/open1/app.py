from dotenv import load_dotenv
import os
import gradio as gr
import openai

load_dotenv()
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
openai.api_key = os.getenv("OPEN_API_KEY")

def generate_output(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    assistant_response = response.choices[0].message.content
    return ("assistant", assistant_response)  # Return a tuple, not a list

prompt = "Enter a message to chat with the AI"

def chat_lm(input, history):
    history = history or []
    if input.strip() != "":  # Ensure input is not empty
        output_text = generate_output(input)
        history.append(("user", input))  # Append user input as a tuple
        history.append(output_text)  # Append the assistant's response tuple
    return history, history  # Return history correctly formatted

block = gr.Blocks()
with block:
    gr.Markdown("""<h1><center>CHAT WITH OPENAI</center></h1>""")
    chatbot = gr.Chatbot(height=550)
    message = gr.Textbox(placeholder=prompt, type="text", label="Message")
    submit = gr.Button("SEND")
    state = gr.State()
    
    submit.click(chat_lm, inputs=[message, state], outputs=[state, chatbot])


block.launch(server_name="0.0.0.0",server_port=7860,debug=True)