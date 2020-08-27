__author__ = 'Illya King'

#   Input List: names, health, magic
#   Output List: names, health, magic, total_health, total_attributes, percent_might, final_score, counter
#
#   Constant Integer MAX_POWER = 256

MAX_POWER = 256
#
#   Function String get_string(String prompt)
#       Declare String Value
#
#       Display prompt
#       Input value
#       return value
#   End Function

def get_string(prompt):
        value = ""

        value = input(prompt)
        return value

#   Function Real get_real(String prompt)
#       Declare String value
#
#       Display prompt
#       Input value
#       While not value is a real number
#           Display value, "is not a number. Please try again."
#           Display prompt
#           Input value
#       End While
#       Return value
#   End Function

def valid_real(value):
    try:
        float(value)
        return True
    except:
        return False

def get_real(prompt):
    value = ""

    value = input(prompt)
    while not valid_real(value):
        print(value, "is not a number. Please try again.")
        value = input(prompt)
    return float(value)

#   Function Boolean y_or_n(String prompt)
#       Declare String value
#
#       Display prompt
#       Input value
#       While True
#           If value == "Y" or value == "y" Then
#               Return true
#           Else If value == "N" or value == "n" Then
#               Return false
#           Else
#               Display "Please enter Y or N!"
#               Display prompt
#               Input value
#           End If
#       End While
#   End Function

def y_or_n(prompt):
    value = ""

    value = input(prompt)
    while True:
        if value == "Y" or value == "y":
            return True
        elif value == "N" or value =="n":
            return False
        else:
            print("Please enter Y or N!")
            value = input(prompt)

#   Function Integer get_adventurers(String [] names, Real[] health, Real[] magic)
#       Declare Boolean done = False
#       Declare Integer counter = 0
#
#       While not done
#           names[counter] = get_string("What is the name of the adventurer ")
#           health[counter] = get_real("How many Health Points does " + names[counter] + " have? ")
#           magic[counter] = get_real("How many Magic Points does " + names[counter] + " have? ")
#           counter = counter + 1
#           done = y_or_n("Are you finished entering adventurer's information (Y/N)? ")
#       End While
#       Return counter
#   End Function

def get_adventurers(names, health, magic):
    done = False
    counter = 0

    while not done:
        names[counter] = get_string("What is the name of the adventurer ")
        health[counter] = get_real("How many Health Points does " + names[counter] + " have? ")
        magic[counter] = get_real("How many Magic Points does " + names[counter] + " have? ")
        counter = counter + 1
        done = y_or_n("Are you finished entering adventurer's information (Y/N)? ")
    return counter

#   Function Real, Real calculate_totals(Integer number_of_adventurers, Real[] health, Real[] magic)
#       Declare Integer counter = 0
#       Declare Real total_health = 0.0
#       Declare Real total_attributes = 0.0
#
#       While counter < number_of_adventurers
#           total_health = total_health + health(counter)
#           total_attributes = total_attributes + health[counter] * magic[counter]
#           counter = counter + 1
#       End While
#       Return total_health, total_attributes
#   End Function

def calculate_totals(number_of_adventurers, health, magic):
    counter = 0
    total_health = 0.0
    total_attributes = 0.0

    while counter < number_of_adventurers:
        total_health = total_health + health[counter]
        total_attributes = total_attributes + health[counter] * magic[counter]
        counter = counter + 1
    return total_health, total_attributes

#   Module display_party(Integer number_of_adventurers, String[] names, Real[] health, Real[] magic,
#                               Real total_health, Real total_attributes)
#       Declare Integer counter = 0
#       Declare Real final_score
#       Declare Real percent_might
#
#       While counter < number_of_adventurers
#           percent_might = 100 * health[counter] / total_health
#           Display "Adventurer", (counter + 1), "-", names[counter], "is", "{:.2f}".format(percent_might),
#                     "% of the party's might based on:", health[counter], "Health Points and", magic[counter], "Magic Points."
#           counter= counter + 1
#       End While
#       percent_alcohol = 100 * total_attributes / total_health
#       Display "Total Health of Party:", total_health"
#       Display "Total Magic Potential:", total_attributes"
#       Display "Success Rate:", "{:.2f}".format(final_score), "Percent"
#   End Module

def display_party(number_of_adventurers, names, health, magic, total_health, total_attributes):
    counter = 0
    final_score = 0.0
    percent_might = 0.0

    while counter < number_of_adventurers:
        percent_might = 1000 * health[counter] / total_health
        print("Adventurer", (counter + 1), "-", names[counter], "is", "{:.2f}".format(percent_might),
                    "% of the party's might based on:", health[counter], "Health Points and", magic[counter], "Magic Points.")
        counter = counter + 1

    final_score = total_attributes / percent_might
    print("Total Health Points of Party:", total_health)
    print("Cumulative Might Points of Party:", total_attributes)
    print("Success Rate:", "{:.2f}".format(final_score ), "%")

#   Module party_success()
#       Declare Strings names[MAX_POWER]
#       Declare Real health[MAX_POWER]
#       Declare Real magic[MAX_POWER]
#       Declare Integer number_of_adventurers
#       Declare Real total_health
#       Declare Real total_attributes
#
#       number_of_adventurers = get_adventurers(names, health, magic)
#       total_health, total_attributes = calculate_totals(number_of_adventurers, health, magic)
#       Call display_party(number_of_adventurers, names, health, magic, total_health, total_attributes)
#   End Module

def party_success():
    names = ["" for x in range(MAX_POWER)]
    magic = [0.0 for x in range(MAX_POWER)]
    health = [0.0 for x in range(MAX_POWER)]
    number_of_adventurers = 0
    total_health = 0.0
    total_attributes = 0.0

    number_of_adventurers = get_adventurers(names, health, magic)
    total_health, total_attributes = calculate_totals(number_of_adventurers, health, magic)
    display_party(number_of_adventurers, names, health, magic, total_health, total_attributes)

party_success()