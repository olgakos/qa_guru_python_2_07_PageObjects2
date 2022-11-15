
class User:
    def __init__(self, *, first_name, last_name, email, gender,
                 phone_number, date_of_birth, subject, hobby, picture,
                 address, state, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.phone_number = phone_number

        self.date_of_birth = date_of_birth

        self.subject = subject
        self.hobby = hobby

        self.picture = picture

        self.address = address
        self.state = state
        self.city = city
