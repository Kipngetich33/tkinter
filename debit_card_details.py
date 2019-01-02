from tkinter import *
import random, personal_details_continuation_7,processing_info
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

    lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "2. Your debit card details", fg = "white",bg = "dark green", bd = 10 , anchor = 'w')
    lblInfo.grid(row = 2 , column = 0)

    # ========================================== form =================================================
    debit_desc_1 = "I would like to apply for a debit card"
    debit_desc_2 = "The type of card we give you depends on our assessment of yourpersonal circumstances."

    want_debit_card = IntVar()
    want_debit_card1 = IntVar()
    name_on_card = StringVar()
    mothers_name = StringVar()
    birth_date = StringVar()

    def call_next(requested_action):
            '''
            function that directs the user to the next form
            that the user is supposed to fill
            '''
            root.destroy()
            if(requested_action == "next"):
                processing_info.call_this_module()     
            elif( requested_action == "previous"):
                personal_details_continuation_7.call_this_module()

    # ============================================ customer 1 ==============================================
    customer_1_section = Label(form_body_left , pady = 10, font =('arial', 20, 'bold' ), text = "First Customer", fg = "Steel Blue" , anchor = 'w')
    customer_1_section.grid(row = 0)

    lblInfo = Label(form_body_left , font =('arial', 15 ), text = debit_desc_1, fg = "black" , anchor = 'w')
    lblInfo.grid(row = 1)

    want_debit_checkbox = Checkbutton(form_body_left,  font = ('arial',16),text = "Yes", variable = want_debit_card,bd = 5)
    want_debit_checkbox.grid(row = 2 ,sticky = 'w')

    want_debit_checkbox1 = Checkbutton(form_body_left,  font = ('arial',16),text = "No", variable = want_debit_card1 ,bd = 5,)
    want_debit_checkbox1.grid(row = 3 ,sticky = 'w')

    lblCustName = Label(form_body_left, font = ('arial',16), text="Customer name to appear on card" , anchor ='w' )
    lblCustName.grid(row = 4)
    txtCustName = Entry(form_body_left, font = ('arial',16), textvariable = name_on_card ,insertwidth = 4, bd = 5,width = 50,
                            bg = "powder blue", justify = "right" )
    txtCustName.grid(row = 5 )

    lblMotherName = Label(form_body_left, font = ('arial',16), text="Mother’s previous name" , anchor ='w' )
    lblMotherName.grid(row = 7)
    txtMotherName = Entry(form_body_left, font = ('arial',16), textvariable = mothers_name , insertwidth = 4, bd =5,width = 50,
                            bg = "powder blue", justify = "right" )
    txtMotherName.grid(row = 8)

    lblBirthDay = Label(form_body_left, font = ('arial',16), text="Your date of birth" , anchor ='w' )
    lblBirthDay.grid(row = 10)
    txtBirthDay = Entry(form_body_left, font = ('arial',16), textvariable = birth_date ,insertwidth = 4,bd =5,width = 50,
                            bg = "powder blue", justify = "right" )
    txtBirthDay.grid(row = 11)

    # ============================================ customer 2 ==============================================
    customer_2_section = Label(form_body_right ,font =('arial', 20, 'bold' ), text = "Second Customer", fg = "Steel Blue" , anchor = 'w')
    customer_2_section.grid(row = 0)

    lblInfo = Label(form_body_right , font =('arial', 15 ), text = debit_desc_1, fg = "black" , anchor = 'w')
    lblInfo.grid(row = 1)

    want_debit_checkbox = Checkbutton(form_body_right,  font = ('arial',16),text = "Yes", variable = want_debit_card,bd = 5)
    want_debit_checkbox.grid(row = 2 ,sticky = 'w')

    want_debit_checkbox1 = Checkbutton(form_body_right,  font = ('arial',16),text = "No", variable = want_debit_card1 ,bd = 5,)
    want_debit_checkbox1.grid(row = 3 ,sticky = 'w')

    lblCustName = Label(form_body_right, font = ('arial',16), text="Customer name to appear on card" , anchor ='w' )
    lblCustName.grid(row = 4)
    txtCustName = Entry(form_body_right, font = ('arial',16), textvariable = name_on_card ,insertwidth = 4, bd = 5 , width = 50,
                            bg = "powder blue", justify = "right" )
    txtCustName.grid(row = 5 )

    lblMotherName = Label(form_body_right, font = ('arial',16), text="Mother’s previous name" , anchor ='w' )
    lblMotherName.grid(row = 6)
    txtMotherName = Entry(form_body_right, font = ('arial',16), textvariable = mothers_name , insertwidth = 4, bd =5,width = 50,
                            bg = "powder blue", justify = "right" )
    txtMotherName.grid(row = 7)

    lblBirthDay = Label(form_body_right, font = ('arial',16), text="Your date of birth" , anchor ='w' )
    lblBirthDay.grid(row = 8)
    txtBirthDay = Entry(form_body_right, font = ('arial',16), textvariable = birth_date ,insertwidth = 4,bd =5,width = 50,
                            bg = "powder blue", justify = "right" )
    txtBirthDay.grid(row = 9)

    # ============================================ bottom section ==============================================

    previousbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                    text = 'Previous', bg = "powder blue",command = lambda: call_next("previous")).grid(row = 1, column = 0)

    nextbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                    text = 'Next', bg = "powder blue", command = lambda: call_next("next")).grid(row = 1, column = 1)

    # -----------------------------------------------------------------------------------------------------
    root.mainloop()