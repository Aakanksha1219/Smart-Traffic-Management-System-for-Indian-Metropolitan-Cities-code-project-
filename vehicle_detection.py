# vehicle_detection.py

from ultralytics import YOLO
import cv2

# Load YOLOv8 nano model (downloads automatically if not present)
model = YOLO('yolov8n.pt')  # You can use yolov8s.pt, yolov8m.pt etc. for better accuracy

def detect_vehicles(image_path):
    # Perform detection
    results = model(image_path)
    annotated_image = results[0].plot()  # Plot detection results

    vehicle_labels = ['car', 'truck', 'bus', 'motorcycle']
    vehicle_count = 0

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            if label in vehicle_labels:
                vehicle_count += 1

    return annotated_image, vehicle_count
