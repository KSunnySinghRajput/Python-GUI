from tkinter import *
root = Tk()


def getvalues():
    print("Form Submitted")
    print(f"Name: {namevalue.get()}, Contact No: {contactsvalue.get()}, Email Id: {emailvalue.get()}, Gender: {gendervalue.get()}, State: {statevalue.get()}, City: {cityvalue.get()}, Country; {nationality.get()}")

    with open("res/formrecords.txt", "a") as f:
        f.write(f"Name: {namevalue.get()}, Contact No: {contactsvalue.get()}, Email Id: {emailvalue.get()}, Gender: {gendervalue.get()}, State: {statevalue.get()}, City: {cityvalue.get()}, Country; {nationality.get()}\n\n")


root.geometry("300x320")
root.title("Registration Form")


Label(root, text="Welcome Form", font="lucida 14 bold").grid(
    row=0, column=1, pady=15)

name = Label(root, text="Name").grid(row=1, column=0, padx=30, pady=5)
contact = Label(root, text="Contact").grid(row=2, column=0, padx=30, pady=5)
email = Label(root, text="Email").grid(row=3, column=0, padx=30, pady=5)
gender = Label(root, text="Gender").grid(row=4, column=0, padx=30, pady=5)
state = Label(root, text="State").grid(row=5, column=0, padx=30, pady=5)
city = Label(root, text="City").grid(row=6, column=0, padx=30, pady=5)


namevalue = StringVar()
contactsvalue = StringVar()
emailvalue = StringVar()
gendervalue = StringVar()
statevalue = StringVar()
cityvalue = StringVar()
nationality = IntVar()

user_entry = Entry(root, textvariable=namevalue).grid(row=1, column=1)
contact_entry = Entry(root, textvariable=contactsvalue).grid(row=2, column=1)
email_entry = Entry(root, textvariable=emailvalue).grid(row=3, column=1)
gender_entry = Entry(root, textvariable=gendervalue).grid(row=4, column=1)
state_entry = Entry(root, textvariable=statevalue).grid(row=5, column=1)
city_entry = Entry(root, textvariable=cityvalue).grid(row=6, column=1)

country = Checkbutton(
    text="Indian", variable=nationality).grid(row=7, column=1)

Button(root, text="Submit", command=getvalues).grid(row=8, column=1)

root.mainloop()
