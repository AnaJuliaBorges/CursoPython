import re

class ValidPhone:
    def __init__(self, telephone):
        if self.valid_telephone(telephone):
            self.number = telephone
        else:
            raise ValueError("Número incorreto!")

    def __str__(self):
        return self.format_number()

    def valid_telephone(self, telephone):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.findall(pattern, telephone)
        if answer:
            return True
        else:
            return False

    def format_number(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.search(pattern, self.number)
        formatted_number = "+{}({}){}-{}".format(
            answer.group(1),
            answer.group(2),
            answer.group(3),
            answer.group(4)
        )
        return formatted_number
