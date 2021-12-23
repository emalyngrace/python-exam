from __future__ import print_function
# Created by sarathkaul on 12/11/19


def convert_time(input_str):
    """
    Converts 12-hour format into 24-hour format.

    :param input_str: A string representing time in 12 hour format.
    :type input_str: str
        :Example of
    usage (input): "07:05 PM"

        :returns output_str, a string representing time in 24 hour format.  The return value is a string object and should be
    formatted as [H]H:[M]M.[S]S.[MS][NS][PS].  For example, 2 minutes and 3 seconds would be returned as 02:03.125000

        :rtype output_str = str
    """
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if input_str[-2:] == "AM" and input_str[:2] == "12":
        return "00" + input_str[2:-2]

    # remove the AM
    elif input_str[-2:] == "AM":
        return input_str[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif input_str[-2:] == "PM" and input_str[:2] == "12":
        return input_str[:-2]

    else:
        # add 12 to hours and remove PM
        return str(int(input_str[:2]) + 12) + input_str[2:8]


if __name__ == '__main__':
    input_time = input("Enter time you want to convert: ")
    print(convert_time(input_time))
