import os
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
from scoring_engine import HybridScoringEngine

load_dotenv()

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("WARNING: GROQ_API_KEY is not set in .env file")

try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    client = None
    print(f"Error initializing Groq client: {e}")

scoring_engine = HybridScoringEngine()

@app.route("/")
def index():
    return render_template("index.html")

def call_llm(prompt, system_message, json_mode=False):
    if not client:
        return {"error": "Groq API key not configured."}
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            response_format={"type": "json_object"} if json_mode else None
        )
        if json_mode:
            return json.loads(completion.choices[0].message.content)
        return {"result": completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

@app.route("/api/generate-ideas", methods=["POST"])
def generate_ideas():
    data = request.json
    domain = data.get("domain", "General")
    problem = data.get("problem", "Any problem")
    tech_level = data.get("tech_level", "Beginner")
    
    system_msg = """You are an expert Hackathon Mentor. Generate 3 unique hackathon ideas based on the user's input.
    Return ONLY a JSON object with an 'ideas' array. Each idea must have: 
    'title', 'tagline', 'problem_solved', and 'core_features' (array of strings)."""
    
    prompt = f"Domain: {domain}\nProblem space: {problem}\nTeam Technical Level: {tech_level}\nProvide 3 ideas."
    
    result = call_llm(prompt, system_msg, json_mode=True)
    return jsonify(result)

@app.route("/api/build-solution", methods=["POST"])
def build_solution():
    data = request.json
    idea = data.get("idea", "")
    
    system_msg = """You are a Solutions Architect for a Hackathon team. 
    Given an idea, outline a viable solution architecture.
    Return ONLY a JSON object with: 'tech_stack' (array), 'mvp_roadmap' (array of steps), and 'unique_angle'."""
    
    prompt = f"Idea: {idea}\nProvide the solution architecture."
    
    result = call_llm(prompt, system_msg, json_mode=True)
    return jsonify(result)

@app.route("/api/generate-pitch", methods=["POST"])
def generate_pitch():
    data = request.json
    idea = data.get("idea", "")
    
    system_msg = """You are a Startup Pitch Coach. Create a 60-second elevator pitch script for the given idea.
    Return ONLY a JSON object with these keys: 'hook', 'problem', 'solution', 'demo' (what to show), 'ask'."""
    
    prompt = f"Idea: {idea}\nWrite the pitch script."
    
    result = call_llm(prompt, system_msg, json_mode=True)
    return jsonify(result)

@app.route("/api/score-idea", methods=["POST"])
def score_idea():
    data = request.json
    idea_text = data.get("idea", "")
    domain = data.get("domain", "General")
    team_size = data.get("team_size", 4)
    timeline_hours = data.get("timeline_hours", 48)
    tech_level = data.get("tech_level", "Beginner")
    
    system_msg = """You are a strict Hackathon Judge. Evaluate the given idea qualitatively.
    Score from 0-10 on Innovation, Feasibility, and Impact.
    Return ONLY a JSON object with exactly this structure:
    {
        "innovation": {"score": int, "reasoning": "string"},
        "feasibility": {"score": int, "reasoning": "string"},
        "impact": {"score": int, "reasoning": "string"}
    }"""
    
    prompt = f"Idea: {idea_text}\nDomain: {domain}\nTeam Size: {team_size}\nTimeline: {timeline_hours} hours\nTech Level: {tech_level}"
    
    llm_eval = call_llm(prompt, system_msg, json_mode=True)
    
    if "error" in llm_eval:
        return jsonify(llm_eval)
        
    final_evaluation = scoring_engine.evaluate(
        idea_text, domain, team_size, timeline_hours, tech_level, llm_eval
    )
    
    return jsonify(final_evaluation)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
