@echo off
echo Deploying USAF SOS Student Directory to Google Cloud Run...
echo.

gcloud config set project directory-app-474617

echo Building and deploying to Cloud Run...
gcloud run deploy roster-app ^
  --source . ^
  --region us-central1 ^
  --platform managed ^
  --allow-unauthenticated ^
  --port 8080 ^
  --memory 1Gi ^
  --cpu 1 ^
  --max-instances 10 ^
  --min-instances 1 ^
  --set-env-vars "GOOGLE_CLOUD_PROJECT=directory-app-474617"

echo.
echo Deployment complete!
echo Your application is available at: https://roster-app-243571769407.us-central1.run.app
echo.
pause
