import cv2

def initialize_camera():
    cap = cv2.VideoCapture(0)  # Use 0 for default camera or replace with the mobile camera URL
    return cap

def capture_frame(cap):
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        return None
    return frame

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()