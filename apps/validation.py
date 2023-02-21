import string


def validate_text(word):
    data = word.split(' ')
    if all(c not in string.ascii_letters for c in word) and len(data)==2 and data[0][0].islower()==False and data[1][0].islower()==False:
        return True
    return False


def validate_phone(phone):
    if str(phone)[:4]=='+996' and len(phone)==13:
        return True
    return False


def validate_email(email):
    if '@gmail.com' in email:
        return True
    return False