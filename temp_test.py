from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()
number = ghs.greenhouse.house_number

print("IoT Greenhouse - Python Introduction.")
print("House Number: " + number)
print()

print("Investigate temperature service.")
print("Use your finger on sensor to warm.")
print("Press PB switch to end.")
while ghs.switches.push_button.is_off():
    #investigate temperature service
    inside_temp = ghs.temperature.get_inside_tempF()
    outside_temp = ghs.temperature.get_outside_tempF()
    print("Inside temp = " + str(inside_temp))
    print("Outside temp = " + str(outside_temp ))
    sleep(2)
    print()

print("Pot test completed.")
