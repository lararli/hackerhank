"""
This code defines a function named time_conversion that takes a string
hour as input and returns a string in 24-hour format.
The input string is in 12-hour format with an AM or PM suffix.

The function first checks if the input string ends with PM and starts with 12.
If that's the case, it returns the input string without the PM suffix
since 12 PM is the same as 12 in 24-hour format.

The second condition checks if the input string ends with AM
and starts with 12. If that's the case,
it returns the input string with the hours replaced with 00,
since 12 AM is equivalent to 00 in 24-hour format.

If the input string ends with AM but doesn't start with 12,
the function returns the input string without the AM suffix.

If none of the above conditions are true,
the function assumes that the input string represents a time in the afternoon or evening,
so it converts the hours part of the string to an integer,
adds 12 to it, and returns the result as a string in 24-hour format.
"""

def time_conversion(hour: str) -> str:
    """
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
    :type hour: string
    :param hour: the time in 12-hour format
    :return: the time in 24-hour format
    """
    if hour.endswith('PM') and hour.startswith('12'):
        return hour[:-2]
    if hour.endswith('AM') and hour.startswith('12'):
        return '00' + hour[2:-2]
    if hour.endswith('AM'):
        return hour[:-2]
    hour_in_military_time = str(int(hour[:2]) + 12) + hour[2:8]
    return hour_in_military_time


if __name__ == '__main__':
    s = input()
    result = time_conversion(s)
    print(result)
