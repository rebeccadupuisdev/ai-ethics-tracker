# AI Ethics Tracker

Tracker of AI ethics incidents (algorithmic bias, unethical data usage, privacy violations, AI discrimination, environmental impact, etc.), using FastAPI, MongoDB and Beanie

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AI-Ethics-Tracker.git
cd AI-Ethics-Tracker
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

## Development

- The application uses FastAPI as the web framework
- Frontend templates are located in `app/frontend/templates/`
- Main application logic is in `app/main.py`
- Views are organized in `app/views/`
