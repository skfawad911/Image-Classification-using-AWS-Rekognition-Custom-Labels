# Image Classification using AWS Rekognition Custom Labels

This project demonstrates how to use **AWS Rekognition Custom Labels** for classifying food images into different categories. The model was trained using 4000 images with 80 food labels and can be used to classify new images effectively.

## Table of Contents

- Introduction
- Prerequisites
- Step 1: Prepare S3 Bucket
- Step 2: Prepare and Upload Data
- Step 3: Create Rekognition Custom Labels Project
- Step 4: Train the Model
- Step 5: Start the Model for Inference
- Step 6: Test the Model
- Step 7: Clean Up Resources
- Contributing


## Project Overview

**Food Image Classification** is a machine learning model built with AWS Rekognition's custom labels feature. The model is trained to recognize and classify various food items based on images. It helps in automating the identification of different types of food with high accuracy.

- **Trained on**: 4000 images, 80 labels
- **Tested on**: 800 images, 80 labels
- **F1 Score**: 0.855
- **Average Precision**: 0.880
- **Overall Recall**: 0.850

## Introduction

This repository focuses on building a custom image classification model using **AWS Rekognition** to identify various types of food. The model is trained with a dataset containing **80 labels** and **4000 images**. Once the model is trained, it can be used to classify new images and predict the type of food with a specified confidence level.


## Prerequisites

Before you start, make sure you have the following:

- **AWS Account**: Required to use AWS Rekognition and S3.
- **AWS CLI**: Installed and configured with access keys (`aws configure`).
- **Python 3.x**: Installed for running scripts to interact with AWS Rekognition.
- **Boto3**: AWS SDK for Python.

  Install Boto3 using pip:
  ```bash
  pip install boto3
  ```
- **Dataset**: Image Datasets that you would like to train your model on

## Project Structure
.
├── test.py                   # Script to test the trained model with new images
└──  README.md               # Project documentation (this file)

## Setup Instructions

### Step 1: Prepare S3 Bucket
- Log in to the AWS Management Console.
- Go to S3 and create a new bucket to store your images.
- Name your bucket (nutrifact) and choose the appropriate region.
- Click Create bucket.

### Step 2: Prepare and Upload Data
- Organize your images into folders, each named according to the label (e.g., adhirasam, chapati, poha).
- Upload the folders containing images to your S3 bucket:
- Each folder should represent a class/label.


### Step 3: Create Rekognition Custom Labels Project
- In the AWS Management Console, navigate to Rekognition > Custom Labels.
- Click Get started and create a new project. Name your project (food-classifier).
- Import dataset from s3
- Enable Automatic Labelling
- Follow the on-screen instructions to create a project.

### Step 4: Train the Model
- In the Rekognition Console, click Train model.
- Select the S3 bucket and the folders containing the training and testing images.
- Set the Training dataset and Testing dataset:
    -- Training set: 80 labels, 3200 images.
    -- Testing set: 80 labels, 800 images.
- Start the training process. It may take several hours to complete based on the size of the dataset(for me it took 4-5 hours).
- Once training is complete, check the training metrics such as F1 score, Average Precision, and Overall Recall.

### Step 5: Start the Model for Inference
- After training, start the model to make predictions:
- Click Start model in the Rekognition Console.
- Select the number of inference units (1 unit is usually sufficient for testing).
- Alternatively, use the AWS CLI:
``` bash
aws rekognition start-project-version --project-version-arn <Your_Model_Version_ARN> --min-inference-units 1
```
- Replace <Your_Model_Version_ARN> with the ARN of your trained model.

### Step 6: Test the Model
- Once the model is running, you can test it with new images
- Create a test.py script
- Run the script to see the detected labels and their confidence scores.

### Step 7: Clean Up Resources
- After testing, you can stop the model to avoid unnecessary charges
- Stop the model using the AWS CLI:
```bash
aws rekognition stop-project-version --project-version-arn <Your_Model_Version_ARN>
```
- Optionally, delete images from the S3 bucket if they are no longer needed

## Contributing
Contributions are welcome! If you find any issues or want to improve this project, feel free to submit a pull request.
