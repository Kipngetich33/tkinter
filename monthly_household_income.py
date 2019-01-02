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

form_body_left = Frame(root, width = 1600 ,height = 500, relief = SUNKEN)
form_body_left.pack(side = LEFT)

# ======================================= Info ==================================================

lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "6.Monthly Household Income and Expenditure", fg = "white",bg = "dark green", bd = 10 , anchor = 'w')
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
# ============================================ section 1 ==============================================

customer_1_section = Label(form_body_left , pady = 10, font =('arial', 20, 'bold' ), text = "First Customer's Income", fg = "Steel Blue" , anchor = 'w')
customer_1_section.grid(row = 0  )

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "Source:", fg = "black" , anchor = 'w', bd = 20)
lblInfo.grid(row = 1 ,column = 0 )

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "If Yes", fg = "steel blue" , anchor = 'w', bd = 20)
lblInfo.grid(row = 1 , column = 1)

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "Frequency e.g Weekly", fg = "black" , anchor = 'w', bd = 20)
lblInfo.grid(row = 1, column = 2 )

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "Direct to a bank", fg = "steel blue" , anchor = 'w', bd = 20)
lblInfo.grid(row = 1, column = 3 )

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "Cheque", fg = "black" , anchor = 'w', bd = 20)
lblInfo.grid(row = 1, column = 4  )

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "Cash", fg = "steel blue" , anchor = 'w', bd = 20)
lblInfo.grid(row = 1, column = 5 )

lblInfo = Label(form_body_left, font =('arial', 15, "bold"), text = "Into this Account", fg = "black" , anchor = 'w', bd = 20)
lblInfo.grid(row = 1, column = 6 )


lblInfo = Label(form_body_left, font =('arial', 15), text = "Salary/ Wages", fg = "black" , anchor = 'w' , bd = 20)
lblInfo.grid(row = 2, column = 0 )

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue", variable = want_debit_card1 )
want_debit_checkbox1.grid(row =2 ,column = 1,sticky = 'w')

txtDrinks = Entry(form_body_left, font = ('arial',16,'bold'), textvariable = drinks , bd =10, insertwidth = 4, width = 20,
                        bg = "powder blue", justify = "right" )
txtDrinks.grid(row = 2, column = 2)

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"),fg = "steel blue", variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =2 ,column = 3,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =2 ,column = 4,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue",variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =2 ,column = 5,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =2 ,column = 6,sticky = 'w')


lblInfo = Label(form_body_left, font =('arial', 15), text = "Benefits", fg = "black" , anchor = 'w' , bd = 20)
lblInfo.grid(row = 3, column = 0 )

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue", variable = want_debit_card1 )
want_debit_checkbox1.grid(row =3,column = 1,sticky = 'w')

txtDrinks = Entry(form_body_left, font = ('arial',16,'bold'), textvariable = drinks , bd =10, insertwidth = 4, width = 20,
                        bg = "powder blue", justify = "right" )
txtDrinks.grid(row = 3, column = 2)

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"),fg = "steel blue", variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =3 ,column = 3,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =3 ,column = 4,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue",variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =3 ,column = 5,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =3 ,column = 6,sticky = 'w')


lblInfo = Label(form_body_left, font =('arial', 15), text = "Pension", fg = "black" , anchor = 'w' , bd = 20)
lblInfo.grid(row = 4, column = 0 )

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue", variable = want_debit_card1 )
want_debit_checkbox1.grid(row =4 ,column = 1,sticky = 'w')

txtDrinks = Entry(form_body_left, font = ('arial',16,'bold'), textvariable = drinks , bd =10, insertwidth = 4, width = 20,
                        bg = "powder blue", justify = "right" )
txtDrinks.grid(row = 4, column = 2)

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"),fg = "steel blue", variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =4,column = 3,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =4 ,column = 4,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue",variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =4,column = 5,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =4 ,column = 6,sticky = 'w')

lblInfo = Label(form_body_left, font =('arial', 15), text = "Investment", fg = "black" , anchor = 'w' , bd = 20)
lblInfo.grid(row = 5, column = 0 )

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue", variable = want_debit_card1 )
want_debit_checkbox1.grid(row =5 ,column = 1,sticky = 'w')

txtDrinks = Entry(form_body_left, font = ('arial',16,'bold'), textvariable = drinks , bd =10, insertwidth = 4, width = 20,
                        bg = "powder blue", justify = "right" )
txtDrinks.grid(row = 5, column = 2)

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"),fg = "steel blue", variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =5 ,column = 3,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =5 ,column = 4,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue",variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =5 ,column = 5,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =5 ,column = 6,sticky = 'w')

lblInfo = Label(form_body_left, font =('arial', 15), text = "Other", fg = "black" , anchor = 'w' , bd = 20)
lblInfo.grid(row = 6, column = 0 )

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue", variable = want_debit_card1 )
want_debit_checkbox1.grid(row =6 ,column = 1,sticky = 'w')

txtDrinks = Entry(form_body_left, font = ('arial',16,'bold'), textvariable = drinks , bd =10, insertwidth = 4, width = 20,
                        bg = "powder blue", justify = "right" )
txtDrinks.grid(row = 6, column = 2)

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"),fg = "steel blue", variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =6 ,column = 3,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =6 ,column = 4,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), fg = "steel blue",variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =6 ,column = 5,sticky = 'w')

want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16,"bold"), variable = want_debit_card1 ,bd = 5)
want_debit_checkbox1.grid(row =6 ,column = 6,sticky = 'w')

# ============================================ bottom section ==============================================

previousbtn = Button(form_body_left,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                text = 'Previous', bg = "powder blue").grid(row = 0, column = 5)

nextbtn = Button(form_body_left,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                text = 'Next', bg = "powder blue").grid(row = 0, column = 6)

# -----------------------------------------------------------------------------------------------------
root.mainloop()