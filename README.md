# Face Vector API

A **FastAPI** application to extract **face embeddings (vectors)** from images using [DeepFace](https://github.com/serengil/deepface). Supports **single or multiple faces** in an image and returns **one vector per detected face**.

---

## Features

* Extract face vectors from any image URL.
* Supports **multiple faces** in the same image.
* Returns **JSON response** with vectors.
* Uses **ArcFace** or **Facenet** models for embeddings.
* Can easily be extended to store vectors in a database.

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/face-vector-api.git
cd face-vector-api
```

2. **Create a virtual environment**

```powershell
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

1. **Run the FastAPI server**

```bash
uvicorn main:app --reload
```

2. **Test the API**
   Open [Swagger UI](http://127.0.0.1:8000/docs) or use **Postman**.

3. **POST request example**

```http
POST /extract-vectors/
Content-Type: application/json

{
  "url": "https://raw.githubusercontent.com/ageitgey/face_recognition/master/examples/obama.jpg"
}
```

**Response example**

```json
{
  "url": "https://raw.githubusercontent.com/ageitgey/face_recognition/master/examples/obama.jpg",
  "num_faces": 1,
  "vectors": [
    [0.123, -0.456, 0.789, ...]   // 512-d vector (ArcFace)
  ]
}
```

---

## Supported Models

| Model Name | Vector Dimension |
| ---------- | ---------------- |
| Facenet    | 128              |
| ArcFace    | 512              |
| VGG-Face   | 2622             |
| OpenFace   | 128              |
| DeepFace   | 4096             |

> You can change the model in `main.py` by modifying the `model_name` parameter in `DeepFace.represent()`.

---

## Notes

* If **no faces are detected**, the API returns:

```json
{
  "num_faces": 0,
  "vectors": []
}
```

* Recommended to keep your **virtual environment outside the project folder**.
* Can be extended to store vectors in a **database** for face recognition or search.

---

## Requirements

* Python 3.10+
* FastAPI
* Uvicorn
* DeepFace
* Pillow
* Requests
* NumPy

> All dependencies are listed in `requirements.txt`.

---

## License

MIT License
