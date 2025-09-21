from flask import Flask, request, jsonify
from flask_cors import CORS
import librosa
import numpy as np
import tempfile
import os

app = Flask(__name__)
CORS(app)  # ✅ allow frontend (localhost:3000) to call backend (localhost:5001)


@app.route("/analyze", methods=["POST"])
def analyze_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        file.save(tmp.name)
        tmp_path = tmp.name

    try:
        # Load audio and compute average frequency
        y, sr = librosa.load(tmp_path, sr=None)
        spectrum = np.abs(np.fft.fft(y))
        freqs = np.fft.fftfreq(len(spectrum), 1 / sr)
        dominant_freq = abs(freqs[np.argmax(spectrum)])

        # Decide noise level based on frequency
        if dominant_freq < 100:
            category = "white-noise-low1.mp3"
        elif dominant_freq < 200:
            category = "white-noise-low2.mp3"
        elif dominant_freq < 400:
            category = "white-noise-mid1.mp3"
        elif dominant_freq < 700:
            category = "white-noise-mid2.mp3"
        elif dominant_freq < 1000:
            category = "white-noise-high1.mp3"
        else:
            category = "white-noise-high2.mp3"

        return jsonify({"frequency": float(dominant_freq), "category": category})
    finally:
        os.remove(tmp_path)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
