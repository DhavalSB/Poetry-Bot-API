import os
import google.generativeai as genai

from dotenv import main
main.load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.0-pro')


def dailyPrompt():
    response = model.generate_content("a 2 line song lyric in quotes vaguely helpful for writing poetry, no extra words")
    return response.text
