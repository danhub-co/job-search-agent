import json
from datetime import datetime

class InterviewPrepAgent:
    def __init__(self, user_profile, job):
        self.profile = user_profile
        self.job = job
        self.prep_package = {}
        
    def prepare(self):
        """Generate complete interview preparation package"""
        print(f"🎯 Preparing interview for: {self.job['title']} at {self.job['company']}\n")
        print("=" * 70)
        
        self.prep_package = {
            'company_research': self._research_company(),
            'technical_questions': self._generate_technical_questions(),
            'behavioral_questions': self._generate_behavioral_questions(),
            'questions_to_ask': self._generate_questions_to_ask(),
            'preparation_tips': self._generate_tips(),
            'generated_at': datetime.now().isoformat()
        }
        
        return self.prep_package
    
    def _research_company(self):
        """Generate company research brief"""
        print("📊 Researching company...\n")
        
        company_info = {
            'Amazon Web Services': {
                'overview': 'Leading cloud computing platform, part of Amazon',
                'products': ['EC2', 'S3', 'Lambda', 'SageMaker', 'RDS'],
                'culture': 'Customer obsession, ownership, innovation, bias for action',
                'leadership_principles': [
                    'Customer Obsession',
                    'Ownership',
                    'Invent and Simplify',
                    'Learn and Be Curious',
                    'Hire and Develop the Best'
                ],
                'recent_news': 'Expanding AI/ML services, focus on generative AI'
            },
            'Google': {
                'overview': 'Technology company specializing in search, cloud, and AI',
                'products': ['Search', 'Cloud', 'Android', 'YouTube', 'AI'],
                'culture': 'Innovation, collaboration, data-driven decisions',
                'values': ['Focus on user', 'Fast is better than slow', 'Great just isn\'t good enough'],
                'recent_news': 'Major investments in AI and quantum computing'
            },
            'Microsoft': {
                'overview': 'Technology corporation focused on software, cloud, and AI',
                'products': ['Azure', 'Office 365', 'Windows', 'GitHub', 'LinkedIn'],
                'culture': 'Growth mindset, diversity and inclusion, innovation',
                'values': ['Respect', 'Integrity', 'Accountability'],
                'recent_news': 'Partnership with OpenAI, Azure AI expansion'
            }
        }
        
        company = self.job['company']
        info = company_info.get(company, {
            'overview': f'{company} - Research specific details before interview',
            'products': ['Research company products/services'],
            'culture': 'Research company culture and values',
            'recent_news': 'Check recent news and announcements'
        })
        
        return info
    
    def _generate_technical_questions(self):
        """Generate likely technical interview questions"""
        print("💻 Generating technical questions...\n")
        
        description = self.job.get('description', '').lower()
        questions = []
        
        # Python questions
        if 'python' in description:
            questions.extend([
                {
                    'question': 'Explain Python decorators and provide a use case',
                    'answer': 'Decorators are functions that modify the behavior of other functions. '
                             'They use @decorator syntax. Use case: logging, authentication, caching. '
                             'Example: @login_required decorator for web routes.',
                    'difficulty': 'Medium'
                },
                {
                    'question': 'What is the difference between list and tuple in Python?',
                    'answer': 'Lists are mutable (can be changed), tuples are immutable. '
                             'Lists use [], tuples use (). Tuples are faster and can be used as dict keys.',
                    'difficulty': 'Easy'
                },
                {
                    'question': 'Explain Python\'s GIL and its implications',
                    'answer': 'Global Interpreter Lock prevents multiple threads from executing Python bytecode simultaneously. '
                             'Impacts CPU-bound multi-threaded programs. Use multiprocessing for parallelism.',
                    'difficulty': 'Hard'
                }
            ])
        
        # ML/AI questions
        if 'machine learning' in description or 'ai' in description:
            questions.extend([
                {
                    'question': 'Explain the bias-variance tradeoff',
                    'answer': 'Bias is error from wrong assumptions (underfitting). '
                             'Variance is error from sensitivity to training data (overfitting). '
                             'Goal is to minimize both for optimal model performance.',
                    'difficulty': 'Medium'
                },
                {
                    'question': 'How do you handle imbalanced datasets?',
                    'answer': 'Techniques: oversampling minority class (SMOTE), undersampling majority class, '
                             'class weights, ensemble methods, use appropriate metrics (F1, precision-recall).',
                    'difficulty': 'Medium'
                },
                {
                    'question': 'Explain gradient descent and its variants',
                    'answer': 'Optimization algorithm to minimize loss. Variants: Batch GD (all data), '
                             'Stochastic GD (one sample), Mini-batch GD (subset). Adam combines momentum and adaptive learning.',
                    'difficulty': 'Hard'
                }
            ])
        
        # AWS questions
        if 'aws' in description:
            questions.extend([
                {
                    'question': 'Explain the difference between S3 and EBS',
                    'answer': 'S3 is object storage for files, accessed via API, highly scalable. '
                             'EBS is block storage for EC2 instances, like a hard drive, lower latency.',
                    'difficulty': 'Easy'
                },
                {
                    'question': 'How would you design a scalable architecture on AWS?',
                    'answer': 'Use ELB for load balancing, Auto Scaling for elasticity, RDS with read replicas, '
                             'CloudFront for CDN, S3 for static assets, Lambda for serverless, multi-AZ deployment.',
                    'difficulty': 'Hard'
                }
            ])
        
        # System design
        questions.append({
            'question': 'Design a URL shortener service',
            'answer': 'Components: API (create/redirect), database (URL mappings), cache (Redis), '
                     'hash function (base62 encoding). Scale: sharding, load balancing, CDN. '
                     'Handle: collisions, analytics, expiration.',
            'difficulty': 'Hard'
        })
        
        return questions
    
    def _generate_behavioral_questions(self):
        """Generate behavioral interview questions with STAR method answers"""
        print("🗣️  Generating behavioral questions...\n")
        
        questions = [
            {
                'question': 'Tell me about a time you faced a difficult technical challenge',
                'framework': 'STAR (Situation, Task, Action, Result)',
                'sample_answer': {
                    'situation': 'ML pipeline was processing 10M events/day but latency increased to 2 hours',
                    'task': 'Reduce latency to under 30 minutes while maintaining accuracy',
                    'action': 'Profiled code, optimized data loading with parallel processing, '
                             'implemented caching, moved to distributed computing with Spark',
                    'result': 'Reduced latency to 20 minutes (90% improvement), saved $50k/year in compute costs'
                },
                'tips': 'Use specific metrics, show problem-solving skills, highlight impact'
            },
            {
                'question': 'Describe a time you had to work with a difficult team member',
                'framework': 'STAR',
                'sample_answer': {
                    'situation': 'Team member consistently missed deadlines, affecting project timeline',
                    'task': 'Address issue while maintaining team morale',
                    'action': 'Had 1-on-1 conversation to understand blockers, offered help, '
                             'adjusted task assignments, set up daily check-ins',
                    'result': 'Team member improved performance, project delivered on time, strengthened team relationship'
                },
                'tips': 'Show empathy, focus on resolution, demonstrate leadership'
            },
            {
                'question': 'Tell me about a time you failed',
                'framework': 'STAR',
                'sample_answer': {
                    'situation': 'Deployed ML model that caused 20% drop in user engagement',
                    'task': 'Quickly identify issue and restore service',
                    'action': 'Rolled back deployment, analyzed logs, found model was overfitted to training data, '
                             'implemented better validation, added A/B testing framework',
                    'result': 'Restored engagement, prevented future issues, established deployment best practices'
                },
                'tips': 'Be honest, focus on learning, show how you improved'
            },
            {
                'question': 'Describe a time you showed leadership',
                'framework': 'STAR',
                'sample_answer': {
                    'situation': 'Team was struggling with unclear requirements and low morale',
                    'task': 'Improve team productivity and satisfaction',
                    'action': 'Organized requirements gathering sessions, implemented agile practices, '
                             'set up mentorship program, celebrated wins',
                    'result': 'Velocity increased 40%, team satisfaction score improved from 6 to 9/10'
                },
                'tips': 'Show initiative, demonstrate impact on team, use metrics'
            }
        ]
        
        # Add company-specific behavioral questions
        if 'Amazon' in self.job['company']:
            questions.append({
                'question': 'Tell me about a time you demonstrated customer obsession',
                'framework': 'STAR (Amazon Leadership Principle)',
                'tips': 'Focus on customer impact, show data-driven decisions, demonstrate ownership'
            })
        
        return questions
    
    def _generate_questions_to_ask(self):
        """Generate smart questions to ask the interviewer"""
        print("❓ Generating questions to ask...\n")
        
        return [
            {
                'category': 'Role & Team',
                'questions': [
                    'What does a typical day look like for this role?',
                    'How is the team structured and who would I work with most closely?',
                    'What are the biggest challenges the team is facing right now?',
                    'How do you measure success for this position?'
                ]
            },
            {
                'category': 'Technical',
                'questions': [
                    'What is the tech stack and why was it chosen?',
                    'How does the team approach technical debt?',
                    'What does the code review process look like?',
                    'How do you balance innovation with maintaining existing systems?'
                ]
            },
            {
                'category': 'Growth',
                'questions': [
                    'What learning and development opportunities are available?',
                    'How does the company support career growth?',
                    'What does the path to senior/lead roles look like?',
                    'Are there opportunities to work on different projects or teams?'
                ]
            },
            {
                'category': 'Culture',
                'questions': [
                    'How would you describe the team culture?',
                    'What do you enjoy most about working here?',
                    'How does the company handle work-life balance?',
                    'What makes someone successful in this role?'
                ]
            }
        ]
    
    def _generate_tips(self):
        """Generate interview preparation tips"""
        return {
            'before_interview': [
                'Review company website and recent news',
                'Practice coding problems on LeetCode/HackerRank',
                'Prepare STAR stories for behavioral questions',
                'Test your tech setup (camera, mic, internet)',
                'Prepare questions to ask interviewers'
            ],
            'during_interview': [
                'Think out loud when solving problems',
                'Ask clarifying questions before coding',
                'Communicate your approach before implementing',
                'Test your code with examples',
                'Be honest if you don\'t know something'
            ],
            'after_interview': [
                'Send thank you email within 24 hours',
                'Reflect on questions you struggled with',
                'Follow up if you don\'t hear back in 1-2 weeks',
                'Continue practicing for future interviews'
            ]
        }
    
    def display_prep_package(self):
        """Display formatted interview prep package"""
        pkg = self.prep_package
        
        print("\n" + "=" * 70)
        print("📚 COMPANY RESEARCH")
        print("=" * 70)
        research = pkg['company_research']
        print(f"\nOverview: {research.get('overview', 'N/A')}")
        print(f"\nKey Products: {', '.join(research.get('products', []))}")
        print(f"\nCulture: {research.get('culture', 'N/A')}")
        if 'leadership_principles' in research:
            print(f"\nLeadership Principles:")
            for principle in research['leadership_principles'][:3]:
                print(f"  • {principle}")
        print(f"\nRecent News: {research.get('recent_news', 'N/A')}")
        
        print("\n" + "=" * 70)
        print("💻 TECHNICAL QUESTIONS")
        print("=" * 70)
        for i, q in enumerate(pkg['technical_questions'][:5], 1):
            print(f"\n{i}. [{q['difficulty']}] {q['question']}")
            print(f"   Answer: {q['answer']}")
        
        print("\n" + "=" * 70)
        print("🗣️  BEHAVIORAL QUESTIONS")
        print("=" * 70)
        for i, q in enumerate(pkg['behavioral_questions'][:3], 1):
            print(f"\n{i}. {q['question']}")
            print(f"   Framework: {q['framework']}")
            if 'sample_answer' in q:
                ans = q['sample_answer']
                print(f"   Example:")
                print(f"     S: {ans['situation']}")
                print(f"     T: {ans['task']}")
                print(f"     A: {ans['action']}")
                print(f"     R: {ans['result']}")
            print(f"   Tips: {q['tips']}")
        
        print("\n" + "=" * 70)
        print("❓ QUESTIONS TO ASK")
        print("=" * 70)
        for category in pkg['questions_to_ask'][:2]:
            print(f"\n{category['category']}:")
            for q in category['questions'][:3]:
                print(f"  • {q}")
        
        print("\n" + "=" * 70)
        print("💡 PREPARATION TIPS")
        print("=" * 70)
        tips = pkg['preparation_tips']
        print("\nBefore Interview:")
        for tip in tips['before_interview'][:3]:
            print(f"  ✓ {tip}")
        print("\nDuring Interview:")
        for tip in tips['during_interview'][:3]:
            print(f"  ✓ {tip}")
    
    def save_prep_package(self, output_file='/tmp/interview_prep.json'):
        """Save prep package to file"""
        with open(output_file, 'w') as f:
            json.dump(self.prep_package, f, indent=2)
        print(f"\n💾 Saved prep package: {output_file}")
        return output_file


if __name__ == "__main__":
    # User profile
    user_profile = {
        'name': 'John Doe',
        'years_experience': 7,
        'skills': ['Python', 'AWS', 'Machine Learning', 'TensorFlow']
    }
    
    # Job
    job = {
        'title': 'Senior Python AI Engineer',
        'company': 'Amazon Web Services',
        'description': 'Build AI/ML solutions using Python, AWS, and machine learning frameworks'
    }
    
    print("🎯 AI Interview Preparation Agent\n")
    print("=" * 70)
    
    # Create agent and prepare
    agent = InterviewPrepAgent(user_profile, job)
    agent.prepare()
    
    # Display
    agent.display_prep_package()
    
    # Save
    agent.save_prep_package()
