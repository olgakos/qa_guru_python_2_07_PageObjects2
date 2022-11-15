from demoqa.model import app
from demoqa.model.data.user import User


def test_submit_student_details(open_and_quit_browser_automation_practice_form):
    olga = User(
        first_name='Olga',
        last_name='Kos',
        email='test@test.test',
        gender='Female',
        phone_number='0123456789', #10!
        date_of_birth=[10, 'January', '2000'],
        subject='Arts',
        #subject='Arts', 'English',
        hobby='Music',
        #hobby='Sports', 'Music',
        picture='siegfriedsassoon.jpg',
        address='Peterburg, Moskowsky 16',
        state='Haryana',
        city='Karnal'
    )

#бизнес-шаг: заполнить форму данными
    app.registration_form.register(olga)

# бизнес-шаг: проверить форму
    app.registration_form.assert_registered(olga)