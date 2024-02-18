import time

from utils.video_utils import capture_frame

def main():
    # Stream URL and directory paths (replace with your values)
    stream_url = 'http://192.168.1.135:8080/video'
    images_dir = "data/temp/images"


    while True:
        # Capture a frame
        
        frame = capture_frame(stream_url, images_dir=images_dir)

        if frame is None:
            print("Failed to capture frame. Skipping...")
            continue

        # Run object detection (replace with your function)
        #detections = run_object_detection(detection_model, frame)

        # Process detections (e.g., draw bounding boxes)
        #detection_utils.process_detections(frame, detections)

        # Optional: Pose estimation if used
        # ... (similar steps for pose estimation)

        # Display or save the processed frame
        # ...

        # Delay between captures
        time.sleep(5)

if __name__ == "__main__":
    main()
