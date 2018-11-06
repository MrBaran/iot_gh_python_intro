from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()
number = ghs.greenhouse.house_number

print("IoT Greenhouse - Python Introduction.")
print("House Number: " + number)
print()

print("Investigate louver and servo action")
print("Open and close.")
for i in range(0,5):
    ghs.servo.move(1)
    sleep(1)
    ghs.servo.move(0)
    sleep(1)
print("Move through servo range.")
print("Push PB switch to end.")
while ghs.switches.pb_switch.is_off():
    for i in range(0, 5, 1):
        index = i/5
        print("Index = " + str(index))
        ghs.servo.move(index)
        sleep(1)
    for i in range(5, 0, -1):
        index = i/5
        print("Index = " + str(index))
        ghs.servo.move(index)
        sleep(.1)
    print()
print("Servo test completed.")

ghs.switches.pb_switch.wait_fo