def is_digit(d):
    return '0' <= d <= '9'
def format_phone_number(phone_number):
    my_string = " "
    for d in phone_number:
        if is_digit(d):
            my_string += d
    if len(digits) != 10 or digits[0] != '0':
        return "Invalid phone number"