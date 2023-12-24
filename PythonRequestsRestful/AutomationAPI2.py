import requests


def main() -> object:
    url = "https://restful-booker.herokuapp.com/booking/"
    id = 23
    URL = url + str(id)
    response_body = requests.get(URL)
    assert response_body.status_code == 200

    data = response_body.json()

    assert "firstname" in data, "First name is not present"
    assert "lastname" in data, "last name is not present"

    assert data["firstname"] == "John", "Name is not correct"
    assert data["lastname"]  == "Smith", "Second name not present"
    assert data["bookingdates"]["checkin"] == "2018-01-01"

if __name__ == "__main__":
    main()
