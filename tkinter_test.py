from cgitb import text
from curses.textpad import Textbox
import tkinter as tk
import os


window = tk.Tk()
window.geometry('800x400')
output = tk.Text(window, height=20, width=50)
drop_down_holder = tk.StringVar(window)
genders_lst = ("Male", "Female", "Genderless")

def descriptions():
    with open('content.txt', 'r') as content:
        text_contents = content.readlines()
    # the for loop to swap $name with whatever is entered in the name_text entry
    for line in text_contents:
        name_replaced = line.replace("$name", str(name_text.get()))
        # the if statement for pronouns
        if gender == "Male":
            for line in name_replaced:
                male_pronouns = line.replace("$pronoun", "he")
                male_pronouns = line.replace("$possessive_pronoun", "his")
                print(male_pronouns)
                #output.insert(tk.END, male_pronouns)
        if gender == "Female":
            for line in name_replaced:
                female_pronouns = line.replace("$pronoun", "she")
                female_pronouns = line.replace("$possessive_pronoun", "hers")
                output.insert(tk.END, female_pronouns)
        if gender == "Genderless":
            for line in name_replaced:
                genderless_pronouns = line.replace("$pronoun", "they")
                genderless_pronouns = line.replace("$possessive_pronoun", "theirs")
                output.insert(tk.END, genderless_pronouns)


name_text = tk.Entry(window)
gender = tk.OptionMenu(window, drop_down_holder, *genders_lst)
button = tk.Button(window, text="Submit", command=descriptions)

gender.pack()
output.pack()
name_text.pack(side = tk.RIGHT)
button.pack(side = tk.LEFT)

window.mainloop()
