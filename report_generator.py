from cProfile import label
from cgitb import text
from curses.textpad import Textbox
from textwrap import wrap
import tkinter as tk
from tkinter import ttk
import pandas as pd
import webbrowser

window = tk.Tk()
# Import the tcl file
window.tk.call('source', 'forest-dark.tcl')
# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')

window.geometry('700x550')
window.wm_title("Ellesha Murphey's Report Generator")
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/3 - windowHeight/2)
window.geometry("+{}+{}".format(positionRight, positionDown))

left_frame = tk.Frame(window)
left_frame.grid(column=0, row=0, sticky=tk.N)
right_frame = tk.Frame(window)
right_frame.grid(column=1, row=0, sticky=tk.N)
#right_frame_canvas = tk.Canvas(right_frame, width=500, height=500, highlightbackground="black", highlightthickness=2, scrollregion=(0,0,500,500))
#right_frame_canvas.grid(sticky=tk.N)


def get_headers():
    excel = pd.read_excel('report_generator.xlsx', sheet_name='descriptors')
    headers = []
    for column in excel:
        headers.append(column)
    return headers

def get_col_values():
    excel = pd.read_excel('report_generator.xlsx', sheet_name='descriptors')
    values = excel[descriptors_holder.get()].values.tolist()
    return values

def generate_descriptors():
    clear_checkboxes()
    excel = pd.read_excel('report_generator.xlsx', sheet_name='descriptors').dropna()
    values = excel[descriptors_holder.get()].values.tolist()   
    chosen_gender = drop_down_holder.get()
    # 3 if statements which will swap the name and pronouns based on gender picked
    if chosen_gender == "Male (he/his)":
        for line in values:
            # swap the name, and pronouns
            male_descriptors = line.replace("$name", str(name_entry.get())).replace("$pronoun", "he").replace("$possessive_pronoun", "his")
            male_descriptors = str(male_descriptors)
            # append each line to the list
            descriptors_lst.append(male_descriptors)
    make_checkboxes()

    if chosen_gender == "Female (she/hers)":
        for line in values:
            female_descriptors = line.replace("$name", str(name_entry.get())).replace("$pronoun", "she").replace("$possessive_pronoun", "hers")
            descriptors_lst.append(female_descriptors)
    make_checkboxes()

    if chosen_gender == "Genderless (they/theirs)":
        for line in values:
            genderless_descriptors = line.replace("$name", str(name_entry.get())).replace("$pronoun", "they").replace("$possessive_pronoun", "theirs")
            descriptors_lst.append(genderless_descriptors)
    make_checkboxes()

def make_checkboxes():
    i = 2
    for index, item in enumerate(descriptors_lst):
        var_lst.append(tk.IntVar(value=0))
        checkbox = ttk.Checkbutton(right_frame, style='ToggleButton', variable=var_lst[index], text=item)#, wraplength=500)
        #togglebutton = ttk.Checkbutton(root, text='Toggle button', style='ToggleButton', variable=var)
        checkbox.grid(row=i, column=0, pady=2, padx=2, columnspan=4, sticky= 'w')
        checkbox_lst.append(checkbox)
        i += 1

def clear_checkboxes():
    for checkbox in checkbox_lst:
        checkbox.destroy()
    checkbox_lst.clear()
    descriptors_lst.clear()
    var_lst.clear()

def write_to_file():
    # create + open a txt file
    with open(str(name_entry.get() + "_report.txt"), "w+") as report:
        # x is the number of the checkbox, int_var is the name of the checkbox?, and int_var.get returns 0 or 1 depending on if it's checked
        for x, int_var in enumerate(var_lst):
            # if int_var is true
            if int_var.get():
                # then write the the corresponding item in the text_lst list to the txt file
                report.writelines(descriptors_lst[x])
    submit_popup()

def submit_popup():
    popup = tk.Tk()
    popup.wm_title("Report generated!")
    windowWidth = popup.winfo_reqwidth()
    windowHeight = popup.winfo_reqheight()
    positionRight = int(popup.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(popup.winfo_screenheight()/3 - windowHeight/2)
    popup.geometry("+{}+{}".format(positionRight, positionDown))
    message = tk.Label(popup, text="The report has been generated alongside this program.")
    message.grid(row=0, pady=10, padx=10)
    okay_button = tk.Button(popup, text="Okay!", command = popup.destroy)
    okay_button.grid(row=1, pady=10, padx=10)


# a list containing the name+pronoun swapped strings
descriptors_lst = []
# a number assigned to each of the lines in the text file
var_lst = []
# a list of all the checkboxes
checkbox_lst = []

descriptors_label = ttk.Label(left_frame, text="Chose the descriptors topic")
descriptors_label.grid(row=0, column=0, pady=2, padx=2, columnspan=2)

descriptors_holder = tk.StringVar()
# the actual drop down menu
#descriptors_file_dropdown = ttk.Combobox(left_frame, descriptors_file_holder)
descriptors_dropdown = ttk.Combobox(left_frame, textvariable=descriptors_holder)
descriptors_dropdown['values'] = get_headers()
descriptors_dropdown.grid(row=1, column=0, pady=2, padx=2, columnspan=2)

# Below is the structure of the window #
# The enter their name label
name_label = ttk.Label(left_frame, text="Enter their name")
name_label.grid(row=3, column=0, pady=2, padx=2, columnspan=2)

# the name entry field
name_entry = ttk.Entry(left_frame)
name_entry.grid(row=4, column=0, pady=2, padx=2, columnspan=2)

# gender label
gender_label = ttk.Label(left_frame, text="Select their prefered pronouns")
gender_label.grid(row=6, column=0, pady=2, padx=2, columnspan=2)

# a list of the genders
genders_lst = ("Male (he/his)", "Female (she/hers)", "Genderless (they/theirs)")
#drop_down_holder = StringVar(value="Select an option")
# a variable to hold the value selected from the dropdown box
drop_down_holder = tk.StringVar(left_frame)
# the actual drop down menu
gender_dropdown = ttk.Combobox(left_frame, textvariable=drop_down_holder)
gender_dropdown['values'] = genders_lst
gender_dropdown.grid(row=7, column=0, pady=2, padx=2, columnspan=2)

spacer1 = ttk.Label(left_frame, text="")
spacer1.grid(row=8, column=0, pady=10, padx=2, columnspan=2)

# the submit button, which runs the descriptions function
button = ttk.Button(left_frame, text="Generate", command=generate_descriptors)
button.grid(row=9, column=0, pady=2, padx=2)

# the clear button, which runs the clear_checkboxes function
button = ttk.Button(left_frame, text="Clear", command=clear_checkboxes)
button.grid(row=9, column=1, pady=2, padx=2)

# the save/export button, this will write the checked descriptors to a text file
button = ttk.Button(left_frame, text="Save/Export", command=write_to_file)
button.grid(row=10, column=0)

# this button opens the help section
help_url = "https://github.com/tom-dell/elles_report_generator/blob/master/README.md"
button = ttk.Button(left_frame, text="Help")#, command=webbrowser.open(help_url))
button.grid(row=10, column=1)


window.mainloop()
