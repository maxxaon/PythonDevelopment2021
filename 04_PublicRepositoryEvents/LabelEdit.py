import tkinter as tk
import string


class InputLabel(tk.Label):
    def __init__(self, master=None, text=''):
        tk.Label.__init__(self, master, text=text, takefocus=True, highlightthickness=2, font=('Monospace', 16))
        self.symbol_width = 13

        self.Cursor = tk.Frame(self, background="blue", height=100, width=2)
        self.cursor_position = 0

        self.bind('<Any-KeyPress>', lambda e: self.keyboard_handler(e))
        self.bind('<Button-1>', lambda e: self.mouse_leftclick_handler(e))

        self.Cursor.place(x=0, y=0)
    
    def keyboard_handler(self, event):
        if event.keysym == 'Left':
            self.cursor_position = max(self.cursor_position - 1, 0)
        elif event.keysym == 'Right':
            self.cursor_position = min(self.cursor_position + 1, len(self['text']))
        elif event.keysym == 'Home':
            self.cursor_position = 0
        elif event.keysym == 'End':
            self.cursor_position = len(self['text'])
        elif event.keysym == 'BackSpace':
            if self.cursor_position == 0:
                return
            self['text'] = self['text'][:self.cursor_position - 1] + self['text'][self.cursor_position:]
            self.cursor_position -= 1
        elif event.keysym == 'Tab':
            return
        elif len(event.char) > 0 and event.char in string.printable:
            self['text'] = self['text'][:self.cursor_position] + event.char + self['text'][self.cursor_position:]
            self.cursor_position += 1     

        self.place_cursor()   
    
    def mouse_leftclick_handler(self, event):
        self.focus()
        self.cursor_position = event.x // self.symbol_width

        self.place_cursor()

    def place_cursor(self):
        self.Cursor.place(x=self.cursor_position * self.symbol_width, y=0)
        

space = tk.Tk()
space.title('LabelEditTest')

input_label = InputLabel(text='1567')
input_label.grid()

space.mainloop()