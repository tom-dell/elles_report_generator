from cgitb import text
from curses.textpad import Textbox
import tkinter as tk
import os


window = tk.Tk()
window.geometry('800x400')


def descriptions():
    with open('content.txt', 'r') as content:
        text_contents = content.readlines()
    # the for loop to swap $name with whatever is entered in the name_text entry
    for line in text_contents:
        name_replaced = line.replace("$name", str(name_entry.get()))
        #output.insert(tk.END, name_replaced)
        # the if statement for pronouns
        if gender_dropdown == "Male":
            for line in name_replaced:
                male_pronouns = line.replace("$pronoun", "he")
                male_pronouns = line.replace("$possessive_pronoun", "his")
                print(male_pronouns)
                #output.insert(tk.END, male_pronouns)
        if gender_dropdown == "Female":
            for line in name_replaced:
                female_pronouns = line.replace("$pronoun", "she")
                female_pronouns = line.replace("$possessive_pronoun", "hers")
                output.insert(tk.END, female_pronouns)
        if gender_dropdown == "Genderless":
            for line in name_replaced:
                genderless_pronouns = line.replace("$pronoun", "they")
                genderless_pronouns = line.replace("$possessive_pronoun", "theirs")
                output.insert(tk.END, genderless_pronouns)


name_label = tk.Label(window, text="Enter their name")
name_label.grid(row=0, column=0, pady=2, padx=2)

name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, pady=2, padx=2)

spacer1 = tk.Label(window, text="")
spacer1.grid(row=0, column=2, pady=2, padx=10)

gender_label = tk.Label(window, text="Enter their prefered pronouns")
gender_label.grid(row=0, column=3, pady=2, padx=2)

genders_lst = ("Male", "Female", "Genderless")
drop_down_holder = tk.StringVar(window)
gender_dropdown = tk.OptionMenu(window, drop_down_holder, *genders_lst)
gender_dropdown.grid(row=0, column=4, pady=2, padx=2)

spacer2 = tk.Label(window, text="")
spacer2.grid(row=0, column=5, pady=2, padx=10)

button = tk.Button(window, text="Submit", command=descriptions)
button.grid(row=0, column=6, pady=2, padx=2)

output = tk.Text(window, height=20, width=80)
output.grid(row=1, column=0, pady=5, padx=5, columnspan=6)


window.mainloop()