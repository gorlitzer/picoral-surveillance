import time

from utils.video_utils import capture_frame

def main():
    # Stream URL and directory paths (replace with your values)
    stream_url = 'http://192.168.1.135:8080/video'
    images_dir = "data/temp/images"


    while True:
        # Capture a frame
        capture_frame(stream_url, images_dir=images_dir)
        print("Frame captured. This is where person detection will happen soon.")
        time.sleep(5)  # Optional delay between captures

if __name__ == "__main__":
    main()
