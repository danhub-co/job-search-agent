from datetime import datetime, timedelta
import json

class ApplicationTracker:
    def __init__(self):
        self.applications = []
        self.follow_up_rules = {
            'Applied': {'days': 7, 'action': 'Send initial follow-up'},
            'Phone Screen': {'days': 3, 'action': 'Follow up on next steps'},
            'Technical Interview': {'days': 5, 'action': 'Request feedback'},
            'Final Interview': {'days': 3, 'action': 'Check on decision timeline'},
            'Offer': {'days': 2, 'action': 'Respond to offer'}
        }
        
    def add_application(self, job, company, status='Applied'):
        """Track new job application"""
        app = {
            'id': len(self.applications) + 1,
            'job_title': job,
            'company': company,
            'status': status,
            'applied_date': datetime.now().isoformat(),
            'last_contact': datetime.now().isoformat(),
            'follow_ups': [],
            'notes': []
        }
        self.applications.append(app)
        print(f"✓ Tracking: {job} at {company}")
        return app
    
    def update_status(self, app_id, new_status, notes=''):
        """Update application status"""
        app = self._get_app(app_id)
        if app:
            old_status = app['status']
            app['status'] = new_status
            app['last_contact'] = datetime.now().isoformat()
            if notes:
                app['notes'].append({
                    'date': datetime.now().isoformat(),
                    'text': notes
                })
            print(f"✓ Updated {app['company']}: {old_status} → {new_status}")
            return app
        return None
    
    def check_follow_ups(self):
        """Check which applications need follow-up"""
        print("🔍 Checking for required follow-ups...\n")
        
        needs_follow_up = []
        now = datetime.now()
        
        for app in self.applications:
            if app['status'] in ['Rejected', 'Accepted', 'Withdrawn']:
                continue
            
            last_contact = datetime.fromisoformat(app['last_contact'])
            days_since = (now - last_contact).days
            
            rule = self.follow_up_rules.get(app['status'])
            if rule and days_since >= rule['days']:
                needs_follow_up.append({
                    'app': app,
                    'days_since': days_since,
                    'action': rule['action']
                })
        
        return needs_follow_up
    
    def generate_follow_up_email(self, app, action):
        """Generate follow-up email template"""
        templates = {
            'Send initial follow-up': {
                'subject': f"Following up on {app['job_title']} Application",
                'body': f"""Dear Hiring Manager,

I hope this email finds you well. I wanted to follow up on my application for the {app['job_title']} position at {app['company']}, which I submitted on {datetime.fromisoformat(app['applied_date']).strftime('%B %d, %Y')}.

I remain very interested in this opportunity and would welcome the chance to discuss how my skills and experience align with your team's needs.

Please let me know if you need any additional information from me.

Thank you for your consideration.

Best regards,
[Your Name]"""
            },
            'Follow up on next steps': {
                'subject': f"Next Steps - {app['job_title']} Position",
                'body': f"""Dear [Interviewer Name],

Thank you for taking the time to speak with me about the {app['job_title']} position. I enjoyed learning more about {app['company']} and the team.

I wanted to follow up on the next steps in the interview process. I'm very excited about this opportunity and look forward to continuing our conversation.

Please let me know if you need any additional information.

Best regards,
[Your Name]"""
            },
            'Request feedback': {
                'subject': f"Following up - {app['job_title']} Interview",
                'body': f"""Dear [Interviewer Name],

I wanted to follow up on my recent interview for the {app['job_title']} position at {app['company']}.

I remain very interested in this role and would appreciate any updates on the hiring timeline or next steps.

Thank you for your time and consideration.

Best regards,
[Your Name]"""
            },
            'Check on decision timeline': {
                'subject': f"Decision Timeline - {app['job_title']} Position",
                'body': f"""Dear [Hiring Manager],

I wanted to check in regarding the {app['job_title']} position. I'm very enthusiastic about the opportunity to join {app['company']} and contribute to the team.

Could you provide an update on the decision timeline?

Thank you for your consideration.

Best regards,
[Your Name]"""
            },
            'Respond to offer': {
                'subject': f"Re: Offer for {app['job_title']} Position",
                'body': f"""Dear [Hiring Manager],

Thank you for extending the offer for the {app['job_title']} position at {app['company']}. I'm excited about this opportunity.

I would like to discuss [compensation/start date/benefits] before making my final decision. Would you be available for a call this week?

Thank you again for this opportunity.

Best regards,
[Your Name]"""
            }
        }
        
        return templates.get(action, {
            'subject': f"Following up - {app['job_title']}",
            'body': f"Following up on {app['job_title']} at {app['company']}"
        })
    
    def auto_follow_up(self):
        """Automatically generate and log follow-ups"""
        follow_ups = self.check_follow_ups()
        
        if not follow_ups:
            print("✓ No follow-ups needed at this time\n")
            return []
        
        print(f"📧 Generating {len(follow_ups)} follow-up emails...\n")
        
        emails = []
        for item in follow_ups:
            app = item['app']
            email = self.generate_follow_up_email(app, item['action'])
            
            # Log follow-up
            app['follow_ups'].append({
                'date': datetime.now().isoformat(),
                'action': item['action'],
                'email_sent': True
            })
            
            emails.append({
                'app_id': app['id'],
                'company': app['company'],
                'job_title': app['job_title'],
                'days_since_contact': item['days_since'],
                'email': email
            })
            
            print(f"✓ Generated follow-up for {app['company']} ({item['days_since']} days)")
        
        return emails
    
    def get_statistics(self):
        """Get application statistics"""
        stats = {
            'total': len(self.applications),
            'by_status': {},
            'response_rate': 0,
            'avg_response_time': 0
        }
        
        for app in self.applications:
            status = app['status']
            stats['by_status'][status] = stats['by_status'].get(status, 0) + 1
        
        # Calculate response rate
        responded = sum(1 for app in self.applications if app['status'] != 'Applied')
        if stats['total'] > 0:
            stats['response_rate'] = f"{(responded / stats['total'] * 100):.1f}%"
        
        return stats
    
    def display_dashboard(self):
        """Display application tracking dashboard"""
        print("\n" + "=" * 70)
        print("📊 APPLICATION DASHBOARD")
        print("=" * 70)
        
        stats = self.get_statistics()
        print(f"\nTotal Applications: {stats['total']}")
        print(f"Response Rate: {stats['response_rate']}")
        print("\nBy Status:")
        for status, count in stats['by_status'].items():
            print(f"  • {status}: {count}")
        
        print("\n" + "=" * 70)
        print("📋 ACTIVE APPLICATIONS")
        print("=" * 70)
        
        active = [a for a in self.applications if a['status'] not in ['Rejected', 'Accepted', 'Withdrawn']]
        
        for app in active:
            days_since = (datetime.now() - datetime.fromisoformat(app['last_contact'])).days
            print(f"\n{app['id']}. {app['job_title']} at {app['company']}")
            print(f"   Status: {app['status']}")
            print(f"   Last Contact: {days_since} days ago")
            print(f"   Follow-ups: {len(app['follow_ups'])}")
    
    def _get_app(self, app_id):
        """Get application by ID"""
        for app in self.applications:
            if app['id'] == app_id:
                return app
        return None
    
    def save_data(self, filename='/tmp/applications.json'):
        """Save tracking data"""
        with open(filename, 'w') as f:
            json.dump(self.applications, f, indent=2)
        print(f"\n💾 Saved tracking data: {filename}")


