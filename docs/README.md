# Raspberry Pi Security Monitoring System

## Project Overview

This project establishes a privacy-centric security monitoring system utilizing Raspberry Pi 5 and Coral AI USB Accelerator. The system identifies individuals in video frames, analyzes their postures and actions, and generates comprehensive security logs.

## Run

1. Install the following libraries:

    ```bash
    sudo apt-get install libgl1-mesa-glx
    pip install -r requirements.txt
    ```

2. Download required models:

   - [MobileNet v3](https://www.kaggle.com/models/google/mobilenet-v3/frameworks/tfLite)
     - Find the desired model on TF Hub.
     - Click "Download" and choose the TensorFlow Lite format.
     - Unzip the downloaded file to extract the `.tflite` model file, rename it to `mobilenet_v3.tflite`, and move it to the `src/models/` folder.

## Key Components

- **TensorFlow Lite Models:**
  - **Object Detection:** [MobileNet v3](https://www.kaggle.com/models/google/mobilenet-v3/frameworks/tfLite) or [EfficientDet-Lite](https://www.kaggle.com/models/tensorflow/efficientdet) (or similar)
  - **Pose Estimation:** PoseNet MobileNet v1 (or similar)
- **Text Generation Model (Alternatives):**
  - Mistral 7B (original choice)
  - Bard (Google AI's factual language model)
  - TinyGPT (lightweight GPT-2 variant)
  - GPT-Neo-X (compressed GPT-Neo)
- **Coral AI USB Accelerator:** Accelerates model inference
- **Software Libraries:** OpenCV, TensorFlow Lite libraries, model-specific libraries

## Hardware

- Raspberry Pi 5 (8GB RAM recommended)
- Coral AI USB Accelerator
- MicroSD Card (128GB or higher recommended)

## Privacy Focus

Data processing and model execution occur entirely on your Raspberry Pi, ensuring complete privacy control.

## Setup and Configuration

1. **Select TensorFlow Lite Models:**
   - Choose based on accuracy, speed, and resource constraints. Experiment to find the best fit.
2. **Integrate Models:**
   - Define processing flow (sequential or parallel) and adjust data formats as needed.
3. **Choose Text Generation Model:**
   - Consider resource constraints, compatibility, and desired capabilities when selecting Mistral 7B or an alternative.
4. **Leverage Coral AI USB Accelerator:**
   - Ensure compatibility and explore optimization techniques for efficient inference.
5. **Test and Iterate:**
   - Start with small datasets and refine based on performance and resource usage.
6. **Implement Security Log Generation:**
   - Utilize the chosen text generation model to create detailed logs based on detected individuals and postures, utilizing prompts and templates for richer information.

## Additional Notes

- Experimentation and customization are key for optimal performance and privacy within your specific environment.
- Consider pre-trained datasets for initial testing and fine-tuning models for better accuracy on your own data.
- Explore community resources and tutorials for troubleshooting and further guidance.

## Remember

This is a starting point. Adapt and modify the setup to fit your specific needs and preferences. With careful planning and optimization, you can create a powerful and privacy-preserving security monitoring system for your Raspberry Pi!
