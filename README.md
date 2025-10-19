🤖 Handwritten Digit Recognizer (MNIST CNN)

A full-stack web application that uses a Convolutional Neural Network (CNN) to recognize handwritten digits (0–9) drawn by a user in a web browser.

✨ Features

Real-time Drawing: Users can draw digits directly onto an HTML5 Canvas.

Image Preprocessing: The drawn 280 × 280 image is resized and inverted to match the 28 × 28 "white digit on black background" format expected by the MNIST model.

High Accuracy: Utilizes a pre-trained CNN model (based on the MNIST dataset) for fast and reliable predictions.

🛠️ Technology Stack
Component	Technology	Role
Frontend	HTML5 / CSS / JS	Provides the user interface and the interactive drawing canvas
Backend	Python / Flask	Serves the webpage and handles prediction requests
Machine Learning	TensorFlow / Keras	Hosts the pre-trained CNN model
🚀 Getting Started
Prerequisites

Python 3.12x installed

Install required libraries:

pip install flask tensorflow pillow numpy

Installation and Setup

Clone the repository:

git clone https://github.com/mahnoorsohail1418-collab/MNIST-Web-App
cd MNIST-Web-App


Ensure Model File is Present:
Place your trained model file mnist_cnn.h5 in the same directory as your Python script.

Run the Flask server:

python app.py


Open the Web App:
The server usually runs at http://127.0.0.1:5000/. Open this URL in your browser.

✍️ Usage

Draw: Use your mouse to draw a single, centered digit (0–9) on the canvas.

Predict: Click the Predict button. The frontend sends the 28 × 28 image data to the backend.

Result: The predicted digit is displayed below the buttons.

Clear: Click Clear to erase the canvas and start a new drawing.

💡 Key Code Concepts

Frontend (JavaScript):
The preprocessCanvas function resizes the 280 × 280 drawing to 28 × 28 and ensures a solid white background before sending the data.

Backend (Python):
The server loads the Base64 image string, converts it to a NumPy array, inverts colors (Black → White), and normalizes pixel values for the model.

📄 License

This project is licensed under the MIT License
.

📧 Contact

GitHub: mahnoorsohail1418-collab
