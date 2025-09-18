from tkinter import messagebox, Canvas, Tk
import random
from helpers import make_star, make_bubble

gui = Tk()
gui.title('Starry Night')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
canvas = Canvas(gui, width=window_width, height=window_height, background='#000022')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

# TODO: the code below (lines 28-50) is repetitive. Replace it with a loop to make
# 1,000 stars that fill the entire canvas. Hints:
#   a) use a loop
#   b) use the random module, and in particular the random.uniform function to
#      to give each star a random (x, y) position and a random width.
#   c) bonus: Draw a constellation (Orion's Belt, Big Dipper, etc.) 

# Create 1000 random stars across the canvas

make_bubble(canvas, (100, 100), 10)
make_bubble(canvas, (200, 200), 30)
make_bubble(canvas, (300, 300), 20)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()