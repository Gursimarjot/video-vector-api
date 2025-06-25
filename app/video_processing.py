
import cv2
import os
from uuid import uuid4

def extract_frames(video_path, output_dir, interval=1):
    os.makedirs(output_dir, exist_ok=True)
    vidcap = cv2.VideoCapture(video_path)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    count = 0
    saved_frames = []

    while True:
        success, frame = vidcap.read()
        if not success:
            break
        if count % (fps * interval) == 0:
            filename = f"{uuid4()}.jpg"
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, frame)
            saved_frames.append(filepath)
        count += 1
    return saved_frames
