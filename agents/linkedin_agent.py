from datetime import datetime
import json
import re

class LinkedInAgent:
    def __init__(self, user_profile):
        self.profile = user_profile
        self.connections = []
        self.messages = []
        
    def optimize_profile(self):
        """Analyze and optimize LinkedIn profile"""
        print("🔍 Analyzing LinkedIn profile...\n")
        
        optimization = {
            'headline': self._optimize_headline(),
            'about': self._optimize_about(),
            'skills': self._optimize_skills(),
            'recommendations': self._generate_skill_endorsements(),
            'score': 0
        }
        
        # Calculate optimization score
        score = 0
        if len(optimization['headline']) > 50:
            score += 25
        if len(optimization['about']) > 200:
            score += 25
        if len(optimization['skills']) >= 10:
            score += 25
        if self.profile.get('experience'):
            score += 25
        
        optimization['score'] = score
        
        return optimization
    
    def _optimize_headline(self):
        """Generate optimized LinkedIn headline"""
        title = self.profile.get('current_title', 'Software Engineer')
        skills = self.profile.get('skills', [])[:3]
        years = self.profile.get('years_experience', 5)
        
        return f"{title} | {', '.join(skills)} | {years}+ Years Experience"
    
    def _optimize_about(self):
        """Generate optimized About section"""
        title = self.profile.get('current_title', 'Software Engineer')
        skills = ', '.join(self.profile.get('skills', [])[:5])
        years = self.profile.get('years_experience', 5)
        
        about = f"""🚀 {title} with {years}+ years of experience building scalable solutions

💡 Specializing in: {skills}

🎯 Passionate about leveraging technology to solve complex problems and drive innovation. Proven track record of delivering high-impact projects and leading cross-functional teams.

📫 Open to connecting with fellow professionals and exploring new opportunities.

#OpenToWork #TechLeadership #Innovation"""
        
        return about
    
    def _optimize_skills(self):
        """Prioritize and organize skills"""
        skills = self.profile.get('skills', [])
        
        # Categorize skills
        categorized = {
            'Technical': [],
            'Leadership': [],
            'Tools': []
        }
        
        tech_keywords = ['Python', 'Java', 'JavaScript', 'Machine Learning', 'AI', 'SQL']
        leadership_keywords = ['Leadership', 'Management', 'Mentoring', 'Agile']
        
        for skill in skills:
            if any(k in skill for k in tech_keywords):
                categorized['Technical'].append(skill)
            elif any(k in skill for k in leadership_keywords):
                categorized['Leadership'].append(skill)
            else:
                categorized['Tools'].append(skill)
        
        return categorized
    
    def _generate_skill_endorsements(self):
        """Generate list of skills to request endorsements for"""
        skills = self.profile.get('skills', [])[:10]
        return [f"Request endorsement for: {skill}" for skill in skills]
    
    def find_recruiters(self, target_companies, job_titles):
        """Find recruiters at target companies"""
        print(f"🔎 Finding recruiters at {len(target_companies)} companies...\n")
        
        recruiters = []
        
        for company in target_companies:
            # Simulate finding recruiters
            recruiters.append({
                'name': f"Recruiter at {company}",
                'title': 'Technical Recruiter',
                'company': company,
                'profile_url': f"linkedin.com/in/{company.lower().replace(' ', '')}-recruiter",
                'mutual_connections': 5,
                'relevance_score': 85
            })
            
            recruiters.append({
                'name': f"Hiring Manager at {company}",
                'title': job_titles[0] if job_titles else 'Engineering Manager',
                'company': company,
                'profile_url': f"linkedin.com/in/{company.lower().replace(' ', '')}-manager",
                'mutual_connections': 3,
                'relevance_score': 90
            })
        
        # Sort by relevance
        recruiters.sort(key=lambda x: x['relevance_score'], reverse=True)
        
        print(f"✓ Found {len(recruiters)} relevant contacts\n")
        return recruiters
    
    def generate_connection_message(self, recruiter, personalized=True):
        """Generate personalized connection request message"""
        
        if personalized:
            message = f"""Hi {recruiter['name'].split()[0]},

I noticed you're a {recruiter['title']} at {recruiter['company']}. I'm a {self.profile.get('current_title', 'Software Engineer')} with expertise in {', '.join(self.profile.get('skills', [])[:2])}.

I'm very interested in opportunities at {recruiter['company']} and would love to connect and learn more about your team.

Looking forward to connecting!

Best,
{self.profile.get('name', 'Your Name')}"""
        else:
            message = f"""Hi {recruiter['name'].split()[0]},

I'd like to add you to my professional network on LinkedIn.

Best regards,
{self.profile.get('name', 'Your Name')}"""
        
        return message
    
    def auto_connect(self, recruiters, max_connections=10):
        """Automatically generate connection requests"""
        print(f"🤝 Generating connection requests for top {max_connections} contacts...\n")
        
        connection_requests = []
        
        for recruiter in recruiters[:max_connections]:
            message = self.generate_connection_message(recruiter, personalized=True)
            
            request = {
                'to': recruiter['name'],
                'company': recruiter['company'],
                'message': message,
                'sent_date': datetime.now().isoformat(),
                'status': 'Pending'
            }
            
            connection_requests.append(request)
            self.connections.append(request)
            
            print(f"✓ Generated request for {recruiter['name']} at {recruiter['company']}")
        
        return connection_requests
    
    def generate_follow_up_message(self, connection, context='job_inquiry'):
        """Generate follow-up message after connection accepted"""
        
        templates = {
            'job_inquiry': f"""Hi {connection['to'].split()[0]},

Thanks for connecting! I wanted to reach out because I'm actively exploring opportunities in {', '.join(self.profile.get('skills', [])[:2])}.

I noticed {connection['company']} is doing exciting work in this space. Would you be open to a brief chat about potential opportunities or could you point me to the right person?

I'd be happy to share my background and discuss how I might contribute to your team.

Thanks!
{self.profile.get('name', 'Your Name')}""",
            
            'informational': f"""Hi {connection['to'].split()[0]},

Thanks for connecting! I'm really interested in learning more about your experience at {connection['company']}.

Would you be open to a quick 15-minute informational chat? I'd love to hear about your role and any advice you might have.

Thanks!
{self.profile.get('name', 'Your Name')}""",
            
            'referral': f"""Hi {connection['to'].split()[0]},

Thanks for connecting! I recently applied for a position at {connection['company']} and was wondering if you might be able to provide a referral or connect me with the hiring team.

I believe my background in {', '.join(self.profile.get('skills', [])[:2])} would be a great fit.

Happy to share more details. Thanks for considering!

{self.profile.get('name', 'Your Name')}"""
        }
        
        return templates.get(context, templates['job_inquiry'])
    
    def track_engagement(self):
        """Track LinkedIn engagement metrics"""
        return {
            'profile_views': 127,
            'search_appearances': 89,
            'connection_requests_sent': len(self.connections),
            'connection_acceptance_rate': '65%',
            'post_impressions': 1543,
            'engagement_rate': '8.2%'
        }
    
    def generate_content_ideas(self):
        """Generate LinkedIn post ideas"""
        print("💡 Generating content ideas...\n")
        
        skills = self.profile.get('skills', [])[:3]
        
        ideas = [
            {
                'topic': f'Technical Deep Dive: {skills[0] if skills else "Your Expertise"}',
                'content': f"""🔧 Quick tip on {skills[0] if skills else "coding"}:

[Share a specific technique or best practice]

This approach helped me [specific result/improvement].

What's your go-to technique? Drop it in the comments! 👇

#{skills[0].replace(' ', '')} #TechTips #SoftwareEngineering""",
                'best_time': 'Tuesday 9 AM',
                'expected_reach': 'Medium'
            },
            {
                'topic': 'Career Journey & Lessons Learned',
                'content': f"""🚀 {self.profile.get('years_experience', 5)} years in tech - here's what I've learned:

1. [Key lesson 1]
2. [Key lesson 2]
3. [Key lesson 3]

What's the best career advice you've received? 

#CareerGrowth #TechCareers #Leadership""",
                'best_time': 'Wednesday 10 AM',
                'expected_reach': 'High'
            },
            {
                'topic': 'Project Success Story',
                'content': f"""✨ Proud to share: [Recent achievement]

The challenge: [Problem you solved]
The solution: [Your approach]
The impact: [Results with metrics]

Key takeaway: [Lesson learned]

#TechInnovation #Engineering #Success""",
                'best_time': 'Thursday 8 AM',
                'expected_reach': 'High'
            },
            {
                'topic': 'Industry Trends & Insights',
                'content': f"""📊 Interesting trend I'm seeing in {skills[0] if skills else "tech"}:

[Your observation about industry trend]

This could mean [implications/opportunities].

What are you seeing in your field? Let's discuss! 💬

#TechTrends #Innovation #FutureTech""",
                'best_time': 'Monday 11 AM',
                'expected_reach': 'Medium'
            }
        ]
        
        return ideas
    
    def create_networking_strategy(self, target_companies, job_titles):
        """Create comprehensive networking strategy"""
        print("📋 Creating networking strategy...\n")
        
        strategy = {
            'week_1': {
                'tasks': [
                    'Optimize LinkedIn profile',
                    f'Connect with 10 recruiters at target companies',
                    'Post 2 pieces of content',
                    'Engage with 20 posts in your industry'
                ],
                'goal': 'Build visibility and initial connections'
            },
            'week_2': {
                'tasks': [
                    'Follow up with accepted connections',
                    'Request 5 informational interviews',
                    'Join 3 relevant LinkedIn groups',
                    'Comment on 30 industry posts'
                ],
                'goal': 'Deepen relationships and gather insights'
            },
            'week_3': {
                'tasks': [
                    'Ask for referrals from warm connections',
                    'Share success story or project highlight',
                    'Connect with hiring managers',
                    'Attend virtual networking events'
                ],
                'goal': 'Convert connections to opportunities'
            },
            'week_4': {
                'tasks': [
                    'Follow up on referrals',
                    'Thank connections who helped',
                    'Continue content posting',
                    'Maintain engagement momentum'
                ],
                'goal': 'Close opportunities and maintain network'
            }
        }
        
        return strategy


