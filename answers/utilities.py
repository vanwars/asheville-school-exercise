from tkinter import Canvas, Tk

def create_canvas(width=None, height=None, title="Animation", background="white"):
    gui = Tk()
    gui.title(title)
    width = width or gui.winfo_screenwidth()
    height = height or gui.winfo_screenheight()
    canvas = Canvas(gui, width=width, height=height, background=background)
    canvas.pack()
    return canvas

def clear(canvas):
    canvas.delete("all")

def update(canvas):
    gui = canvas.winfo_toplevel()  
    gui.update()


def circle(canvas, centerX, centerY, radius, color='#FF4136', tag=None, stroke_width=2, outline=None):
    ellipse(
        canvas, centerX, centerY, radius, radius, color=color, tag=tag,
        stroke_width=stroke_width, outline=outline
    )

def ellipse(canvas, centerX, centerY, radius_x, radius_y, color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = centerX, centerY
    return canvas.create_oval(
        [ x - radius_x, y - radius_y, x + radius_x, y + radius_y ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )

def rect(canvas, x, y, width, height, color="#3D9970", tag=None):
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)], 
        fill=color, 
        width=0,
        tags=tag
    )
    

# def update_position(canvas, tag, x=2, y=0):
#     '''
#     updates the x and y position of all shapes that have been tagged
#     with the tag argument
#     '''
#     canvas.move(tag, x, y)




def make_star(canvas, center, diameter):
    '''
    demo function that show you how to draw a star, given the convenience
    functions that are available in this module
    '''
    circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=0,
        outline='white',
        color='white'
    )

def make_bubble(canvas, center, diameter):
    '''
    demo function that show you how to draw a bubble, given the convenience
    functions that are available in this module
    '''
    circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=1,
        outline='white',
        color=None
    )