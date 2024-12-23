import requests
import constants

def get_occupancy_status():
    url = f"{constants.SERVER_IP}/{constants.OCCUPANCY_URL}"
    try:
        response = requests.get(url,timeout=3)
        # response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        status_data = response.json()
        print(f'SERVER RETUREND {status_data[0]["Status"]} OCCUPANCY STATUS')
        # Convert the status data to the required format
        return status_data[0]['Status']
        
    except Exception as e:
        print(f"Error fetching occupancy status: {e}")
        return None

if __name__ == '__main__':
    result = get_occupancy_status()
    print(result)