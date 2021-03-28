import tkinter as tk
import re

def canvas_to_text():
    text.delete('1.0', tk.END)
    for oval in canvas.find_all():
        x0, y0, x1, y1 = canvas.coords(oval)
        border_color, fill_color = canvas.itemcget(oval, 'outline'), canvas.itemcget(oval, 'fill')
        width = canvas.itemcget(oval, 'width')
        
        text.insert(tk.END, f'coords {x0} {y0} {x1} {y1} width {width} fill_color {fill_color} border_color {border_color}\n')

def text_to_canvas():
    lines = text.get("1.0", tk.END).splitlines()
    canvas.delete('all')
    text.tag_delete("mistake")

    for line_num in range(len(lines)):
        if (lines[line_num].strip() == ''):
            continue
        try:
            _coords, x0, y0, x1, y1, _width, width, _fill_color, fill_color, _border_color, border_color = lines[line_num].split()
            assert(_coords == 'coords' and _width == 'width' and _fill_color == 'fill_color' and _border_color == 'border_color')
            canvas.create_oval(float(x0), float(y0), float(x1), float(y1), width=float(width), outline=border_color, fill=fill_color)
        except:
            line_num_tk = line_num + 1
            text.tag_add("mistake", f"{line_num_tk}.0", f"{line_num_tk}.end")
    text.tag_config("mistake", foreground="red")
    
    



space = tk.Tk()

text = tk.Text(space)
text.grid(row=1, column=0, sticky="NEWS")

canvas = tk.Canvas(space)
canvas.grid(row=1, column=1, sticky="NEWS")

text_to_canvas_button = tk.Button(space, text='text to canvas', command=text_to_canvas)
canvas_to_text_button = tk.Button(space, text='canvas to text', command=canvas_to_text)
text_to_canvas_button.grid(row=0, column=0)
canvas_to_text_button.grid(row=0, column=1)


space.columnconfigure(0, weight=1)
space.columnconfigure(1, weight=1)
space.rowconfigure(1, weight=1)


canvas.bind('<ButtonPress-1>', lambda e: button_press(e))
canvas.bind('<ButtonRelease>', lambda e: button_release(e))
canvas.bind('<Motion>', lambda e: motion(e))

operation = "nothing" # nothing, creating, moving
current_oval = None
press_x = None
press_y = None

def button_press(event):
    global operation, current_oval, press_x, press_y

    press_x = event.x
    press_y = event.y
    ovals = canvas.find_overlapping(press_x, press_y, press_x, press_y)
    if len(ovals) > 0:
        operation = 'moving'
        current_oval = ovals[-1]
        canvas.tag_raise(current_oval)
    else:
        operation = 'creating'
        current_oval = canvas.create_oval(press_x, press_y, press_x, press_y, width=2, fill='blue')

def button_release(event):
    global operation

    operation = 'nothing'

def motion(event):
    global press_x, press_y

    x, y = event.x, event.y

    if operation == 'moving':
        canvas.move(current_oval, x - press_x, y - press_y)
        press_x = x
        press_y = y
    elif operation == 'creating':
        canvas.coords(current_oval, press_x, press_y, x, y)


space.mainloop()