__author__ = 'Illya King'

# Input List: container_length, container_width, commodity_length, commodity_width, commodity_height
# Output list: container_length, container_width, commodity_length, commodity_width,
# Output List: commodity_height, container_square_inches, does_or_does_not, dim_percentage

# Function Real
#   Declare container_length
#   Declare container_width
#   Declare commodity_length
#   Declare commodity_width
#   Declare commodity_height
#
#   Display "Enter in the container's length: "
#   Input container_length
#   Display "Enter in the container's width: "
#   Input container_width
#   Display "Enter in the commodity's length: "
#   Input commodity_length
#   Display "Enter in the commodity's width: "
#   Input commodity_width
#   Display "Enter in the commodity's height: "
#   Input commodity_height
#   Return container_length, container_width, commodity_length, commodity_width, commodity_height
# End Function

def get_dimensions():
    container_length = 0.0
    container_width = 0.0
    commodity_length = 0.0
    commodity_width = 0.0
    commodity_height = 0.0

    container_length = float(input("Enter in the container's length: "))
    container_width = float(input("Enter in the container's width: "))
    commodity_length = float(input("Enter in the commodity's length: "))
    commodity_width = float(input("Enter in the commodity's width: "))
    commodity_height = float(input("Enter in the commodity's height: "))
    return container_length, container_width, commodity_length, commodity_width, commodity_height

# Function Real calculate_commodity_square_inches(Real commodity_length, commodity_width)
#   Declare Real commodity_square_inches
#
#   commodity_square_inches = commodity_length * commodity_width
#   Return commodity_square_inches
# End Function

def calculate_commodity_square_inches(commodity_length, commodity_width):
    commodity_square_inches = 0.0

    commodity_square_inches = commodity_length * commodity_width

    return commodity_square_inches

# Function Real calculate_container_square_inches(Real container_length, Real container_width)
#   Declare = container_square_inches
#
#   container_square_inches = container_length * container_width
#   Return container_square_inches
# End Function

def calculate_container_sqaure_inches(container_length, container_width):
    container_square_inches = 0.0

    container_square_inches = container_length * container_width

    return container_square_inches

# Function Real calculate_total_space_occupied()
#   Declare Real total_space_occupied
#
#   total_space_occupied = commodity_square_inches / container_square_inches
#   Return total_space_occupied

# End Function

def calculate_total_space_occupied(commodity_square_inches, container_square_inches):
    total_space_occupied = 0.0

    total_space_occupied = commodity_square_inches / container_square_inches

    return total_space_occupied

# Function string calculate_does_or_does_not(Real dim_percentage)
#   Declare String does_or_does_not
#
#   If dim_percentage <= .65 then
#       does_or_does_not = "does"
#   Else
#       does_or_does_not = "does not"
#   End IF
#   Return does_or_does_not
# End Function

def calculate_does_or_does_not(total_space_occupied):
    does_or_does_not = ""

    if total_space_occupied <= 0.65:
        does_or_does_not = "does"
    else:
        does_or_does_not = "does not"
    return does_or_does_not

# Module output_dimensions(Real commodity_length, Real commodity_width, Real commodity_height, Real container_length, Real container_width, Real container_square_inches, Real total_space_occupied, String does_or_does_not)
#   Display "Commodity occupies", commodity_length, "inches by", commodity_width, "inches by", commodity_height, "inches"
#   Display "In a container with an area of", container_length, "inches &", container_width, "inches or", container_square_inches,
#           "square inches of space"
#   Display "Which occupies", total_space_occupied, "percent of a lift truck skids, pallets or platforms"
#   Display "Shipment", does_or_does_not, "meet the requirement of NMFC item 680 note c."
# End Module

def output_dimensions(commodity_length, commodity_width, commodity_height, container_length, container_width, container_square_inches, total_space_occupied, does_or_does_not):
    print("Commodity occupies", commodity_length, "inches by", commodity_width, "inches by", commodity_height, "inches")
    print("In a container with an area of", container_length, "inches &", container_width, "inches or", container_square_inches,
          "square inches of space")
    print("Which occupies", "{0:.0f}%".format(total_space_occupied * 100), "percent of a lift truck skids, pallets or platforms")
    print("Shipment", does_or_does_not, "meet the requirement of NMFC item 680 note c.")

# Module calculate_item_680()
#   Declare container_length
#   Declare container_width
#   Declare commodity_length
#   Declare commodity_width
#   Declare commodity_height
#   Declare Real total_space_occupied
#   Declare Real dim_percentage
#   Declare String does_or_does_not
#
#   Set container_length, container_width, commodity_length, commodity_width, commodity_height = get_dimensions()
#   Set container_square_inches, commodity_square_inches = total_space_occupied()
#   Set dim_percentage = commodity_square_inches / container_square_inches
#   Set does_or_does_not = dim_percentage(total_space_occupied)
#   Call output_dimensions(dim_percentage, total_space_occupied)
# End Module

def calculate_item_680():

    container_length, container_width, commodity_length, commodity_width, commodity_height = get_dimensions()
    container_square_inches = calculate_container_sqaure_inches(container_length, container_width)
    commodity_square_inches = calculate_commodity_square_inches(commodity_length, commodity_width)
    total_space_occupied = calculate_total_space_occupied(commodity_square_inches, container_square_inches)
    does_or_does_not = calculate_does_or_does_not(total_space_occupied)
    output_dimensions(commodity_length, commodity_width, commodity_height, container_length, container_width, container_square_inches, total_space_occupied, does_or_does_not)

calculate_item_680()