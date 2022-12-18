from cProfile import label
from curses.textpad import Textbox
from textwrap import wrap
import tkinter as tk
from tkinter import ttk
import pandas as pd
import webbrowser

#create the window
window = tk.Tk()
# Import the tcl file
window.tk.call('source', 'forest-dark.tcl')
# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')
#set window size and position
window.geometry('700x550')
window.wm_title("Ellesha Murphey's Report Generator")
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/3 - windowHeight/2)
window.geometry("+{}+{}".format(positionRight, positionDown))
#creating the two side by side frames
left_frame = tk.Frame(window)
left_frame.grid(column=0, row=0, sticky=tk.N)
right_frame = tk.Frame(window)
right_frame.grid(column=1, row=0, sticky=tk.N)

# Create a canvas to hold the scrollbar and the frame with the scrollable content
right_canvas = tk.Canvas(right_frame, width=400, height=500, highlightbackground="black", highlightthickness=2)
right_canvas.pack()

# Create a vertical scrollbar and place it on the canvas
scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=right_canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the canvas to use the scrollbar
right_canvas.configure(yscrollcommand=scrollbar.set)

# Define a frame to hold the checkboxes
checkbox_frame = tk.Frame(right_canvas)

# Place the frame inside the canvas
right_canvas.create_window((0, 0), window=checkbox_frame, anchor="nw")

# Bind the scroll event of the canvas to the function that will scroll the frame
checkbox_frame.bind(
    "<Configure>",
    lambda e: right_canvas.configure(
        scrollregion=right_canvas.bbox("all")
    )
)

#right_canvas.bind_all("<MouseWheel>", lambda event: right_canvas.yview_scroll(-1*(event.delta//120), "units"))


#the lists, i want to somehow remove these global lists
checkbutton_lst = []
genders_lst = ["Male", "Female", "Gender-neutral"]

#returns a list of headers in the descriptors tab
def get_headers():
    excel = pd.read_excel('report_generator.xlsx', sheet_name='descriptors')
    headers = [col for col in excel if not col.startswith('Unnamed:')]
    return headers

def get_descriptors():
    excel = pd.read_excel('report_generator.xlsx', sheet_name='descriptors')
    values = excel[descriptors_holder.get()]
    values = values.dropna()
    values.to_list()
    return values

def get_name():
    name = name_entry.get()
    return str(name)

def get_pronouns():
    chosen_gender = drop_down_holder.get()
    if chosen_gender == "Male":
        pronouns = ["he", "his"]
    if chosen_gender == "Female":
        pronouns = ["she", "her"]
    if chosen_gender == "Gender-neutral":
        pronouns = ["they", "their"]
    return pronouns

def generate_descriptors():
    clear_checkboxes()
    descriptors = get_descriptors()
    name = get_name()
    pronouns = get_pronouns()
    
    descriptors_lst = []
    for line in descriptors:
        swapped = line.replace("$name", name).replace("$pronoun", pronouns[0]).replace("$possessive_pronoun", pronouns[1])
        descriptors_lst.append(swapped)
    return descriptors_lst

def make_checkboxes():
    descriptors_lst = generate_descriptors()
    for item in descriptors_lst:
        checkbutton = tk.Checkbutton(checkbox_frame, text=str(item), wraplength=350)#, style="ToggleButton", width=40)
        checkbutton.pack(padx=10, pady=10, anchor='w')
        checkbutton_lst.append(checkbutton)
    descriptors_lst.clear()

def clear_checkboxes():
    for checkbox in checkbutton_lst:
        checkbox.destroy()
    checkbutton_lst.clear()

def write_to_file():
    name = get_name()
    selected_descriptors = []
    for checkbox in checkbutton_lst:
        if checkbox.instate(['selected']):
            selected_descriptors.append(checkbox.cget("text"))
    with open("%s_report.txt" %(name), "w+") as report:
        for selected_descriptor in selected_descriptors:
            report.writelines(selected_descriptor + "\n")
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

def open_help():
    help_url = "https://github.com/tom-dell/elles_report_generator/blob/master/README.md"
    webbrowser.open(help_url)

descriptors_label = ttk.Label(left_frame, text="Chose the descriptors topic")
descriptors_label.grid(row=0, column=0, pady=2, padx=2, columnspan=2)

descriptors_holder = tk.StringVar()
descriptors_dropdown = ttk.Combobox(left_frame, textvariable=descriptors_holder)
descriptors_dropdown['values'] = get_headers()
descriptors_dropdown.grid(row=1, column=0, pady=2, padx=2, columnspan=2)

name_label = ttk.Label(left_frame, text="Enter their name")
name_label.grid(row=3, column=0, pady=2, padx=2, columnspan=2)

# the name entry field
name_entry = ttk.Entry(left_frame)
name_entry.grid(row=4, column=0, pady=2, padx=2, columnspan=2)

# gender label
gender_label = ttk.Label(left_frame, text="Select their prefered pronouns")
gender_label.grid(row=6, column=0, pady=2, padx=2, columnspan=2)

# a variable to hold the value selected from the dropdown box
drop_down_holder = tk.StringVar(left_frame)
# the actual drop down menu
gender_dropdown = ttk.Combobox(left_frame, textvariable=drop_down_holder)
gender_dropdown['values'] = genders_lst
gender_dropdown.grid(row=7, column=0, pady=2, padx=2, columnspan=2)

spacer1 = ttk.Label(left_frame, text="")
spacer1.grid(row=8, column=0, pady=10, padx=2, columnspan=2)

# the submit button, which runs the descriptions function
button = ttk.Button(left_frame, text="Generate", command=make_checkboxes)
button.grid(row=9, column=0, pady=2, padx=2)

# the clear button, which runs the clear_checkboxes function
button = ttk.Button(left_frame, text="Clear", command=clear_checkboxes)
button.grid(row=9, column=1, pady=2, padx=2)

# the save/export button, this will write the checked descriptors to a text file
button = ttk.Button(left_frame, text="Save/Export", command=write_to_file)
button.grid(row=10, column=0)

# this button opens the help section

button = ttk.Button(left_frame, text="Help", command=open_help)
button.grid(row=10, column=1)

right_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
window.mainloop()
