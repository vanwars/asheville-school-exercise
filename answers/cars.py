import time
from utilities import rect, circle, create_canvas, clear, update

# Function definition here:
def draw_car(canvas, x=0, y=0, color="#3D9970", tag=None):
    '''
    demo function that show you how to draw a car, given the convenience
    functions that are available in this module
    '''
    rect(canvas, x + 50, y, 100, 40, color=color, tag=tag)
    rect(canvas, x, y + 30, 200, 45, color=color, tag=tag)
    circle(canvas, x + 50, y + 80, 20, color='black', tag=tag)
    circle(canvas, x + 150, y + 80, 20, color='black', tag=tag)

# create the canvas (window for drawing)
canvas = create_canvas(title="Animation", background="white")
window_width = canvas.winfo_screenwidth()

# create a variable to store the x position of the car:
car1_x = 0
car2_x = window_width

    

########################## YOUR CODE BELOW THIS LINE ##############################

while True:

    # And again...
    clear(canvas)
    car1_x += 4
    car2_x -= 8
    draw_car(canvas, x=car1_x, y=50, color="teal", tag="car1")
    draw_car(canvas, x=car2_x, y=250, color="hotpink", tag="car2")

    if car1_x > window_width:
        car1_x = -100
    if car2_x < -200:
        car2_x = window_width
    
    update(canvas)
    time.sleep(.01)




########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()