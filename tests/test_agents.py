#!/usr/bin/env python3
"""Test suite for job search agents"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'agents'))

from job_search import JobSearchAgent
from resume_generator import ApplicationPackageGenerator
from application_tracker import ApplicationTracker

def test_job_search_agent():
    """Test job search functionality"""
    preferences = {
        'keywords': 'Python Engineer',
        'required_skills': ['Python'],
        'remote_only': True,
        'min_match_score': 40
    }
    agent = JobSearchAgent(preferences)
    jobs = agent.search_jobs('Python Engineer')
    assert len(jobs) > 0
    assert all('title' in job for job in jobs)
    print("✓ Job search agent test passed")

def test_resume_generator():
    """Test resume generation"""
    profile = {
        'name': 'Test User',
        'skills': ['Python', 'AWS'],
        'years_experience': 5,
        'email': 'test@example.com',
        'phone': '555-1234',
        'location': 'Test City',
        'experience': [],
        'education': []
    }
    job = {
        'title': 'Python Engineer',
        'company': 'Test Corp',
        'description': 'Python development role'
    }
    generator = ApplicationPackageGenerator(profile)
    package = generator.generate_package(job)
    assert 'resume' in package
    assert 'cover_letter' in package
    print("✓ Resume generator test passed")

def test_application_tracker():
    """Test application tracking"""
    tracker = ApplicationTracker()
    tracker.add_application('Python Engineer', 'Test Corp')
    assert len(tracker.applications) > 0
    assert tracker.applications[0]['job_title'] == 'Python Engineer'
    print("✓ Application tracker test passed")

if __name__ == '__main__':
    try:
        test_job_search_agent()
        test_resume_generator()
        test_application_tracker()
        print("\n🎉 All tests passed!")
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)