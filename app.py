from flask import Flask, request, jsonify
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

mp_face_mesh = mp.solutions.face_mesh

def detect_face_shape(image):
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if not results.multi_face_landmarks:
            return "Unknown"

        landmarks = results.multi_face_landmarks[0].landmark

        jaw_left = np.array([landmarks[234].x, landmarks[234].y])
        jaw_right = np.array([landmarks[454].x, landmarks[454].y])
        chin = np.array([landmarks[152].x, landmarks[152].y])
        forehead = np.array([landmarks[10].x, landmarks[10].y])

        width = np.linalg.norm(jaw_left - jaw_right)
        length = np.linalg.norm(forehead - chin)

        ratio = width / length

        if ratio > 0.9:
            return "Round"
        elif ratio < 0.75:
            return "Oval"
        else:
            return "Square"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['image']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    face_shape = detect_face_shape(image)

    suggestions = {
        "Round": ["Layered Cut", "Side Part", "Long Bob"],
        "Oval": ["Any Style", "Pixie Cut", "Waves"],
        "Square": ["Soft Curls", "Side Bangs", "Shoulder Length"]
    }

    return jsonify({
        "face_shape": face_shape,
        "suggestions": suggestions.get(face_shape, ["Try another photo"])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
