import rrb3 as rrb
#from rrb3 import rrb
from random import randint

rr = rrb.RRB3(12, 12) # Battery voltage 12V, motor 12V

T = 20  # 20 seconds to extend


def test_motors():
    rr.set_motors(0, 0, 0, 0)
    print("Are Both motors stopped?")

    rr.set_motors(1, 0, 1, 0)
    print("Are Both motors going forwards?")

    rr.set_motors(0.5, 0, 0.5, 0)
    print("Are both motors going forwards at half speed?")

    rr.set_motors(1, 1, 1, 1)
    print("Are both motors going backwards?")

    rr.set_motors(0, 0, 0, 0)
    print("Are the motors off now?")

test_motors()

extended = False

try:
	while True:
		if rr.get_distance() < 20:
			if extended:  # if extended retract and vice versa
				print("retracting")
				rr.set_led1(True)  # LED 1 on
				rr.reverse(T, 1.0)
				rr.set_led1(False)
				extended = False
			else:
				print("extending")
				rr.set_led2(True)
				rr.forward(T, 1.0)
				rr.set_led2(False)
				extended = True
			print("done")
finally:
	rr.cleanup() # Set all GPIO pins to safe input state
