# 🏡 NestAI

> *[Tagline Coming Soon]*

### AI-powered Multi-Agent Relocation Intelligence Platform

Relocating isn't just about finding a house.

It's about choosing the neighborhood where you'll build your future.

NestAI brings together specialized AI agents that collaboratively evaluate housing, education, healthcare, commute, and affordability to help individuals and families make confident relocation decisions.

Built with **Google Agent Development Kit (ADK)**, **Gemini**, **FastAPI**, **React**, and **Model Context Protocol (MCP)**.

---

## 🌍 Why NestAI?

Moving to a new city often means spending hours researching:

- 🏠 Housing prices
- 🎓 Schools
- 🏥 Hospitals
- 🚇 Public transport
- 💰 Cost of living
- 🌳 Neighborhood quality

This information is scattered across dozens of websites.

NestAI transforms this fragmented research into one intelligent, explainable workflow powered by specialized AI agents.

Instead of asking one AI model to do everything, NestAI delegates responsibilities across multiple domain experts, allowing every aspect of relocation to be analyzed independently before generating a unified recommendation.

---

# ✨ Features

## 🤖 Multi-Agent Intelligence

Rather than relying on one large prompt, NestAI coordinates multiple specialist agents using Google ADK.

Each agent focuses exclusively on its own domain.

- 🏠 Housing
- 🎓 Education
- 🏥 Healthcare
- 🚗 Commute
- 💰 Budget

This produces more modular, transparent and explainable recommendations.

---

## 🧠 Coordinator Agent

A central Coordinator Agent:

- Collects user preferences
- Validates relocation requirements
- Delegates work to specialists
- Aggregates their outputs
- Produces the final recommendation

---

## 📊 LifeScore Engine

NestAI introduces the **LifeScore**, a unified quality-of-life score that combines multiple specialist evaluations into one easy-to-understand recommendation.

Instead of forcing users to compare dozens of metrics manually, LifeScore summarizes overall neighborhood suitability while preserving transparency.

---

## 🔌 Model Context Protocol (MCP)

NestAI integrates MCP servers to provide grounded information rather than relying solely on model knowledge.

Current integrations include:

- 🌐 Browser MCP
  - Housing research
  - School information

- 🗺 Google Maps MCP
  - Commute estimation
  - Hospital proximity
  - Distance calculations

---

## 🖥 Modern Dashboard

The React frontend provides a clean interface for visualizing relocation recommendations.

Features include:

- Dark mode
- Candidate neighborhood cards
- LifeScore display
- Recommendation section
- Relocation checklist
- Agent status visualization

---

# 🏗 System Architecture

```text
                    User
                      │
                      ▼
            Coordinator Agent
                      │
     ┌────────┬────────┬────────┬────────┬────────┐
     ▼        ▼        ▼        ▼        ▼
 Housing   School  Healthcare Commute  Budget
     │        │        │        │        │
     └────────┴────────┴────────┴────────┴────────┘
                      │
               LifeScore Engine
                      │
                      ▼
         Relocation Recommendation
                      │
                      ▼
             React Dashboard
```

---

# 🔄 Workflow

1. User provides relocation preferences.

2. Coordinator validates the request.

3. Housing Agent identifies candidate neighborhoods.

4. Specialist agents evaluate:

   - Housing
   - Schools
   - Healthcare
   - Commute
   - Budget

5. LifeScore Engine combines the evaluations.

6. Final recommendations are displayed to the user.

---

# 🛠 Technology Stack

## AI

- Google Agent Development Kit (ADK)
- Gemini
- Multi-Agent Orchestration

## Backend

- Python
- FastAPI
- Pydantic

## Frontend

- React
- Vite
- CSS

## External Integrations

- Browser MCP
- Google Maps MCP

## Development

- uv
- Git
- GitHub

---

# 📂 Project Structure

```
nestai/
│
├── app/
│   ├── specialists/
│   ├── engines/
│   ├── mcp/
│   ├── skills/
│   ├── models.py
│   ├── fast_api_app.py
│   └── agent.py
│
├── frontend/
│
├── tests/
│
├── pyproject.toml
├── Dockerfile
├── main.py
└── README.md
```

---

# 🚀 Running Locally

## Clone

```bash
git clone https://github.com/ojaswedhane-dev/nestai.git
cd nestai
```

## Environment

```bash
cp .env.example .env
```

Add your Gemini API Key.

```
GEMINI_API_KEY=YOUR_KEY
```

---

## Backend

```bash
agents-cli install
uv run python main.py
```

---

## Frontend

```bash
cd frontend
npm install
npm run dev
```

---

# 📸 Screenshots

> *(Add screenshots before submission.)*

- Dashboard
- Dark Mode
- ADK Agent Trace
- Candidate Neighborhoods
- Final Recommendation

---

# 🚀 Future Roadmap

- Connect the React dashboard directly to the ADK backend
- Interactive map visualizations
- User-adjustable LifeScore weighting
- Crime and environmental quality metrics
- Real-time relocation comparisons
- Property listing integrations

---

# 👨‍💻 Developer

Built by **Ojas Wedhane**

Google × Kaggle Vibe Coding Capstone Project

---

# 📄 License

Licensed under the Apache License 2.0.