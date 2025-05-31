# YOLOv8 Object Detection on Video 🎯📹

This project demonstrates real-time object detection on a video using **YOLOv8** (You Only Look Once) by **Ultralytics**. The script loads a pre-trained YOLOv8 model and performs object detection on a video file, displaying bounding boxes and class labels for detected objects.

## 🔍 Features

- Utilizes **YOLOv8n** for fast and accurate object detection
- Works on video files
- Annotates detections with bounding boxes and class labels
- Easily customizable for webcam or other video sources

## 🖥️ Demo

https://user-images.githubusercontent.com/your-username/demo-video.mp4  
*Sample output video showing YOLOv8 object detection in action.*

## 📁 Files Included

- `object_detection.py` - Main script for object detection
- `coco.txt` - COCO dataset class labels
- `video_sample1.mp4` - Sample input video (you can replace it with your own)
- `requirements.txt` - Required Python packages
- `env.yml` - Optional Conda environment file

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenCV
- Ultralytics YOLOv8

### Installation

#### Option 1: Using `pip`

```bash
pip install -r requirements.txt
python object_detection.py
````

#### Option 2: Using Conda

```bash
conda env create -f env.yml
conda activate yolov8-env
python object_detection.py
```

## 📦 Requirements

```
ultralytics
opencv-python
numpy
```

(Also defined in `requirements.txt`)

## 🧠 How It Works

* Loads YOLOv8n model via Ultralytics
* Reads class names from `coco.txt`
* Runs detection frame-by-frame on video
* Annotates each frame with boxes and labels
* Displays the output in a window

## 📸 Sample Output

![Sample Output](https://your-screenshot-link.com/output.jpg)

## 👤 Author

**Your Name**
Connect with me on [LinkedIn](https://www.linkedin.com/in/akash-rapolu-67043a344/)
Project on GitHub: [YOLOv8-Object-Detection](https://github.com/Rapoluakash/yolov8-object-detection))

## 📄 License

This project is licensed under the MIT License.

---

### 💡 Tip:

Press **`Q`** during video playback to quit the visualization window.

```

---

Would you like me to customize this with your actual GitHub username and LinkedIn link? Or help generate a cover image or output screenshot for the `README`?
```
