# Mystical Vision 👁️

Mystical Vision is a **simple**, **adaptable**, and **efficiently optimized even with less resources** for AI/ML-powered image classification tool designed to streamline your image analysis workflows. Built with Python and leveraging CNN-based image classifiers, it empowers you to effortlessly manage data labeling, train custom models, and accurately predict image classes. Whether you're a student, researcher, or enthusiast, Mystical Vision provides an intuitive platform to explore the world of image recognition.

> Developed it for my 11th Standard CBSE Final Examination Project.
## Features 

- **Data Labeling:** Folder based data input for process of preparing your image datasets for training.
- **Custom Model Training:** Generate tailored data models using your own datasets and configurations.
- **Adaptable to Diverse Datasets:**  Easily configurable to work with various image datasets for generating specialized models.
- **Pre-trained Model Support:** Utilize readily available pre-trained models for quick and efficient class prediction.
- **Versatile Applications:** Applicable to diverse fields including: 
     - Medical Imaging Analysis (e.g., Brain Tumor, Lung Cancer, Skin Cancer detection) 
     - Object Recognition (e.g., Food classification)
     - Expression Analysis (e.g., Human Face Expressions, Dog Emotions, Mask Detection)
     - And many more as imagined.
- **User-Friendly Interface:** Usable with a simple user interface with standard navigation, built using PyQt5.
- **Cross-Platform Compatibility:** Runs seamlessly on Windows, macOS, and Linux, due the use of standard Python libraries.

---
## Usage 📋

1. **Download or Clone from GitHub:**  
	```
	git clone https://github.com/SuhasSP-SSP/MysticalVision 
	```
	
	```
	cd MysticalVision
	```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application:** Execute the `MysticalVision.py` to launch the Mystical Vision application.
#### Train a New Model & Predict 🛠️
1. **Create New Project:** In the application UI, navigate to "Create New Project".
2. **Select Dataset Folder:** Choose the folder containing your organized image dataset (with class subfolders).
3. **Name Your Project:** Enter a name for your project (this will be used for saving the model).
4. **Generate Model:** Click "Continue" to start training your custom model.
5. **Predict Images:** Once training is complete, use the "Single Image Prediction" or "Multiple Image Prediction" options to classify new images using your newly trained model.
#### Use an Existing Trained Model 📂
1. **Open Existing Model:** In the application UI, navigate to "Open Existing Model".
2. **Select Model File:** Choose your .hdf5 model file.
3. **Predict Images:** Use the "Single Image Prediction" or "Multiple Image Prediction" options to classify images using your loaded model.

🚨 **DISCLAIMER:** This application is designed and best used at a screen resolution of **1366 ✕ 768** due to the current UI layout settings and is still not responsive for other screen resolutions.

---

### Sample Datasets for Testing
- [Dog Emotions Dataset (Kaggle)](https://www.kaggle.com/datasets/devzohaib/dog-emotions-prediction/data)
- [Face Mask Detection Dataset (Kaggle)](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection/data)
- [Brain Tumor Balanced Dataset (Kaggle)](https://www.kaggle.com/datasets/soumyapal22/brain-tumor-balanced-dataset/data)


For advanced customization or specific needs, further changes and adaptation will be required in the code.
While primarily a personal project, feedback and suggestions for improvement are always welcome! 

✨ **Special Mention:** This project's core image classification functionality utilizes the Python package from [pranav377/image-classifier](https://github.com/pranav377/image-classifier/) to make this one possible!
