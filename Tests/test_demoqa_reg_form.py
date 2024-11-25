from selene_in_action_py13.conditions import match
from selene import browser
from selene.support.shared import browser

def test_student_registration_form():
    #----------------
    browser.open('/automation-practice-form')

    #---------------
    browser.element('#firstName').should(match.blank).type('Nastya').press_enter()
