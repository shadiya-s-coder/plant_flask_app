from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
import numpy as np
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "cnn_model.keras"
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "static",
    "uploads"
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}


def allowed_file(filename):

    return (
        "." in filename
        and
        filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


model = load_model(MODEL_PATH)

print("CNN model loaded successfully!")

class_names = [
    "disease",
    "healthy"
]

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

@app.route(
    "/detection",
    methods=["GET", "POST"]
)
def detection():

    prediction = None
    confidence = None
    image_path = None
    error = None

    if request.method == "POST":

        if "plant_image" not in request.files:

            error = "Please select a plant image."

            return render_template(
                "detection.html",
                error=error
            )


        file = request.files["plant_image"]

        if file.filename == "":

            error = "Please select a plant image."

            return render_template(
                "detection.html",
                error=error
            )

        if not allowed_file(file.filename):

            error = (
                "Invalid file type. "
                "Please upload JPG, JPEG, PNG or WEBP."
            )

            return render_template(
                "detection.html",
                error=error
            )

        filename = secure_filename(
            file.filename
        )

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        img = image.load_img(
            filepath,
            target_size=(224, 224)
        )

        img_array = image.img_to_array(
            img
        )

        img_array = img_array / 255.0

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        prediction_value = model.predict(
            img_array,
            verbose=0
        )


        probability = float(
            prediction_value[0][0]
        )

        if probability >= 0.5:

            prediction = class_names[1]

            confidence = probability * 100

        else:

            prediction = class_names[0]

            confidence = (1 - probability) * 100

        image_path = url_for(
            "static",
            filename=f"uploads/{filename}"
        )

    return render_template(
        "detection.html",
        prediction=prediction,
        confidence=confidence,
        image_path=image_path,
        error=error
    )

@app.route("/how-it-works")
def how_it_works():

    return render_template(
        "how_it_works.html"
    )

@app.route("/plant-health")
def plant_health():

    return render_template(
        "plant_health.html"
    )


@app.route("/about")
def about():

    return render_template(
        "about.html"
    )

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )