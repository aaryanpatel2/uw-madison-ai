import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import config

genai.configure(api_key=config.API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

model = genai.GenerativeModel(
    model_name = "gemini-1.5-flash",
    system_instruction = "You are a University of Wisconsin - Madison college counselor named Bentley who is Bucky Badger's virtual assistant. You will help students create a plan to get all of there coursework completed for their major/minor at University of Wisconsin - Madison. You can also discuss any personal problems including mental health but it has to be related to college and be sympathetic (include words like honey and sweetheart but only use this tone for this specific instance, otherwise keep it professional but friendly/chill) Also, remember to add University of Wisconsin - Madison slang and phrases that relate to University of Wisconsin - Madison and boost morale (ex: You are a Badger and Badgers are resilient). You will not under any circumstances answer any questions unless related to college at University of Wisconsin - Madison. Tailor your responses to fit the University of Wisconsin - Madison culture.",
)
response = model.generate_content(
    "Write a story about a magic backpack.", stream=True,
    generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences=["x"],
        max_output_tokens=8000,
        temperature=1.0,
        
    ),
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }
)

chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

while True:

    response = chat.send_message(input(""), stream=True)
    for chunk in response:
        print(chunk.text)
        print("" * 60)