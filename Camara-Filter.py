from __future__ import annotations
import argparse
import sys
import cv2

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture webcam video and display a live black-and-white feed."
    )
    parser.add_argument(
        "--camera",
        type=int,
        default=0,
        help="OS index of the camera device (default: 0).",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=118,
        help="Threshold for mapping grayscale to pure black/white (0-255).",
    )
    return parser.parse_args()

def grab_camara(camera_index: int, threshold: int) -> None:
    capture = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
    if not capture.isOpened():
        raise SystemExit(f"Unable to open camera #{camera_index}.")
    window_name = "Camara App - Press 'q' to quit"
    threshold_state = {"value": threshold}
    def _update_threshold(position: int) -> None:
        threshold_state["value"] = position
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1920, 1080)
    cv2.createTrackbar("Threshold", window_name, threshold, 255, _update_threshold)

    try:
        while True:
            success, frame = capture.read()
            if not success:
                print("Frame grab failed; exiting.", file=sys.stderr)
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, black_white = cv2.threshold(
                gray, threshold_state["value"], 255, cv2.THRESH_BINARY
            )
            cv2.imshow(window_name, black_white)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()

def main() -> None:
    args = parse_args()
    grab_camara(args.camera, args.threshold)

if __name__ == "__main__":
    main()
