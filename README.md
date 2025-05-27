# Hurricane Damage Classification

This project classifies hurricane damage using deep learning and transfer learning with the VGG16 model.

---

## 🧪 Virtual Environment Setup

It is recommended to use a Python virtual environment to keep dependencies isolated.

### Step 1: Create and Activate the Virtual Environment

On **Linux/macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

On **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 2: Upgrade pip
```bash
pip install --upgrade pip
```

---

## 📦 Install Required Packages

Install TensorFlow and other dependencies:

```bash
pip install tensorflow==2.16.2 keras==3.3.3 ml-dtypes==0.3.1 tensorboard==2.16.2
pip install numpy pillow pandas scikit-learn jupyter
```

---

## 📓 Set Up Jupyter Kernel (Optional)

To use this environment in Jupyter notebooks:

```bash
python -m ipykernel install --user --name=hurricane-env --display-name "Python (hurricane-env)"
```

You can now select **"Python (hurricane-env)"** from Jupyter Notebook/Lab as the kernel.

---

## 🧠 Description

- Uses VGG16 (pretrained on ImageNet) to extract features from images.
- Images are resized to 224×224 before feature extraction.
- Extracted features (25088-dimensional) are passed to a custom fully connected neural network.
- Labels are one-hot encoded using pandas.
- The model is trained and saved for future inference.

---

## 📁 Dataset Structure

Organize your dataset folder as follows:

```
dataset_folder/
├── class_0/
│   ├── image1.jpg
│   └── ...
├── class_1/
│   ├── image2.jpg
│   └── ...
```

---

## 💾 Output

The trained model is saved in:

```
image_classification_model/
```

---

## 📌 Notes

- Full code and explanation are available in the Jupyter Notebook.
- Make sure image files are readable and consistently formatted (e.g., `.jpg`, `.png`).
- Add `venv/` to `.gitignore` to avoid tracking virtual environments.

```

