from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x1600+0+0")
root.title("LLYODS BANK")

# =========================================== Form Top Section ==============================================================
Tops = Frame(root, width = 1600,  relief = SUNKEN)
Tops.pack(side=TOP)

lblInfo = Label(Tops , font =('arial', 50 , 'bold'), text = "LLYODS BANK", fg = "Steel Blue", bd = 10 , anchor = 'w')
lblInfo.grid(row = 0 , column = 0)

lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "Sole /Joint Lloyds Bank account", fg = "Steel Blue", bd = 10 , anchor = 'w')
lblInfo.grid(row = 1 , column = 0)

# =========================================== Form Body Section =============================================================

form_body_left = Frame(root, width = 800 ,height = 500, bg = "light blue" , relief = SUNKEN)
form_body_left.pack(side = LEFT)

form_body_right = Frame(root, width = 800 ,height = 500, bg = "dark green" , relief = SUNKEN)
form_body_right.pack(side = RIGHT)

# ======================================= Info ==================================================

lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "2. Your debit card details", fg = "white",bg = "dark green", bd = 10 , anchor = 'w')
lblInfo.grid(row = 2 , column = 0)

# -----------------------------------------------------------------------------------------------------
root.mainloop()