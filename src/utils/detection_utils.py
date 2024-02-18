# Contains functions for preprocessing frames, processing detections, and visualization

import cv2
import numpy as np
import logging

def preprocess_frame(frame, model_input_size):
    """
    Preprocesses a frame for object detection based on the provided model requirements.

    Args:
        frame (np.ndarray): RGB image array of the frame.
        model_input_size (tuple): Size of the input expected by the model (height, width).

    Returns:
        np.ndarray: Preprocessed frame in the format expected by the model.
    """

    # Resize the frame to match the model's input size
    frame = cv2.resize(frame, model_input_size[::-1], interpolation=cv2.INTER_AREA)
    logging.debug(f"Resized frame shape: {frame.shape}")

    # If the model expects normalized pixel values (0-1)
    frame = frame.astype(np.float32) / 255.0
    logging.debug(f"Normalized frame min/max: {frame.min()}/{frame.max()}")

    # Expand dimensions to match the expected input shape for the model
    frame = np.expand_dims(frame, axis=0)

    # Return the preprocessed frame
    return frame

def process_detections(frame, detections):
    """
    Visualizes and analyzes object detections on a frame.

    Args:
        frame (np.ndarray): RGB image array of the frame.
        detections (list): List of detection results (boxes, labels, scores).
    """

    # Example processing steps:
    # - Iterate through each detection
    for box, label, score in detections:
        # - Draw bounding box on the frame
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
        # - Add label and score text
        text = f"{label}: {score:.2f}"
        cv2.putText(frame, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # - Optionally perform further analysis based on detections

    return frame
