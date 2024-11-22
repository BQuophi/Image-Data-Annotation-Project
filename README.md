* * * * *

Image Data Annotation Project
=============================

This project demonstrates the process of gathering, organizing, and annotating image data for a machine learning model training. It covers steps from downloading images to annotating them in Makesense.ai and saving the annotations in YOLO format.

Project Overview
----------------

In this project, we will:

1.  Download images from Google Images based on specified keywords.
2.  Organize images into folders for easy accessibility.
3.  Annotate images using Makesense.ai.
4.  Save annotations in YOLO format, making them ready for training object detection models.

* * * * *

Setup
-----

1.  **Environment**\
    Ensure you have Python 3 installed. Install necessary libraries:

    ```
    pip install requests beautifulsoup4 fastapi

    ```

    For annotation, [Makesense.ai](https://www.makesense.ai/) was used.

2.  **Folder Structure**\
    Set up the following structure:

    ```
    project_root/
    ├── images/       # For storing downloaded images
    ├── labels/       # For storing YOLO annotation files

    ```

* * * * *

Steps
-----

### Step 1: Download Images

Python Script - `bulk_images_downloader.py` to download the images.

1.  **Running the script**:

    ```
    python bulk_images_downloader.py

    ```

2.  **Explanation of the script**:
    -   The script sends a request to Google Images for the specified search term.
    -   It parses the returned HTML, finds image URLs, and saves each image to the `images/` folder.

**Note:** For compliance with Google's terms of service, this was done responsibly.

### Step 2: Organize Images into Folders

After downloading, check that the images are in the `images/` folder. Organize them by class (if needed for multi-class annotation) to help with annotation in Makesense.ai.

### Step 3: Annotate Images with Makesense.ai

1.  **Upload Images**: Go to [Makesense.ai](https://www.makesense.ai/) and upload images from the `images/` folder.
2.  **Annotate**: Draw bounding boxes around objects of interest and assign labels.
   ![Annot2](https://github.com/user-attachments/assets/d28de68a-68e0-4cbe-b3cc-2556fe64f766)

4.  **Export Annotations**: After completing annotations, download the YOLO format labels and save them in the `labels/` folder.
   ![Annot1](https://github.com/user-attachments/assets/8b09718f-8265-4559-8a08-e6dc994062c1)


### Step 4: Save Annotations in YOLO Format

Once annotations are downloaded, place all `.txt` label files in the `labels/` folder. This format makes it easy to load data for training object detection models.

* * * * *

Usage
-----

With the image and annotation data prepared:

1.  We can load images and annotations into a model training pipeline.
2.  Adjust paths as needed to integrate with training scripts.

Repository Structure
----------------------------

```
project_root/
├── images/           # Contains downloaded images
├── labels/           # Contains YOLO-format annotation files
├── bulk_image_downloader.py    # Script for downloading images
└── README.md         # Documentation

```
