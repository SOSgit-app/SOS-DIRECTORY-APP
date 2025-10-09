# USAF SOS Student Directory

A web application for searching Squadron Officer School student information and viewing building maps.

## Features

- Student search functionality
- Real-time search results
- Building floor maps
- Responsive design for mobile devices
- Air Force themed interface

## Prerequisites

- Python 3.9 or higher
- Docker (for containerized deployment)
- Firebase project (for data storage)
- Git

## Local Development Setup

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd student-directory-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Firebase:
   - Go to the [Firebase Console](https://console.firebase.google.com/)
   - Create a new project named "student-directory-app"
   - Go to Project Settings > Service Accounts
   - Generate a new private key
   - Copy the contents to your `.env` file

5. Create `.env` file:
   - Copy the `.env.example` template
   - Fill in your Firebase credentials

6. Run the application:
   ```bash
   python app.py
   ```

## Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t student-directory-app .
   ```

2. Run the container:
   ```bash
   docker run -p 8080:8080 --env-file .env student-directory-app
   ```

## Google Cloud App Engine Deployment

1. Install Google Cloud SDK
2. Authenticate with your Google Cloud account:
   ```bash
   gcloud auth login
   ```
3. Set your project:
   ```bash
   gcloud config set project directory-app-474617
   ```
4. Deploy to App Engine:
   ```bash
   gcloud app deploy
   ```

## Environment Variables

Create a `.env` file with the following variables:
```
FIREBASE_PROJECT_ID=directory-app-474617
FIREBASE_PRIVATE_KEY_ID=your-private-key-id
FIREBASE_PRIVATE_KEY="your-private-key"
FIREBASE_CLIENT_EMAIL=your-client-email
FIREBASE_CLIENT_ID=your-client-id
FIREBASE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
FIREBASE_TOKEN_URI=https://oauth2.googleapis.com/token
FIREBASE_AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
FIREBASE_CLIENT_X509_CERT_URL=your-client-cert-url
```

## Project Structure

```
student-directory-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── app.yaml              # App Engine configuration
├── .env                  # Environment variables
├── .gitignore           # Git ignore rules
├── static/              # Static files
│   ├── sos-logo.png
│   ├── SOSfirstfloorX.png
│   └── SOSsecondfloorX.png
└── templates/           # HTML templates
    └── index.html
```

## Security Notes

- Never commit the `.env` file or any sensitive credentials
- Keep Firebase credentials secure
- Update dependencies regularly for security patches
- Use HTTPS in production

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 

## Container Image URL

gcr.io/directory-app-474617/roster-app
