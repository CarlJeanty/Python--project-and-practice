# creating my function 
def mu_function():
    print('hello')
    print("Buy")
# notes 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def face_back():
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right() 
    while front_is_clear():
        move()
    turn_left()
        
#for i in range(1,7):
#    jump()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()