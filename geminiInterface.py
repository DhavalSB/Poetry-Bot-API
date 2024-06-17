import os
import google.generativeai as genai

from dotenv import main
main.load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro')

generation_config=genai.types.GenerationConfig(
        candidate_count=1,
        temperature=1.0
)

def dailyPrompt():
#Legacy    response = model.generate_content("a 2 line song lyric in quotes vaguely helpful for writing poetry, no extra words")

    response = model.generate_content(
#        contents = "write something about 20 words in length in quotes",
        contents = "generate a poetry prompt in quotes only, but make it different",
        generation_config = generation_config
    )
    return response.text
