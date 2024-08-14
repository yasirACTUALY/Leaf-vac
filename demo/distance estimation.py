import cv2
import numpy as np

# Known distance from the camera to the object (in centimeters)
KNOWN_DISTANCE = 50.0  

# Known width of the object (in centimeters)
KNOWN_WIDTH = 10.0  

# Function to calculate the focal length
def calculate_focal_length(known_distance, known_width, width_in_frame):
    return (width_in_frame * known_distance) / known_width

# Function to estimate the distance to the object
def estimate_distance(focal_length, known_width, width_in_frame):
    return (known_width * focal_length) / width_in_frame

# Initialize the camera
cap = cv2.VideoCapture(0)

# Capture a frame to calculate the focal length
ret, frame = cap.read()

# Assume the object is already centered and at the known distance in the initial frame
# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Assume the largest contour is the object
contour = max(contours, key=cv2.contourArea)

# Get the bounding box for the contour
x, y, w, h = cv2.boundingRect(contour)

# Calculate the focal length
focal_length = calculate_focal_length(KNOWN_DISTANCE, KNOWN_WIDTH, w)

print(f"Focal Length: {focal_length}")

# Start the video loop
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)

        # Estimate the distance to the object
        distance = estimate_distance(focal_length, KNOWN_WIDTH, w)
        cv2.putText(frame, f"Distance: {distance:.2f} cm", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Draw the bounding box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Distance Estimation', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
