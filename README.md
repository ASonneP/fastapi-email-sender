# FastAPI Email Sender App

A FastAPI-based application for sending emails using Gmail's SMTP server.

## Features

- Send emails asynchronously using FastAPI and `fastapi-mail`
- Background task support for non-blocking email sending
- Secure environment variable management with `python-dotenv`

## Requirements

- Python 3.10+
- Gmail account with app-specific password or OAuth2 setup

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ASonneP/fastapi-email-sender
   cd fastapi-email-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**

   Create a `.env` file in the root directory and fill it with the following values:

   ```plaintext
   SMTP_USER=your_email@gmail.com
   APP_PASSWORD=your_app_password
   ```

   > Ensure you have generated an [App Password](https://support.google.com/accounts/answer/185833) if using 2-Step Verification.

## Running the Application

1. **Run the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation:**
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Usage

- **Send an Email:**
  - Endpoint: `POST /send-email/`
  - Request Body:
    ```json
    {
      "receiver_email": "sonnep.pilot@gmail.com",
      "subject": "Test Email",
      "body": "This is a test email from FastAPI using Postman."
    }
    ```
