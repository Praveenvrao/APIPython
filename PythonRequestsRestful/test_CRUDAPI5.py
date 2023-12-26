import requests
import pytest


def token_creation():
    print("Token creation")
    URL = "https://restful-booker.herokuapp.com/auth"
    Headers = {"Content-Type": "application/json"}
    Json_Payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(URL, Headers, Json_Payload)
    data = response.json()
    Token = data['token']
    print(Token)
    return Token


'''@pytest.mark.putrequest1
def test_updatebooking():
    print("Updating booking")
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = "2"
    PUT_URL = URL + booking_id
    Cookie_value = "token="+token_creation()
    Headers = {
        "Content-Type": "application/json",
        "Cookie": Cookie_value
    }
    Json_Payload = {
        "firstname": "John",
        "lastname": "CENA",
        "totalprice": 381,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(PUT_URL, Headers, Json_Payload)
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert data["booking"]["firstname"] == "John", "Incorrect firstname printed"
    assert data["bookingdates"]["checkout"] == "2019-01-01"'''


@pytest.mark.delete
def test_delete():
    print("Delete booking")
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = "2"
    PUT_URL = URL + booking_id
    Cookie_value = "token=" + token_creation()
    Headers = {
        "Content-Type": "application/json",
        "Cookie": Cookie_value
    }
    response = requests.delete(PUT_URL, Headers)
    # Assertions
    assert response.status_code == 201
