from selene import browser, be, have


def test_google_positive(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_google_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('!qwer418*#*@(#(welkrjghtwergkhwelirgoiweuhrgiwuehrg[').press_enter()
    browser.element('[id="botstuff"]').should(have.text('Your search - !qwer418*#*@(#(welkrjghtwergkhwelirgoiweuhrgiwuehrg[ - did not match any documents.'))