# GitLab CI/CD Setup for Google Cloud Run Deployment

This guide will help you set up automatic deployment from GitLab to Google Cloud Run.

## Prerequisites

- Google Cloud Project: `directory-app-474617`
- GitLab Repository: `SOSgit-app/SOS-DIRECTORY-APP`
- Google Cloud SDK installed locally

## Step 1: Create Google Cloud Service Account

Run the setup script to create a service account with the necessary permissions:

```bash
chmod +x setup-gcp-service-account.sh
./setup-gcp-service-account.sh
```

This script will:
- Create a service account named `gitlab-ci-deployer`
- Assign required roles for deployment
- Generate and download a service account key

## Step 2: Configure GitLab CI/CD Variables

1. Go to your GitLab project: https://gitlab.com/SOSgit-app/SOS-DIRECTORY-APP
2. Navigate to **Settings** > **CI/CD**
3. Expand the **Variables** section
4. Add the following variable:

| Key | Value | Type | Flags |
|-----|-------|------|-------|
| `GCP_SERVICE_ACCOUNT_KEY` | [Base64 encoded service account key] | Variable | ✓ Protected, ✓ Masked |

### To get the base64 encoded key:

```bash
cat gitlab-ci-key.json | base64 -w 0
```

Copy the output and paste it as the value for `GCP_SERVICE_ACCOUNT_KEY`.

## Step 3: Pipeline Configuration

The `.gitlab-ci.yml` file is already configured with:

- **Trigger**: Automatic deployment on push to `main` branch
- **Target**: Google Cloud Run in `us-central1` region
- **Service**: `roster-app`
- **Resources**: 1GB memory, 1 CPU
- **Scaling**: 1-10 instances (auto-scaling)
- **Access**: Public (unauthenticated)

### Environment Variables Set:
- `SECRET_KEY=roster-production-key`
- `DATABASE_URL=sqlite:///app/roster_data.db`

## Step 4: Deploy

1. Commit and push the `.gitlab-ci.yml` file:
   ```bash
   git add .gitlab-ci.yml
   git commit -m "Add GitLab CI/CD pipeline for Cloud Run deployment"
   git push origin main
   ```

2. Monitor the deployment:
   - Go to your GitLab project
   - Navigate to **CI/CD** > **Pipelines**
   - Watch the deployment progress

## Step 5: Verify Deployment

Once the pipeline completes successfully, your application will be available at:
```
https://roster-app-243571769407.us-central1.run.app
```

## Pipeline Stages

The CI/CD pipeline consists of one stage:

### Deploy Stage
- Authenticates with Google Cloud using service account
- Builds and pushes Docker image to Container Registry
- Deploys to Cloud Run with specified configuration

## Troubleshooting

### Common Issues:

1. **Authentication Failed**
   - Verify the service account key is correctly base64 encoded
   - Ensure the key is added as a GitLab CI/CD variable

2. **Permission Denied**
   - Check that all required roles are assigned to the service account
   - Verify the service account has access to the project

3. **Build Failed**
   - Ensure Dockerfile is present in the repository
   - Check that all required files are committed

4. **Deployment Failed**
   - Verify the Cloud Run API is enabled
   - Check that the service name matches the configuration

### Useful Commands:

```bash
# Check pipeline logs
gitlab-ci-multi-runner logs

# Test deployment locally
gcloud run deploy roster-app --source . --platform managed --region us-central1

# View service account roles
gcloud projects get-iam-policy directory-app-474617 --flatten="bindings[].members" --filter="bindings.members:gitlab-ci-deployer@directory-app-474617.iam.gserviceaccount.com"
```

## Security Notes

- The service account key is stored securely in GitLab CI/CD variables
- The key is base64 encoded and masked in logs
- Only the `main` branch can trigger deployments
- Delete the local service account key file after adding it to GitLab

## Cleanup

After successful setup, you can safely delete:
- `gitlab-ci-key.json` (local file)
- `setup-gcp-service-account.sh` (optional)
