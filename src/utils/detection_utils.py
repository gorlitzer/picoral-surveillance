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


def process_detections(frame, outputs):
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

        # Iterate over each detection in the output array
        for j, (box, label, score) in enumerate(zip(boxes, labels, scores)):
            logging.debug(f"Processing detection {j + 1}/{len(boxes)} - Label: {label}, Score: {score:.2f}")

            # Visualize the detection on the frame (modify according to your visualization logic)
            frame = visualize_detection(frame, box, label, score)

    logging.debug("Detections processing complete.")
    return frame


def visualize_detection(frame, box, label, score):
    """
    Visualizes a single detection on the input frame.

    Args:
        frame (np.ndarray): RGB image array of the frame.
        box (list or np.ndarray): Detection box coordinates.
        label (int): Detection label.
        score (float): Detection score.

    Returns:
        np.ndarray: Frame with visualized detection.
    """
    logging.debug("Visualizing detection...")

    # Modify this function according to your visualization logic
    # Drawing a bounding box and text on the frame as an example
    box = np.array(box, dtype=int)
    color = (0, 255, 0)  # Green color
    thickness = 2

    frame = cv2.rectangle(frame, tuple(box[:2]), tuple(box[2:]), color, thickness)
    label_text = f"Label: {label}, Score: {score:.2f}"
    frame = cv2.putText(frame, label_text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness, cv2.LINE_AA)

    logging.debug("Detection visualization complete.")
    return frame
