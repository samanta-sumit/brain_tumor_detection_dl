from flask import Flask,render_template,request,send_from_directory
from tensorflow.keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

#creat app

app= Flask(__name__)

# load model
model= load_model("model.h5")

# calsses labels 
class_labels=['pitutary','glioma','meningioma']

#define the foldd upload folder
UPLOAD_FOLDER = "./uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

# Helper function to predict tumor type
def predict_tumor(image_path):
    IMAGE_SIZE = 128
    img = load_img(image_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    img_array = img_to_array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    confidence_score = np.max(predictions, axis=1)[0]

    if class_labels[predicted_class_index] == 'notumor':
        return "No Tumor", confidence_score
    else:
        return f"Tumor: {class_labels[predicted_class_index]}", confidence_score


# routes

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # handle upload 
        file = request.files['file']

        if file:
            #save the file 
            file_location = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
            file.save(file_location)



            # predict result

            result,confidence = predict_tumor(file_location)

            # Return result along with image path for display
            return render_template('index.html', result=result, confidence=f"{confidence*100:.2f}%", file_path=f'/uploads/{file.filename}')

    return render_template('index.html', result=None) 

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def get_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)