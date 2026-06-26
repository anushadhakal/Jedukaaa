import time
from pages.register_page import RegisterPage


class TestRegisterPage:

    url = "https://www.jeduka.com/register.html"

    # TC16
    def test_register_page_loads_with_3_steps(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        register = RegisterPage(self.driver)

        assert "Register" in self.driver.title or "jeduka" in self.driver.title, \
            "Register page title is incorrect"
        assert "register" in self.driver.current_url, \
            "URL does not contain 'register'"

        assert register.is_step1_visible(), "Step 1 (Personal Details) is not visible"
        assert register.is_step2_visible(), "Step 2 (Future Education Prospects) is not visible"
        assert register.is_step3_visible(), "Step 3 (Current education details) is not visible"

    # TC18
    def test_country_dropdown_and_state_dynamic_update(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        register = RegisterPage(self.driver)

        options = register.get_country_dropdown_options()
        assert len(options) > 1, "Country dropdown has no options"

        register.select_country("Nepal")
        time.sleep(2)

        state_options = register.get_state_dropdown_options()
        assert len(state_options) > 1, "State dropdown did not update after selecting Nepal"

    # TC19
    def test_preferred_country_dropdown_has_major_destinations(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        register = RegisterPage(self.driver)

        option_text = " ".join(register.get_preferred_country_options())

        expected_countries = ["USA", "Canada", "UK", "Australia", "Germany", "France"]
        for country in expected_countries:
            assert country in option_text, f"{country} not found in Preferred Country dropdown"

    # TC20
    def test_preferred_course_dropdown_has_categories(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        register = RegisterPage(self.driver)

        option_text = " ".join(register.get_preferred_course_options())

        expected_courses = ["MBA", "Engineering", "IT", "Science", "Arts", "Law", "Medicine"]
        for course in expected_courses:
            assert course in option_text, f"{course} not found in Preferred Course dropdown"

    # TC21
    def test_exam_radio_buttons_selectable(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        register = RegisterPage(self.driver)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        register.click_ielts_radio()
        assert register.is_ielts_selected(), "IELTS radio button is not selected"

        # Selecting TOEFL should deselect IELTS (radio button behaviour — only one allowed)
        register.click_toefl_radio()
        assert register.is_toefl_selected(), "TOEFL radio button is not selected"
        assert not register.is_ielts_selected(), \
            "IELTS should be deselected after selecting TOEFL (radio buttons allow only one selection)"

    # TC_SUBMIT
    def test_valid_form_submission_leads_to_success(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        register = RegisterPage(self.driver)

        # Step 1 — fill personal details
        register.enter_full_name("Test User")
        register.enter_email("testuser@example.com")
        register.enter_mobile("9876543210")
        register.select_country("India")
        time.sleep(2)  # wait for state dropdown to populate

        # Step 3 — accept privacy (scrollIntoView handled inside the method) and submit
        register.click_privacy_checkbox()
        register.click_submit_without_privacy()
        time.sleep(3)

        # After successful submission the page should leave register.html
        # OR show a thank you / success message
        submitted = (
            "register" not in self.driver.current_url
            or "thank" in self.driver.page_source.lower()
            or "success" in self.driver.page_source.lower()
            or "submitted" in self.driver.page_source.lower()
        )
        assert submitted, "Form submission failed — no success message or page change detected"

    # TC22
    def test_form_submission_fails_without_privacy_policy(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        register = RegisterPage(self.driver)

        register.click_submit_without_privacy()
        time.sleep(1)

        assert "register" in self.driver.current_url, \
            "Form submitted even though Privacy Policy was not accepted"

    # TC23
    def test_privacy_policy_and_terms_links(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        register = RegisterPage(self.driver)

        register.click_privacy_policy_link()
        time.sleep(2)
        assert "privacy" in self.driver.current_url.lower(), \
            "Privacy Policy link did not navigate correctly"

        self.driver.back()
        time.sleep(1)

        register.click_terms_link()
        time.sleep(2)
        assert "terms" in self.driver.current_url.lower() or "condition" in self.driver.current_url.lower(), \
            "Terms and Conditions link did not navigate correctly"
