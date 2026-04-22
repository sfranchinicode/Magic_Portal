# Magic Portal 

A lightweight Flask-based image portal that allows users to browse and upload images into categorized galleries. Built to demonstrate backend routing, file handling, and simple authentication using environment variables.

---

## Features

- Multi-portal image galleries (e.g. `art`, `photos`)
- Slideshow-style image viewer
- Password-protected uploads per portal
- Automatic HEIC → JPEG conversion
- File type validation for uploads
- Secure filename handling
- Flash messages for user feedback
- Organized static file structure

---

## Tech Stack

- Python 3
- Flask
- Pillow
- pillow-heif
- Werkzeug

---

## Project Structure

Magic_Portal/
├── app.py                  # Main Flask application
├── upload_utils.py         # File validation + image conversion helpers
├── templates/
│   ├── index.html          # Image slideshow page
│   └── upload.html         # Upload interface
├── static/
│   ├── art/                # Art images
│   └── photos/             # Photo images
├── requirements.txt
└── .gitignore

---

## Setup & Installation

### 1. Clone the repository
git clone https://github.com/your-username/magic-portal.git
cd magic-portal

### 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

---

## Environment Variables

Create a `.env` file or set environment variables manually:

FLASK_SECRET_KEY=your_secret_key
ART_PASSWORD=your_art_upload_password
PHOTOS_PASSWORD=your_photos_upload_password
FLASK_DEBUG=1

---

## Running the App

python app.py

Then open in your browser:

http://localhost:5000/art
http://localhost:5000/photos

---

## How It Works

- Each portal maps to a folder inside `static/`
- Images are displayed in a looping slideshow
- Uploads require a portal-specific password
- Files are validated and safely stored
- HEIC images are automatically converted to JPEG

---

## Security Notes

- No hardcoded secrets (uses environment variables)
- Upload filenames are sanitized using Werkzeug
- File extensions are validated before saving
- Flask secret key is not stored in source code
- Debug mode should be disabled in production

---

## Future Improvements

- User authentication system
- Database-backed image storage
- Image compression pipeline
- Upload rate limiting
- Admin dashboard for moderation

---

## Purpose

This project was built as a backend-focused exercise in:

Flask routing and templating
File upload handling
Image processing
Secure configuration practices
