import requests
import constants

def send_request(relay_id,mode):
    # url = f'http://10.112.70.51:3001/updatemode/{board_id}'
    payload = {
        "Relay": relay_id, # 0 , 1 (no automatic detection) 
        "Mode" : mode
    }
    
    url = f'{constants.SERVER_IP}/{constants.DEFAULT_RELAY_URL}/{constants.BOARD_ID}'

    try:
        response = requests.put(url,json=payload,timeout=3)
        if response.status_code == 200:
            print(f'Relay {str(relay_id)} mode changed to {str(mode)}')
            return True
        print(response.status_code)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == '__main__':
    print(send_request(1,1))