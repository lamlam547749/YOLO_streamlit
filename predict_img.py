from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load a model
model = YOLO("yolov11/best.pt")  # Load a custom model

# Predict with the model
results = model("test.jpg")  # Predict on an image

# Convert to numpy array for easier visualization
image = cv2.imread("test.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Draw bounding boxes and show confidence scores
for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
    confidence = box.conf[0]  # Confidence score
    label = f"{confidence:.2f}"
    
    # Draw the box and label on the image
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Blue box
    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Show the image with bounding boxes
plt.imshow(image)
plt.axis("off")
plt.show()
