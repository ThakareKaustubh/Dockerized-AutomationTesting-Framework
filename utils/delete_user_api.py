import requests


def delete_user_from_api(url, email, passwd):
    payload = {
        "email": email,
        "password": passwd
    }
    response = requests.delete(f"{url}/api/deleteAccount", data=payload)
    if response.status_code == 200:
        return response.json()["message"]

    elif response.status_code != 200:
        raise Exception(f"User creation failed: {response.text}")
