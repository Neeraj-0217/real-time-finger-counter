import cv2 as cv
import mediapipe as mp
import time

class HandDetector:
    def __init__(self, mode=False, maxHand=2, detectionCon=0.85, trackCon=0.7):
        self.mode = mode
        self.maxHand = maxHand
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.tipId = [4,8,12,16,20]

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHand, min_detection_confidence=self.detectionCon, min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def find_position(self, img, draw=True):
        self.lm_list_all = []  # List to store landmarks for all hands
        self.bbox_all = []     # List to store bounding boxes for all hands

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                lm_list = []  # Landmark list for the current hand
                x_list = []
                y_list = []
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append([id, cx, cy])
                    x_list.append(cx)
                    y_list.append(cy)

                # Bounding box for the current hand
                xmin, xmax = min(x_list), max(x_list)
                ymin, ymax = min(y_list), max(y_list)
                bbox = xmin, ymin, xmax, ymax

                self.lm_list_all.append(lm_list)
                self.bbox_all.append(bbox)

                # Optionally draw bounding box
                if draw:
                    cv.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)

        return self.lm_list_all, self.bbox_all

    def fingers_up(self, lm_list):
        fingers = []

        if len(lm_list) == 0:
            return [0, 0, 0, 0, 0]  # No fingers detected

        # Identify hand type: Left or Right
        hand_type = "Left" if lm_list[4][1] < lm_list[17][1] else "Right"

        # Thumb: Use x-coordinates for left/right hand
        if hand_type == "Right":
            if lm_list[self.tipId[0]][1] > lm_list[self.tipId[0] - 1][1]:
                fingers.append(1)  # Thumb is up
            else:
                fingers.append(0)  # Thumb is down
        else:  # For left hand, reverse the comparison
            if lm_list[self.tipId[0]][1] < lm_list[self.tipId[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        # 4 Fingers: Compare y-coordinates of tip and middle joint
        for id in range(1, 5):
            if lm_list[self.tipId[id]][2] < lm_list[self.tipId[id] - 2][2]:
                fingers.append(1)  # Finger is up
            else:
                fingers.append(0)  # Finger is down

        return fingers

    def calculate_distance(self, point1, point2):
        x1, y1 = point1[1], point1[2]
        x2, y2 = point2[1], point2[2]
        return int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)


def main():
    pTime = 0
    cap = cv.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lm_list = detector.find_position(img)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv.imshow("Image", img)
        cv.waitKey(1)

if __name__ == "__main__":
    main()