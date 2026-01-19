from datetime import datetime
import json
import re

class ResumeGenerator:
    def __init__(self, user_profile):
        self.profile = user_profile
        
    def generate_resume(self, job):
        """Generate tailored resume for specific job"""
        print(f"📄 Generating resume for: {job['title']} at {job['company']}\n")
        
        # Extract keywords from job description
        keywords = self._extract_keywords(job['description'])
        
        # Build tailored resume
        resume = {
            'header': self._build_header(),
            'summary': self._build_summary(job, keywords),
            'skills': self._build_skills(keywords),
            'experience': self._build_experience(job, keywords),
            'education': self._build_education(),
            'match_score': self._calculate_keyword_match(keywords)
        }
        
        return resume
    
    def _extract_keywords(self, description):
        """Extract important keywords from job description"""
        tech_keywords = ['Python', 'AWS', 'Machine Learning', 'AI', 'TensorFlow', 
                        'Docker', 'Kubernetes', 'SQL', 'React', 'Node.js', 'Java',
                        'Django', 'Flask', 'PostgreSQL', 'MongoDB', 'Git']
        
        found = [kw for kw in tech_keywords if kw.lower() in description.lower()]
        return found
    
    def _build_header(self):
        return {
            'name': self.profile['name'],
            'email': self.profile['email'],
            'phone': self.profile['phone'],
            'location': self.profile['location'],
            'linkedin': self.profile.get('linkedin', '')
        }
    
    def _build_summary(self, job, keywords):
        """Generate tailored professional summary"""
        years = self.profile.get('years_experience', 5)
        top_skills = ', '.join(keywords[:3]) if keywords else 'software development'
        
        return f"{years}+ years experienced {job['title']} specializing in {top_skills}. " \
               f"Proven track record of delivering scalable solutions and driving innovation."
    
    def _build_skills(self, keywords):
        """Build skills section prioritizing job keywords"""
        all_skills = self.profile.get('skills', [])
        
        # Prioritize matching keywords
        matched = [s for s in all_skills if s in keywords]
        other = [s for s in all_skills if s not in keywords]
        
        return matched + other
    
    def _build_experience(self, job, keywords):
        """Tailor experience section to highlight relevant work"""
        experiences = []
        
        for exp in self.profile.get('experience', []):
            # Enhance bullet points with matching keywords
            enhanced_bullets = []
            for bullet in exp.get('bullets', []):
                # Check if bullet mentions relevant keywords
                relevance = sum(1 for kw in keywords if kw.lower() in bullet.lower())
                enhanced_bullets.append({
                    'text': bullet,
                    'relevance': relevance
                })
            
            # Sort by relevance
            enhanced_bullets.sort(key=lambda x: x['relevance'], reverse=True)
            
            experiences.append({
                'title': exp['title'],
                'company': exp['company'],
                'duration': exp['duration'],
                'bullets': [b['text'] for b in enhanced_bullets[:4]]  # Top 4 most relevant
            })
        
        return experiences
    
    def _build_education(self):
        return self.profile.get('education', [])
    
    def _calculate_keyword_match(self, keywords):
        """Calculate how well resume matches job"""
        user_skills = set(s.lower() for s in self.profile.get('skills', []))
        job_keywords = set(k.lower() for k in keywords)
        
        if not job_keywords:
            return 0
        
        match = len(user_skills.intersection(job_keywords))
        return int((match / len(job_keywords)) * 100)
    
    def format_resume_text(self, resume):
        """Format resume as text"""
        text = []
        
        # Header
        h = resume['header']
        text.append(f"{h['name'].upper()}")
        text.append(f"{h['email']} | {h['phone']} | {h['location']}")
        if h.get('linkedin'):
            text.append(f"LinkedIn: {h['linkedin']}")
        text.append("")
        
        # Summary
        text.append("PROFESSIONAL SUMMARY")
        text.append("-" * 50)
        text.append(resume['summary'])
        text.append("")
        
        # Skills
        text.append("TECHNICAL SKILLS")
        text.append("-" * 50)
        text.append(", ".join(resume['skills']))
        text.append("")
        
        # Experience
        text.append("PROFESSIONAL EXPERIENCE")
        text.append("-" * 50)
        for exp in resume['experience']:
            text.append(f"\n{exp['title']} | {exp['company']}")
            text.append(exp['duration'])
            for bullet in exp['bullets']:
                text.append(f"  • {bullet}")
        text.append("")
        
        # Education
        text.append("EDUCATION")
        text.append("-" * 50)
        for edu in resume['education']:
            text.append(f"{edu['degree']} - {edu['school']} ({edu['year']})")
        
        return "\n".join(text)


