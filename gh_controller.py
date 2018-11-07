from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()
number = ghs.greenhouse.house_number

print("IoT Greenhouse - Python Introduction.")
print("House Number: " + number)
print()

print("Greenhouse controller")
print()

print("Turn potentiometer fully counter-clockwise.")
while ghs.analog.pot.get_value() > 0:
    pass

current_temp = ghs.temperature.get_inside_temp_F()
print("Current internal temperature is " + str(current_temp))
print("Turn pot to set threshold temperature.")
print("Press push-button switch when done.")
old_threshold = current_temp
threshold = current_temp
while ghs.switches.push_button.is_off():
    pot_value = ghs.analog.pot.get_value()
    threshold = round(current_temp + pot_value/1023 * 10, 1)
    if threshold != old_threshold:
        print(threshold, end=" ")
        old_threshold = threshold
    sleep(.5)

print("Turn potentiometer fully counter-clockwise.")
while ghs.analog.pot.get_value() > 0:
    pass

pos_index = 1
# Can you create code that uses the pot to set
# an open position for the louver that is less than 1?
print("Turn pot to set open position.")
print("Press push-button switch when done.")
while ghs.switches.push_button.is_off():
    pot_value = ghs.analog.pot.get_value()
    pos_index = pot_value/1023
    ghs.servo.move(pos_index)
    sleep(.2)

while True:
    tempF = ghs.temperature.get_inside_temp_F()
    print("temp = " + str(tempF))
    if tempF > threshold and status == "CLOSED":
        print("opening")
        ghs.servo.move(pos_index)
    elif tempF < threshold and status == "OPEN":
        print("closing")
        ghs.servo.move(0)
    sleep(5)


