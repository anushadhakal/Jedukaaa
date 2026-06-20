import time
import pytest
from pages.register_page import RegisterPage


class TestRegisterPage:

    # TC16
    def test_register_page_loads_with_3_steps(self, driver):
        register = RegisterPage(driver)
        register.open()

        assert "Register" in register.get_title() or "jeduka" in register.get_title(), \
            "Register page title is incorrect"
        assert "register" in register.get_current_url(), \
            "URL does not contain 'register'"

        assert register.is_step1_visible(), "Step 1 (Personal Details) is not visible"
        assert register.is_step2_visible(), "Step 2 (Future Education) is not visible"
        assert register.is_step3_visible(), "Step 3 (Current Education) is not visible"

    # TC17
    def test_gender_radio_buttons_selectable(self, driver):
        register = RegisterPage(driver)
        register.open()

        register.click_male_radio()
        assert register.is_male_radio_selected(), "Male radio button is not selected"

        register.click_female_radio()
        assert register.is_female_radio_selected(), "Female radio button is not selected"
        assert not register.is_male_radio_selected(), "Male should be deselected after clicking Female"

    # TC18
    def test_country_dropdown_and_state_dynamic_update(self, driver):
        register = RegisterPage(driver)
        register.open()

        options = register.get_country_dropdown_options()
        assert len(options) > 1, "Country dropdown has no options"

        register.select_country("Nepal")
        time.sleep(2)

        state_options = register.get_state_dropdown_options()
        assert len(state_options) > 1, "State dropdown did not update after selecting Nepal"

    # TC19
    def test_preferred_country_dropdown_has_major_destinations(self, driver):
        register = RegisterPage(driver)
        register.open()

        options = register.get_preferred_country_options()
        option_text = " ".join(options)

        expected_countries = ["USA", "Canada", "UK", "Australia", "Germany", "France"]
        for country in expected_countries:
            assert country in option_text, f"{country} not found in Preferred Country dropdown"

    # TC20
    def test_preferred_course_dropdown_has_10_categories(self, driver):
        register = RegisterPage(driver)
        register.open()

        options = register.get_preferred_course_options()
        option_text = " ".join(options)

        expected_courses = ["MBA", "Engineering", "IT", "Science", "Arts", "Law", "Medicine"]
        for course in expected_courses:
            assert course in option_text, f"{course} not found in Preferred Course dropdown"

    # TC21
    def test_exam_checkboxes_independently_selectable(self, driver):
        from selenium.webdriver.common.by import By
        register = RegisterPage(driver)
        register.open()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # BUG-004: Exam selection inputs must be checkboxes so that multiple
        # exams can be selected simultaneously.  The site currently uses radio
        # buttons, which allow only one selection at a time.
        exam_label_xpath = (
            "//label[contains(translate(text(),"
            "'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'IELTS')]"
            "//input | "
            "//input[contains(translate(@value,"
            "'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'IELTS') or "
            "contains(translate(@name,"
            "'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'IELTS')]"
        )
        ielts_inputs = driver.find_elements(By.XPATH, exam_label_xpath)
        assert any(el.get_attribute("type") == "checkbox" for el in ielts_inputs), (
            "BUG-004: IELTS exam input is not a checkbox — "
            "the site uses radio buttons instead of checkboxes, "
            "preventing multiple exam selections at once"
        )

        register.click_ielts_checkbox()
        assert register.is_ielts_checked(), "IELTS checkbox is not checked"

        register.click_toefl_checkbox()
        assert register.is_toefl_checked(), "TOEFL checkbox is not checked"

        # Both should remain checked simultaneously
        assert register.is_ielts_checked(), "IELTS became unchecked after selecting TOEFL"
        assert register.is_toefl_checked(), "TOEFL became unchecked"

    # TC22
    def test_form_submission_fails_without_privacy_policy(self, driver):
        register = RegisterPage(driver)
        register.open()

        # Submit without accepting privacy policy
        register.click_submit_without_privacy()
        time.sleep(1)

        # Form should still be on register page (not submitted)
        assert "register" in register.get_current_url(), \
            "Form submitted even though Privacy Policy was not accepted"

    # TC23
    def test_privacy_policy_and_terms_links(self, driver):
        register = RegisterPage(driver)
        register.open()

        register.click_privacy_policy_link()
        time.sleep(2)
        assert "privacy" in driver.current_url.lower(), \
            "Privacy Policy link did not navigate correctly"

        driver.back()
        time.sleep(1)

        register.click_terms_link()
        time.sleep(2)
        assert "terms" in driver.current_url.lower() or "condition" in driver.current_url.lower(), \
            "Terms and Conditions link did not navigate correctly"
