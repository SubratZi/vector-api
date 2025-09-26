from fastapi import FastAPI
from pydantic import BaseModel
from deepface import DeepFace
import requests
from PIL import Image
import io
import numpy as np

app = FastAPI()

class ImageURL(BaseModel):
    url: str

def get_face_vectors(url: str):
    response = requests.get(url)
    response.raise_for_status()
    image = Image.open(io.BytesIO(response.content)).convert("RGB")
    image_np = np.array(image)


    detections = DeepFace.extract_faces(
        img_path=image_np,
        detector_backend="retinaface",
        enforce_detection=False 
    )

    if not detections:
        return []

    vectors = []
    for face in detections:
        cropped_face = face["face"]
        embedding = DeepFace.represent(
            img_path=cropped_face,
            model_name="ArcFace",
            enforce_detection=False
        )[0]["embedding"]
        vectors.append(embedding)

    return vectors

@app.post("/generate-embeddings/")
def extract_vectors(data: ImageURL):
    try:
        vectors = get_face_vectors(data.url)
        if not vectors:
            return {"embeddings": []}
        return {
            "embeddings": vectors
        }
    except Exception as e:
        return {"error": str(e)}