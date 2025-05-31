# 1. Importing Required Libraries
import cv2
import random
import numpy as np
from ultralytics import YOLO
import os

# 2. Load COCO Class Labels
with open(r"C:\Users\rapol\vs code\YELO PROCTICE\coco.txt", "r") as f:
    class_list = f.read().splitlines()

# 3. Assign Random Colors to Each Class
detection_colors = [tuple(random.randint(0, 255) for _ in range(3)) for _ in class_list]

# 4. Load the YOLOv8 Model
model = YOLO(r"C:\Users\rapol\vs code\YELO PROCTICE\yolov8n.pt")

# 5. Load the Video File
video_path = r"C:\Users\rapol\vs code\YELO PROCTICE\video\video_sample1.mp4"
cap = cv2.VideoCapture(video_path)

# 6. Check If Video Opened Successfully
if not cap.isOpened():
    print("can't open video")
    exit()

# 7. Get Video Frame Dimensions (Optional)
frame_wid = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_hyt = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 8. Frame-by-Frame Processing Loop
while True:
    ret, frame = cap.read()

    # 9. Exit on End of Stream
    if not ret:
        print("can't receive frame (stream end). Exiting...")
        break

    # 10. YOLOv8 Prediction on the Frame
    results = model.predict(source=frame, conf=0.45, verbose=False)

    # 11. Loop Through Detected Results
    for result in results:
        boxes = result.boxes

        # 12. Draw Bounding Boxes and Labels
        for i, box in enumerate(boxes):
            cls_id = int(box.cls[0].item())
            conf = float(box.conf[0].item())
            bb = box.xyxy[0].tolist()

            # 13. Draw Box and Class Label
            cv2.rectangle(frame, (int(bb[0]), int(bb[1])), (int(bb[2]), int(bb[3])), detection_colors[cls_id], 2)

            label = f"{class_list[cls_id]}, {round(conf * 100, 1)}%"
            cv2.putText(frame, label, (int(bb[0]), int(bb[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    # 14. Display the Annotated Frame
    cv2.imshow("YOLO Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 15. Cleanup
cap.release()
cv2.destroyAllWindows()