class CoverLetterGenerator:
    def __init__(self, user_profile):
        self.profile = user_profile
        
    def generate_cover_letter(self, job):
        """Generate tailored cover letter"""
        print(f"✉️  Generating cover letter for: {job['title']} at {job['company']}\n")
        
        letter = {
            'date': datetime.now().strftime("%B %d, %Y"),
            'greeting': f"Dear {job['company']} Hiring Manager,",
            'opening': self._opening_paragraph(job),
            'body': self._body_paragraphs(job),
            'closing': self._closing_paragraph(job),
            'signature': self.profile['name']
        }
        
        return letter
    
    def _opening_paragraph(self, job):
        """Generate opening paragraph"""
        return f"I am writing to express my strong interest in the {job['title']} position at {job['company']}. " \
               f"With {self.profile.get('years_experience', 5)}+ years of experience in software engineering and a " \
               f"proven track record of delivering innovative solutions, I am excited about the opportunity to contribute to your team."
    
    def _body_paragraphs(self, job):
        """Generate body paragraphs highlighting relevant experience"""
        paragraphs = []
        
        # Paragraph 1: Technical skills
        skills = self.profile.get('skills', [])[:5]
        para1 = f"My technical expertise includes {', '.join(skills[:-1])}, and {skills[-1]}. " \
                f"I have successfully applied these technologies to build scalable, high-performance systems " \
                f"that drive business value and enhance user experiences."
        paragraphs.append(para1)
        
        # Paragraph 2: Relevant experience
        if self.profile.get('experience'):
            recent = self.profile['experience'][0]
            para2 = f"In my recent role as {recent['title']} at {recent['company']}, " \
                    f"I {recent['bullets'][0].lower()} This experience has prepared me to make immediate " \
                    f"contributions to {job['company']}'s mission."
            paragraphs.append(para2)
        
        return paragraphs
    
    def _closing_paragraph(self, job):
        """Generate closing paragraph"""
        return f"I am particularly drawn to {job['company']} because of your commitment to innovation and excellence. " \
               f"I would welcome the opportunity to discuss how my skills and experience align with your team's needs. " \
               f"Thank you for considering my application."
    
    def format_cover_letter_text(self, letter):
        """Format cover letter as text"""
        text = []
        
        text.append(self.profile['name'])
        text.append(self.profile['email'])
        text.append(self.profile['phone'])
        text.append("")
        text.append(letter['date'])
        text.append("")
        text.append(letter['greeting'])
        text.append("")
        text.append(letter['opening'])
        text.append("")
        for para in letter['body']:
            text.append(para)
            text.append("")
        text.append(letter['closing'])
        text.append("")
        text.append("Sincerely,")
        text.append(letter['signature'])
        
        return "\n".join(text)


