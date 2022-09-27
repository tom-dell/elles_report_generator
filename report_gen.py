
gender = "Male"
name_text = "Tom"

def descriptions():
    with open('content.txt', 'r') as content:
        text_contents = content.readlines()
        for line in text_contents:
            final_text = line.replace("$name", name_text).replace("$pronoun", "he").replace("$possessive_pronoun", "his")
            print(final_text)


descriptions()