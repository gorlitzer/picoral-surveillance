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

def process_object_detections(frame, outputs):
    """
    Processes and visualizes the detections on the input frame.

    Args:
        frame (np.ndarray): RGB image array of the frame.
        outputs (list): List of model outputs as NumPy arrays.

    Returns:
        np.ndarray: Processed frame with visualized detections.
    """
    logging.debug("Processing detections...")

    # Assuming each element in outputs is a NumPy array containing detection information
    for i, output in enumerate(outputs):
        logging.debug(f"Processing output {i + 1}/{len(outputs)}...")

        # Assuming the structure of output array (modify according to your structure)
        boxes = output[:, :4]  # Assuming the first four elements represent box coordinates
        labels = output[:, 4].astype(int)  # Assuming the fifth element represents the label
        scores = output[:, 5]  # Assuming the sixth element represents the score

        # Debugging: Print detection information
        for j, (box, label, score) in enumerate(zip(boxes, labels, scores)):
            logging.debug(f"Detection {j + 1}/{len(boxes)} - Label: {label}, Score: {score:.2f}, Box: {box}")

        # Visualize the detections on the frame
        frame = visualize_detection(frame, boxes, labels, scores)

    logging.debug("Detections processing complete.")
    return frame

def visualize_detection(frame, boxes, labels, scores):
    """
    Visualizes detections on the input frame.

    Args:
        frame (np.ndarray): RGB image array of the frame.
        boxes (np.ndarray): Detection box coordinates.
        labels (np.ndarray): Detection labels.
        scores (np.ndarray): Detection scores.

    Returns:
        np.ndarray: Frame with visualized detections.
    """
    logging.debug("Visualizing detections...")

    for box, label, score in zip(boxes, labels, scores):
        box = np.array(box, dtype=int)
        color = (0, 255, 0)  # Green color
        thickness = 2

        # Draw bounding box
        frame = cv2.rectangle(frame, tuple(box[:2]), tuple(box[2:]), color, thickness)

        # Debugging: Print label and score
        logging.debug(f"Label: {label}, Score: {score:.2f}")

    logging.debug("Detection visualization complete.")
    return frame

def detections_found(detections):
    """
    Checks if object detections are found based on the inference results.

    Args:
        detections (list): List of detection results.

    Returns:
        bool: True if detections are found, False otherwise.
    """
    # Assuming each detection is represented by a bounding box and a confidence score
    return len(detections) > 0 and detections[0]['confidence'] > detection_threshold
