import time
import cv2
import os

def capture_frame(stream_url, images_dir="images"):
    """
    Capture a single frame from a stream and save it to a directory.
    """
    # Create a VideoCapture object
    cap = cv2.VideoCapture(stream_url)

    # Check if stream is opened successfully
    if not cap.isOpened():
        print("Cannot open stream")
        return

    # Ensure the images directory exists
    os.makedirs(images_dir, exist_ok=True)

    # Capture a frame
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame. Exiting ...")
    else:
        # Generate a unique filename with timestamp
        filename = os.path.join(images_dir, f"frame_{int(time.time())}.png")

        # Write the frame to the file
        cv2.imwrite(filename, frame)
        print(f"Saved frame to {filename}")

    # Release resources
    cap.release()
