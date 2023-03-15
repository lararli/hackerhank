"""
Convert 12-hour AM/PM format into military time (24-hour format).
"""


def time_conversion(hour: str) -> str:
    """
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
    :type hour: string
    :param hour: the time in 12 hour format
    :return: the time in 24 hour format
    """
    if hour[-2:] == 'PM' and hour[:2] == '12':
        return hour[:-2]
    if hour[-2:] == 'AM' and hour[:2] == '12':
        return '00' + hour[2:-2]
    if hour[-2:] == 'AM':
        return hour[:-2]
    return str(int(s[:2]) + 12) + s[2:8]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = time_conversion(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()
