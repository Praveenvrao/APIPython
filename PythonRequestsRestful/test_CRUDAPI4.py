# Creating new booking

import requests
import pytest

@pytest.mark.positivecase
def test_createbooking():
    print("Creating new booking")
    URL = "https://restful-booker.herokuapp.com/booking"
    Headers = {"Content-Type": "application/json"}
    Json_Payload = {
        "firstname": "John",
        "lastname": "Caps",
        "totalprice": 381,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(URL, Headers, Json_Payload)
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "John", "Incorrect firstname printed"
    assert data["bookingdates"]["checkin"] == "2018-01-01"


@pytest.mark.negativecase
def test_createbooking2():
    print("Creating new booking")
    URL = "https://restful-booker.herokuapp.com/booking"
    Headers = "Content-Type: application/json"
    Json_Payload = {}
    response = requests.post(URL, Headers, Json_Payload)
    # Assertions
    assert response.status_code == 500
