import yaml
import os
import requests


def load_registration_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'login_test.yaml')
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)["login_data"]


def create_user_from_api(url):
    data = load_registration_data()
    payload = {
        "name": data["username"],
        "email": data["email"],
        "password": data["password"],
        "title": data["title"],
        "birth_date": data["birthdate"]["day"],
        "birth_month": data["birthdate"]["month"],
        "birth_year": data["birthdate"]["year"],
        "firstname": data["address"]["first_name"],
        "lastname": data["address"]["last_name"],
        "company": data["address"]["company"],
        "address1": data["address"]["address1"],
        "address2": data["address"]["address2"],
        "country": data["address"]["country"],
        "zipcode": data["address"]["zipcode"],
        "state": data["address"]["state"],
        "city": data["address"]["city"],
        "mobile_number": data["address"]["mobile_number"],
        "form_type": "create_account"
    }

    response = requests.post(f"{url}/api/createAccount", data=payload)
    if response.json()["responseCode"] == 201:
        return data["email"], data["password"], data["username"]

    elif response.status_code != 200:
        raise Exception(f"User creation failed: {response.text}")

