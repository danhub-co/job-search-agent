#!/bin/bash

echo "🚀 Setting up GitHub repository for AI Job Search Agent"
echo "====================================================="

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is required but not installed"
    echo "Install it from: https://cli.github.com/"
    exit 1
fi

# Create GitHub repository
echo "📦 Creating GitHub repository..."
gh repo create ai-job-search-agent --public --description "🤖 Autonomous AI job search system with agents for finding, applying, and tracking opportunities" --clone=false

# Add remote origin
git remote add origin https://github.com/$(gh api user --jq .login)/ai-job-search-agent.git

# Push to GitHub
echo "⬆️ Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Repository created successfully!"
echo "🔗 Repository URL: https://github.com/$(gh api user --jq .login)/ai-job-search-agent"
echo ""
echo "🔧 CI/CD Features:"
echo "  ✓ Automated testing on Python 3.8, 3.9, 3.10"
echo "  ✓ Code linting with flake8"
echo "  ✓ Test coverage reporting"
echo "  ✓ Automated deployment on main branch"
echo "  ✓ Docker containerization"
echo "  ✓ Multi-service deployment with docker-compose"
echo ""
echo "🚀 Next steps:"
echo "  1. Enable GitHub Actions in repository settings"
echo "  2. Add any required secrets for deployment"
echo "  3. Push changes to trigger CI/CD pipeline"