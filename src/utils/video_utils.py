import os
import cv2
import time
import logging

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
        logging.error("Failed to capture frame. Skipping...")
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
        logging.debug(f"Saved frame to {filename}")
    except ValueError as e:
        logging.error(f"Saved frame to {filename}")
        return None

    finally:
        # Release resources regardless of success or failure
        cap.release()

    return frame  # Return the captured frame

def save_frame_with_detections(frame, images_dir):
    """
    Save the frame with detections as an image with a unique filename.

    Args:
        frame (np.ndarray): RGB image array with visualized detections.
        images_dir (str): Directory where the image will be saved.

    Returns:
        str: The filename of the saved image.
    """
    # Generate a unique filename with timestamp
    filename = os.path.join(images_dir, f"frame_{int(time.time())}.png")

    try:
        # Save the frame with detections as an image
        cv2.imwrite(filename, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        logging.debug(f"Frame with detections saved: {filename}")
        return filename
    except Exception as e:
        logging.error(f"Failed to save frame with detections. Error: {e}")
        return None
    finally:
        # Add additional logging for debugging
        if os.path.exists(filename):
            logging.debug(f"File {filename} exists.")
        else:
            logging.debug(f"File {filename} does not exist.")
