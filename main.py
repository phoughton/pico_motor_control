import PicoMotorDriver
import time

board = PicoMotorDriver.KitronikPicoMotor()

motor_left = 1
motor_right = 2

def turn(hand_direction="right", speed=50, hardness=50):
    # hardness between 100 and -90
    # 100 is max with tracks going fully in opposite direction (hard turn)
    # -90 is close to minimum with tracks going at 100 and 90 (slow turn)
    
    lead_track_direction = "f"
    trailing_track_direction = "f"
    
    lead_track_speed = speed
    trailing_track_speed = int((-hardness/100)*speed)
    
    if trailing_track_speed < 0:
        trailing_track_direction = "r"
    
    trailing_track_speed = abs(trailing_track_speed)
    
    if hand_direction == "left":
        board.motorOn(motor_left, trailing_track_direction, trailing_track_speed)
        board.motorOn(motor_right, lead_track_direction, lead_track_speed)
    
    if hand_direction == "right":
        board.motorOn(motor_left, lead_track_direction, lead_track_speed)
        board.motorOn(motor_right, trailing_track_direction, trailing_track_speed)

def dead_stop():
    board.motorOff(motor_left)
    board.motorOff(motor_right)

def spin(direction="right", duration=2):
    if direction not in ["right", "left"]:
        raise ValueError("direction was invalid")
    
    if duration  < 0 or duration > 20:
        raise ValueError("duration was outside expected range")

    turn(hand_direction=direction, speed=100, hardness=90)
    time.sleep(duration)
    dead_stop()

def slow_s():
    turn(hand_direction="right", speed=100, hardness=-50)
    time.sleep(1)
    dead_stop()
    turn(hand_direction="left", speed=100, hardness=-50)
    time.sleep(1)
    dead_stop()


spin("left", 1)

