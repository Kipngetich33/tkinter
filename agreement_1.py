from tkinter import *
import random, processing_info_1, agreement_2
import time


def call_this_module():
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

    lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "4. Bank Agreement", fg = "white",bg = "dark green", bd = 10 , anchor = 'w')
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

    question_1 = "Your banking relationship with us"
    q_1_1 = "(the Personal Banking terms and conditions)"
    q_2 = "Advised and provided with Interest Rates Applicable to this Account"
    q_3 = "Financial Services Compensation Scheme Information Sheet"

    def call_next(requested_action):
            '''
            function that directs the user to the next form
            that the user is supposed to fill
            '''
            root.destroy()
            if(requested_action == "next"):
                agreement_2.call_this_module()
            elif( requested_action == "previous"):
                processing_info_1.call_this_module()
    # ============================================ customer 1 ==============================================
    customer_1_section = Label(form_body_left , pady = 10, font =('arial', 20, 'bold' ), text = "First Customer", fg = "Steel Blue" , anchor = 'w')
    customer_1_section.grid(row = 0)

    lblInfo = Label(form_body_left , font =('arial', 15), text = "Consent Given", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 1)

    want_debit_checkbox = Radiobutton(form_body_left, font = ('arial',15),text = "Yes", variable = want_debit_card,
                            value ="1" ,bd = 5)
    want_debit_checkbox.grid(row = 2 ,sticky = 'w')

    lblInfo = Label(form_body_left , font =('arial', 15), text = "Consent Declined", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 3)

    want_debit_checkbox = Radiobutton(form_body_left, font = ('arial',15),text = "Yes", variable = want_debit_card,
                            value ="1" ,bd = 5)
    want_debit_checkbox.grid(row = 4 ,sticky = 'w')

    lblInfo = Label(form_body_left , font =('arial', 15), text = "Date", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 5)

    txtReference = Entry(form_body_left, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 6)

    # ============================================ customer 2 ==============================================
    customer_1_section = Label(form_body_right , pady = 10, font =('arial', 20, 'bold' ), text = "Second Customer", fg = "Steel Blue" , anchor = 'w')
    customer_1_section.grid(row = 0)

    lblInfo = Label(form_body_right , font =('arial', 15), text = "Consent Given", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 1)

    want_debit_checkbox = Radiobutton(form_body_right, font = ('arial',15),text = "Yes", variable = want_debit_card,
                            value ="1" ,bd = 5)
    want_debit_checkbox.grid(row = 2 ,sticky = 'w')

    lblInfo = Label(form_body_right , font =('arial', 15), text = "Consent Declined", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 3)

    want_debit_checkbox = Radiobutton(form_body_right, font = ('arial',15),text = "Yes", variable = want_debit_card,
                            value ="1" ,bd = 5)
    want_debit_checkbox.grid(row = 4 ,sticky = 'w')

    lblInfo = Label(form_body_right , font =('arial', 15), text = "Date", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 5)

    txtReference = Entry(form_body_right, font = ('arial',15), textvariable = fries , bd =5, insertwidth = 4,
                            bg = "powder blue", justify = "right" )
    txtReference.grid(row = 6)
    # ============================================ bottom section ==============================================

    previousbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                    text = 'Previous', bg = "powder blue", command = lambda: call_next("previous")).grid(row = 1, column = 0)

    nextbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                    text = 'Next', bg = "powder blue", command = lambda: call_next("next")).grid(row = 1, column = 1)

    # -----------------------------------------------------------------------------------------------------
    root.mainloop()