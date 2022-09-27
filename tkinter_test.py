from cgitb import text
from curses.textpad import Textbox
import tkinter as tk
import os


window = tk.Tk()
window.geometry('800x400')


def descriptions():
    # open the file of text
    with open('content.txt', 'r') as content:
        text_contents = content.readlines()
        # grab the value in the drop down menu, which is being held by drop_down_holder
        chosen_gender = drop_down_holder.get()
        if chosen_gender == "Male (he/his)":
            for line in text_contents:
                # swap the name, and pronouns
                male_text = line.replace("$name", str(name_entry.get())).replace("$pronoun", "he").replace("$possessive_pronoun", "his")
                # insert the outcome of the replacements into the text box
                output.insert(tk.END, male_text)

        if chosen_gender == "Female (she/hers)":
            for line in text_contents:
                female_text = line.replace("$name", str(name_entry.get())).replace("$pronoun", "she").replace("$possessive_pronoun", "hers")
                output.insert(tk.END, female_text)

        if chosen_gender == "Genderless (they/theirs)":
            for line in text_contents:
                genderless_text = line.replace("$name", str(name_entry.get())).replace("$pronoun", "they").replace("$possessive_pronoun", "theirs")
                output.insert(tk.END, genderless_text)

# The enter their name label
name_label = tk.Label(window, text="Enter their name")
name_label.grid(row=0, column=0, pady=2, padx=2)

# the name entry field
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, pady=2, padx=2)

# a spacer to seperate the name section from the pronoun section
spacer1 = tk.Label(window, text="")
spacer1.grid(row=0, column=2, pady=2, padx=10)

# gender label
gender_label = tk.Label(window, text="Enter their prefered pronouns")
gender_label.grid(row=0, column=3, pady=2, padx=2)

# a list of the genders
genders_lst = ("Male (he/his)", "Female (she/hers)", "Genderless (they/theirs)")
# a variable to hold the value selected from the dropdown box
drop_down_holder = tk.StringVar(window)
# the actual drop down menu
gender_dropdown = tk.OptionMenu(window, drop_down_holder, *genders_lst)
gender_dropdown.grid(row=0, column=4, pady=2, padx=2)

# a spacer to seperate the gender stuff from the submit button
spacer2 = tk.Label(window, text="")
spacer2.grid(row=0, column=5, pady=2, padx=10)

# the submit button, which runs the descriptions function
button = tk.Button(window, text="Submit", command=descriptions)
button.grid(row=0, column=6, pady=2, padx=2)

# the output box
output = tk.Text(window, height=20, width=80)
output.grid(row=1, column=0, pady=5, padx=5, columnspan=6)

window.mainloop()