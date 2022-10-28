class Email:
    def __init__(self, email, symbol="x"):
        self.full_email = email
        self.email = symbol * email.find("@") + email[email.find("@")::]

    def __str__(self):
        return self.email


# print(Email("vania.martynyuck@yandex.ru"))


class Phone:
    def __init__(self, phone_number, symbol="x", k=3):
        self.full_phone_number = phone_number
        n = len(phone_number)
        self.phone_number = ""
        index = n - 1
        while k > 0 and index >= 0:
            if phone_number[index].isdigit():
                self.phone_number = symbol + self.phone_number
                k -= 1
            else:
                self.phone_number = phone_number[index] + self.phone_number
            index -= 1
        self.phone_number = phone_number[:index + 1:] + self.phone_number

    def __str__(self):
        return " ".join(self.phone_number.split())


# print(Phone("8 (916) 320      50-20", k=4))


class Skype:
    def __init__(self, skype, symbol="x"):
        self.full_skype = skype
        start = skype.find("skype:") + 6
        stop = skype.find("?call") if skype.find("?call") > -1 else len(skype)
        print(skype[:start:] + symbol*3 + skype[stop::])


# Skype("skype:alex.maxim")
# Skype("<a href=\"skype:alex.max?call\">skype</a>")
