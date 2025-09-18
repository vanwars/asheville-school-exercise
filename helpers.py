def make_circle(canvas, center, radius, color='#FF4136', tag=None, stroke_width=2, outline=None):
    make_oval(
        canvas, center, radius, radius, color=color, tag=tag,
        stroke_width=stroke_width, outline=outline
    )

def make_oval(canvas, center, radius_x, radius_y, color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    return canvas.create_oval(
        [ x - radius_x, y - radius_y, x + radius_x, y + radius_y ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )

def make_rectangle(canvas, top_left, width, height, color="#3D9970", tag=None):
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)], 
        fill=color, 
        width=0,
        tags=tag
    )
    

def update_position(canvas, tag, x=2, y=0):
    '''
    updates the x and y position of all shapes that have been tagged
    with the tag argument
    '''
    canvas.move(tag, x, y)

def make_car(canvas, top_left=(0, 0), color="#3D9970", tag=None):
    '''
    demo function that show you how to draw a car, given the convenience
    functions that are available in this module
    '''
    x, y = top_left
    make_rectangle(canvas, (x + 50, y), 100, 40, color=color, tag=tag)
    make_rectangle(canvas, (x, y + 30), 200, 45, color=color, tag=tag)
    make_circle(canvas, (x + 50, y + 80), 20, color='black', tag=tag)
    make_circle(canvas, (x + 150, y + 80), 20, color='black', tag=tag)

def make_star(canvas, center, diameter):
    '''
    demo function that show you how to draw a star, given the convenience
    functions that are available in this module
    '''
    make_circle(
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
    make_circle(
        canvas,
        center,
        diameter / 2,
        stroke_width=1,
        outline='white',
        color=None
    )