from selene import browser, have
import resource


class PracticeFormPage:

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_checkbox(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def fill_foto(self, file):
        browser.element('#uploadPicture').set_value(resource.path(file))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def fill_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def successful_authentication(self, text):
        browser.element('#example-modal-sizes-title-lg').should(
            have.text(
                f'{text}'
            )
        )

    def registered_user_data(self, fio, email,
                             gender, phone, birthday, subjects,
                             hobbies, photo, street,
                             state_and_city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{fio}',
            f'{email}',
            f'{gender}',
            f'{phone}',
            f'{birthday}',
            f'{subjects}',
            f'{hobbies}',
            f'{photo}',
            f'{street}',
            f'{state_and_city}'
        ))
