# Deploy DeepGuard Backend on Emergent.sh

## Prerequisites
- GitHub repository: https://github.com/Munazir151/DeepGuard_backend
- Emergent.sh account

## Deployment Steps

### 1. Sign up/Login to Emergent.sh
Visit [emergent.sh](https://emergent.sh) and create an account or log in.

### 2. Create New App
- Click "New App" or "Deploy"
- Select "Import from GitHub"
- Choose the repository: `Munazir151/DeepGuard_backend`
- Select branch: `main`

### 3. Configure Build Settings
- **Framework Preset**: Python
- **Build Command**: (leave empty or use default)
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Python Version**: 3.11 (or the version in runtime.txt)

### 4. Environment Variables
No environment variables required for basic deployment.

### 5. Deploy
- Click "Deploy"
- Wait for the build to complete (may take several minutes due to TensorFlow installation)
- Once deployed, you'll receive a URL like: `https://your-app.emergent.sh`

### 6. Test the Deployment
After deployment, test your backend:
```bash
curl https://your-app.emergent.sh/
```

You should see the API response.

### 7. Update Frontend
Copy your deployed backend URL and update the frontend environment variable:
- Edit `my-app/.env.local`
- Update `NEXT_PUBLIC_API_URL=https://your-app.emergent.sh`

## Troubleshooting

### Build Fails
- Check that all dependencies are in requirements.txt
- Ensure the model file (deepfake_detection_inception.h5) is committed to the repo
- Check build logs for specific errors

### Large Model File
The model file is large (~92MB). If GitHub rejects it:
1. Use Git LFS (Large File Storage)
2. Or host the model file separately (S3, cloud storage)
3. Update main.py to download the model on startup

### Memory Issues
If the app crashes due to memory:
- Upgrade to a larger tier on emergent.sh
- Optimize model loading
- Use model quantization techniques

## Notes
- The app uses TensorFlow which requires significant memory
- Model loading takes time on first startup
- CORS is configured to allow all origins (adjust in production)
