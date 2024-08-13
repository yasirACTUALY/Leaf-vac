import cv2
import numpy as np
import mss
from pynput import mouse
import time
# Load YOLO
net = cv2.dnn.readNet('yolov3.weights', 'cfg/yolov3.cfg')
layer_names = net.getLayerNames()
outputlayers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load COCO class labels
with open('data/coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Global variables to store the coordinates
top_left = None
bottom_right = None

def on_click(x, y, button, pressed):
    global top_left, bottom_right

    # Capture the top-left corner on the first click
    if pressed and top_left is None:
        top_left = (x, y)
        print(f"Top-left corner set at: {top_left}")

    # Capture the bottom-right corner on the second click
    elif pressed and bottom_right is None:
        bottom_right = (x, y)
        print(f"Bottom-right corner set at: {bottom_right}")

        # Stop the listener after getting both coordinates
        return False

# Start the mouse listener to capture the corners
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# Calculate width and height from the coordinates
width = bottom_right[0] - top_left[0]
height = bottom_right[1] - top_left[1]

# Define the screen region to capture
screen_region = {"top": top_left[1], "left": top_left[0], "width": width, "height": height}

# Initialize screen capture
sct = mss.mss()
# counts the frames per second
fps = 0
frame_count = 0
start = time.time()
while True:
    # Capture the screen
    screenshot = sct.grab(screen_region)

    # Convert to a numpy array
    frame = np.array(screenshot)

    # Convert from BGRA to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    height, width, channels = frame.shape

    # Prepare the frame for YOLO
    blob = cv2.dnn.blobFromImage(frame, scalefactor=0.00392, size=(416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(outputlayers)

    # Process each detection
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for obj in out:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # Confidence threshold
                center_x = int(obj[0] * width)
                center_y = int(obj[1] * height)
                w = int(obj[2] * width)
                h = int(obj[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-max suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    items = []
    for i in indices:
        box = boxes[i]
        x, y, w, h = box
        label = str(classes[class_ids[i]])

        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        items.append(label)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    print(items)
    
    # Display the frame
    cv2.imshow('Object Detection', frame)
    fps +=1
    if fps == 30:
        end = time.time()
        print(f"FPS: {fps / (end - start)}")
        fps = 0
        start = time.time()

    # Break loop on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
