import os
import google.generativeai as genai

from dotenv import main
main.load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.0-pro')

generation_config=genai.types.GenerationConfig(
        candidate_count=1,
        max_output_tokens=45,
        temperature=0.72
)

def dailyPrompt():
#Legacy    response = model.generate_content("a 2 line song lyric in quotes vaguely helpful for writing poetry, no extra words")

    response = model.generate_content(
        contents = "write a short creative prompt in quotes, no extra words",
        generation_config = generation_config
    )
    return response.text
