from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.environ['groq_API_KEY']
client=Groq()
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "is origin of morality prudential?",
        }
    ],
    model="llama-3.3-70b-versatile",
    stream=False,
    temperature=1.5
)

print(chat_completion.choices[0].message.content)
