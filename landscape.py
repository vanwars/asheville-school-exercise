import time
import random
from utilities import rect, circle, create_canvas, clear, update

# create the canvas (window for drawing)
canvas = create_canvas(title="Starry Night", background="#000022")
window_width = canvas.winfo_screenwidth()
window_height = canvas.winfo_screenheight()

# variables that hold values for what the circle should look like
x = 400
y = 200
radius =20
outline_width = 1
outline_color = 'white'
fill_color = '#669bbc'  # Place to find nice colors: https://coolors.co/palettes/trending
circle(canvas, x, y, radius=radius, stroke_width=outline_width, outline=outline_color, color=fill_color)


########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()