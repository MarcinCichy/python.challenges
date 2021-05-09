# Challenge: Convert Temperatures
# from RealPython, Python Basics, chapter 6.3
#

def convert_cel_to_far(cel_degr_input):
    """ Returns temperature in degrees Farenheit converted from degrees Celsius """
    far_degr = (cel_degr_input*9/5) + 32
    return far_degr
  
def convert_far_to_cel(far_degr_input):
    """ Returns temperature in degrees v converted from degrees Farenheit """
    cel_degr = (far_degr_input-32) * 5/9
    return cel_degr

far_degr_input = float(input ("Enter a temperature in degrees F: "))                                    # take from user value of temperature in degrees Farenheit, converting it to a float and assign it to variable far_degr_input
print (f"{far_degr_input} degrees F = {(convert_far_to_cel(far_degr_input)):.2f} degrees C \n")         # print result of convert_far_to_cel rounded to two decimal places
cel_degr_input = float(input ("Enter a temperature in degrees C: "))                                    # take from user value of temperature in degrees Celsius, converting it to a float and assign it to variable cel_degr_input
print (f"{cel_degr_input} degrees C = {(convert_cel_to_far(cel_degr_input)):.2f} degrees F \n")         # print result of convert_cel_to_far rounded to two decimal places









