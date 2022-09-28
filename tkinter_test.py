from cgitb import text
from curses.textpad import Textbox
import tkinter as tk
import os

window = tk.Tk()
window.geometry('600x700')

top_frame = tk.Frame(window)
top_frame.grid(row=0, sticky=tk.EW)
center_frame = tk.Frame(window, width=100, height=500, highlightbackground="black", highlightthickness=2)
center_frame.grid(row=1, sticky=tk.EW, pady=2, padx=3)
center_frame_canvas = tk.Canvas(center_frame, width=100, height=500)
center_frame_canvas.grid(sticky=tk.NE)

'''
y_scrollbar = tk.Scrollbar(center_frame, command=center_frame_canvas.yview)
y_scrollbar.grid(row=0, column=1, sticky=tk.NS)
center_frame_canvas.configure(yscrollcommand=y_scrollbar.set)
center_frame_canvas.configure(scrollregion=center_frame_canvas.bbox("all"))
'''

def generate_content():
    # open the file of text
    with open('content.txt', 'r') as content:
        # read lines in the text file
        text_contents = content.readlines()
        # grab the value in the drop down menu, which is being held by drop_down_holder
        chosen_gender = drop_down_holder.get()

        # 3 if statements which will swap the name and pronouns based on gender picked
        if chosen_gender == "Male (he/his)":
            for line in text_contents:
                # swap the name, and pronouns
                male_text = line.replace("$name", str(name_entry.get())).replace("$pronoun", "he").replace("$possessive_pronoun", "his")
                # append each line to the list
                text_lst.append(male_text)
        make_checkboxes()

        if chosen_gender == "Female (she/hers)":
            for line in text_contents:
                female_text = line.replace("$name", str(name_entry.get())).replace("$pronoun", "she").replace("$possessive_pronoun", "hers")
                text_lst.append(female_text)
        make_checkboxes()

        if chosen_gender == "Genderless (they/theirs)":
            for line in text_contents:
                genderless_text = line.replace("$name", str(name_entry.get())).replace("$pronoun", "they").replace("$possessive_pronoun", "theirs")
                text_lst.append(genderless_text)
        make_checkboxes()

def make_checkboxes():
    i = 2
    for index, item in enumerate(text_lst):
        var_lst.append(tk.IntVar(value=0))
        checkbox = tk.Checkbutton(center_frame_canvas, variable=var_lst[index], text=item, wraplength=500)
        checkbox.grid(row=i, column=0, pady=2, padx=2, columnspan=4, sticky= 'w')
        checkbox_lst.append(checkbox)
        i += 1

def clear_checkboxes():
    for checkbox in checkbox_lst:
        checkbox.destroy()
    checkbox_lst.clear()
    text_lst.clear()
    var_lst.clear()

# a list containing the name+pronoun swapped strings
text_lst = []
# a number assigned to each of the lines in the text file
var_lst = []
# a list of all the checkboxes
checkbox_lst = []

# Below is the structure of the window #
# The enter their name label
name_label = tk.Label(top_frame, text="Enter their name")
name_label.grid(row=0, column=0, pady=2, padx=2)

# the name entry field
name_entry = tk.Entry(top_frame)
name_entry.grid(row=1, column=0, pady=2, padx=2)

# a spacer to seperate the name section from the pronoun section
spacer1 = tk.Label(top_frame, text="")
spacer1.grid(row=0, column=1, pady=2, padx=10, rowspan=2)

# gender label
gender_label = tk.Label(top_frame, text="Select their prefered pronouns")
gender_label.grid(row=0, column=1, pady=2, padx=2)

# a list of the genders
genders_lst = ("Male (he/his)", "Female (she/hers)", "Genderless (they/theirs)")
# a variable to hold the value selected from the dropdown box
drop_down_holder = tk.StringVar(top_frame)
# the actual drop down menu
gender_dropdown = tk.OptionMenu(top_frame, drop_down_holder, *genders_lst)
gender_dropdown.grid(row=1, column=1, pady=2, padx=2)

# a spacer to seperate the gender stuff from the submit button
spacer2 = tk.Label(top_frame, text="")
spacer2.grid(row=0, column=2, pady=2, padx=10, rowspan=2)

# the submit button, which runs the descriptions function
button = tk.Button(top_frame, text="Submit", command=generate_content)
button.grid(row=0, column=3, pady=2, padx=2, rowspan=2)

# the clear button, which runs the clear_checkboxes function
button = tk.Button(top_frame, text="Clear", command=clear_checkboxes)
button.grid(row=0, column=4, pady=2, padx=2, rowspan=2)

window.mainloop()