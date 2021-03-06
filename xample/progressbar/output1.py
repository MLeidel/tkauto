'''
code file:
date:
commants:
    tkauto generated
    progressbar
'''

from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        # self.columnconfigure(1, weight=1, pad=100)
        # self.rowconfigure(1, weight=1, pad=20)

        # customize widget style when using ttk...
        # style = Style()
        # style.configure("TButton", width=10)

        self.progbar = Progressbar(self, orient='horizontal', mode='indeterminate', maximum=20 )
        self.progbar.grid(row=1, column=1)
        # self.progbar.start() | self.progbar.stop() | self.progbar.grid_forget() | self.progbar.grid(self, ...)

        btn_on = Button(self, text='Turn On', command=self.prog_on, width=20)
        btn_on.grid(row=2, column=1)

        btn_off = Button(self, text='Turn Off', command=self.prog_off, width=20)
        btn_off.grid(row=3, column=1)

        self.prog_off()

    def prog_on(self):
        ''' show and turn on progressbar '''
        self.progbar.grid(row=1, column=1)  # EDIT
        self.progbar.start()  # EDIT

    def prog_off(self):
        ''' remove and turn off progressbar '''
        self.progbar.grid_forget()  # EDIT
        self.progbar.stop()  # EDIT

# root = Tk()
# Requires ttkthemes module
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="radiance")

root.title("Tkinter Demo")
app = Application(root)
app.mainloop()
