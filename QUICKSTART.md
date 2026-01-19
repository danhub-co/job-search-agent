# 🚀 Quick Start Guide

## Installation

```bash
cd /tmp/job-search-agent
pip install -r requirements.txt
```

## Configuration

1. Edit `config.json` with your information:
   - Personal details (name, email, phone)
   - Skills and experience
   - Job preferences
   - Target companies

2. Customize settings:
   - `auto_apply`: Enable/disable automatic applications
   - `auto_follow_up`: Enable/disable automatic follow-ups
   - `max_applications_per_day`: Limit daily applications

## Usage

### Run Complete Pipeline
```bash
python main.py
```

This will:
1. ✅ Optimize your LinkedIn profile
2. 🔍 Search for matching jobs
3. 📄 Generate tailored resumes & cover letters
4. 🎯 Prepare interview materials
5. 🤝 Create LinkedIn connection requests
6. 📊 Track all applications

### Run Individual Agents

**Search Jobs:**
```bash
python agents/job_search.py
```

**Generate Resume:**
```bash
python agents/resume_generator.py
```

**Prepare Interview:**
```bash
python agents/interview_prep.py
```

**Track Applications:**
```bash
python agents/application_tracker.py
```

**LinkedIn Networking:**
```bash
python agents/linkedin_agent.py
```

## Output Files

All generated files are saved in the project directory:

- `resume_[Company]_[Position].txt` - Tailored resumes
- `cover_letter_[Company]_[Position].txt` - Cover letters
- `interview_prep.json` - Interview preparation
- `applications.json` - Application tracking
- `linkedin_networking.json` - Networking data

## Tips

1. **Update your profile regularly** - Keep skills and experience current
2. **Review generated content** - Personalize before sending
3. **Track your metrics** - Monitor response rates
4. **Follow up consistently** - Use the auto follow-up system
5. **Network actively** - Connect with 5-10 people per week

## Workflow Example

```bash
# Day 1: Setup and search
python main.py

# Day 2-7: Review and send applications
# Check generated resumes and cover letters
# Send connection requests on LinkedIn

# Day 8+: Follow up
python agents/application_tracker.py
# Send follow-up emails for applications > 7 days old

# Ongoing: Track and iterate
# Update status as you progress through interviews
# Continue networking and applying
```

## Support

For issues or questions, review the README.md or check individual agent files for detailed documentation.

---

**Good luck with your job search!** 🎉
