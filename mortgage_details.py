from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("LLYODS BANK")

# =========================================== Form Top Section ==============================================================
Tops = Frame(root, width = 1600,  relief = SUNKEN)
Tops.pack(side=TOP)

Tops1 = Frame(root, width = 1600, height = 5,  relief = SUNKEN, bg = "steel blue")
Tops1.pack(side=TOP)

lblInfo = Label(Tops , font =('arial', 50 , 'bold'), text = "LLYODS BANK", fg = "Steel Blue", bd = 10 , anchor = 'w')
lblInfo.grid(row = 0 , column = 0)

lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "Sole /Joint Lloyds Bank account", fg = "Steel Blue", bd = 10 , anchor = 'w')
lblInfo.grid(row = 1 , column = 0)


# =========================================== Form Body Section =============================================================

form_body_left = Frame(root, width = 800 ,height = 500, relief = SUNKEN)
form_body_left.pack(side = LEFT)

form_body_right = Frame(root, width = 800 ,height = 500 , relief = SUNKEN)
form_body_right.pack(side = RIGHT)

form_body_bottom = Frame(root, width = 1600 ,height = 100 , relief = SUNKEN)
form_body_bottom.pack(side = BOTTOM)

form_body_bottom1 = Frame(root, width = 1600 ,height = 5 , relief = SUNKEN ,bg = "steel blue")
form_body_bottom1.pack(side = BOTTOM)

# ======================================= Info ==================================================

lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "8.3 Your Mortgage Details", fg = "white",bg = "dark green", bd = 10 , anchor = 'w')
lblInfo.grid(row = 2 , column = 0)

# ========================================== form =================================================

want_debit_card = IntVar()
want_debit_card1 = IntVar()
name_on_card = StringVar()
mothers_name = StringVar()
birth_date = StringVar()
rand = StringVar()
fries = StringVar()
burger = StringVar()
drinks = StringVar()

q_1 = "The total amount of any borrowing"
q_2 = "or credit facilities held on a"
q_3 = "joint basis should be shown in full"
q_4 = "against both account holders."
# ============================================ customer 1 ==============================================

customer_1_section = Label(form_body_left , pady = 10, font =('arial', 20, 'bold' ), text = "First Customer", fg = "Steel Blue" , anchor = 'w')
customer_1_section.grid(row = 0)

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "Do you have a mortgage?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 1 )

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16),text = "Yes", variable = want_debit_card1 ,bd = 5,)
want_debit_checkbox1.grid(row =2 ,column = 1,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16),text = "No", variable = want_debit_card1 ,bd = 5,)
want_debit_checkbox1.grid(row = 3 ,column = 1,sticky = 'w')

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "If yes is it with Lloyds Bank?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 4 )

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16),text = "Yes", variable = want_debit_card1 ,bd = 5,)
want_debit_checkbox1.grid(row =5 ,column = 1,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16),text = "No", variable = want_debit_card1 ,bd = 5,)
want_debit_checkbox1.grid(row = 6 ,column = 1,sticky = 'w')

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "What is the outstanding", fg = "black" , anchor = 'w')
lblInfo.grid(row = 7, column = 0 )
lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "balance on your mortgage?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 8, column = 0 )
txtDrinks = Entry(form_body_left, font = ('arial',16,'bold'), textvariable = drinks , bd =10, insertwidth = 4, width = 20,
                        bg = "powder blue", justify = "right" )
txtDrinks.grid(row = 8, column = 1)

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "What is the value of your house?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 9, column = 0 )
txtDrinks = Entry(form_body_left, font = ('arial',16,'bold'), textvariable = drinks , bd =10, insertwidth = 4, width = 20,
                        bg = "powder blue", justify = "right" )
txtDrinks.grid(row = 9, column = 1)

# ============================================ customer 2 ==============================================

customer_1_section = Label(form_body_right , pady = 10, font =('arial', 20, 'bold' ), text = "Second Customer", fg = "Steel Blue" , anchor = 'w')
customer_1_section.grid(row = 0)

lblInfo = Label(form_body_right, font =('arial', 15, "bold"), text = "Do you have a mortgage?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 1 )

want_debit_checkbox1 = Checkbutton(form_body_right,  font = ('arial',16),text = "Yes", variable = want_debit_card1 ,bd = 5,)
want_debit_checkbox1.grid(row =2 ,column = 1,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_right,  font = ('arial',16),text = "No", variable = want_debit_card1 ,bd = 5,)
want_debit_checkbox1.grid(row = 3 ,column = 1,sticky = 'w')

lblInfo = Label(form_body_right, font =('arial', 15, "bold"), text = "If yes is it with Lloyds Bank?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 4 )

want_debit_checkbox1 = Checkbutton(form_body_right,  font = ('arial',16),text = "Yes", variable = want_debit_card1 ,bd = 5,)
want_debit_checkbox1.grid(row =5 ,column = 1,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_right,  font = ('arial',16),text = "No", variable = want_debit_card1 ,bd = 5,)
want_debit_checkbox1.grid(row = 6 ,column = 1,sticky = 'w')

lblInfo = Label(form_body_right, font =('arial', 15, "bold"), text = "What is the outstanding", fg = "black" , anchor = 'w')
lblInfo.grid(row = 7, column = 0 )
lblInfo = Label(form_body_right, font =('arial', 15, "bold"), text = "balance on your mortgage?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 8, column = 0 )
txtDrinks = Entry(form_body_right, font = ('arial',16,'bold'), textvariable = drinks , bd =10, insertwidth = 4, width = 20,
                        bg = "powder blue", justify = "right" )
txtDrinks.grid(row = 8, column = 1)

lblInfo = Label(form_body_right, font =('arial', 15, "bold"), text = "What is the value of your house?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 9, column = 0 )
txtDrinks = Entry(form_body_right, font = ('arial',16,'bold'), textvariable = drinks , bd =10, insertwidth = 4, width = 20,
                        bg = "powder blue", justify = "right" )
txtDrinks.grid(row = 9, column = 1)

# ============================================ bottom section ==============================================

previousbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                text = 'Previous', bg = "powder blue").grid(row = 1, column = 0)

nextbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                text = 'Next', bg = "powder blue").grid(row = 1, column = 1)

# -----------------------------------------------------------------------------------------------------
root.mainloop()