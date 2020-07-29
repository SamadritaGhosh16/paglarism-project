# GUI
from tkinter import *
from tkinter import messagebox
from dbhelper import *
from entry_validate import *
from consinesimilar import *



root = Tk()
root.minsize(150, 150)
root.config(bg="#8b7bdb")

mbox = LabelFrame(root, text="Select your language ", padx=5, pady=5, bg="#7bb3db")
click = StringVar()
click.set("English")
drop = OptionMenu(mbox, click, "English", "Bengali", "Hindi").pack()
mbox.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

label1 = LabelFrame(root, text="What will be your Question? ", padx=5, pady=5, bg="#7bb3db")
Qnt1 = Entry(label1, width=30, bg="#7bdbce")
Qnt1.pack()  # Entrybox
label1.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

label2 = LabelFrame(root, text="Enter your name ", padx=5, pady=5)  # label
Qnt2 = Entry(label2, width=30)
Qnt2.pack()
label2.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

label3 = LabelFrame(root, text="What is your company's name? ", padx=5, pady=5)  # label
Qnt3 = Entry(label3, width=30)
Qnt3.pack()
label3.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

label4 = LabelFrame(root, text="Enter your phone number ", padx=5, pady=5)  # label
Qnt4 = Entry(label4, width=30)
Qnt4.pack()
label4.grid(row=4, column=0, padx=10, pady=10, columnspan=2)


def submit():
    f = 0
    incorrect = "Your input for "  # incorrect message to be displayed
    question = Qnt1.get()  # pulling the contains of the entry
    if quest_valid(question) != True:  # calling fuction from entryvalidator and checking
        incorrect = incorrect + "Question "
    else:
        f += 1

    name = Qnt2.get()
    if name_valid(name) != True:
        incorrect = incorrect + "Name "
    else:
        f += 1

    company = Qnt3.get()
    if quest_valid(company) != True:
        incorrect = incorrect + "Company "
    else:
        f += 1

    num = Qnt4.get()
    if call_valid(num) != True:
        incorrect = incorrect + "Number "
    else:
        f += 1

    incorrect = incorrect + "contains improper keys.\nkindly recheck them "  # final incorrect message

    if f == 4:
        submitdb(question, name, company, num)  # takes the inputs and submits in dbcheck
    else:
        messagebox.showerror("Error", incorrect)

    Qnt1.delete(0, END)
    Qnt2.delete(0, END)
    Qnt3.delete(0, END)  # clears the entry box after it is submitted
    Qnt4.delete(0, END)


labl_submit = LabelFrame(root, padx=5, pady=5)
sub_butn = Button(labl_submit, text="Submit", command=submit).pack()  # creatingbutton
labl_submit.grid(row=5, column=0, padx=10, pady=10)

labl_view = LabelFrame(root, padx=5, pady=5)
view_butn = Button(labl_view, text="View").pack()  # creatingbutton
labl_view.grid(row=5, column=1, padx=10, pady=10)

'''
e=Entry(root)
e.pack()
print("your")
print(e.get())

'''
root.mainloop()