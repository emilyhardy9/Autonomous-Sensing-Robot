from gpiozero import Robot, LineSensor

robot = Robot(left=(7, 8), right=(9, 10))
left_sensor = LineSensor(17)
right_sensor = LineSensor(4)
front_sensor = LineSensor(27)

speed = 0.5

def motor_speed():
    while True:
        left_detect = int(left_sensor.value)
        right_detect = int(right_sensor.value)
        front_detect = int(front_sensor.value)
        left_mot = 0
        right_mot = 0

        if left_detect == 0 and right_detect == 1:
            left_mot = 1
        elif left_detect == 1 and right_detect == 0:
            right_mot = -1
        elif front_detect == 0:
            right_mot, left_mot = 0, 0
        else:
            left_mot = -1
            right_mot = 0.9

        yield (right_mot, left_mot)

robot.source = motor_speed()

sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()
front_sensor.close()
