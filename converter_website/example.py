import requests

AUTH_URL = "http://localhost:8000/auth"
CONVERT_URL = "http://localhost:8000/convert"
USER = "omri"
PASSWORD = "Password1!"
CONVERT_TEST_JSON = [{"name": "device", "strVal": "iPhone", "metadata": "not interesting"},
                     {"name": "isHuman", "boolVal": "false", "lastSeen": "not interesting"}]


def main():
    response = requests.post(AUTH_URL, json={"username": USER, "password": PASSWORD})
    if response.ok:
        access_token = response.json()['access_token']
        convert_result = requests.post(CONVERT_URL, json=CONVERT_TEST_JSON, headers={'Authorization': 'Bearer ' +
                                                                                                      access_token})
        print(convert_result.json())
    else:
        print("Couldn't connect ")


if __name__ == "__main__":
    main()
