
# FastAPI Video Vector Search App

## 🚀 Features
- Upload videos (`.mp4`) and extract frames every second
- Compute color histogram vectors from each frame
- Store and query frame vectors using Qdrant

## ▶️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Qdrant locally:
```bash
docker run -p 6333:6333 qdrant/qdrant
```

3. Start the FastAPI app:
```bash
uvicorn app.main:app --reload
```

4. Open your browser to:
```
http://localhost:8000/docs
```

## 🧪 API Endpoints

### POST /upload_video
- Upload an `.mp4` file.
- Extracts frames and stores their vectors.

### POST /search_similar
- Upload an image file.
- Returns the most similar frames based on vector similarity.

## 📂 Project Structure
- `app/` – Core FastAPI application
- `frames/` – Where extracted frame images are stored
