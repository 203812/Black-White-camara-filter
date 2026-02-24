# Camara App
Simple script that grabs your webcam feed and displays a live black-and-white preview. It converts each frame to grayscale and applies a binary threshold so the video appears in stark black & white.

## Requirements

- Python 3.9+
- [`opencv-python`](https://pypi.org/project/opencv-python/) (see `requirements.txt`)

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python Camara-Filter.py`
3. Quit the window by pressing `q`.

Optional flags:

- `--camera`: the OS index of the camera device (default `0`).
- `--threshold`: brightness cutoff to decide whether a pixel becomes black or white (0–255, default `127`).
- Adjust the `Threshold` slider inside the preview window at any time to change how light or dark the output becomes.
- The preview window opens at 1920×1080 by default but can be resized as needed.
