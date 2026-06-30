def turn_right():
    turn_left()
    turn_left()
    turn_left()
def wall_on_left():
    turn_right()
    if wall_in_front():
        turn_left()
        move()
while not(at_goal()):
    if front_is_clear():
        move()
    else:
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        move()
        while not wall_in_front():
            wall_on_left()
        turn_left()    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
