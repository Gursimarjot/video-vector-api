
from fastapi import FastAPI, File, UploadFile, HTTPException
from app.video_processing import extract_frames
from app.feature_extraction import compute_color_histogram
from app.qdrant_client import create_collection_if_not_exists, upload_vector, search_similar
from app.utils import ensure_dir_exists, generate_unique_filename, save_upload_file
import os

print("main.py started")

app = FastAPI()
create_collection_if_not_exists()

@app.post("/upload_video")
async def upload_video(file: UploadFile = File(...)):
    ensure_dir_exists("frames")
    video_filename = generate_unique_filename(".mp4")
    save_upload_file(file, video_filename)

    frame_paths = extract_frames(video_filename, "frames")
    os.remove(video_filename)

    for i, frame in enumerate(frame_paths):
        vec = compute_color_histogram(frame)
        upload_vector(i, vec, {"path": frame})

    return {"message": f"Processed {len(frame_paths)} frames"}

@app.post("/search_similar")
async def search_similar_frames(file: UploadFile = File(...)):
    ensure_dir_exists("frames")
    image_filename = generate_unique_filename(".jpg")
    save_upload_file(file, image_filename)

    vec = compute_color_histogram(image_filename)
    results = search_similar(vec)
    os.remove(image_filename)

    return [
        {"frame": r.payload["path"], "score": r.score}
        for r in results
    ]
