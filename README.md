# Digit Recognition Web App

This is a simple web application for recognizing hand-drawn digits using a trained deep learning model. Users can upload an image of a handwritten digit, and the application will return the recognized digit.

## Table of Contents

- [Digit Recognition Web App](#digit-recognition-web-app)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Usage](#usage)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [How to Use](#how-to-use)
  - [Analysis](#analysis)
  - [Directory Structure](#directory-structure)
  - [Credits](#credits)

## Overview

This project consists of a Jupyter Notebook (`main.ipynb`) for model training and analysis and a Flask web application (`app.py`) for serving the trained model and providing a user interface for digit recognition.

The main steps involved in this project are as follows:

1. **Model Training**: A deep learning model is trained on a dataset of handwritten digits to recognize digits from images.

2. **Web Application**: A web application is built using Flask to allow users to upload images of handwritten digits and get real-time predictions from the trained model.

The best-fit model has been saved in the HDF5 file format.

**Note: This application works only for 28x28 images of digits.**

## Usage

This section provides instructions on setting up and using the web application.

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.7 or higher
- Flask (Python web framework)
- Keras (deep learning library)
- NumPy (numerical computing library)

You can install the required Python packages using `pip`:

```bash
pip install Flask keras numpy
```

### Installation

Follow these steps to install and run the web application:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/digit-recognition-app.git
```

2. Navigate to the project directory:

```bash
cd digit-recognition-app
```

3. Run the Flask application:

```bash
python app.py
```

4. Open a web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the web application.

## How to Use

1. Visit the application URL ([http://127.0.0.1:5000](http://127.0.0.1:5000)).

2. You'll see a simple web page with the option to upload an image file.

3. Choose an image of a handwritten digit (e.g., a scanned or photographed digit drawing) and click the "Recognize" button.

4. The web application will display the recognized digit.

## Analysis

The analysis and code for training the deep learning model can be found in the `main.ipynb` Jupyter Notebook. You can access it by following this - [`main.ipynb`](\\Model%20Training\\main.ipynb).

The `main.ipynb` notebook includes the following analysis:

- Data preparation and exploration
- Model architecture and training
- Model evaluation
- Saving the trained model as an HDF5 file

## Directory Structure

The project directory structure is organized as follows:

- [`app.py`](/app.py): The Flask web application.
- [`templates`](/templates): HTML templates for the web application.
- [`Model Training`](/Model%20Training): Directory to store the trained model (HDF5 format).
- [`main.ipynb`](\\Model%20Training\\main.ipynb): Jupyter Notebook with analysis and model training code.

## Credits

This project was created by [Srihari M](https://github.com/SrihariMurali01).
