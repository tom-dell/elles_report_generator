import os

name = input("What is their name? ")
pronoun = input("What pronoun do they use? ")
report = open(name + "_report.txt", "w+")


######################################################################
#### Change text below ####
######################################################################

geo_1 = str(pronoun + " is very good at geography")
geo_2 = str(pronoun + " needs some adult help with geography")
geo_3 = str(pronoun + " is worse than tom at geography")

comms_1 = str(pronoun + " is very good at communicating")
comms_2 = str(pronoun + " often needs help communicating")
comms_3 = str(pronoun + " is bad at communicating")

######################################################################
######################################################################

def geography():
    print("\n\n" + "Geography")
    print("1: " + geo_1 + "\n" + "2: " + geo_2 + "\n" + "3: " + geo_3 + "\n")
    geo_level = input("How good at geography are they? (any key to skip): ")
    if geo_level == "1":
        report.write(geo_1 + "\n\n")
    if geo_level == "2":
        report.write(geo_2 + "\n\n")
    if geo_level == "3":
        report.write(geo_3 + "\n\n")
    else:
        report.write("\n")

def communication():
    print("\n\n" + "Communication")
    print("1: " + comms_1 + "\n" + "2: " + comms_2 + "\n" + "3: " + comms_3 + "\n")
    comms_level = input("How good at communication are they? (any key to skip): ")
    if comms_level == "1":
        report.write(comms_1 + "\n\n")
    if comms_level == "2":
        report.write(comms_2 + "\n\n")
    if comms_level == "3":
        report.write(comms_3 + "\n\n")
    else:
        report.write("\n")
        
geography()
communication()

report.close()