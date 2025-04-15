# Language Learning Portal Backend

This is the backend server for the Language Learning Portal, built with Flask and SQLite.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

## Running the Server

To start the development server:
```bash
python app.py
```

The server will run on `http://localhost:5000`

## API Endpoints

- `GET /words` - Get all words
- `GET /words/:id` - Get a specific word
- `GET /groups` - Get all groups
- `GET /groups/:id` - Get a specific group
- `GET /groups/:id/words` - Get all words in a specific group

## Database Schema

The database contains the following tables:
- words
- word_groups
- groups
- study_sessions
- study_activities
- word_review_items

See Technical-Specs.md for detailed schema information. 