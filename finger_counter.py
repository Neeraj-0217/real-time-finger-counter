import cv2 as cv
import time
import HandTrackingModule as htm
import numpy as np

# --- Configuration and Initialization ---
# Initialize video capture (0 for default webcam)
cap = cv.VideoCapture(0)
# Set frame width and height (optional, improves consistency)
cap.set(3, 1280) # Width
cap.set(4, 720)  # Height

# Initialize hand detector with slightly higher confidence for production use
detector = htm.HandDetector(detectionCon=0.75, trackCon=0.7)

# Load images for finger counts (You will need to create or download these images: 
# images for 0.png, 1.png, ..., 5.png, perhaps icons or simple digit images)
# For this example, we will just simulate them or use a simple rectangle/text display.

# --- Main Finger Counting Loop ---
pTime = 0 # Previous time for FPS calculation

while True:
    success, img = cap.read()
    if not success:
        print("Error: Unable to access the camera.")
        break

    # 1. Hand Detection and Landmark Extraction
    img = detector.find_hands(img, draw=True)
    # Get landmarks and bounding boxes for all detected hands
    lm_list_all, bbox_all = detector.find_position(img, draw=True)
    
    # 2. Finger Counting and Visualization
    total_fingers_combined = 0 
    
    # Check if hands are detected
    if lm_list_all:
        for i, lm_list in enumerate(lm_list_all):
            # Check which fingers are up for the current hand
            fingers = detector.fingers_up(lm_list)
            
            # Count the fingers up for this hand
            total_fingers = fingers.count(1)
            total_fingers_combined += total_fingers

            # Display individual hand count near the bounding box
            x, y, _, _ = bbox_all[i]
            
            # Use a slightly larger and bolder text for the individual hand count
            cv.putText(
                img, f"Count: {total_fingers}", (x, y - 40),
                cv.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 0), 2
            )

    # 3. Overall Dashboard Display (Top of the screen)
    # Create a clean rectangle at the top-left for the total count
    img_height, img_width, _ = img.shape
    
    # Display the total number of fingers in a large, prominent box
    cv.rectangle(img, (0, 0), (300, 100), (0, 100, 255), cv.FILLED)
    cv.putText(img, f'Total: {total_fingers_combined}', (20, 70), 
               cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    # 4. FPS Calculation and Display (for performance monitoring)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    # Display FPS in the corner
    cv.putText(img, f'FPS: {int(fps)}', (img_width - 150, 40), 
               cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # 5. Show the resulting frame
    cv.imshow("Real-time Finger Counter", img)

    # Exit on pressing 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()