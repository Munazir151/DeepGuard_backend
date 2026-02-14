"""
Hugging Face Spaces entry point for DeepGuard Deepfake Detection API
This file imports the FastAPI app from main.py for HF Spaces compatibility
"""
from main import app

# Hugging Face Spaces will automatically detect and run this FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
