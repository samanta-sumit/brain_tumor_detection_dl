# brain_tumor_detection_dl

This project focuses on detecting brain tumors from MRI images using a Convolutional Neural Network (CNN) built with TensorFlow and Keras. It classifies brain tumors into three categories: Pituitary, Glioma, and Meningioma.

# Project Pipeline
-Data Collection & Preprocessing

 MRI images loaded and resized
 Image normalization and augmentation

-Model Architecture

 CNN built using Keras with Conv2D, MaxPooling2D, Dense layers, Dropout, etc.-Training & Evaluation

-Model trained on labeled dataset

 Accuracy and loss visualized using matplotlib

-Prediction

 Model used to predict tumor type from new images

-Web Deployment

 Flask app created to upload and predict tumors from user-uploaded MRI scans

# Technologies Used
-Python

-TensorFlow / Keras

-NumPy

-OpenCV

-Flask (for web deployment)

-Matplotlib / Seaborn (for visualization)

-Jupyter Notebook

# Installation
# clone the repository
git clone https://github.com/yourusername/brain-tumor-detection.git

cd brain-tumor-detection

# Create and activate a virtual environmen
python -m venv venv

source venv/bin/activate 

# Install the dependencies
pip install -r requirements.txt

# How To Run 
1. Train the Model
   
   python train_model.py
   
3. Run the Flask App

   python app.py

# Project Structure


brain-tumor-detection/

1.uploads/               # Folder to store uploaded MRI images

2. static/                # Static assets for Flask

3. templates/             # HTML templates

4. model.h5               # Trained model

5. app.py                 # Flask app

6. train_model.py         # Script to train the CNN

7. requirements.txt       # Python dependencies

8. README.md              # Project readme


# Results 
<img width="547" height="255" alt="image" src="https://github.com/user-attachments/assets/bf126ffc-5ebe-407d-ac8b-0517e243f01b" />

<img width="1638" height="803" alt="image" src="https://github.com/user-attachments/assets/0b44b3f1-1bf6-4895-bb43-41e0bf99f208" />

<img width="997" height="840" alt="image" src="https://github.com/user-attachments/assets/aa126cb6-715a-43a2-af39-75089904673f" />

