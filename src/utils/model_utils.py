# Contains functions for loading and running TensorFlow Lite models

import time
import logging
import tensorflow as tf

def load_image_recognition_models(object_detection_model_path, pose_estimation_model_path):
    # Load object detection model
    object_detection_model = load_model(object_detection_model_path)

    # Load pose estimation model
    pose_estimation_model = load_model(pose_estimation_model_path)

    return object_detection_model, pose_estimation_model


def load_model(model_path):
    """
    Loads a TensorFlow Lite model.

    Args:
        model_path (str): Path to the TFLite model file.

    Returns:
        tf.lite.Interpreter: The loaded model interpreter.
    """

    logging.debug(f"Loading TensorFlow Lite model from: {model_path}")

    try:
        interpreter = tf.lite.Interpreter(model_path=model_path)
        interpreter.allocate_tensors()
        logging.debug("Model loaded successfully.")
        return interpreter
    except Exception as e:
        logging.error(f"Failed to load the model. Error: {e}")
        return None


def get_model_input_size(interpreter):
    """
    Gets the input size expected by the model from the TensorFlow Lite interpreter.

    Args:
        interpreter (tf.lite.Interpreter): TensorFlow Lite model interpreter.

    Returns:
        tuple: Size of the input expected by the model (height, width).
    """
    # Get the input details (assuming single input)
    input_details = interpreter.get_input_details()
    model_input_size = tuple(input_details[0]['shape'][1:3])
    return model_input_size


def run_inference(interpreter, input_data):
    """
    Runs inference on a TensorFlow Lite model, including timing measurements.

    Args:
        interpreter (tf.lite.Interpreter): The loaded model interpreter.
        input_data (list): List of preprocessed input data for the model.

    Returns:
        list: List of model outputs as NumPy arrays.
    """

    logging.debug("Starting inference...")

    start_time = time.time()  # Capture start time

    # Set input data
    for i, data in enumerate(input_data):
        logging.debug(f"Setting input tensor {i} with shape: {data.shape}")
        interpreter.set_tensor(interpreter.get_input_details()[i]['index'], data)

    # Run inference
    logging.debug("Invoking model...")
    interpreter.invoke()

    # Get outputs
    logging.debug("Retrieving output tensors...")
    output_details = interpreter.get_output_details()
    outputs = [interpreter.get_tensor(details['index']) for details in output_details]

    for i, output in enumerate(outputs):
        logging.debug(f"Output tensor {i} shape: {output.shape}")

    inference_time = time.time() - start_time  # Calculate elapsed time
    logging.debug(f"Inference complete. Inference time: {inference_time:.4f} seconds")

    return outputs

