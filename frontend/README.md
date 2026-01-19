# Frontend Setup

## Quick Start

```bash
./start_frontend.sh
```

Then open http://localhost:8000 in your browser.

## Manual Setup

### 1. Install Dependencies
```bash
pip install flask flask-cors
```

### 2. Start Backend API
```bash
python3 api.py
```

### 3. Start Frontend (in new terminal)
```bash
cd frontend
python3 -m http.server 8000
```

### 4. Open Browser
Navigate to http://localhost:8000

## Features

- **Dashboard**: View stats and recent applications
- **Job Search**: Search and filter jobs with AI matching
- **Applications**: Track all applications and statuses
- **Profile**: Manage your profile and preferences

## API Endpoints

- `GET/POST /api/profile` - User profile
- `POST /api/jobs/search` - Search jobs
- `POST /api/applications/generate` - Generate application
- `GET /api/applications` - List applications
- `PUT /api/applications/:id/status` - Update status
- `POST /api/interview/prep` - Interview preparation
- `POST /api/linkedin/optimize` - LinkedIn optimization
- `POST /api/linkedin/recruiters` - Find recruiters
