from datetime import datetime

class DatasBr:
    def __init__(self):
        self.registration_moment = datetime.today()

    def __str__(self):
        return self.format_date()

    def format_date(self):
        formatted_date = self.registration_moment.strftime("%d/%m/%Y %H:%M")
        return formatted_date

    def registration_moment_difference(self):
        registration_moment = datetime.today() - self.registration_moment
        print(registration_moment)
