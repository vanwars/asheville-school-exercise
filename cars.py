from tkinter import Canvas, Tk
import time
from helpers import make_car, update_position

gui = Tk()
gui.title("Animation")
canvas = Canvas(gui, width=500, height=500, background="white")
canvas.pack()
########################## YOUR CODE BELOW THIS LINE ##############################

# draw car (and give it a unique tag 'car1')
make_car(canvas, top_left=(0, 50), color="#3D9970", tag="car1")

# Move the car 20 pixels to the right and the sleep for 1 second:
update_position(canvas, "car1", x=20, y=0)
gui.update()
time.sleep(1)

# Do it again...
update_position(canvas, "car1", x=20, y=0)
gui.update()
time.sleep(1)

# And again...
update_position(canvas, "car1", x=20, y=0)
gui.update()
time.sleep(1)

# And again...
update_position(canvas, "car1", x=20, y=0)
gui.update()
time.sleep(1)

# And again...
update_position(canvas, "car1", x=20, y=0)
gui.update()
time.sleep(1)

# And again...
update_position(canvas, "car1", x=20, y=0)
gui.update()
time.sleep(1)


########################## YOUR CODE ABOVE THIS LINE ##############################
# makes sure the canvas keeps running:
canvas.mainloop()