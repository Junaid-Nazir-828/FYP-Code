import cv2
import time
import constants
import threading

def take_picture():
    while True:
        # RTSP URL with username and password (encoded)
        # cap = cv2.VideoCapture(constants.RTSP_URL)
        cap = cv2.VideoCapture(0)

        # Check if video capture object opened successfully
        if not cap.isOpened():
            print("Error opening video capture object")
            exit()

        # Capture frame-by-frame
        while True:
            # Capture frame
            ret, frame = cap.read()

            # Check if frame capture was successful
            if not ret:
                print("Error capturing frame")
                break
            # Resize the frame to 800x400
            resized_frame = cv2.resize(frame, (800, 400))
            # Display the frame (optional)
            cv2.imshow("Camera Stream", resized_frame)

            filename = "camera_image.jpg"
            # Save the frame as an image
            cv2.imwrite(filename, resized_frame)
            print(f"Image saved as: {filename}")
            break
        # Release resources
        cap.release()
        cv2.destroyAllWindows()

        time.sleep(10)

if __name__ == '__main__':
    thread_1 = threading.Thread(target=take_picture)
    thread_1.start()