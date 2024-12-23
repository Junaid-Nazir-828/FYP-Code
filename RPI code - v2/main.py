import detect
from api_calls import get_bounded_rectangles_with_device_id , upload_image , check_server_status
import time
import threading
import detect
from detect_change import check_change
import constants
from pic import take_picture

previous_rectangles_data = False
count = 1

while True:
    try:
        check_server_status()
        print('SERVER IS ACTIVE')
        break
    except Exception as e:
        print(e)
        print('SERVER INACTIVE')
        print('RETRY IN 5 seconds')
        time.sleep(5)
        continue

# start taking images 
Thread_picture = threading.Thread(target=take_picture)
Thread_picture.start()

try:
    print('UPLAODING IMAGE IN 10 seconds')
    upload_image()
except Exception as e:
    print('UNABLE TO UPLOAD THE IMAGE')
    time.sleep(5)

while True:
    time.sleep(10)
    try:
        rectangle_data = get_bounded_rectangles_with_device_id(constants.CAMERA_ID)
        print(rectangle_data)
        if len(rectangle_data) < 1:
            print('NO RECTANGLES DRAWN')
            print('RETRY IN 5 seconds')
            time.sleep(5)
            continue
    except Exception as e:
        print('NO RECTANGLE')
        print('RETRY IN 5 seconds')
        time.sleep(5)
        continue
    
    else:
        # in case the program is getting rectangles first time
        if count == 1:
            # pass the image
            if len(rectangle_data) > 0:
                thread1 = threading.Thread(target=detect.start_detection,args=(rectangle_data,))
                thread1.start()
                previous_rectangles_data = rectangle_data

                count = 2
                time.sleep(10)
            else:
                print('NO RECTANGLES DRAWN')
        else:
            change_status = check_change(rectangle_data,previous_rectangles_data)
            
            if change_status:
                print('DETECTED CHANGE IN RECTANGLES')
                # change the variable here to exit the thread
                constants.CONTINUE_THREAD = False
                count = 1
                print('INITIATING DETECTION AGAIN IN 10 SECONDS')
                time.sleep(10)
                constants.CONTINUE_THREAD = True
                
