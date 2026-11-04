import turtle

root = None
screen = None
pen = None

def _init_root(main_root):
    global root, screen, pen

    root = main_root

    def initialise():
        global screen, pen
        screen = turtle.Screen()
        pen = turtle.Turtle()

    root.after(0, initialise)

def _draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

def draw_line(x1, y1, x2, y2):
    root.after(0, _draw_line, x1, y1, x2, y2)

def fill_tri(x1, y1, x2, y2, x3, y3):
    root.after(0, pen.begin_fill)
    draw_line(x1, y1, x2, y2)
    draw_line(x2, y2, x3, y3)
    draw_line(x3, y3, x1, y1)
    root.after(0, pen.end_fill)

def set_color(c):
    pen.color(c)
    pen.fillcolor(c)

def set_title(name):
    root.after(0, screen.title, name)

def set_width(w):
    root.after(0, pen.width, w)

def clear():
    root.after(0, pen.clear)

def update():
    root.after(0, screen.update)

def setup_screen(width, hight, bg=(0, 0, 0)):
    root.after(0, screen.screensize(width, hight, bg))
