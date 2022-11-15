from selene import command
from selene.support.conditions import have
from selene.support.shared.jquery_style import s
from demoqa.utils import files
from demoqa.model.controls import dropdown, date_controls
from demoqa.model.data.user import User


class RegistrationForm():
    def register(self, user: User):
        self.set_first_name(user.first_name)
        self.set_last_name(user.last_name)
        self.set_email(user.email)
        self.set_gender(user.gender)
        self.set_phone_number(user.phone_number)
        self.set_date_of_birth(user.date_of_birth)
        self.set_subject(user.subject)
        self.set_hobby(user.hobby)
        self.set_picture(user.picture)
        self.set_address(user.address)
        self.scroll_to_bottom()
        self.set_state(user.state)
        self.set_city(user.city)
        self.click_submit()

    def set_first_name(self, first_name):
        s('#firstName').type(first_name)
        return self

    def set_last_name(self, last_name):
        s('#lastName').type(last_name)
        return self

    def set_email(self, email):
        s('#userEmail').type(email)
        return self

    def set_gender(self, gender):
        if gender == 'Male':
            s('.custom-control-label[for="gender-radio-1"]').click()
        elif gender == 'Female':
            s('.custom-control-label[for="gender-radio-2"]').click()
        elif gender == 'Other':
            s('.custom-control-label[for="gender-radio-3"]').click()
        return self

    def set_phone_number(self, number):
        s('#userNumber').type(number)
        return self

    def set_date_of_birth(self, date):
        s('#dateOfBirthInput').click()
        date_controls.select_month(date[1])
        date_controls.select_year(date[2])
        date_controls.select_day(date[1], date[0])
        return self

    def set_subject(self, value):
        s('#subjectsInput').type(value).press_enter()
        return self

    def set_hobby(self, hobby):
        if hobby == 'Sports':
            s('.custom-control-label[for="hobbies-checkbox-1"]').click()
        elif hobby == 'Reading':
            s('.custom-control-label[for="hobbies-checkbox-2"]').click()
        elif hobby == 'Music':
            s('.custom-control-label[for="hobbies-checkbox-3"]').click()
        return self

    def set_picture(self, path):
        s('#uploadPicture').send_keys(files.abs_path_from_project_root(path))
        return self

    def set_address(self, address):
        s('#currentAddress').type(address)
        return self

    def set_state(self, value: str):
        dropdown.select(s('#state'), value)
        return self

    def set_city(self, value: str):
        dropdown.select(s('#city'), value)
        return self

    def click_submit(self):
        s('#submit').perform(command.js.click)
        return self

    def scroll_to_bottom(self):
        s('#state').perform(command.js.scroll_into_view)
        return self

    def assert_registered(self, user):
        day = str(user.date_of_birth[0])
        if user.date_of_birth[0] < 10:
            day = '0' + day

        data = [
            ('Student Name', f'{user.first_name} {user.last_name}'),
            ('Student Email', user.email),
            ('Gender', user.gender),
            ('Mobile', user.phone_number),
            ('Date of Birth', f'{day} {user.date_of_birth[1]},{user.date_of_birth[2]}'),
            ('Subjects', user.subject),
            ('Hobbies', user.hobby),
            ('Picture', user.picture),
            ('Address', user.address),
            ('State and City', f'{user.state} {user.city}')
        ]
        rows = s('.modal-content').all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))







