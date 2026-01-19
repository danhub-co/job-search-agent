#!/usr/bin/env python3
"""
Agentic AI Job Search System
Main orchestrator integrating all agents
"""

import sys
import json
from datetime import datetime

# Import all agents
sys.path.insert(0, '/tmp/job-search-agent/agents')

from job_search import JobSearchAgent
from resume_generator import ApplicationPackageGenerator
from interview_prep import InterviewPrepAgent
from application_tracker import ApplicationTracker
from linkedin_agent import LinkedInAgent


class JobSearchOrchestrator:
    def __init__(self, user_profile):
        self.profile = user_profile
        self.job_agent = None
        self.resume_gen = None
        self.interview_prep = None
        self.tracker = ApplicationTracker()
        self.linkedin = LinkedInAgent(user_profile)
        
    def run_full_pipeline(self, job_preferences):
        """Run complete job search pipeline"""
        print("🤖 AGENTIC JOB SEARCH SYSTEM")
        print("=" * 70)
        print(f"User: {self.profile['name']}")
        print(f"Target: {job_preferences['keywords']}\n")
        
        # Step 1: Optimize LinkedIn
        print("\n" + "=" * 70)
        print("STEP 1: LinkedIn Profile Optimization")
        print("=" * 70)
        optimization = self.linkedin.optimize_profile()
        print(f"✓ Profile Score: {optimization['score']}/100")
        
        # Step 2: Search Jobs
        print("\n" + "=" * 70)
        print("STEP 2: Job Search")
        print("=" * 70)
        self.job_agent = JobSearchAgent(job_preferences)
        jobs = self.job_agent.search_jobs(job_preferences['keywords'])
        filtered = self.job_agent.filter_jobs(jobs)
        print(f"✓ Found {len(filtered)} matching jobs")
        
        # Step 3: Generate Applications
        print("\n" + "=" * 70)
        print("STEP 3: Generate Application Materials")
        print("=" * 70)
        self.resume_gen = ApplicationPackageGenerator(self.profile)
        
        applications = []
        for job in filtered[:3]:  # Top 3 jobs
            package = self.resume_gen.generate_package(job)
            applications.append(package)
            
            # Track application
            self.tracker.add_application(job['title'], job['company'])
        
        print(f"✓ Generated {len(applications)} application packages")
        
        # Step 4: Interview Prep
        print("\n" + "=" * 70)
        print("STEP 4: Interview Preparation")
        print("=" * 70)
        if filtered:
            prep_agent = InterviewPrepAgent(self.profile, filtered[0])
            prep_package = prep_agent.prepare()
            print(f"✓ Prepared for {filtered[0]['company']}")
        
        # Step 5: LinkedIn Networking
        print("\n" + "=" * 70)
        print("STEP 5: LinkedIn Networking")
        print("=" * 70)
        target_companies = [j['company'] for j in filtered[:3]]
        recruiters = self.linkedin.find_recruiters(target_companies, [job_preferences['keywords']])
        connections = self.linkedin.auto_connect(recruiters, max_connections=5)
        print(f"✓ Generated {len(connections)} connection requests")
        
        # Step 6: Setup Tracking
        print("\n" + "=" * 70)
        print("STEP 6: Application Tracking")
        print("=" * 70)
        self.tracker.display_dashboard()
        
        # Summary
        print("\n" + "=" * 70)
        print("📊 PIPELINE SUMMARY")
        print("=" * 70)
        summary = {
            'profile_optimized': True,
            'jobs_found': len(jobs),
            'applications_generated': len(applications),
            'interviews_prepared': 1,
            'connections_initiated': len(connections),
            'applications_tracked': len(self.tracker.applications)
        }
        print(json.dumps(summary, indent=2))
        
        return summary


def main():
    # User profile
    user_profile = {
        'name': 'John Doe',
        'email': 'john.doe@email.com',
        'phone': '(555) 123-4567',
        'location': 'San Francisco, CA',
        'linkedin': 'linkedin.com/in/johndoe',
        'current_title': 'Senior Software Engineer',
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
    
    # Job preferences
    job_preferences = {
        'keywords': 'Python AI Engineer',
        'required_skills': ['Python', 'AI', 'Machine Learning', 'AWS'],
        'remote_only': True,
        'min_match_score': 40,
        'preferred_companies': ['Amazon', 'Google', 'Microsoft']
    }
    
    # Run pipeline
    orchestrator = JobSearchOrchestrator(user_profile)
    orchestrator.run_full_pipeline(job_preferences)


if __name__ == "__main__":
    main()
