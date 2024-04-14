

## Overview
This Flask application provides an API for detecting circular objects in images and identifying their colors. It's particularly tuned to distinguish between red objects and transparent ones, which is useful in wine glasses detction.

## Features
- **Circle Detection**: Detect circles in any given image with adjustable parameters for sensitivity and accuracy.
- **Color Recognition**: Identify whether the detected circles are red or transparent.
- **Robust Validation**: Incorporate advanced image processing techniques to minimize false positives, especially in complex scenes.

## Installation

### Prerequisites
- Python 3.8+
- Flask
- OpenCV
- NumPy
- SciKit-Image

### Setup
Clone this repository to your local machine:

```bash
git clone https://github.com/Merci202/praktikum.git
cd praktikum-api` 

Install the required packages:

bashCopy code

`pip install -r requirements.txt` 

### Running the Application

Start the Flask application by:

bashCopy code

`python app.py` 

The API will be available at `http://127.0.0.1:5000/` on your local machine.

## API Endpoints

### POST /detect_image

This endpoint accepts a JSON object containing the `url` of an image and returns the detection results as a JSON object. The results include the positions and colors (red or transparent) of detected circles.

#### Request Example

jsonCopy code

`{
  "url": "abc.png"
}` 

#### Response Example

jsonCopy code

`{
  "grid": [
    [
      [true, "red"],
      [false, null],
      [false, null]
    ],
    [
      [false, null],
      [false, null],
      [false, null]
    ],
    [
      [false, null],
      [false, null],
      [false, null]
    ]
  ]
}` 

### GET /get_picture

Fetches the image with the specified name from the server.

#### Query Parameter

-   `name`: The name of the image to retrieve.

#### Example

urlCopy code

`GET /get_picture?name=image_name` 

### POST /take_picture

Takes a picture using the system's camera and saves it with a specified name provided in the JSON body of the request.

#### Request Example

jsonCopy code

`{
  "name": "new_image"
}` 

### DELETE /delete_picture

Deletes the image with the specified name from the server.

#### Query Parameter

-   `name`: The name of the image to delete.

#### Example

urlCopy code

`DELETE /delete_picture?name=image_name` 

## Examples

Here are some curl commands to interact with the API:

### Detect Image

bashCopy code

`curl -X POST http://127.0.0.1:5000/detect_image -H "Content-Type: application/json" -d "{\"url\": \"abc.png\"}"` 

### Get Picture

bashCopy code

`curl http://127.0.0.1:5000/get_picture?name=abc` 

### Take Picture

bashCopy code

`curl -X POST http://127.0.0.1:5000/take_picture -H "Content-Type: application/json" -d "{\"name\": \"new_image\"}"` 

### Delete Picture

bashCopy code

`curl -X DELETE http://127.0.0.1:5000/delete_picture?name=abc`



