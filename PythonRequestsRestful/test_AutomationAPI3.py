import pytest
import requests

def test_sample1():
    assert 5 == 5
def test_sample2():
    assert 6 != 4
def test_sample3():
    url = "https://restful-booker.herokuapp.com/booking/"
    id = 23
    URL = url + str(id)
    response_body = requests.get(URL)
    assert response_body.status_code == 200

    data = response_body.json()

    assert "firstname" in data, "First name is not present"
    assert "lastname" in data, "last name is not present"

    assert data["firstname"] == "Josh", "Name is not correct"
    assert data["lastname"] == "Allen", "Second name not present"
    assert data["bookingdates"]["checkin"] == "2018-01-01"
