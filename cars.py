import time
from utilities import rect, circle, create_canvas, clear, update

# 1. Define the draw_car function:
def draw_car(canvas, x=0, y=0, color="#3D9970", tag=None):
    rect(canvas, x + 50, y, 100, 40, color=color, tag=tag) # top of the car
    rect(canvas, x, y + 30, 200, 45, color=color, tag=tag) # bottom of the car
    circle(canvas, x + 50, y + 80, 20, color='black', tag=tag) # left wheel
    circle(canvas, x + 150, y + 80, 20, color='black', tag=tag) # right wheel

# 2. Create the canvas (window for drawing)
canvas = create_canvas(title="Animation", background="white")
window_width = canvas.winfo_screenwidth()
window_height = canvas.winfo_screenheight()

# 3. create a variable to store the x position of the car:
car1_x = 0

# 4. Draw the car in the initial position...
draw_car(canvas, x=car1_x, y=50, color="teal", tag="car1")
update(canvas)





########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()