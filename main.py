from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

app = FastAPI(title="Sim Sage API")

# Allow CORS for testing and integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to Sim Sage – Simulation-First Mentorship API"}

# /mentor route for tone-filtered guidance
@app.post("/mentor")
def mentor_response(prompt: str, role: str = "standard_user"):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    full_prompt = f"You are Sim Sage, a simulation-first digital mentor using First-Person Mentor Voice™. Your user is a {role}. Answer the following with psychologically safe guidance:\n\n{prompt}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are Sim Sage, a simulation mentorship assistant."},
                {"role": "user", "content": full_prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return {"response": response.choices[0].message["content"].strip()}
    except Exception as e:
        return {"error": str(e)}
