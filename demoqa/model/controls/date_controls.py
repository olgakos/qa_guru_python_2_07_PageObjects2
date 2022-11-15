from selene import command
from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss


def select_month(month):
    s('.react-datepicker__month-select').click()
    ss('.react-datepicker__month-select option').by(have.exact_text(month)).first.click()


def select_year(year):
    s('.react-datepicker__year-select').click()
    element_year = ss('.react-datepicker__year-select option').by(have.exact_text(year)).first
    element_year.perform(command.js.scroll_into_view)
    element_year.click()


def select_day(month, day):
    s(f'[aria-label*="{month} {day}"]').click()


def type_date(date):
    s('#dateOfBirthInput').type(date)
