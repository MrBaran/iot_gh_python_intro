from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

print("IoT Greenhouse.\n")
#Make up a name for your house and enter below
name = "your house name here"

ghs = IoTGreenhouseService()
ghs.greenhouse.name = name
number = ghs.greenhouse.house_number

print("House Number: " + number)

tempF = ghs.temperature.get_inside_temp_F()
print("House temperature is " + str(tempF))
state = ghs.servo.get_status()
print("House state is " + state)

ghs.web_service.post_greenhouse()

threshold = tempF + 5
print("Threshold set to " + str(threshold))

while True:
    tempF = ghs.temperature.get_inside_temp_F()
    status = ghs.servo.get_status()
    print("temp = " + str(tempF))
    if tempF > threshold and status == "CLOSED":
        print("opening")
        ghs.servo.move(+1)
    elif tempF < threshold and status == "OPEN":
        print("closing")
        ghs.servo.move(-1)
        
    #part 2
    fan_status = ghs.fan.get_status()
    if tempF > threshold + 5 and fan_status == "OFF":
        print("Activating fan.")
        ghs.fan.on()
    elif tempF < threshold + 5 and fan_status == "ON":
        print("Fan is off.")
        ghs.fan.off()
    
    #part 3
    #use white led to simulate heater
    heater_status = ghs.lamps.white.get_status()
    if tempF < threshold - 5 and heater_status == "OFF":
        print("Activating heater.")
        ghs.lamps.white.on()
    if tempF > threshold - 5 and heater_status == "ON":
        print("Heater is off.")
        ghs.lamps.white.off()

    ghs.web_service.post_greenhouse()
    sleep(5)


