from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()
number = ghs.greenhouse.house_number

print("IoT Greenhouse - Python Introduction.")
print("House Number: " + number)
print()

print("testing potentiometer values.")
while ghs.switches.push_button.is_off():
    pot_value = ghs.ain_pot.get_value()
    print("Pot value: " + str(pos))
    sleep(1)

print("Pot test completed.")
