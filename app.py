import os
import gradio.interface
from groq import Groq
from dotenv import load_dotenv
import gradio
load_dotenv('C:/Programming/api/key.env')

def get_grok_response(prompt):
    client=Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )   
    chat_completion=client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":"You are highly educated computer scientist, eli5 me whatever i ask"
            },
            {
                "role":"user",
                "content":prompt
            }
        ],
        model="llama-3.3-70b-versatile",

    )
    return chat_completion.choices[0].message.content
def grok_chat(message):
    try:
       response=get_grok_response(message)
       return response
    except Exception as e:
        return f"Error:{str(e)}"

    

demo=gradio.Interface(
    fn=get_grok_response,
    inputs=gradio.Textbox(lines=4,placeholder='enter prompt'),
    outputs=gradio.Textbox(label='Groq says...'),
    title="Groq AI",
    description="Chat with llama 3",
)

if __name__=="__main__":
    demo.launch()