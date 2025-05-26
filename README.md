# Hurricane Damage Classification

This project classifies hurricane damage using deep learning and transfer learning with the VGG16 model.

## Installation

It is recommended to use a virtual environment.

```bash
pip install keras tensorflow-cpu numpy pillow pandas scikit-learn
```

## Description

- Uses VGG16 (pretrained on ImageNet) to extract features from images.
- Images are resized to 224×224 before feature extraction.
- Extracted features (25088-dimensional) are flattened and passed to a custom fully connected neural network.
- Labels are one-hot encoded using pandas.
- The model is trained and saved for future inference.

## Dataset Structure

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

## Output

The trained model is saved in:

```
image_classification_model/
```

## Notes

- Full code and explanation are available in the Jupyter Notebook.
- Ensure that all image files are readable and follow consistent formats (e.g., `.jpg`, `.png`).
