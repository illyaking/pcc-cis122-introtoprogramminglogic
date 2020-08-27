__author__ = 'Illya King'

# Formula credit: https://www.w3resource.com/projects/python/python-projects-1.php
# Formula credit: https://github.com/MrBlaise/learnpython/blob/master/Numbers/pi.py

# Input List: input_string, radius_value
# Output List: calc_pi, pi_digits
#
# Function Boolean is_valid_integer(String input_string)
#   Declare Boolean is_valid
#
#   is_valid = is input_string a valid integer?
#   Return is_valid
# End Function

def is_valid_integer(input_string):
    try:
        val = int(input_string)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

# Function Integer get_number_of_pi_number()
#   Declare String input_string
#   Declare Boolean is_valid
#
#   Display "How many digits do you want to take pi to? "
#   Input input_string
#   Set is_valid = is_valid_integer(input_string)
#   While Not is_valid
#       Display "Please enter a whole number! "
#       Input input_string
#       is_valid = is_valid_integer(input_string)
#   End While
#   input_integer = int(input_string)
#   Return input_integer
# End Function

def get_number_of_pi_numbers():
    input_string = input("How many digits do you want to take pi to? ")
    is_valid = is_valid_integer(input_string)
    while not is_valid:
        input_string = input("Please enter a whole number! ")
        is_valid = is_valid_integer(input_string)
    input_integer = int(input_string)
    return input_integer

# Prints out the value of Pi until the limit stated in the input_string is reached
#
# Module input_string(limit)
#   Set decimal = limit (as defined by get_number_of_pi_digits
#   Set counter = 0
#   while counter is not = decimal + 1
#   Do math as set by https://github.com/MrBlaise/learnpython/blob/master/Numbers/pi.py
# End Module

def calc_pi(limit):

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    # yield digit
                    yield n
                    # insert period after first digit
                    if counter == 0:
                            yield '.'
                    # end
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr

# Module calculate_pi_sequence()
#   Declares pi_digits the limit value provided by calc_pi
#   Calls calc_pi with limit defined by get_number_of_pi_numbers()
#   Declares i = 0
#   Sets pi_digit = calc_pi(get_number_of_pi_numbers())
#       i = value
#       if i = 40 digits
#       print output of the calc_pi generator above
#       if 40 digit limit reached
#       new line
# End Module

def calculate_pi_sequence():
    pi_digits = calc_pi(get_number_of_pi_numbers())
    i = 0
    for d in pi_digits:
        print(d, end='')
        i += 1
        if i == 40:
            print("")
            i = 0

if __name__ == '__main__':
    calculate_pi_sequence()