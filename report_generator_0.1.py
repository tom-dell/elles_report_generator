from cProfile import label
from cgitb import text
from curses.textpad import Textbox
from textwrap import wrap
import tkinter as tk

window = tk.Tk()
window.geometry('600x700')
window.wm_title("Ellesha Murphey's Report Generator")
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/3 - windowHeight/2)
window.geometry("+{}+{}".format(positionRight, positionDown))

top_frame = tk.Frame(window)
top_frame.grid(row=0, sticky=tk.EW)
center_frame = tk.Frame(window)
center_frame.grid(row=1, sticky=tk.EW, pady=2, padx=3)
center_frame_canvas = tk.Canvas(center_frame, width=500, height=500, highlightbackground="black", highlightthickness=2, scrollregion=(0,0,500,500))
center_frame_canvas.grid(sticky=tk.NE)
bottom_frame = tk.Frame(window)
bottom_frame.grid(row=2, sticky=tk.EW)


'''
v_bar = tk.Scrollbar(center_frame_canvas)
v_bar.grid(sticky=tk.N)
v_bar.config(command=center_frame_canvas.yview)
center_frame_canvas.config(yscrollcommand=v_bar.set)
'''


def generate_descriptors():
    # open the file of text
    with open('descriptors.txt', 'r') as descriptors:
        # read lines in the text file
        descriptors_contents = descriptors.readlines()
        # grab the value in the drop down menu, which is being held by drop_down_holder
        chosen_gender = drop_down_holder.get()

        # 3 if statements which will swap the name and pronouns based on gender picked
        if chosen_gender == "Male (he/his)":
            for line in descriptors_contents:
                # swap the name, and pronouns
                male_descriptors = line.replace("$name", str(name_entry.get())).replace("$pronoun", "he").replace("$possessive_pronoun", "his")
                # append each line to the list
                descriptors_lst.append(male_descriptors)
        make_checkboxes()

        if chosen_gender == "Female (she/hers)":
            for line in descriptors_contents:
                female_descriptors = line.replace("$name", str(name_entry.get())).replace("$pronoun", "she").replace("$possessive_pronoun", "hers")
                descriptors_lst.append(female_descriptors)
        make_checkboxes()

        if chosen_gender == "Genderless (they/theirs)":
            for line in descriptors_contents:
                genderless_descriptors = line.replace("$name", str(name_entry.get())).replace("$pronoun", "they").replace("$possessive_pronoun", "theirs")
                descriptors_lst.append(genderless_descriptors)
        make_checkboxes()

def make_checkboxes():
    i = 2
    for index, item in enumerate(descriptors_lst):
        var_lst.append(tk.IntVar(value=0))
        checkbox = tk.Checkbutton(center_frame_canvas, variable=var_lst[index], text=item, wraplength=500)
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

def help_popup():
    popup = tk.Tk()
    popup.wm_title("Help")
    windowWidth = popup.winfo_reqwidth()
    windowHeight = popup.winfo_reqheight()
    positionRight = int(popup.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(popup.winfo_screenheight()/3 - windowHeight/2)
    popup.geometry("+{}+{}".format(positionRight, positionDown))
    heading = tk.Label(popup, text="Descriptors")
    heading.grid(row=0, pady=5, padx=5)
    message = tk.Label(popup, text="To create the descriptors, click the button below to create a text file alongside this program with some sample descriptors." + "\n" + "When writing your own, ensure each one is on a new line." + "\n" + "For available substitutions you can use in your descriptors, see below.")
    message.grid(row=0, pady=10, padx=10)
    create_sample_button = tk.Button(popup, text="Create sample descriptors file", command = create_sample)
    create_sample_button.grid(row=1, pady=10, padx=10)
    subs = tk.Label(popup, text="$name -> Whatever is entered into the name text field" + "\n" + "$pronoun -> The pronoun listed in the dropdown box (he/she/they)"  + "\n" + "$possessive_pronoun -> The possessive pronoun listed in the dropdown box (his/hers/theirs)")
    subs.grid(row=2, pady=10)
    example = tk.Label(popup, text="For example, if you had the template:" + "\n" + "$name plays well with $possessive_noun toys and $pronoun likes to play with $possessive_pronoun friends." + "\n" + "If you entered the name Miles, and the gender as he/him, it would become:" + "\n" + "Miles plays well with his toys and he likes to play with his friends.")
    example.grid(row=3)
    okay_button = tk.Button(popup, text="Okay!", command = popup.destroy)
    okay_button.grid(row=4, pady=10, padx=10)

def create_sample():
    with open("sample_descriptors.txt", "w+") as sample_descriptors:
        sample_descriptors.write("$name is kind, creative and imaginative member of our classroom. \n")
        sample_descriptors.write("$name seeks humour and joy in every day. \n")
        sample_descriptors.write("$name is observant and in tune with the needs of $possessive_pronoun friends and people around them and responds with a caring nature. \n")
    sample_create_popup()

def sample_create_popup():
    popup = tk.Tk()
    popup.wm_title("Sample file created")
    windowWidth = popup.winfo_reqwidth()
    windowHeight = popup.winfo_reqheight()
    positionRight = int(popup.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(popup.winfo_screenheight()/3 - windowHeight/2)
    popup.geometry("+{}+{}".format(positionRight, positionDown))
    heading = tk.Label(popup, text="Sample descriptors file created, don't forget to remove the word sample_ from the file name!")
    heading.grid(row=0, pady=5, padx=5)
    okay_button = tk.Button(popup, text="Okay!", command = popup.destroy)
    okay_button.grid(row=4, pady=10, padx=10)


# a list containing the name+pronoun swapped strings
descriptors_lst = []
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
button = tk.Button(top_frame, text="Generate", command=generate_descriptors)
button.grid(row=0, column=3, pady=2, padx=2, columnspan=2)

# the clear button, which runs the clear_checkboxes function
button = tk.Button(top_frame, text="Clear", command=clear_checkboxes)
button.grid(row=1, column=3, pady=2, padx=2, columnspan=2)

# the save/export button, this will write the checked descriptors to a text file
button = tk.Button(bottom_frame, text="Save/Export", command=write_to_file)
button.grid(row=0, column=0)

# this button opens the help section
button = tk.Button(bottom_frame, text="Help", command=help_popup)
button.grid(row=0, column=1)

window.mainloop()