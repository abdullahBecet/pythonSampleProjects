import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

def locNum(number):
    number = phonenumbers.parse(number)
    return(geocoder.description_for_number(number,'tr'))

def carNum(number):
    number=phonenumbers.parse(number)
    return(carrier.name_for_number(number,'tr'))

def zoneNum(number):
    number=phonenumbers.parse(number)
    return(timezone.time_zones_for_number(number))


def main():
    number=input("Please add country code to the beginning of your number: ")
    print(f"Your number location is {locNum(number)}.")
    print(f"Your number carrier is {carNum(number)}.")
    print(f"Your number time zone is {zoneNum(number)}.")

main()


