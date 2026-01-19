from datetime import datetime
import json
import re

class JobSearchAgent:
    def __init__(self, preferences):
        self.preferences = preferences
        self.jobs_found = []
        self.applied_jobs = []
        
    def search_jobs(self, keywords, location="Remote"):
        """Search for jobs - demo with sample data"""
        print(f"🔍 Searching for: {keywords} in {location}\n")
        
        # Sample job data
        jobs = self._get_sample_jobs()
        
        # Filter by keywords
        filtered = [j for j in jobs if any(k.lower() in j['title'].lower() or k.lower() in j['description'].lower() 
                                           for k in keywords.split())]
        
        self.jobs_found.extend(filtered)
        print(f"✓ Found {len(filtered)} jobs\n")
        return filtered
    
    def _get_sample_jobs(self):
        """Sample job listings"""
        return [
            {
                'title': 'Senior Python AI Engineer',
                'company': 'Amazon Web Services',
                'location': 'Remote',
                'description': 'Build AI/ML solutions using Python, AWS, and machine learning frameworks',
                'url': 'https://amazon.jobs/example1',
                'salary': '$150k-$200k',
                'source': 'LinkedIn',
                'posted': '2024-01-10'
            },
            {
                'title': 'Machine Learning Engineer',
                'company': 'Google',
                'location': 'Remote',
                'description': 'Develop ML models with Python, TensorFlow, and cloud infrastructure',
                'url': 'https://careers.google.com/example2',
                'salary': '$160k-$210k',
                'source': 'Indeed',
                'posted': '2024-01-12'
            },
            {
                'title': 'AI Research Scientist',
                'company': 'Microsoft',
                'location': 'Remote',
                'description': 'Research and implement cutting-edge AI algorithms using Python and Azure',
                'url': 'https://careers.microsoft.com/example3',
                'salary': '$170k-$220k',
                'source': 'Glassdoor',
                'posted': '2024-01-11'
            },
            {
                'title': 'Full Stack Developer',
                'company': 'Startup Inc',
                'location': 'San Francisco, CA',
                'description': 'Build web applications with React and Node.js',
                'url': 'https://startup.com/jobs/example4',
                'salary': '$120k-$150k',
                'source': 'AngelList',
                'posted': '2024-01-13'
            },
            {
                'title': 'Python Backend Engineer',
                'company': 'TechCorp',
                'location': 'Remote',
                'description': 'Develop scalable backend services with Python, Django, and PostgreSQL',
                'url': 'https://techcorp.com/careers/example5',
                'salary': '$130k-$170k',
                'source': 'LinkedIn',
                'posted': '2024-01-09'
            },
            {
                'title': 'Data Scientist - AI/ML',
                'company': 'DataCo',
                'location': 'Remote',
                'description': 'Apply machine learning and AI to solve business problems with Python',
                'url': 'https://dataco.com/jobs/example6',
                'salary': '$140k-$180k',
                'source': 'Indeed',
                'posted': '2024-01-14'
            },
            {
                'title': 'DevOps Engineer',
                'company': 'CloudTech',
                'location': 'New York, NY',
                'description': 'Manage AWS infrastructure and CI/CD pipelines',
                'url': 'https://cloudtech.com/careers/example7',
                'salary': '$135k-$175k',
                'source': 'LinkedIn',
                'posted': '2024-01-08'
            },
            {
                'title': 'AI Engineer - NLP',
                'company': 'Amazon',
                'location': 'Remote',
                'description': 'Build NLP models using Python, transformers, and AWS services',
                'url': 'https://amazon.jobs/example8',
                'salary': '$155k-$195k',
                'source': 'Amazon Jobs',
                'posted': '2024-01-15'
            }
        ]
    
    def filter_jobs(self, jobs):
        """Filter jobs based on preferences"""
        filtered = []
        
        for job in jobs:
            score = self._calculate_match_score(job)
            if score >= self.preferences.get('min_match_score', 50):
                job['match_score'] = score
                filtered.append(job)
        
        filtered.sort(key=lambda x: x['match_score'], reverse=True)
        
        print(f"✓ Filtered to {len(filtered)} matching jobs\n")
        return filtered
    
    def _calculate_match_score(self, job):
        """Calculate how well job matches preferences"""
        score = 0
        
        required_skills = self.preferences.get('required_skills', [])
        description = (job.get('title', '') + ' ' + job.get('description', '')).lower()
        
        for skill in required_skills:
            if skill.lower() in description:
                score += 20
        
        if self.preferences.get('remote_only', False):
            if 'remote' in job.get('location', '').lower():
                score += 30
        
        salary_str = str(job.get('salary', '')).lower()
        if 'not specified' not in salary_str and salary_str:
            score += 10
        
        preferred_companies = self.preferences.get('preferred_companies', [])
        for company in preferred_companies:
            if company.lower() in job.get('company', '').lower():
                score += 20
                break
        
        return min(score, 100)
    
    def rank_jobs(self, jobs):
        """Rank and display jobs by relevance"""
        for i, job in enumerate(jobs[:10], 1):
            print(f"{i}. [{job['match_score']}%] {job['title']}")
            print(f"   Company: {job['company']}")
            print(f"   Location: {job['location']}")
            print(f"   Salary: {job['salary']}")
            print(f"   Source: {job['source']}")
            print(f"   URL: {job['url']}\n")
        
        return jobs
    
    def auto_apply(self, jobs, max_applications=5):
        """Auto-apply to top matching jobs"""
        print(f"🤖 Auto-applying to top {max_applications} jobs...\n")
        
        for job in jobs[:max_applications]:
            print(f"✓ Applied to: {job['title']} at {job['company']}")
            self.applied_jobs.append({
                'title': job['title'],
                'company': job['company'],
                'match_score': job['match_score'],
                'applied_at': datetime.now().isoformat(),
                'status': 'Applied'
            })
        
        print(f"\n✓ Successfully applied to {len(self.applied_jobs)} jobs")
    
    def track_applications(self):
        """Track application status"""
        print("\n📋 Application Tracker:\n")
        for i, app in enumerate(self.applied_jobs, 1):
            print(f"{i}. {app['title']} at {app['company']}")
            print(f"   Match: {app['match_score']}% | Status: {app['status']}")
            print(f"   Applied: {app['applied_at']}\n")
    
    def get_report(self):
        """Generate comprehensive search report"""
        return {
            'search_summary': {
                'total_found': len(self.jobs_found),
                'total_applied': len(self.applied_jobs),
                'success_rate': f"{(len(self.applied_jobs)/len(self.jobs_found)*100):.1f}%" if self.jobs_found else "0%"
            },
            'applications': self.applied_jobs
        }


