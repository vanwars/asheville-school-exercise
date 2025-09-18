import time
import random
from utilities import rect, circle, create_canvas, clear, update

# create the canvas (window for drawing)
my_canvas = create_canvas(title="Starry Night", background="#000022")
window_width = my_canvas.winfo_screenwidth()
window_height = my_canvas.winfo_screenheight()
# create a variable to store the x position of the car:
x_position = 0

########################## YOUR CODE BELOW THIS LINE ##############################

i = 0
while i < 1000:
    x = random.uniform(0, window_width)
    y = random.uniform(0, window_height)
    radius = random.uniform(5, 20)
    fill_color = random.choice(["#780000","#c1121f","#fdf0d5","#003049","#669bbc"])
    circle(my_canvas, x, y, radius, stroke_width=1, outline='white', color=fill_color)
    i += 1

update(my_canvas)




########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
my_canvas.mainloop()