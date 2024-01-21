# Image Caption Generator

This project utilizes a combination of ResNet50 and LSTM models to generate captions/description for uploaded images. The trained model is deployed using Streamlit, allowing users to easily upload pictures and receive descriptive captions.

## Overview

- **Model Architecture:**
  - ResNet50: Used for feature extraction from images.
  - LSTM: Employed to generate sequential captions based on the extracted features.

- **Deployment:**
  - The trained model is deployed on Streamlit, creating a user-friendly interface for image captioning.

## Technologies Used

- **TensorFlow/Keras:** The deep learning framework used for building and training the ResNet50 and LSTM models.
- **NLTK:** Natural Language Toolkit is used for processing and handling text data.
- **Streamlit:** Utilized for deploying the interactive web application.

## Deployed Project

The Image Captioning App is deployed and accessible [here](https://capgen.streamlit.app).

## License

This project is licensed under the [MIT License](LICENSE.md). See the [LICENSE.md](LICENSE.md) file for details.

