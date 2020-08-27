__author__ = 'Illya King'

#   Input List: names, health, magic
#   Output List: names, health, magic, total_health, total_magic, total_attributes, percent_might, final_score, counter
#
#   Constant Integer MAX_POWER = 256

MAX_POWER = 256

#   Class Statistics
#       Private Integer _number_of_adventurers
#       Private Adventurer _adventurer[MAX_POWER]
#       Private Real _total_health
#       Private Real _total_magic
#       Private Real _total_attributes
#
#       Public Module get_adventurers()
#          Declare Boolean done = False
#          Declare Adventurer adventurers
#          Declare Boolean is_adventurer = true
#
#          While not done
#              Set is_adventurer = y_or_n("Is the character a squire (Y/N)? ")
#              If is_adventurer Then
#                  Set adventurer = New SquireStats()
#              Else
#                  Set adventurer = New Adventurer()
#              End If
#              Call adventurer.input()
#              Set _adventurers[_number_of_adventurers] = adventurer
#              Set _number_of_adventurers = _number_of_adventurers + 1
#              Set done = y_or_n("Are you finished entering party member's information (Y/N)? ")
#          End While
#      End Function
#
#      Public Module display()
#           Declare Integer counter = 0
#           Declare Real final_score
#           Declare Real percent_might
#           Declare Adventurer adventurer
#
#           While counter < _number_of_adventurers
#               Set adventurer = _adventurers[counter]
#               Set percent_might = (adventurer.get_health() / (_total_health + _total_magic)) * 100
#               Display "Adventurer", (counter + 1), "-", adventurer.get_name(), "is", "{:.2f}".format(percent_might),
#                       "% of the party's might based on:", adventurer.get_health(), "Health Points and", adventurer.get_magic(), "Magic Points."
#               Set counter= counter + 1
#           End While
#           Set percent_might = (adventurer.get_health() / (_total_health + _total_magic)) * 100
#           Set final_score = (self._total_attributes / percent_might) / 100
#           Display "Total Health of Party:", _total_health"
#           Display "Total Magic Potential:", _total_attributes"
#           Display "Success Rate:", "{:.2f}".format(final_score), "Percent"
#       End Module

class Statistics:
    _number_of_adventurers = 0
    _adventurers = [None for x in range(MAX_POWER)]
    _total_health = 0.0
    _total_magic = 0.0
    _total_attributes = 0.0

    def get_adventurers(self):
        done = False
        adventurer = None
        is_alcoholic = True

        while not done:
            is_adventurer = y_or_n("Is the character a squire (Y/N)? ")
            if(is_adventurer):
                adventurer = SquireStats()
            else:
                adventurer = Adventurer()
            adventurer.input()
            self._adventurers[self._number_of_adventurers] = adventurer
            self._number_of_adventurers = self._number_of_adventurers + 1
            done = y_or_n("Are you finished entering party member's information (Y/N)? ")

    def display(self):
        counter = 0
        final_score = 0.0
        percent_might = 0.0
        adventurer = None

        final_score = 100

        while counter < self._number_of_adventurers:
            adventurer = self._adventurers[counter]
            percent_might = (adventurer.get_health() / (self._total_health + self._total_magic)) * 100
            print("Character", (counter + 1), "-", adventurer.get_names(), "is", "{:.2f}".format(percent_might),
                    "% of the party's might based on:", adventurer.get_health(), "Health Points and",
                    adventurer.get_magic(), "Magic Points.")
            counter = counter + 1

        final_score = (self._total_attributes / percent_might) / 100
        print("Total Health Points of Party:", self._total_health)
        print("Cumulative Might Points of Party:", self._total_attributes)
        print("Success Rate:", "{:.2f}".format(final_score), "%")

    def calculate(self):
        counter = 0
        adventurer = None

        while counter < self._number_of_adventurers:
            adventurer = self._adventurers[counter]
            self._total_health = self._total_health + adventurer.get_health()
            self._total_magic = self._total_magic + adventurer.get_magic()
            self._total_attributes = self._total_attributes + adventurer.get_health() * adventurer.get_magic()
            counter = counter + 1

#   Class Adventurers
#       Private String _names
#       Private Real _health
#       Private Real _magic
#
#       Public Module input()
#           Set _names = get_string("What is the name of the character? ")
#           Set _health = get_real("How many Health Points does " + _names + " have? ")
#           Set _magic = get_real("How many Magic Points does " + _names + " have? ")
#       End Module
#
#       Public Function String get_names()
#           Return _names
#       End Function
#
#       Public Function Real get_health()
#           Return _health
#       End Function
#
#       Public Function Real get_magic()
#           Return _magic
#       End Function
#
#   End Class
#
#   Public Module calculate()
#       Declare Integer counter = 0
#       Declare Adventurer adventurer
#
#       While counter < number_of_adventurers
#           Set adventurer = _adventurers[counter]
#           Set total_health = _total_health + adventurer.get_health()
#           Set total_magic = _total_magic + adventure.get_magic()
#           Set total_attributes = _total_attributes + adventurer.get_health() * adventurer.get_magic()
#           counter = counter + 1
#       End While
#   End Function

class Adventurer:
    _names = ""
    _health = 0.0
    _magic = 0.0

    def input(self):
        self._names = get_string("What is the name of the character? ")
        self._health = get_real("How many Health Points does " + self._names + " have? ")
        self._magic = get_real("How many Magic Points does " + self._names + " have? ")

    def get_names(self):
        return self._names

    def get_health(self):
        return self._health

    def get_magic(self):
        return self._magic

# Class SquireStats Extend Adventurer
#
#       Public Module input()
#          Set _names = get_string("What is the name of the squire? ")
#          Set _health = get_real("How many Health Points does " + _names + " have? ")
#       End Module
#
class SquireStats(Adventurer):
    def input(self):
        self._names = get_string("What is the name of the squire? ")
        self._health = get_real("How many Health Points does " + self._names + " have? ")

#   Function String get_string(String prompt)
#       Declare String Value
#
#       Display prompt
#       Input value
#       Return value
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

#   Module party_success()
#       Declare Adventurers adventurers[MAX_POWER]
#       Declare Integer number_of_adventurers
#       Declare Real total_health
#       Declare Real total_magic
#       Declare Real total_attributes
#       Declare Statistics statistics
#
#       Set statistics = New Statistics()
#       Call statistics.get_adventurers()
#       Call statistics.calculate()
#       Call statistics.display()
#   End Module

def party_success():
    statistics = None

    statistics = Statistics()
    statistics.get_adventurers()
    statistics.calculate()
    statistics.display()

party_success()