if __name__ == "__main__":
    print("🎯 Application Status Tracker with Auto Follow-ups\n")
    print("=" * 70)
    
    # Initialize tracker
    tracker = ApplicationTracker()
    
    # Add sample applications with different dates
    print("\n📝 Adding applications...\n")
    
    # Recent application
    app1 = tracker.add_application("Senior Python AI Engineer", "Amazon Web Services")
    
    # Application needing follow-up (simulate 8 days ago)
    app2 = tracker.add_application("Machine Learning Engineer", "Google")
    app2['applied_date'] = (datetime.now() - timedelta(days=8)).isoformat()
    app2['last_contact'] = (datetime.now() - timedelta(days=8)).isoformat()
    
    # Application in phone screen (simulate 4 days ago)
    app3 = tracker.add_application("AI Research Scientist", "Microsoft")
    app3['status'] = 'Phone Screen'
    app3['last_contact'] = (datetime.now() - timedelta(days=4)).isoformat()
    
    # Application in technical interview (simulate 6 days ago)
    app4 = tracker.add_application("Data Scientist", "Meta")
    app4['status'] = 'Technical Interview'
    app4['last_contact'] = (datetime.now() - timedelta(days=6)).isoformat()
    
    # Recent application
    app5 = tracker.add_application("Backend Engineer", "Netflix")
    
    # Display dashboard
    tracker.display_dashboard()
    
    # Check and generate follow-ups
    print("\n" + "=" * 70)
    print("🔔 AUTO FOLLOW-UP SYSTEM")
    print("=" * 70 + "\n")
    
    emails = tracker.auto_follow_up()
    
    # Display generated emails
    if emails:
        print("\n" + "=" * 70)
        print("📧 GENERATED FOLLOW-UP EMAILS")
        print("=" * 70)
        
        for email_data in emails[:2]:  # Show first 2
            print(f"\n{'─' * 70}")
            print(f"To: {email_data['company']} ({email_data['job_title']})")
            print(f"Days Since Contact: {email_data['days_since_contact']}")
            print(f"{'─' * 70}")
            print(f"\nSubject: {email_data['email']['subject']}\n")
            print(email_data['email']['body'])
    
    # Update some statuses
    print("\n" + "=" * 70)
    print("🔄 STATUS UPDATES")
    print("=" * 70 + "\n")
    
    tracker.update_status(1, 'Phone Screen', 'Recruiter called, technical interview scheduled')
    tracker.update_status(3, 'Technical Interview', 'Completed coding challenge')
    
    # Final dashboard
    tracker.display_dashboard()
    
    # Save data
    tracker.save_data()
    
    # Statistics
    print("\n" + "=" * 70)
    print("📈 STATISTICS")
    print("=" * 70)
    stats = tracker.get_statistics()
    print(json.dumps(stats, indent=2))
