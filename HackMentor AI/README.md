<div align="center">

# 🚀 HackMentor AI

### *The AI-Powered Hackathon Co-Pilot for Every Student*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

<br/>

> **"From zero idea to winning pitch — in minutes."**
> 
> HackMentor AI is not just a tool. It's your personal hackathon team: *Idea Architect. Technical Lead. Pitch Coach. Honest Judge.* — all in one.

<br/>

![HackMentor AI Banner](https://img.shields.io/badge/🏆_Hackathon_Grade_AI_Platform-6366F1?style=for-the-badge&logoColor=white)

</div>

---

## 🧠 Why HackMentor AI — And Not Any Other Tool?

> Let's be brutally honest. Most hackathon tools fail students. Here's why **HackMentor AI is different:**

| Feature | ChatGPT / Generic AI | Other Hackathon Tools | **HackMentor AI** |
|---|---|---|---|
| Hackathon-specific guidance | ❌ General answers | ⚠️ Partial | ✅ 100% scoped to hackathons |
| Explains *why* you scored what you scored | ❌ | ❌ | ✅ Full reasoning per dimension |
| Adjusts scores based on rules (team size, domain) | ❌ | ❌ | ✅ Deterministic rule engine |
| Generates executable MVP roadmaps | ❌ | ⚠️ Generic | ✅ Tech-stack aware plans |
| Structured 60-sec pitch script | ❌ | ❌ | ✅ Section-by-section |
| Built for non-technical students | ❌ | ❌ | ✅ Core design principle |
| One-click idea → full submission pipeline | ❌ | ❌ | ✅ End-to-end flow |

**Bottom line:** Other tools give you a fish. HackMentor AI teaches you to fish — *and then wins you the fishing competition.*

---

## ✨ What HackMentor AI Does

HackMentor AI is a **4-module intelligent platform** that walks any student — technical or not — from a vague problem statement to a fully formed hackathon submission.

```
💡 Idea → 📊 Score → 🏗️ Build → 🎤 Pitch
```

### Module 1 — 💡 AI Idea Generator
> *"I don't know what to build"* — No more.

Provide your domain, problem area, and team skill level. Our LLM generates **3 ranked, original hackathon ideas**, each with:
- A compelling title and tagline
- The core problem it solves
- A list of buildable features

### Module 2 — 📊 Hybrid Evaluation Engine *(Our Crown Jewel)*
> This is not just an AI score. This is an **explainable, trustworthy score**.

We combine two scoring layers:

```
Final Score = LLM Qualitative Score + Deterministic Rule Adjustments
```

**Layer 1 — LLM (Groq / LLaMA 3.3 70B):**
The model evaluates your idea like a real hackathon judge on 3 dimensions:
- `Innovation` — How novel is the solution?
- `Feasibility` — Can it be built in the timeframe?
- `Impact` — How meaningful is the outcome?

**Layer 2 — Rule Engine (Deterministic Adjustments):**
Instead of blindly trusting AI, we apply hard hackathon logic:

| Rule | Triggered By | Adjustment |
|---|---|---|
| Hardware constraint | Mentions IoT, sensors, Arduino | Feasibility −1 |
| Low innovation | Existing APIs, No-code wrappers | Innovation −1 |
| High-impact domain | Health, Agriculture, Education | Impact +1 |
| Small team risk | Team ≤ 2 members | Feasibility −1 |
| Tight timeline | Hackathon ≤ 24 hours | Feasibility −1 |
| Scalability signal | "Million users", "global", "platform" | Impact +1 |
| Advanced tech | AI/ML, Web3, Blockchain | Innovation +1 |
| Skill mismatch | Beginner + complex AI stack | Feasibility −1 |

**Why this matters:** The rule engine adds *consistency and trust*. Every adjustment is shown to the user with a clear, human-readable explanation.

**Verdict Scale:**
```
🏆 8.5+ → Hackathon Winner Potential
🚀 7.0 – 8.4 → Strong Idea — Refine & Submit
🔧 5.0 – 6.9 → Needs Work — See Suggestions
💡 < 5.0 → Pivot Recommended
```

### Module 3 — 🏗️ Solution Builder
> *"Okay I have the idea. Now what do I build?"*

Paste your idea in and instantly receive:
- **Recommended Tech Stack** — tailored to your idea
- **MVP Execution Roadmap** — step-by-step, buildable in hackathon time
- **Unique Angle** — your differentiator against every other team

### Module 4 — 🎤 Pitch Generator
> *"I built it, but I can't present it."*

Get a fully scripted 60-second elevator pitch:
- 🎣 **Hook** — grab the judges in 10 seconds
- 😡 **Problem** — make them feel the pain
- 💡 **Solution** — the aha moment
- 💻 **Demo** — what to show, what to say
- 🎤 **Ask** — confidence close

---

## 🛠️ Tech Stack

```
Backend:        Python + Flask
AI Engine:      Groq API (LLaMA 3.3 70B — Ultra-fast inference)
Scoring:        Hybrid: LLM + Deterministic Rule Engine
Frontend:       Vanilla HTML/CSS/JS (Zero framework bloat)
Styling:        Dark Glassmorphism UI (Premium UX)
```

---

## 📁 Project Structure

```
HackMentor AI/
├── app.py                  # Flask backend + API routes
├── scoring_engine.py       # 💥 Hybrid scoring logic (LLM + Rules)
├── requirements.txt        # Python dependencies
├── .env                    # Your Groq API Key (not committed)
├── static/
│   ├── css/style.css       # Premium dark glass UI
│   └── js/app.js           # SPA navigation and API calls
└── templates/
    └── index.html          # Single-page app shell
```

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/your-username/hackmentor-ai.git
cd hackmentor-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API Key
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```
> Get your free key at [console.groq.com](https://console.groq.com)

### 4. Run the server
```bash
python app.py
```

### 5. Open in browser
```
http://localhost:5000
```

---

## 🌊 Full User Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     HackMentor AI Flow                       │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
   [Enter Domain + Problem + Tech Level]
         │
         ▼
   💡 LLM Generates 3 Ranked Ideas
         │
         ▼
   [Select: "Analyze this Idea →"]   ← Auto-prefills all modules
         │
         ▼
   📊 LLM Scores Idea (Innovation, Feasibility, Impact)
         │
         ▼
   ⚙️  Rule Engine Applies Deterministic Adjustments
         │
         ▼
   🏆 Final Score + Verdict + Explanations Displayed
         │
         ▼
   🏗️  Solution Builder → Tech Stack + MVP Roadmap
         │
         ▼
   🎤  Pitch Generator → 60-Second Script
         │
         ▼
   🚀  WIN THE HACKATHON
```

---

## 🔥 Real Example

**Input:**
> Domain: Agriculture | Idea: IoT device to help farmers detect crop disease early | Team: 3 | Timeline: 36h

**LLM Output:**
```
Innovation:  7 — Novel use of IoT in precision agriculture
Feasibility: 6 — Hardware prototyping feasible in 36h
Impact:      9 — Directly addresses farmer livelihood crisis
```

**Rule Engine Adjustments:**
```
-1 Feasibility → Hardware/IoT components in hackathon constraint
+1 Impact      → Agriculture is a high-impact critical domain
```

**Final Score:**
```
Innovation:  7 ✅
Feasibility: 5 ⚠️
Impact:      10 🔥
Total:       7.3 → 🚀 Strong Idea — Refine & Submit
```

---

## 🙌 Who Is This For?

| User | Benefit |
|---|---|
| 👶 First-time hackers | Structured guidance from zero to submission |  
| 🎓 Non-technical students | No code knowledge needed to generate strong ideas |
| 🧑‍💻 Developers | Skip brainstorming, go straight to building |
| 👥 Hackathon organizers | Use it as a workshop tool for participants |
| 🏫 Colleges | Integrate it into hackathon prep workshops |

---

## 🏆 Why You Should Choose HackMentor AI

> **Other hackathon projects:**
> - Build a product. Give it to participants. Done.
>
> **HackMentor AI:**
> - Empowers participants to build *their own* products — better, faster, and with confidence.

The platform is built around one core insight:

> *The biggest barrier to hackathon success isn't talent — it's structured thinking.*

HackMentor AI gives every student — regardless of technical skill — the structured thinking of a senior engineer, a UX designer, a startup mentor, and a pitch coach, all woven together into a seamless workflow that takes under 10 minutes to complete.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

**Built with 🧠 by a team that believes every student deserves a mentor.**

*Stop guessing. Start building. Start winning.*

⭐ **Star this repo if HackMentor AI helped you!** ⭐

</div>
