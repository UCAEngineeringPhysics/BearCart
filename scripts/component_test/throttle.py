import sys
import os
from gpiozero import PhaseEnableMotor
from time import sleep
import json

# Load configs
params_file_path = os.path.join(os.path.dirname(sys.path[0]), 'configs.json')
params_file = open(params_file_path)
params = json.load(params_file)

# SETUP
is_lifted = input("Is any tire having contact with the ground or other objects? [yes/no]")
assert is_lifted=="no"
is_ready = input("Are you ready to start motor test? [yes/no]")
assert is_ready=="yes"
print("Motor will increase and decrease speed. Both directions will be tested. Please fasten your seat belt!")
for i in reversed(range(1, 4)):
    print(i)
    sleep(1)
print("Here we go...")

# LOOP
try:
    motor = PhaseEnableMotor(
        phase=params['throttle_dir_pin'], 
        enable=params['throttle_pwm_pin'],
    )
    for i in range(100):
        motor.forward(i*0.01)
        print(f"Forward at {i*0.01}")
        sleep(0.2)
    for i in reversed(range(100)):
        motor.forward(i*0.01)
        print(f"Forward at {i*0.01}")
        sleep(0.2)
    print("Stop")
    motor.stop()
    sleep(1)
    for i in range(100):
        motor.backward(i*0.01)
        print(f"Backward at {i*0.01}")
        sleep(0.2)
    for i in reversed(range(100)):
        motor.backward(i*0.01)
        print(f"Backward at {i*0.01}")
        sleep(0.2)
except KeyboardInterrupt:
    motor.stop()
    motor.close()
    print("Test interrupted!")

motor.stop()
motor.close()
print("Test completed!")

