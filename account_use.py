from tkinter import *
import random, personal_details
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

    form_body_left = Frame(root, width = 1600 ,height = 500, relief = SUNKEN)
    form_body_left.pack(side = LEFT)

    form_body_bottom = Frame(root, width = 1600 ,height = 100 , relief = SUNKEN)
    form_body_bottom.pack(side = BOTTOM)

    form_body_bottom1 = Frame(root, width = 1600 ,height = 5 , relief = SUNKEN ,bg = "steel blue")
    form_body_bottom1.pack(side = BOTTOM)

    # ======================================= Info ==================================================

    lblInfo = Label(Tops , font =('arial', 20 , 'bold'), text = "Account's Use", fg = "white",bg = "dark green", bd = 10 , anchor = 'w')
    lblInfo.grid(row = 2 , column = 0)

    # ========================================== form =================================================

    use_of_account = StringVar()

    def call_next(requested_action):
        if(requested_action == "next"):
            customer_1_data = []
            customer_2_data = []
            columns = ["What will you be using the account for"]
            customer_1_data.append(use_of_account.get())
            customer_2_data.append(use_of_account.get())

            # destroy the current route and call the next
            root.destroy()
            personal_details.call_this_module(customer_1_data,customer_2_data,columns)
        else:
            pass

    # ============================================ customer 1 ==============================================
    customer_1_section = Label(form_body_left , pady = 10, font =('arial', 20, 'bold' ), text = "First Customer", fg = "Steel Blue" , anchor = 'w')
    customer_1_section.grid(row = 0)

    lblInfo = Label(form_body_left , font =('arial', 15 ), text = "Please write clearly in the white spaces with capital letters or cross the boxes.", fg = "black" , anchor = 'w')
    lblInfo.grid(row = 1)

    lblInfo1 = Label(form_body_left , font =('arial', 15 ), text = "Please complete all sections of this form.", fg = "black" , anchor = 'w')
    lblInfo1.grid(row = 2)

    lblInfo2 = Label(form_body_left , font =('arial', 15 ), text = "What will you be using the Account for?", fg = "black" , anchor = 'w')
    lblInfo2.grid(row = 3)
    txtCustName = Entry(form_body_left, font = ('arial',16), textvariable = use_of_account ,insertwidth = 4, bd = 5,width = 50,
                            bg = "powder blue", justify = "right" )
    txtCustName.grid(row = 5 )

    # ============================================ bottom section ==============================================

    previousbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                    text = 'Previous', bg = "powder blue" , command = lambda: call_next("previous")).grid(row = 1, column = 0)

    nextbtn = Button(form_body_bottom,padx = 10 , pady = 5 , bd = 5, fg = "black", font = ('arial',15,'bold'),
                    text = 'Next', bg = "powder blue", command = lambda: call_next("next")).grid(row = 1, column = 1)

    # -----------------------------------------------------------------------------------------------------
    root.mainloop()
