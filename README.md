# CodeReview AI

Automated code analysis and refactoring powered by generative AI.

## Overview

CodeReview AI is an intelligent tool that helps developers write cleaner and more secure code. By leveraging the Gemini 2.0 Flash model, the application acts as an automated pair programmer. It evaluates code snippets submitted via the web interface, scores the overall quality, highlights specific issues categorized by severity, and provides a fully refactored version of the code. The system is designed for speed and simplicity to ensure developers can seamlessly integrate it into their daily workflows.

## Features

* **Multi Language Support:** Analyze code in Python, JavaScript, TypeScript, Java, Go, C++, Rust, and PHP.
* **Instant AI Feedback:** Get a code quality score out of 10 and a one line summary assessment.
* **Granular Issue Tracking:** Identify critical bugs, warnings, and structural suggestions with line specific details.
* **Actionable Solutions:** View a "Quick fix" and a "Best fix" for every detected issue.
* **Automated Refactoring:** Receive a complete, improved version of your submitted code.
* **Review History:** Automatically save and retrieve past code reviews using MongoDB.
* **Modern Interface:** A sleek dark themed UI optimized for developer experience and readability.

## Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | HTML5, Vanilla JavaScript, CSS3 |
| **Backend** | Python, FastAPI, Uvicorn |
| **AI Integration** | LangChain, Google Gemini 2.0 Flash (`langchain-google-genai`) |
| **Database** | MongoDB (`pymongo`) |
| **Configuration** | `python-dotenv` |

## Architecture

The system follows a straightforward client server architecture. The frontend sends raw code and language metadata to the FastAPI backend. The backend constructs a prompt using LangChain and queries the Gemini API. The structured JSON response is then parsed, saved to MongoDB, and returned to the frontend for rendering.

```mermaid
graph TD
    A[Frontend UI] -->|POST /api/review| B(FastAPI Server)
    B --> C{LangChain Prompt}
    C -->|API Request| D[Gemini 2.0 Flash]
    D -->|JSON Response| C

Project Structure
.
├── app/
│   ├── db/
│   │   └── mongo.py            # MongoDB connection and collection setup
│   ├── routes/
│   │   └── review.py           # API endpoints (/review, /history)
│   ├── services/
│   │   └── llm_service.py      # LangChain setup and Gemini prompt templates
│   ├── main.py                 # FastAPI application entry point
│   └── mongo.py                # Duplicate/Alias DB connection file
├── .vscode/                    # VSCode C/C++ runner configurations
├── index.html                  # Main frontend interface
├── requirement.txt             # Python dependencies
└── .gitignore                  # Git ignore rules
Installation
Follow these steps to run the application locally.

Clone the repository:

Bash
git clone [https://github.com/vaibhavidhenge23/code-reviewer.git](https://github.com/vaibhavidhenge23/code-reviewer.git)
cd code-reviewer
Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirement.txt
Set up environment variables:
Create a .env file in the root directory and add the following keys:

Code snippet
MONGO_URI=your_mongodb_connection_string
GEMINI_API_KEY=your_google_gemini_api_key
Usage
Start the backend server:

Bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
The API will be available at http://127.0.0.1:8000.

Launch the frontend:
Open index.html directly in your web browser.

Review Code:
Select your programming language from the sidebar, paste your code into the editor (or upload a file), and click the "Review" button to see the analysis.

Configuration
The application relies on two primary environment variables stored in the .env file:

MONGO_URI: The connection string for your MongoDB instance (local or Atlas). The app automatically creates a database named codereview and a collection named reviews.

GEMINI_API_KEY: Your authentication key for Google's Generative AI services.

API Modules
POST /api/review
Accepts a JSON payload containing code and language. Returns a structured review containing a score, summary, list of issues, and refactored code.
Payload:

JSON
{
  "code": "def hello(): print('world')",
  "language": "python"
}
GET /api/history
Fetches the 10 most recent code reviews from the MongoDB database, sorted by creation date in descending order.
Contributing
Contributions are welcome. If you have an idea for an improvement or found a bug, please follow these steps:

Fork the project.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

Roadmap
Implement GPT-4o and Claude agent integrations.

Add user authentication and personalized review histories.

Support bulk repository scanning and GitHub webhook integrations.

Add exporting capabilities for review reports (PDF/Markdown).

License
Distributed under the MIT License. See LICENSE for more information.
