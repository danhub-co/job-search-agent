#!/usr/bin/env python3
"""Demo data generator for testing frontend"""

import json
import random
from datetime import datetime, timedelta

# Sample companies and jobs
companies = [
    {'name': 'Google', 'logo': 'google.com'},
    {'name': 'Amazon', 'logo': 'amazon.com'},
    {'name': 'Microsoft', 'logo': 'microsoft.com'},
    {'name': 'Apple', 'logo': 'apple.com'},
    {'name': 'Meta', 'logo': 'meta.com'},
    {'name': 'Netflix', 'logo': 'netflix.com'},
    {'name': 'Tesla', 'logo': 'tesla.com'},
]

job_titles = [
    'Senior Python Engineer',
    'AI/ML Engineer', 
    'Full Stack Developer',
    'Data Scientist',
    'DevOps Engineer',
    'Software Architect',
    'Backend Engineer'
]

skills = ['Python', 'JavaScript', 'AWS', 'Docker', 'Kubernetes', 'React', 'Node.js', 'SQL', 'MongoDB', 'TensorFlow']

def generate_jobs(count=10):
    jobs = []
    for i in range(count):
        company = random.choice(companies)
        jobs.append({
            'id': i,
            'title': random.choice(job_titles),
            'company': company['name'],
            'location': random.choice(['Remote', 'San Francisco, CA', 'New York, NY', 'Seattle, WA']),
            'match_score': random.randint(60, 95),
            'required_skills': random.sample(skills, random.randint(3, 6)),
            'description': f"Join {company['name']} as a {random.choice(job_titles)} and work on cutting-edge technology..."
        })
    return jobs

def generate_applications(count=5):
    apps = []
    for i in range(count):
        company = random.choice(companies)
        status = random.choice(['Applied', 'Interview Scheduled', 'Offer Received', 'Rejected'])
        apps.append({
            'id': i,
            'position': random.choice(job_titles),
            'company': company['name'],
            'status': status,
            'applied_date': (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat()
        })
    return apps

if __name__ == '__main__':
    # Generate demo data
    demo_data = {
        'jobs': generate_jobs(15),
        'applications': generate_applications(8)
    }
    
    with open('demo_data.json', 'w') as f:
        json.dump(demo_data, f, indent=2)
    
    print("✓ Demo data generated: demo_data.json")
    print(f"  - {len(demo_data['jobs'])} jobs")
    print(f"  - {len(demo_data['applications'])} applications")