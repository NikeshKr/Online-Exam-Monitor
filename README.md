# Online-Exam-Monitor
Designed to monitor student's activities during examination.
# Real-time Face Detection with OpenCV

## Overview
This project utilizes OpenCV to perform real-time face detection using a webcam. It employs the Haar Cascade Classifier to identify faces in the captured video frames and highlights them with rectangles.

## Features
- Real-time face detection using webcam feed.
- Rectangles drawn around detected faces.
- Dynamic color indication for the first detected face.

## Requirements
- Python 3.x
- OpenCV

## Installation
1. Clone the repository: `git clone https://github.com/your-username/your-repository.git`
2. Install OpenCV: `pip install opencv-python`

## Usage
1. Run the script: `python your_script.py`
2. Press 'q' to exit the video feed.

## Configuration
You can customize the face detection parameters in the script:
- `scaleFactor`: Controls the image size reduction during face detection.
- `minNeighbors`: Specifies the number of neighbors a region should have to be considered a face.
- `minSize`: Minimum size of the detected face.
- `flags`: Additional flags for face detection.

## Example
![Face Detection Example](link-to-screenshot-or-gif)

