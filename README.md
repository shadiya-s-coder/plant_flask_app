# 🌱 Plant Disease Prediction using CNN
  A deep learning-based **Plant Disease Prediction Web Application** built using **Python, TensorFlow/Keras, and Flask**. The application allows users to upload a plant leaf image and uses a trained Convolutional Neural Network (CNN) model to predict whether the plant is **Healthy** or **Diseased**.

## TO HAVE A DEMO
Download all the files locally.
Type the below comment lines in command prompt.
Open your browser and visit: http://127.0.0.1:5000/

## PROJECT OVERVIEW
  Plant diseases can significantly affect crop production and plant health. This project uses **Deep Learning and Computer Vision** to automatically analyze plant leaf images and predict their health condition.
  The trained CNN model is integrated into a **Flask web application**, providing a simple and user-friendly interface for image upload and prediction.

## FEATURES
* 🌿 Upload a plant leaf image
* 🤖 CNN-based image classification
* 🔍 Predicts plant health condition
* 📊 Displays prediction results through a web interface
* 🎨 Responsive and user-friendly Flask interface
* 📁 Organized HTML templates and CSS styling
* 🧠 Trained deep learning model using TensorFlow/Keras

## TECHNOLOGIES USED
* **Python**
* **Flask**
* **TensorFlow**
* **Keras**
* **NumPy**
* **Pillow**
* **HTML5**
* **CSS3**
* **Gunicorn**

## MACHINE LEARNING MODEL
  The application uses a trained **Convolutional Neural Network (CNN)** model saved as: cnn_model.keras
  The model processes the uploaded plant image and predicts its corresponding class.

### PREDICTION CLASSES
   * ✅ Healthy
   * ❌ Diseased

## PROJECT STRUCTURE
plant_flask_app/
│
├── app.py
├── cnn_model.keras
├── requirements.txt
├── .python-version
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── uploads/
│
└── templates/
    ├── base.html
    ├── index.html
    ├── detection.html
    ├── plant_health.html
    ├── about.html
    └── how_it_works.html
    
## INSTALLATION AND SETUP
```bash
git clone https://github.com/shadiya-s-coder/plant_flask_app.git
```
```bash
cd plant_flask_app
```
```bash
python -m venv venv
```
**Windows:**
```bash
venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```
```bash
python app.py
```

## HOW IT WORKS
1. User opens the Plant Disease Prediction web application.
2. User uploads a plant leaf image.
3. Flask receives the uploaded image.
4. The image is processed and prepared for the CNN model.
5. The trained CNN model analyzes the image.
6. The application displays the predicted plant health condition.

## FUTURE IMPROVEMENTS
* Support for more plant species and diseases
* Improve model accuracy using a larger dataset
* Add confidence scores to predictions
* Deploy the application using a higher-memory cloud platform
* Add real-time plant disease detection using a camera
* Expand the model to identify specific types of plant diseases

## PROJECT PURPOSE
  This project demonstrates the practical application of:
* Deep Learning
* Convolutional Neural Networks
* Image Classification
* Computer Vision
* Flask Web Development
* Model Deployment Integration

## PROJECT
This project was developed as a practical Machine Learning and Deep Learning project demonstrating the integration of a trained CNN model with a Flask web application.
