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

lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "1. Your Personal Details (Continuation-2)", fg = "white",bg = "dark green", bd = 10 , anchor = 'w')
lblInfo.grid(row = 2 , column = 0)

# ========================================== form =================================================
debit_desc_1 = "If you are a student, you will only need to complete this form"
debit_desc_2 = "if you do not meet the criteria for a Student account."

want_debit_card = IntVar()
want_debit_card1 = IntVar()
name_on_card = StringVar()
mothers_name = StringVar()
birth_date = StringVar()
rand = StringVar()
fries = StringVar()
burger = StringVar()
drinks = StringVar()

# ============================================ customer 1 ==============================================
customer_1_section = Label(form_body_left , pady = 10, font =('arial', 20, 'bold' ), text = "First Customer", fg = "Steel Blue" , anchor = 'w')
customer_1_section.grid(columnspan = 2)

lblInfo = Label(form_body_left , font =('arial', 15), text = " how long since you last worked?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 1)

lblInfo = Label(form_body_left , font =('arial', 15), text = " Years", fg = "black" , anchor = 'w')
lblInfo.grid(row = 2)

txtCustName = Entry(form_body_left, font = ('arial',15), textvariable = name_on_card ,insertwidth = 4, bd = 5,width = 10,
                        bg = "powder blue", justify = "right" )
txtCustName.grid(row = 3 )

lblInfo = Label(form_body_left , font =('arial', 15), text = "Months", fg = "black" , anchor = 'w')
lblInfo.grid(row = 4)

txtCustName = Entry(form_body_left, font = ('arial',15), textvariable = name_on_card ,insertwidth = 4, bd = 5,width = 10,
                        bg = "powder blue", justify = "right" )
txtCustName.grid(row = 5 )

lblReference = Label(form_body_left, font = ('arial',15), text="Your country of birth" , bd =5, anchor ='w' )
lblReference.grid(row = 6, column =0)
txtReference = Entry(form_body_left, font = ('arial',15), textvariable = rand , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtReference.grid(row = 6, column =1)

lblFries = Label(form_body_left, font = ('arial',15), text="Your Town/City of birth" , anchor ='w' )
lblFries.grid(row = 7, column =0)
txtReference = Entry(form_body_left, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtReference.grid(row = 7, column =1)

lblBurger = Label(form_body_left, font = ('arial',15,), text="Your Nationality" , anchor ='w' )
lblBurger.grid(row = 8, column =0)
txtBurger = Entry(form_body_left, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 8, column =1)

lblFries = Label(form_body_left, font = ('arial',15), text="Your additional nationalities" , anchor ='w' )
lblFries.grid(row = 9, column =0)

txtBurger = Entry(form_body_left, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 10, column =0)

txtBurger = Entry(form_body_left, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 10, column =1)

txtBurger = Entry(form_body_left, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 11, column =0)

txtBurger = Entry(form_body_left, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 11, column =1)

txtBurger = Entry(form_body_left, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 12, column =0)

lblFries = Label(form_body_left, font = ('arial',15), text="Country of Residence" , anchor ='w' )
lblFries.grid(row = 13, column =0)
txtReference = Entry(form_body_left, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtReference.grid(row = 13, column =1)
# ============================================ customer 2 ==============================================
customer_1_section = Label(form_body_right , pady = 10, font =('arial', 20, 'bold' ), text = "Second Customer", fg = "Steel Blue" , anchor = 'w')
customer_1_section.grid(row = 0)

lblInfo = Label(form_body_right , font =('arial', 15), text = "how long since you last worked?", fg = "black" , anchor = 'w')
lblInfo.grid(row = 1)

lblInfo = Label(form_body_right , font =('arial', 15), text = " Years", fg = "black" , anchor = 'w')
lblInfo.grid(row = 2)

txtCustName = Entry(form_body_right, font = ('arial',15), textvariable = name_on_card ,insertwidth = 4, bd = 5,width = 10,
                        bg = "powder blue", justify = "right" )
txtCustName.grid(row = 3 )

lblInfo = Label(form_body_right , font =('arial', 15), text = "Months", fg = "black" , anchor = 'w')
lblInfo.grid(row = 4)

txtCustName = Entry(form_body_right, font = ('arial',16), textvariable = name_on_card ,insertwidth = 4, bd = 5,width = 10,
                        bg = "powder blue", justify = "right" )
txtCustName.grid(row = 5 )

lblReference = Label(form_body_right, font = ('arial',15), text="Your country of birth" , bd =5, anchor ='w' )
lblReference.grid(row = 6, column =0)
txtReference = Entry(form_body_right, font = ('arial',15), textvariable = rand , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtReference.grid(row = 6, column =1)

lblFries = Label(form_body_right, font = ('arial',15), text="Your Town/City of birth" , anchor ='w' )
lblFries.grid(row = 7, column =0)
txtReference = Entry(form_body_right, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtReference.grid(row = 7, column =1)

lblBurger = Label(form_body_right, font = ('arial',15), text="Your Nationality" , anchor ='w' )
lblBurger.grid(row = 8, column =0)
txtBurger = Entry(form_body_right, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 8, column =1)

lblFries = Label(form_body_right, font = ('arial',15), text="Your additional nationalities:" , anchor ='w' )
lblFries.grid(row = 9, column =0)

txtBurger = Entry(form_body_right, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 10, column =0)

txtBurger = Entry(form_body_right, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 10, column =1)

txtBurger = Entry(form_body_right, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 11, column =0)

txtBurger = Entry(form_body_right, font = ('arial',16,'bold'), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 11, column =1)

txtBurger = Entry(form_body_right, font = ('arial',15), textvariable = burger , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtBurger.grid(row = 12, column =0)

lblFries = Label(form_body_right, font = ('arial',15), text="Country of Residence" , anchor ='w' )
lblFries.grid(row = 13, column =0)
txtReference = Entry(form_body_right, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                        bg = "powder blue", justify = "right" )
txtReference.grid(row = 13, column =1)
# ============================================ bottom section ==============================================

previousbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                text = 'Previous', bg = "powder blue").grid(row = 1, column = 0)

nextbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                text = 'Next', bg = "powder blue").grid(row = 1, column = 1)

# -----------------------------------------------------------------------------------------------------
root.mainloop()