if __name__ == "__main__":
    print("🤖 Agentic Job Search System\n")
    print("=" * 70)
    
    # Define preferences
    preferences = {
        'required_skills': ['Python', 'AI', 'Machine Learning', 'AWS'],
        'remote_only': True,
        'min_match_score': 40,
        'preferred_companies': ['Amazon', 'Google', 'Microsoft']
    }
    
    # Initialize agent
    agent = JobSearchAgent(preferences)
    
    print("\n📝 Your Preferences:")
    print(f"   Skills: {', '.join(preferences['required_skills'])}")
    print(f"   Remote Only: {preferences['remote_only']}")
    print(f"   Min Match Score: {preferences['min_match_score']}%")
    print(f"   Preferred Companies: {', '.join(preferences['preferred_companies'])}\n")
    
    print("=" * 70)
    
    # Search
    jobs = agent.search_jobs("Python AI Engineer", "Remote")
    
    # Filter
    filtered_jobs = agent.filter_jobs(jobs)
    
    # Rank and display
    print("📊 Top Matching Jobs:\n")
    ranked_jobs = agent.rank_jobs(filtered_jobs)
    
    # Auto-apply
    if ranked_jobs:
        print("=" * 70)
        agent.auto_apply(ranked_jobs, max_applications=3)
        
        # Track applications
        print("=" * 70)
        agent.track_applications()
    
    # Final report
    print("=" * 70)
    report = agent.get_report()
    print("📈 FINAL REPORT:")
    print(json.dumps(report, indent=2))
