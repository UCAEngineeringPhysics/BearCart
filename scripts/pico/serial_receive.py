"""
Upload this script to the pico board, then rename it to main.py.
"""
import sys
import select
from machine import Pin, PWM

# SETUP
motor = PWM(Pin(15))
servo = PWM(Pin(16))
motor.freq(50)
servo.freq(50)
poller = select.poll()
poller.register(sys.stdin, select.POLLIN)
event = poller.poll()

# LOOP
while True:
    # read data from serial
    for msg, _ in event:
        buffer = msg.readline().rstrip().split(',')
        if len(buffer) == 2:
            servo_duty, motor_duty = int(buffer[0]), int(buffer[1])
            servo.duty_ns(servo_duty)
            motor.duty_ns(motor_duty)