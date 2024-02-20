import time
import logging

from utils.video_utils import capture_frame, save_frame_with_detections
from utils.coloredlogs_utils import configure_colored_logging
from utils.detection_utils import preprocess_frame, process_object_detections
from utils.model_utils import load_image_recognition_models, get_model_input_size, run_inference

def main():
    # Stream URL and directory paths
    stream_url = 'http://192.168.1.135:8080/video'
    images_dir = "data/temp/images/frames"
    processed_frames_dir = "data/temp/images/processed_frames"

    # Load botn object detection and pose estimation models
    obj_detect_model_path = "src/models/mobilenet_v3.tflite"
    pose_estim_model_path = "src/models/posenet_mobilenet.tflite"

    object_detection_model, pose_estimation_model = load_image_recognition_models(obj_detect_model_path, pose_estim_model_path)

    od_model_input_size = get_model_input_size(object_detection_model)

    while True:

        frame = capture_frame(stream_url, images_dir=images_dir)  # Capture a frame

        if frame is None:
            logging.warning("Failed to capture frame. Skipping...")
            continue

        # Preprocess the frame
        preprocessed_frame = preprocess_frame(frame, od_model_input_size)

        # Run object detection inference
        detections = run_inference(object_detection_model, [preprocessed_frame])

        # Process and visualize detections and pose estimation results
        processed_frame = process_object_detections(frame, detections)

        save_frame_with_detections(processed_frame, processed_frames_dir)
        
        # Log the detections
        # logging.debug(f"processed_frame: {processed_frame}")

    #    # Check if object detections are found
    #     if detections_found(detections):
    #         # Run pose estimation
    #         pose_estimation_results = run_inference(pose_estimation_model, [preprocessed_frame])

    #         # Process and visualize detections and pose estimation results
    #         processed_frame = process_detections(frame, detections, pose_estimation_results)

            # Display or save the processed frame
            # ...

        # Delay between captures
        time.sleep(5)
        return

if __name__ == "__main__":
    
    configure_colored_logging()

    main()
