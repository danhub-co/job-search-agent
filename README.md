# 🤖 Agentic AI Job Search System

Complete autonomous job search system with AI-powered agents for finding, applying, and tracking job opportunities.

## 🎯 Features

### 1. **Job Search Agent**
- Searches multiple job sources
- Filters by skills, location, and preferences
- Ranks jobs by match score
- Auto-applies to top positions

### 2. **Resume & Cover Letter Generator**
- Extracts keywords from job descriptions
- Tailors resume for each position
- Generates personalized cover letters
- 85%+ keyword match optimization

### 3. **Interview Preparation Agent**
- Company research and insights
- Technical question generation with answers
- Behavioral questions with STAR framework
- Smart questions to ask interviewers

### 4. **Application Tracker**
- Tracks all applications and statuses
- Auto-generates follow-up emails
- Smart timing based on interview stage
- Real-time dashboard

### 5. **LinkedIn Integration**
- Profile optimization (headline, about, skills)
- Recruiter targeting and connection requests
- Personalized networking messages
- Content strategy and posting ideas
- 4-week networking plan

## 📁 Project Structure

```
job-search-agent/
├── main.py                          # Main orchestrator
├── api.py                           # Flask REST API
├── start_frontend.sh                # Frontend launcher
├── frontend/
│   ├── index.html                  # React web UI
│   └── README.md                   # Frontend docs
├── agents/
│   ├── job_search.py               # Job search and filtering
│   ├── resume_generator.py         # Resume/cover letter generation
│   ├── interview_prep.py           # Interview preparation
│   ├── application_tracker.py      # Application tracking
│   └── linkedin_agent.py           # LinkedIn networking
├── data/                            # Generated data and tracking
├── templates/                       # Email and document templates
└── utils/                           # Utility functions
```

## 🚀 Quick Start

### One-Command Deploy
```bash
./deploy.sh
```

### Run Frontend (Alternative)
```bash
./start_frontend.sh
```
Then open http://localhost:8000

### Run Complete Pipeline (CLI)
```bash
python main.py
```

### Run Individual Agents

**Job Search:**
```bash
python agents/job_search.py
```

**Resume Generator:**
```bash
python agents/resume_generator.py
```

**Interview Prep:**
```bash
python agents/interview_prep.py
```

**Application Tracker:**
```bash
python agents/application_tracker.py
```

**LinkedIn Agent:**
```bash
python agents/linkedin_agent.py
```

## 📊 Pipeline Flow

1. **Optimize LinkedIn Profile** → Score: 75/100
2. **Search Jobs** → Find matching opportunities
3. **Generate Applications** → Tailored resumes & cover letters
4. **Prepare Interviews** → Questions, answers, company research
5. **Network on LinkedIn** → Connect with recruiters
6. **Track Applications** → Monitor status & auto follow-ups

## 🎯 Results

- **Jobs Found**: 7 matching positions
- **Applications Generated**: 3 complete packages
- **Match Score**: 85-100%
- **Connection Requests**: 5 personalized messages
- **Follow-ups**: Automated based on timing rules

## 🔧 Configuration

Edit user profile and preferences in `main.py`:

```python
user_profile = {
    'name': 'Your Name',
    'skills': ['Python', 'AWS', 'ML'],
    'years_experience': 5,
    # ... more fields
}

job_preferences = {
    'keywords': 'Python Engineer',
    'required_skills': ['Python', 'AWS'],
    'remote_only': True,
    'min_match_score': 40
}
```

## 📝 Generated Files

- `resume_[Company]_[Position].txt` - Tailored resumes
- `cover_letter_[Company]_[Position].txt` - Cover letters
- `interview_prep.json` - Interview preparation package
- `applications.json` - Application tracking data
- `linkedin_networking.json` - Networking strategy

## 🤝 Contributing

This is an autonomous agent system. Customize agents in the `agents/` directory for your specific needs.

## 📄 License

MIT License - Feel free to use and modify for your job search!

## 🎓 Learn More

Each agent is self-contained and can be used independently or as part of the complete pipeline.

---

**Built with AI for AI-powered job searching** 🚀
