import time
import cv2
import os

# Contains functions related to video capture and frame saving

def capture_frame(stream_url, images_dir="images"):
    """
    Captures a single frame from a stream, saves it to a directory,
    and returns the frame.
    """

    # Create a VideoCapture object
    cap = cv2.VideoCapture(stream_url)

    # Check if stream is opened successfully
    if not cap.isOpened():
        print("Cannot open stream")
        return None  # Return None on error

    # Ensure the images directory exists
    os.makedirs(images_dir, exist_ok=True)

    # Capture a frame
    try:
        ret, frame = cap.read()

        if not ret:
            raise ValueError("Can't receive frame")

        # Generate a unique filename with timestamp
        filename = os.path.join(images_dir, f"frame_{int(time.time())}.png")

        # Write the frame to the file
        cv2.imwrite(filename, frame)
        print(f"Saved frame to {filename}")

    except ValueError as e:
        print(f"Error capturing frame: {e}")
        return None

    finally:
        # Release resources regardless of success or failure
        cap.release()

    return frame  # Return the captured frame

