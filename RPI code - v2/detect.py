import cv2
# import urllib.parse
# import constants
from api_calls import change_device_status
from ultralytics import YOLO
import constants
import time

def start_detection(coordinates):
    roi_coords = []
    box_status = []

    four_readings = []
    rectangle_ids = []
    for coord in coordinates:
        tup = (int(coord['x1']),  # x1
               int(coord['y1']),  # y1
               int(coord['x2']),  # x2
               int(coord['y2']),  # y2
               coord['RectangleID']
               )
        rectangle_ids.append(coord['RectangleID'])
        roi_coords.append(tup)
        box_status.append(0)

    model = YOLO('yolov8n.pt')

    def detect_person(image):
        results = model.predict(source=image,classes=0)
        # results = model(image,clas)
        return results

    while constants.CONTINUE_THREAD:
        # Load and resize an image
        image = cv2.imread(constants.IMAGE_PATH)
        resized_image = cv2.resize(image, (800, 400))

        # Draw red rectangles on the image
        for (x1, y1, x2, y2, device_id) in roi_coords:
            cv2.rectangle(resized_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Detect humans only within the red rectangles
        for (x1, y1, x2, y2, device_id) in roi_coords:
            # Crop the region of interest (ROI)
            roi = resized_image[y1:y2, x1:x2]

            # Perform detection on the ROI
            results = detect_person(roi)
            # Iterate over the detections and draw bounding boxes
            box_status[0] = 0
            for result in results:
                for index , bbox in enumerate(result.boxes):
                    # Get the bounding box coordinates relative to the ROI
                    bx1, by1, bx2, by2 = bbox.xyxy[0].tolist()
                    # confidence = bbox.conf.item()
                    # label = result.names[int(bbox.cls.item())]

                    # Draw the bounding box and label on the ROI
                    cv2.rectangle(roi, (int(bx1), int(by1)), (int(bx2), int(by2)), (0, 255, 0), 2)
                    # cv2.putText(roi, f'{label} {confidence:.2f}', (int(bx1), int(by1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    box_status[0] = 1
            # Replace the ROI in the original image with the modified ROI
            resized_image[y1:y2, x1:x2] = roi

            print('box status:', box_status)

        if len(four_readings) == 4:
            four_readings.pop(0)
        four_readings.append(box_status[:])

        result = []
        print(four_readings)
        if len(four_readings) == 4:
            for index, values in enumerate(zip(*four_readings)):
                if any(values):
                    result.append(1)
                    change_device_status(rectangle_ids[index],1)
                else:
                    result.append(0)
                    change_device_status(rectangle_ids[index],0) # change occupancy status

        print('Final Result', result)

        # Save the result image (optional)
        output_path = 'detected_image.jpg'
        cv2.imwrite(output_path, resized_image)

        time.sleep(10)

    # Display the image with bounding boxes
    # cv2.imshow('Person Detection', resized_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# 292,63 594,358
if __name__ == '__main__':
    start_detection('camera_image.jpg', [{'x1': 50, 'y1': 50, 'x2': 200, 'y2': 200, 'DeviceID': 17},{'x1': 300, 'y1': 100, 'x2': 450, 'y2': 250, 'DeviceID': 17},{'x1': 500, 'y1': 150, 'x2': 650, 'y2': 300, 'DeviceID': 17}])
