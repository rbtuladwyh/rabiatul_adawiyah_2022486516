import tkinter # function to import tkinter into python program
from tkinter import ttk # function to shorten tkinter word 
import mysql.connector # function to connect mysql
from datetime import date # function to import date for age calculation
import tkinter.messagebox # fucntion to give warning for user
today = date.today() # today day to calculat with date of birth

# Function to insert data into the table
def insert_data():
    First_Name = first_name_entry.get()
    Last_Name = last_name_entry.get()
    Title = title_combobox.get()
    Gender = gender_combobox.get()
    Date = day_entry.get()
    Month = month_entry.get()
    Year = year_entry.get()
    Address = address_entry.get()
    First_Contact = contact1_entry.get()
    Second_Contact = contact2_entry.get()
    First_Email = email1_entry.get()
    Second_Email = email2_entry.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="opac_registration"
    )
    cursor = mydb.cursor()

    cursor.execute("INSERT INTO user_registration (First_Name, Last_Name, Title, Gender, Date, Month, Year, Address, First_Contact, Second_Contact, First_Email, Second_Email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (First_Name, Last_Name, Title, Gender, Date, Month, Year, Address, First_Contact, Second_Contact, First_Email, Second_Email))

    mydb.commit()
    mydb.close() 

# Function to calculage user age 
def get_age():
    date = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    age = today.year-year-((today.month, today.day)<(month,date))
    date_entry2.config(state='normal')
    date_entry2.insert(tkinter.END,age)
    date_entry2.config(state='disabled')

# Function to check user click the terms & conditions
def check_terms_and_save():

    if accept_var.get():
        insert_data()

    else:
        tkinter.messagebox.showwarning(title= "Error", message= "You have not accept the terms")

# Window title, geometry, frame and background color
window = tkinter.Tk()
window.title('OPAC Registration')
window.geometry("600x600")
window["background"] = "#F8C8DC"
frame = tkinter.Frame(window, bg= "#F8C8DC")
frame.pack()

# Page Title with background and font type size and color
label = ttk.Label(frame, text= "OPAC SELF REGISTRATION", font= ("Hopeful Christmas Solid", 20), foreground= "#008000")
label.grid(ipadx= 20, ipady= 20)
label['background'] = "#F8C8DC"

# User Information Frame
user_info_frame = tkinter.LabelFrame(frame, text= "User Information", font= ("Arial Narrow", 14), foreground= "#008000")
user_info_frame.grid(row= 1, column= 0, padx= 20, pady= 10)
user_info_frame.config(font= ("Arial, 14"))
user_info_frame["background"] = "#F8C8DC"

# User Name Label
first_name_label = tkinter.Label(user_info_frame, text= "First Name", foreground= "#008000")
first_name_label.grid(row= 1, column= 0)
last_name_label = tkinter.Label(user_info_frame, text= "Last Name", foreground= "#008000")
last_name_label.grid(row= 1, column= 1)
first_name_label["background"] = "#F8C8DC"
last_name_label["background"] = "#F8C8DC"

# User Name Entry for user to input text
first_name_entry = tkinter.Entry(user_info_frame, foreground= "#008000") 
last_name_entry = tkinter.Entry(user_info_frame, foreground= "#008000")
first_name_entry.grid(row= 2, column= 0)
last_name_entry.grid(row= 2, column= 1)

# User Title label and entry
title_label = tkinter.Label(user_info_frame, text= "Title", foreground= "#008000")
title_combobox = ttk.Combobox(user_info_frame, values= ["Mr.", "Ms.", "Mrs."], foreground= "#008000")
title_label.grid(row= 1, column= 2)
title_combobox.grid(row= 2, column= 2)
title_label['background'] = "#F8C8DC"

# User Gender label and entry
gender_label = tkinter.Label(user_info_frame, text= "Gender", foreground= "#008000")
gender_combobox = ttk.Combobox(user_info_frame, values= ["Male", "Female"], foreground= "#008000")
gender_label.grid(row= 3, column= 0)
gender_combobox.grid(row= 4, column= 0)
gender_label['background'] = "#F8C8DC"

# User Date of Birth label
birth_label = tkinter.Label(user_info_frame, text= "Date of Birth", foreground= "#008000")
birth_label.grid(row= 3, column= 1)
birth_label['background'] = "#F8C8DC"
day_label=ttk.Label(user_info_frame,text="Date:", foreground= "#008000")
month_label=ttk.Label(user_info_frame,text="Month: ", foreground= "#008000")
year_label=ttk.Label(user_info_frame,text="Year: ", foreground= "#008000")
day_label.grid(row= 4, column=1)
month_label.grid(row= 5, column= 1)
year_label.grid(row= 6, column= 1)

# User Date Entry 
day_entry=ttk.Entry(user_info_frame,width= 10, foreground= "#008000")
month_entry=ttk.Entry(user_info_frame,width= 10, foreground= "#008000")
year_entry=ttk.Entry(user_info_frame, width= 10, foreground= "#008000")
day_entry.grid(row= 4, column=2)
month_entry.grid(row= 5, column= 2)
year_entry.grid(row= 6, column= 2)
day_label['background'] = "#F8C8DC"
month_label['background'] = "#F8C8DC"
year_label['background'] = "#F8C8DC"

# User age will be displayed after user click save button # calculation part
date_label2 = tkinter.Label(user_info_frame, text= "Your Age:", foreground= "#008000")
date_label2.grid(row= 5, column= 0)
date_entry2 = tkinter.Entry(user_info_frame, width= 10,state="disabled", foreground= "#008000")
date_entry2.grid(row= 6, column= 0)
date_label2['background'] = "#F8C8DC"

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx= 10, pady= 5)

