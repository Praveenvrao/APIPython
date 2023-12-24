# API
#Requests

import requests
def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/5383")
    print(response_body.text)
    print(response_body.status_code)
    #print(response_body.json())
    if response_body.status_code == 200:
        print("TC1 Status code is successful")
    else:
        print("TC1 Status code is not successful")

if __name__ == "__main__":
    main()

#---------------------------

def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/5")
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.headers)
    print(response_body.json())
    if response_body.status_code == 200:
        print("TC1 Status code is successful")
    else:
        print("TC1 Status code is not successful")

if __name__ == "__main__":
    main()

