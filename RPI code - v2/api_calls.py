import requests
import constants
# from pic import take_picture
import time

def get_bounded_rectangles_with_device_id(camera_id):
    url = f"http://{constants.IOTSERVER}/getRectangleData/{camera_id}"
    # try:
    response = requests.get(url,timeout=3)
    response.raise_for_status()  # Check if the request was successful
    data = response.json()
    return data
    # except requests.exceptions.HTTPError as http_err:
    #     print(f"HTTP error occurred: {http_err}")
    # except Exception as err:
    #     print(f"An error occurred: {err}")

# Function to upload an image
def upload_image():
    time.sleep(10)
    upload_url = f"http://{constants.IOTSERVER}/fetch-image"
    
    with open('camera_image.jpg', 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(upload_url, files=files,timeout=3)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        if data['success']:
            print(f"Image uploaded successfully. Filename: {data['filename']}")
            return data['filename']


# Function to get automation status
# def get_automation_status(device_id):
#     base_url = f"http://{constants.IOTSERVER}/getAutomationStatus/"
#     url = f"{base_url}{device_id}"
#     response = requests.get(url,timeout=3)
#     response.raise_for_status()  # Check if the request was successful
#     data = response.json()
    
#     return data['Manual_Status']

# def change_manual_status(deviceid):
#     url = f"http://{constants.IOTSERVER}/updateManualStatus/{deviceid}"  # Replace with your API URL
#     payload = {'Manual_Status': 0}  # Replace with the appropriate value
#     headers = {'Content-Type': 'application/json'}
    
#     response = requests.put(url, json=payload, headers=headers)
    
#     if response.status_code == 200:
#         print("API call successful: Manual status updated successfully.")
#     else:
#         print(f"API call failed with status code {response.status_code}: {response.text}")


def change_device_status(rectangleID,status):
    url = f"http://{constants.IOTSERVER}/updateBoardStatus/{rectangleID}"  # Replace with your actual API URL
    payload = {'status': status}
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.put(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("Device status updated successfully")
        elif response.status_code == 404:
            print("Device not found")
        else:
            print(f"Failed to update device status. Status code: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"Error occurred while updating device status: {str(e)}")


def check_server_status():
    api_url = f'http://{constants.IOTSERVER}/checkServerStatus'
    response = requests.get(api_url,timeout=3)
    data = response.json()
    server_status = data.get('serverStatus', False)
    return server_status