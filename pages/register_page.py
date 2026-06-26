from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class RegisterPage:

    # Step headings — exact text visible on page
    step1_heading_xpath = "//*[contains(text(),'Personal Details')]"
    step2_heading_xpath = "//*[contains(text(),'Future Education Prospects')]"
    step3_heading_xpath = "//*[contains(text(),'Current education details')]"

    # Step 1 — Personal Details
    # Using the placeholder text inside the first <option> to uniquely identify each dropdown
    full_name_xpath = "//input[@placeholder='Full Name']"
    email_xpath = "//input[@placeholder='Email Id']"
    mobile_xpath = "//input[@placeholder='Mobile Number']"
    country_dropdown_xpath = "//select[./option[contains(text(),'Country You Are Currently Living In')]]"
    state_dropdown_xpath = "//select[./option[contains(text(),'State You Are Currently Living In')]]"

    # Step 2 — Future Education Prospects
    preferred_country_xpath = "//select[./option[contains(text(),'Preferred Country')]]"
    preferred_course_xpath = "//select[./option[contains(text(),'Preferred Course')]]"

    # Step 3 — Exam Appeared (radio buttons — only one can be selected at a time)
    ielts_radio_xpath = "//label[contains(.,'IELTS')]//input[@type='radio'] | //input[@type='radio' and (@value='IELTS' or @value='ielts')]"
    toefl_radio_xpath = "//label[contains(.,'TOEFL')]//input[@type='radio'] | //input[@type='radio' and (@value='TOEFL' or @value='toefl')]"

    # Privacy checkbox and submit button — exact text from page
    privacy_checkbox_xpath = "//input[@type='checkbox']"
    submit_button_xpath = "//button[contains(translate(text(),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'SUBMIT TO GET CALL BACK')]"
    privacy_policy_link_xpath = "//a[contains(text(),'Privacy Policy')]"
    terms_link_xpath = "//a[contains(text(),'Terms and Conditions')]"

    def __init__(self, driver):
        self.driver = driver

    # ── Step visibility ────────────────────────────────────────────────────────

    def is_step1_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.step1_heading_xpath))
            )
            return True
        except:
            return False

    def is_step2_visible(self):
        try:
            element = self.driver.find_element(By.XPATH, self.step2_heading_xpath)
            return element.is_displayed()
        except:
            return False

    def is_step3_visible(self):
        try:
            element = self.driver.find_element(By.XPATH, self.step3_heading_xpath)
            return element.is_displayed()
        except:
            return False

    # ── Personal Details inputs ────────────────────────────────────────────────

    def enter_full_name(self, name):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.full_name_xpath))
        )
        field.clear()
        field.send_keys(name)

    def enter_email(self, email):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.email_xpath))
        )
        field.clear()
        field.send_keys(email)

    def enter_mobile(self, mobile):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.mobile_xpath))
        )
        field.clear()
        field.send_keys(mobile)

    def click_privacy_checkbox(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.privacy_checkbox_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        self.driver.execute_script("arguments[0].click();", checkbox)

    # ── Country / State dropdowns ──────────────────────────────────────────────

    def get_country_dropdown_options(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.country_dropdown_xpath))
        )
        return [option.text for option in Select(dropdown).options]

    def select_country(self, country_name):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.country_dropdown_xpath))
        )
        Select(dropdown).select_by_visible_text(country_name)

    def get_state_dropdown_options(self):
        import time
        time.sleep(2)
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.state_dropdown_xpath))
        )
        return [option.text for option in Select(dropdown).options]

    # ── Preferred country / course dropdowns ───────────────────────────────────

    def get_preferred_country_options(self):
        try:
            dropdown = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.preferred_country_xpath))
            )
            return [option.text for option in Select(dropdown).options]
        except Exception:
            pass
        study_dests = ['USA', 'United States', 'UK', 'United Kingdom',
                       'Australia', 'Canada', 'Germany', 'France']
        return self.driver.execute_script("""
            var dests = arguments[0];
            var selects = document.querySelectorAll('select');
            for (var s of selects) {
                var opts = Array.from(s.options).map(function(o) { return o.text; });
                var hits = dests.filter(function(d) {
                    return opts.some(function(o) { return o.indexOf(d) !== -1; });
                });
                if (hits.length >= 3) return opts;
            }
            return [];
        """, study_dests) or []

    def get_preferred_course_options(self):
        try:
            dropdown = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.preferred_course_xpath))
            )
            return [option.text for option in Select(dropdown).options]
        except Exception:
            pass
        course_keywords = ['MBA', 'Engineering', 'Medicine', 'Science',
                           'Arts', 'Law', 'IT', 'Computer']
        return self.driver.execute_script("""
            var kw = arguments[0];
            var selects = document.querySelectorAll('select');
            for (var s of selects) {
                var opts = Array.from(s.options).map(function(o) { return o.text; });
                var hits = kw.filter(function(k) {
                    return opts.some(function(o) { return o.indexOf(k) !== -1; });
                });
                if (hits.length >= 3) return opts;
            }
            return [];
        """, course_keywords) or []

    # ── Exam radio buttons ─────────────────────────────────────────────────────

    def click_ielts_radio(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.ielts_radio_xpath))
            )
            element.click()
            return
        except Exception:
            pass
        clicked = self.driver.execute_script("""
            for (var l of document.querySelectorAll('label')) {
                if (l.textContent.toUpperCase().indexOf('IELTS') !== -1) {
                    var r = l.querySelector('input[type="radio"]');
                    if (r) { r.click(); return true; }
                    l.click(); return true;
                }
            }
            for (var r of document.querySelectorAll('input[type="radio"]')) {
                if ((r.value || '').toUpperCase().indexOf('IELTS') !== -1) {
                    r.click(); return true;
                }
            }
            return false;
        """)
        if not clicked:
            raise Exception("IELTS radio button not found on page")

    def click_toefl_radio(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.toefl_radio_xpath))
            )
            element.click()
            return
        except Exception:
            pass
        clicked = self.driver.execute_script("""
            for (var l of document.querySelectorAll('label')) {
                if (l.textContent.toUpperCase().indexOf('TOEFL') !== -1) {
                    var r = l.querySelector('input[type="radio"]');
                    if (r) { r.click(); return true; }
                    l.click(); return true;
                }
            }
            for (var r of document.querySelectorAll('input[type="radio"]')) {
                if ((r.value || '').toUpperCase().indexOf('TOEFL') !== -1) {
                    r.click(); return true;
                }
            }
            return false;
        """)
        if not clicked:
            raise Exception("TOEFL radio button not found on page")

    def is_ielts_selected(self):
        try:
            elements = self.driver.find_elements(By.XPATH, self.ielts_radio_xpath)
            if elements:
                return elements[0].is_selected()
        except Exception:
            pass
        return bool(self.driver.execute_script("""
            for (var l of document.querySelectorAll('label')) {
                if (l.textContent.toUpperCase().indexOf('IELTS') !== -1) {
                    var r = l.querySelector('input[type="radio"]');
                    if (r) return r.checked;
                }
            }
            for (var r of document.querySelectorAll('input[type="radio"]')) {
                if ((r.value || '').toUpperCase().indexOf('IELTS') !== -1) return r.checked;
            }
            return false;
        """))

    def is_toefl_selected(self):
        try:
            elements = self.driver.find_elements(By.XPATH, self.toefl_radio_xpath)
            if elements:
                return elements[0].is_selected()
        except Exception:
            pass
        return bool(self.driver.execute_script("""
            for (var l of document.querySelectorAll('label')) {
                if (l.textContent.toUpperCase().indexOf('TOEFL') !== -1) {
                    var r = l.querySelector('input[type="radio"]');
                    if (r) return r.checked;
                }
            }
            for (var r of document.querySelectorAll('input[type="radio"]')) {
                if ((r.value || '').toUpperCase().indexOf('TOEFL') !== -1) return r.checked;
            }
            return false;
        """))

    # ── Form submission / links ────────────────────────────────────────────────

    def click_submit_without_privacy(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.submit_button_xpath))
        )
        button.click()

    def click_privacy_policy_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.privacy_policy_link_xpath))
        )
        link.click()

    def click_terms_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.terms_link_xpath))
        )
        link.click()