class ApplicationPackageGenerator:
    def __init__(self, user_profile):
        self.resume_gen = ResumeGenerator(user_profile)
        self.cover_letter_gen = CoverLetterGenerator(user_profile)
        
    def generate_package(self, job):
        """Generate complete application package"""
        print(f"📦 Generating application package for {job['company']}\n")
        print("=" * 70)
        
        # Generate resume
        resume = self.resume_gen.generate_resume(job)
        
        # Generate cover letter
        cover_letter = self.cover_letter_gen.generate_cover_letter(job)
        
        # Package
        package = {
            'job': job,
            'resume': resume,
            'cover_letter': cover_letter,
            'generated_at': datetime.now().isoformat()
        }
        
        print(f"✓ Resume generated (Match: {resume['match_score']}%)")
        print(f"✓ Cover letter generated")
        print("")
        
        return package
    
    def save_package(self, package, output_dir='/tmp'):
        """Save resume and cover letter to files"""
        job_title = package['job']['title'].replace(' ', '_')
        company = package['job']['company'].replace(' ', '_')
        
        # Save resume
        resume_file = f"{output_dir}/resume_{company}_{job_title}.txt"
        resume_text = self.resume_gen.format_resume_text(package['resume'])
        with open(resume_file, 'w') as f:
            f.write(resume_text)
        
        # Save cover letter
        cover_file = f"{output_dir}/cover_letter_{company}_{job_title}.txt"
        cover_text = self.cover_letter_gen.format_cover_letter_text(package['cover_letter'])
        with open(cover_file, 'w') as f:
            f.write(cover_text)
        
        print(f"💾 Saved: {resume_file}")
        print(f"💾 Saved: {cover_file}")
        
        return resume_file, cover_file


if __name__ == "__main__":
    # User profile
    user_profile = {
        'name': 'John Doe',
        'email': 'john.doe@email.com',
        'phone': '(555) 123-4567',
        'location': 'San Francisco, CA',
        'linkedin': 'linkedin.com/in/johndoe',
        'years_experience': 7,
        'skills': ['Python', 'AWS', 'Machine Learning', 'TensorFlow', 'Docker', 
                   'Kubernetes', 'SQL', 'Django', 'React', 'Git'],
        'experience': [
            {
                'title': 'Senior Software Engineer',
                'company': 'Tech Corp',
                'duration': '2020 - Present',
                'bullets': [
                    'Built ML pipelines processing 10M+ daily events using Python and AWS',
                    'Designed microservices architecture with Docker and Kubernetes',
                    'Led team of 5 engineers delivering AI-powered features',
                    'Reduced infrastructure costs by 40% through optimization'
                ]
            },
            {
                'title': 'Software Engineer',
                'company': 'StartupXYZ',
                'duration': '2017 - 2020',
                'bullets': [
                    'Developed RESTful APIs using Django and PostgreSQL',
                    'Implemented CI/CD pipelines with Jenkins and AWS',
                    'Built real-time analytics dashboard with React',
                    'Mentored junior developers on best practices'
                ]
            }
        ],
        'education': [
            {
                'degree': 'BS Computer Science',
                'school': 'Stanford University',
                'year': '2017'
            }
        ]
    }
    
    # Sample job
    job = {
        'title': 'Senior Python AI Engineer',
        'company': 'Amazon Web Services',
        'location': 'Remote',
        'description': 'Build AI/ML solutions using Python, AWS, and machine learning frameworks. '
                      'Experience with TensorFlow, Docker, and Kubernetes required.',
        'url': 'https://amazon.jobs/example1'
    }
    
    print("🤖 AI Resume & Cover Letter Generator\n")
    print("=" * 70)
    
    # Generate package
    generator = ApplicationPackageGenerator(user_profile)
    package = generator.generate_package(job)
    
    # Save files
    print("=" * 70)
    resume_file, cover_file = generator.save_package(package)
    
    print("\n" + "=" * 70)
    print("📄 RESUME PREVIEW:\n")
    print(generator.resume_gen.format_resume_text(package['resume']))
    
    print("\n" + "=" * 70)
    print("✉️  COVER LETTER PREVIEW:\n")
    print(generator.cover_letter_gen.format_cover_letter_text(package['cover_letter']))