if __name__ == "__main__":
    print("🔗 LinkedIn Integration & Networking Agent\n")
    print("=" * 70)
    
    # User profile
    user_profile = {
        'name': 'John Doe',
        'current_title': 'Senior Software Engineer',
        'years_experience': 7,
        'skills': ['Python', 'AWS', 'Machine Learning', 'Docker', 'Kubernetes', 
                   'TensorFlow', 'Leadership', 'Agile', 'System Design', 'SQL'],
        'experience': [
            {'title': 'Senior Software Engineer', 'company': 'Tech Corp'}
        ]
    }
    
    # Initialize agent
    agent = LinkedInAgent(user_profile)
    
    # Optimize profile
    print("\n📝 PROFILE OPTIMIZATION")
    print("=" * 70 + "\n")
    
    optimization = agent.optimize_profile()
    
    print(f"Optimization Score: {optimization['score']}/100\n")
    print(f"Headline:\n{optimization['headline']}\n")
    print(f"About Section:\n{optimization['about']}\n")
    print(f"Skills by Category:")
    for category, skills in optimization['skills'].items():
        if skills:
            print(f"  {category}: {', '.join(skills)}")
    
    # Find recruiters
    print("\n" + "=" * 70)
    print("🎯 RECRUITER TARGETING")
    print("=" * 70 + "\n")
    
    target_companies = ['Amazon Web Services', 'Google', 'Microsoft']
    job_titles = ['Senior Software Engineer', 'ML Engineer']
    
    recruiters = agent.find_recruiters(target_companies, job_titles)
    
    print("Top Recruiters:")
    for i, rec in enumerate(recruiters[:5], 1):
        print(f"{i}. {rec['name']} - {rec['title']} at {rec['company']}")
        print(f"   Relevance: {rec['relevance_score']}% | Mutual: {rec['mutual_connections']}\n")
    
    # Auto-connect
    print("=" * 70)
    print("🤝 CONNECTION REQUESTS")
    print("=" * 70 + "\n")
    
    requests = agent.auto_connect(recruiters, max_connections=3)
    
    print("\n" + "─" * 70)
    print("Sample Connection Message:")
    print("─" * 70)
    print(requests[0]['message'])
    
    # Follow-up messages
    print("\n" + "=" * 70)
    print("💬 FOLLOW-UP MESSAGES")
    print("=" * 70 + "\n")
    
    follow_up = agent.generate_follow_up_message(requests[0], 'job_inquiry')
    print("Job Inquiry Follow-up:")
    print("─" * 70)
    print(follow_up)
    
    # Content ideas
    print("\n" + "=" * 70)
    print("📱 CONTENT STRATEGY")
    print("=" * 70 + "\n")
    
    content_ideas = agent.generate_content_ideas()
    
    for i, idea in enumerate(content_ideas[:2], 1):
        print(f"{i}. {idea['topic']}")
        print(f"   Best Time: {idea['best_time']} | Reach: {idea['expected_reach']}")
        print(f"\n{idea['content']}\n")
    
    # Networking strategy
    print("=" * 70)
    print("📅 4-WEEK NETWORKING STRATEGY")
    print("=" * 70 + "\n")
    
    strategy = agent.create_networking_strategy(target_companies, job_titles)
    
    for week, details in strategy.items():
        print(f"{week.upper().replace('_', ' ')}:")
        print(f"Goal: {details['goal']}")
        print("Tasks:")
        for task in details['tasks']:
            print(f"  ✓ {task}")
        print()
    
    # Engagement metrics
    print("=" * 70)
    print("📊 ENGAGEMENT METRICS")
    print("=" * 70 + "\n")
    
    metrics = agent.track_engagement()
    print(json.dumps(metrics, indent=2))
    
    # Save data
    print("\n💾 Saving networking data...")
    with open('/tmp/linkedin_networking.json', 'w') as f:
        json.dump({
            'profile_optimization': optimization,
            'connection_requests': requests,
            'content_ideas': content_ideas,
            'strategy': strategy,
            'metrics': metrics
        }, f, indent=2)
    
    print("✓ Saved: /tmp/linkedin_networking.json")
