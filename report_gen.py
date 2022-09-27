
gender = "Male"
name_text = "Tom"

def descriptions():
    with open('content.txt', 'r') as content:
        text_contents = content.readlines()
    # the for loop to swap $name with whatever is entered in the name_text entry
    for line in text_contents:
        name_replaced = line.replace("$name", str(name_text))

def gender():
    # the if statement for pronouns
    if gender == "Male":
        replacers = {"$pronoun":"he", "$possessive_pronoun":"his"}
        final_text = name_replaced.replace(replacers)
        print(final_text)

descriptions()