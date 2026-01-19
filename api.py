#!/usr/bin/env python3
"""Flask API for Job Search Agent System"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import json
from datetime import datetime

sys.path.insert(0, '/tmp/job-search-agent/agents')

from job_search import JobSearchAgent
from resume_generator import ApplicationPackageGenerator
from interview_prep import InterviewPrepAgent
from application_tracker import ApplicationTracker
from linkedin_agent import LinkedInAgent

app = Flask(__name__)
CORS(app)

# Global state
tracker = ApplicationTracker()

@app.route('/api/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        with open('config.json', 'w') as f:
            json.dump({'user_profile': request.json}, f, indent=2)
        return jsonify({'success': True})
    
    with open('config.json') as f:
        return jsonify(json.load(f).get('user_profile', {}))

@app.route('/api/jobs/search', methods=['POST'])
def search_jobs():
    data = request.json
    agent = JobSearchAgent(data)
    jobs = agent.search_jobs(data['keywords'])
    filtered = agent.filter_jobs(jobs)
    return jsonify(filtered)

@app.route('/api/applications/generate', methods=['POST'])
def generate_application():
    data = request.json
    profile = data['profile']
    job = data['job']
    
    gen = ApplicationPackageGenerator(profile)
    package = gen.generate_package(job)
    tracker.add_application(job['title'], job['company'])
    
    return jsonify(package)

@app.route('/api/applications', methods=['GET'])
def get_applications():
    return jsonify(tracker.applications)

@app.route('/api/applications/<int:app_id>/status', methods=['PUT'])
def update_status(app_id):
    status = request.json['status']
    tracker.update_status(app_id, status)
    return jsonify({'success': True})

@app.route('/api/interview/prep', methods=['POST'])
def interview_prep():
    data = request.json
    agent = InterviewPrepAgent(data['profile'], data['job'])
    prep = agent.prepare()
    return jsonify(prep)

@app.route('/api/linkedin/optimize', methods=['POST'])
def linkedin_optimize():
    profile = request.json
    agent = LinkedInAgent(profile)
    result = agent.optimize_profile()
    return jsonify(result)

@app.route('/api/linkedin/recruiters', methods=['POST'])
def find_recruiters():
    data = request.json
    agent = LinkedInAgent(data['profile'])
    recruiters = agent.find_recruiters(data['companies'], data['keywords'])
    return jsonify(recruiters)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