# Contact Information Frame
contact_info_frame = tkinter.LabelFrame(frame, text= "Contact Information", font= ("Arial Narrow", 14), foreground= "#008000")
contact_info_frame.grid(row= 6, column= 0, sticky= "news", padx= 20, pady= 10)
contact_info_frame.config(font= ("Arial, 14"))
contact_info_frame["background"] = "#F8C8DC"

# User Full Address label and entry
address_label = tkinter.Label(contact_info_frame, text= "Address", foreground= "#008000")
address_label.grid(row= 1, column= 2)
address_entry = tkinter.Entry(contact_info_frame, foreground= "#008000")
address_entry.grid(row= 2, column= 2)
address_label['background'] = "#F8C8DC"

# User Phone Number label and entry
# Primary Phone Number
contact1_label = tkinter.Label(contact_info_frame, text= "Primary Number", foreground= "#008000")
contact1_label.grid(row= 1, column= 0)
contact1_entry = tkinter.Entry(contact_info_frame, foreground= "#008000")
contact1_entry.grid(row= 2, column= 0)
contact1_label['background'] = "#F8C8DC"

# Secondary Phone Number
contact2_label = tkinter.Label(contact_info_frame, text= "Secondary Number", foreground= "#008000")
contact2_label.grid(row= 1, column= 1)
contact2_entry = tkinter.Entry(contact_info_frame, foreground= "#008000")
contact2_entry.grid(row= 2, column= 1)
contact2_label['background'] = "#F8C8DC"

# User Email label and entry
# Primary Email
email1_label = tkinter.Label(contact_info_frame, text= "Primary Email", foreground= "#008000")
email1_label.grid(row= 3, column= 0)
email1_entry = tkinter.Entry(contact_info_frame, foreground= "#008000")
email1_entry.grid(row= 4, column= 0)
email1_label['background'] = "#F8C8DC"

# Secondary Email
email2_label = tkinter.Label(contact_info_frame, text= "Secondary Email", foreground= "#008000")
email2_label.grid(row= 3, column= 1)
email2_entry = tkinter.Entry(contact_info_frame, foreground= "#008000")
email2_entry.grid(row= 4, column= 1)
email2_label['background'] = "#F8C8DC"

for widget in contact_info_frame.winfo_children():
    widget.grid_configure(padx= 10, pady= 5)

# Accept terms 
terms_frame = tkinter.LabelFrame(frame, text= "Terms & Conditions", font= ("Arial Narrow", 14), foreground= "#008000")
terms_frame.grid(row= 15, column= 0, sticky= "news", padx= 20, pady= 10)
terms_frame['background'] = "#F8C8DC"

accept_var = tkinter.StringVar()
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable= accept_var, onvalue= "Accepted", offvalue= "Not Accepted", foreground= "#008000")
terms_check.grid(row= 0, column= 0)
terms_check['background'] = "#F8C8DC"

# Buttons to perform operations
insert_button = ttk.Button(window, text= "Save", command=lambda: [insert_data(), get_age(), check_terms_and_save()])
insert_button.pack()

window.mainloop()