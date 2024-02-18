import time
import logging

from utils.video_utils import capture_frame
from utils.coloredlogs_utils import configure_colored_logging
from utils.detection_utils import preprocess_frame
from utils.model_utils import load_model, get_model_input_size, run_inference

# Load model
model = load_model("src/models/mobilenet_v3.tflite")
model_input_size = get_model_input_size(model)

def main():
    # Stream URL and directory paths
    stream_url = 'http://192.168.1.135:8080/video'
    images_dir = "data/temp/images"

    while True:

        frame = capture_frame(stream_url, images_dir=images_dir)  # Capture a frame

        if frame is None:
            logging.warning("Failed to capture frame. Skipping...")
            continue

        # Preprocess the frame
        preprocessed_frame = preprocess_frame(frame, model_input_size)

        # Run inference
        detections = run_inference(model, [preprocessed_frame])  # Pass preprocessed frame as input

        # Process and visualize detections
        #processed_frame = process_detections(frame, detections)

        # Optional: Pose estimation if used
        # ... (similar steps for pose estimation)

        # Display or save the processed frame
        # ...

        # Delay between captures
        time.sleep(5)
        return

if __name__ == "__main__":
    
    configure_colored_logging()

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    main()
