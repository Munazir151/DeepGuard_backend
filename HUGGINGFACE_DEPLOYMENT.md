# Deploy DeepGuard Backend on Hugging Face Spaces 🤗

## Why Hugging Face Spaces?

- ✅ **Free hosting** for ML/AI applications
- ✅ **Optimized for TensorFlow** and ML models
- ✅ **Automatic Docker deployment**
- ✅ **Built-in GPU support** (optional)
- ✅ **Easy integration** with frontends
- ✅ **Public API access**

## Prerequisites

- Hugging Face account (free): https://huggingface.co/join
- GitHub repository: https://github.com/Munazir151/DeepGuard_backend

---

## 🚀 Deployment Steps

### Step 1: Create a Hugging Face Space

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Fill in details:
   - **Space name**: `deepguard-backend` (or your choice)
   - **License**: MIT
   - **Select SDK**: **Docker**
   - **Space visibility**: Public (or Private)

4. Click **"Create Space"**

### Step 2: Connect Your GitHub Repository

You have two options:

#### Option A: Upload Files Directly

1. In your new Space, click **"Files and versions"**
2. Click **"Add file"** → **"Upload files"**
3. Upload all backend files:
   - `main.py`
   - `app.py`
   - `requirements.txt`
   - `Dockerfile`
   - `README.md` (with YAML frontmatter)
   - `deepfake_detection_inception.h5` (the model file)

4. Click **"Commit changes to main"**

#### Option B: Git Clone and Push (Recommended)

```bash
# Clone your new Space
git clone https://huggingface.co/spaces/YOUR_USERNAME/deepguard-backend
cd deepguard-backend

# Copy all files from your GitHub backend folder
# Then push to Hugging Face
git add .
git commit -m "Initial deployment: DeepGuard API"
git push
```

### Step 3: Wait for Build

- Hugging Face will automatically detect the Dockerfile
- Build typically takes 3-5 minutes (TensorFlow installation)
- Watch the build logs in the **"Logs"** tab
- Status will change from "Building" → "Running"

### Step 4: Get Your API URL

Once deployed, your API will be available at:
```
https://YOUR_USERNAME-deepguard-backend.hf.space
```

Example endpoints:
- `https://YOUR_USERNAME-deepguard-backend.hf.space/` - Health check
- `https://YOUR_USERNAME-deepguard-backend.hf.space/models` - List models
- `https://YOUR_USERNAME-deepguard-backend.hf.space/predict` - Upload image
- `https://YOUR_USERNAME-deepguard-backend.hf.space/docs` - Interactive API docs

---

## 🧪 Testing Your Deployment

### Test via cURL
```bash
# Health check
curl https://YOUR_USERNAME-deepguard-backend.hf.space/

# Get available models
curl https://YOUR_USERNAME-deepguard-backend.hf.space/models

# Upload image for prediction
curl -X POST "https://YOUR_USERNAME-deepguard-backend.hf.space/predict" \
  -F "file=@test_image.jpg"
```

### Test via Browser
Visit the interactive API docs:
```
https://YOUR_USERNAME-deepguard-backend.hf.space/docs
```

You can test all endpoints directly from the browser!

---

## 🔧 Configuration Files Explained

### README.md (YAML Frontmatter)
```yaml
---
title: DeepGuard Deepfake Detection API
emoji: 🔍
sdk: docker
app_port: 7860
---
```
This tells HF Spaces:
- SDK: Use Docker (not Gradio/Streamlit)
- Port: 7860 (HF Spaces default)

### Dockerfile
Already configured to:
- Install TensorFlow and dependencies
- Copy model file
- Expose port 7860
- Run FastAPI with uvicorn

### app.py
Entry point that imports your FastAPI app from `main.py`

---

## 📝 Update Frontend Configuration

After deployment, update your frontend:

1. Open `my-app/.env.local`
2. Update the API URL:
   ```env
   NEXT_PUBLIC_API_URL=https://YOUR_USERNAME-deepguard-backend.hf.space
   ```
3. Restart your Next.js dev server

---

## ⚡ Performance & Limits

### Free Tier (CPU)
- ✅ Perfect for demos and testing
- ⚡ ~2-3 seconds per prediction
- 💾 Model loads on first request (~30 seconds)
- 🔄 Auto-sleeps after 48 hours of inactivity

### Upgrade Options
If you need better performance:
- **Persistent**: Keep Space always running ($0.03/hour)
- **GPU Upgrade**: Enable GPU for faster inference
  - Settings → Hardware → Select GPU tier

---

## 🐛 Troubleshooting

### Build Fails
**Problem**: Build timeout or memory error

**Solutions**:
1. Check Dockerfile syntax
2. Verify all files uploaded correctly
3. Ensure model file is present
4. Check build logs for specific errors

### Space Shows "Building" Forever
**Problem**: Build stuck

**Solutions**:
1. Click "Factory Reboot" in settings
2. Or: Delete and recreate the Space
3. Check if model file is too large (>2GB may cause issues)

### API Returns 503 Error
**Problem**: Space is sleeping or loading model

**Solutions**:
1. First request takes 30-60 seconds (model loading)
2. Wait and retry
3. Check logs for errors
4. Enable "Persistent" mode in settings

### CORS Errors from Frontend
**Problem**: Browser blocking requests

**Solution**: Already configured in `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📊 Monitoring & Logs

- **View Logs**: Click "Logs" tab in your Space
- **Check Status**: Top of Space shows "Running" or "Building"
- **API Metrics**: Settings → Usage & Metrics

---

## 🔒 Security Considerations

### Public Spaces
- Your Space is public by default
- API is accessible to anyone
- Good for demos and portfolios

### Private Spaces
If you need private deployment:
1. Settings → Visibility → Private
2. Access requires authentication
3. Good for production apps

### Rate Limiting
Consider adding rate limiting for production:
```python
from slowapi import Limiter
# Add to main.py
```

---

## 🎯 Next Steps

1. ✅ **Deploy** your Space on Hugging Face
2. ✅ **Test** all API endpoints
3. ✅ **Update** frontend `.env.local` with your Space URL
4. ✅ **Test** frontend → backend connection
5. 🚀 **Deploy** frontend to Vercel/Netlify

---

## 💡 Tips

- **Model Loading**: First API call takes longer (model loading)
- **Keep Alive**: Enable "Persistent" to avoid cold starts
- **Updates**: Just push to your Space's Git repo to update
- **Versioning**: Use Git tags/branches for versions
- **Documentation**: The `/docs` endpoint is great for sharing

---

## 📚 Resources

- [Hugging Face Spaces Docs](https://huggingface.co/docs/hub/spaces)
- [FastAPI on HF Spaces](https://huggingface.co/docs/hub/spaces-sdks-docker-fastapi)
- [Docker SDK Guide](https://huggingface.co/docs/hub/spaces-sdks-docker)

---

## ✅ Checklist

Before deployment, ensure:
- [ ] All files are in the repository
- [ ] README.md has YAML frontmatter
- [ ] Dockerfile exposes port 7860
- [ ] Model file is included
- [ ] requirements.txt is complete
- [ ] CORS is enabled in main.py

After deployment:
- [ ] Space shows "Running" status
- [ ] API endpoints respond correctly
- [ ] `/docs` page loads
- [ ] Image upload works
- [ ] Frontend can connect to API

---

**Your backend is now ready for Hugging Face deployment! 🎉**
