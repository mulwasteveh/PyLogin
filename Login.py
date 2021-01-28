from tkinter import *
import mysql.connector
from mysql.connector import Error


mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = ""

)
print(mydb)

      #button_funtion
def backbutton(self, widget):
       self.top.go_back()

def sign_here():
    top= Toplevel()
    top.geometry("400x500")
    top.title("SIGN_UP PAGE")
    top.configure(background="pink")
    l1 = Label(top, text="PLEASE FILL THIS FORM", font="times 20 bold")
    l1.place(x=20, y=10)
    l1.anchor="center"

    l2 = Label(top, text="First Name", font="bold")
    l2.place(x=10, y=50)
    entry1= Entry(top)
    entry1.place(x=150, y=50)

    l3 = Label(top, text="second Name", font="bold")
    l3.place(x=10, y=100)
    entry2 = Entry(top)
    entry2.place(x=150, y=100)

    l4 = Label(top, text="Reg No", font="bold")
    l4.place(x=10, y=150)
    entry3 = Entry(top)
    entry3.place(x=150, y=150)

    l5 = Label(top, text="Email adress", font="bold")
    l5.place(x=10, y=200)
    entry4 = Entry(top)
    entry4.place(x=150, y=200)

    l6 = Label(top, text="Admitted to", font="bold")
    l6.place(x=10, y=250)
    entry5 = Entry(top)
    entry5.place(x=150, y=250)

    l7 = Label(top, text="Date", font="bold")
    l7.place(x=10, y=300)
    entry6 = Entry(top)
    entry6.place(x=150, y=300)

    l8 = Label(top, text="Gender", font="bold")
    l8.place(x=10, y=350)
    mb= Menubutton(top, text="M/F", relief= RAISED)
    mb.place(x=150, y=350)
    mb.menu = Menu(mb,)
    mb["menu"] = mb.menu

    Male = IntVar()
    Female = IntVar()

    mb.menu.add_checkbutton(label="M",
                            variable=Male)
    mb.menu.add_checkbutton(label="F",
                            variable=Female)


    bt1= Button(top, text="Back", font="times 17 bold", command=backbutton)
    bt1.place(x=50, y=430)

    bt2 = Button(top, text="Submit", font="times 17 bold")
    bt2.place(x=220, y=430)


#creates a GUI window
main_screen = Tk()

#sets the title of the GUI window
main_screen.title("Login page")

#sets the backgroud color of the GUI window
main_screen.configure(background="cyan")

#the size
main_screen.geometry("400x400")

#inputs the first name
label1=Label(main_screen,text="Enter first name:", font="times 14 bold")
label1.place(x=10,y=10)
l1=Entry(main_screen)
l1.place(x=180, y=10)

#inputs the second name
label2=Label(main_screen,text="Enter second name:", font="times 14 bold")
label2.place(x=10,y=50)
l2=Entry(main_screen)
l2.place(x=180, y=50)

#reg no section
label3=Label(main_screen,text="Enter Reg No:", font="times 14 bold")
label3.place(x=10,y=90)
l3=Entry(main_screen)
l3.place(x=180, y=90)

#inputs the registration number of comrade
label1=Label(main_screen,text="Faculty name:", font="times 14 bold")
label1.place(x=10,y=130)

#creating a clicked function
def clicked(args):
    clicked.set("SCAI")

drop = OptionMenu(main_screen, clicked, "SCAI", "FESS", "BCOM", "EDA", "SOKU")
drop.place(x=180, y=130)

#sign up button
label3= Button(main_screen, text="sign up", font="times 10 bold" ,command = sign_here)
label3.place(x=150, y=250)

#login button
label3= Button(main_screen, text="Login", font="times 10 bold",)
label3.place(x=150, y=300)

#this calls the main_account_screen() fuction
main_screen.mainloop()