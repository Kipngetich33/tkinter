from tkinter import *
import random, personal_details_continuation_5, personal_details_continuation_7
import time


def  call_this_module():
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

    lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "1.2 Your residential details(Continued_1)", fg = "white",bg = "dark green", bd = 10 , anchor = 'w')
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

    def call_next(requested_action):
            '''
            function that directs the user to the next form
            that the user is supposed to fill
            '''
            root.destroy()
            if(requested_action == "next"):
                personal_details_continuation_7.call_this_module()      
            elif( requested_action == "previous"):
                personal_details_continuation_5.call_this_module()

    # ============================================ customer 1 ==============================================
    customer_1_section = Label(form_body_left , pady = 10, font =('arial', 20, 'bold' ), text = "First Customer", fg = "Steel Blue" , anchor = 'w')
    customer_1_section.grid(row = 0)

    lblInfo = Label(form_body_left , font =('arial', 15), text = "Your previous address", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 1)

    lblInfo = Label(form_body_left , font =('arial', 15), text = "(if less than three years at current address)", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 2)

    txtCustName = Entry(form_body_left, font = ('arial',15), textvariable = name_on_card ,insertwidth = 4, bd = 5,width = 10,
                            bg = "powder blue", justify = "right" )
    txtCustName.grid(row = 3 )

    lblReference = Label(form_body_left, font = ('arial',15), text="Post Code" , bd =5, anchor ='w' )
    lblReference.grid(row = 4, column =0)
    txtReference = Entry(form_body_left, font = ('arial',15), textvariable = rand , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 4, column =1)

    lblFries = Label(form_body_left, font = ('arial',15), text="Country" , anchor ='w' )
    lblFries.grid(row = 5, column =0)
    txtReference = Entry(form_body_left, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 5, column =1)

    lblInfo = Label(form_body_left , font =('arial', 15), text = "When did you start living at this address?", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 6)

    lblReference = Label(form_body_left, font = ('arial',15), text="Month" , bd =5, anchor ='w' )
    lblReference.grid(row = 7, column =0)
    txtReference = Entry(form_body_left, font = ('arial',15), textvariable = rand , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 7, column =1)

    lblFries = Label(form_body_left, font = ('arial',15), text="Year" , anchor ='w' )
    lblFries.grid(row = 8, column =0)
    txtReference = Entry(form_body_left, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 8, column =1)



    # ============================================ customer 2 ==============================================
    customer_1_section = Label(form_body_right , pady = 10, font =('arial', 20, 'bold' ), text = "Second Customer", fg = "Steel Blue" , anchor = 'w')
    customer_1_section.grid(row = 0)

    lblInfo = Label(form_body_right , font =('arial', 15), text = "Your previous address", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 1)

    lblInfo = Label(form_body_right , font =('arial', 15), text = "(if less than three years at current address)", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 2)

    txtCustName = Entry(form_body_right, font = ('arial',15), textvariable = name_on_card ,insertwidth = 4, bd = 5,width = 10,
                            bg = "powder blue", justify = "right" )
    txtCustName.grid(row = 3 )

    lblReference = Label(form_body_right, font = ('arial',15), text="Post Code" , bd =5, anchor ='w' )
    lblReference.grid(row = 4, column =0)
    txtReference = Entry(form_body_right, font = ('arial',15), textvariable = rand , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 4, column =1)

    lblFries = Label(form_body_right, font = ('arial',15), text="Country" , anchor ='w' )
    lblFries.grid(row = 5, column =0)
    txtReference = Entry(form_body_right, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 5, column =1)

    lblInfo = Label(form_body_right , font =('arial', 15), text = "When did you start living at this address?", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 6)

    lblReference = Label(form_body_right, font = ('arial',15), text="Month" , bd =5, anchor ='w' )
    lblReference.grid(row = 7, column =0)
    txtReference = Entry(form_body_right, font = ('arial',15), textvariable = rand , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 7, column =1)

    lblFries = Label(form_body_right, font = ('arial',15), text="Year" , anchor ='w' )
    lblFries.grid(row = 8, column =0)
    txtReference = Entry(form_body_right, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 8, column =1)


    # ============================================ bottom section ==============================================

    previousbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                    text = 'Previous', bg = "powder blue", command = lambda: call_next("previous")).grid(row = 1, column = 0)

    nextbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                    text = 'Next', bg = "powder blue", command = lambda: call_next("next")).grid(row = 1, column = 1)

    # -----------------------------------------------------------------------------------------------------
    root.mainloop()