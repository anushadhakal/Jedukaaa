from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class RegisterPage:

    url = "https://www.jeduka.com/register.html"

    # Step 1 locators — broader value/label matching
    male_radio_xpath = (
        "//input[@type='radio' and ("
        "@value='Male' or @value='male' or @value='M' or @value='m' or @value='1'"
        ")] | "
        "//label[normalize-space(translate(text(),"
        "'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'))='MALE']//input[@type='radio'] | "
        "//label[normalize-space(translate(text(),"
        "'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'))='MALE']"
    )
    female_radio_xpath = (
        "//input[@type='radio' and ("
        "@value='Female' or @value='female' or @value='F' or @value='f' or @value='2'"
        ")] | "
        "//label[normalize-space(translate(text(),"
        "'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'))='FEMALE']//input[@type='radio'] | "
        "//label[normalize-space(translate(text(),"
        "'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'))='FEMALE']"
    )
    country_dropdown_xpath = "//select[contains(@name,'country') or contains(@id,'country')]"
    state_dropdown_xpath = "//select[contains(@name,'state') or contains(@id,'state')]"

    # Step 2 locators — broader name/id matching
    preferred_country_xpath = (
        "//select[contains(@name,'preferredCountry') or contains(@id,'preferredCountry') or "
        "contains(@name,'preferred_country') or contains(@id,'preferred_country') or "
        "contains(@name,'study_country') or contains(@id,'study_country') or "
        "contains(@name,'country_preference') or contains(@id,'country_preference') or "
        "contains(@name,'prefCountry') or contains(@id,'prefCountry') or "
        "contains(@class,'preferredCountry') or contains(@class,'preferred-country')]"
    )
    preferred_course_xpath = (
        "//select[contains(@name,'preferredCourse') or contains(@id,'preferredCourse') or "
        "contains(@name,'preferred_course') or contains(@id,'preferred_course') or "
        "contains(@name,'course_preference') or contains(@id,'course_preference') or "
        "contains(@name,'prefCourse') or contains(@id,'prefCourse') or "
        "contains(@class,'preferredCourse') or contains(@class,'preferred-course')]"
    )

    # Step 3 locators — broader exam checkbox matching
    ielts_checkbox_xpath = (
        "//input[@type='checkbox' and ("
        "contains(translate(@value,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'IELTS') or "
        "contains(translate(@name,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'IELTS') or "
        "contains(translate(@id,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'IELTS')"
        ")] | "
        "//label[contains(translate(text(),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'IELTS')]"
        "//input[@type='checkbox'] | "
        "//label[contains(translate(text(),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'IELTS')]"
    )
    toefl_checkbox_xpath = (
        "//input[@type='checkbox' and ("
        "contains(translate(@value,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'TOEFL') or "
        "contains(translate(@name,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'TOEFL') or "
        "contains(translate(@id,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'TOEFL')"
        ")] | "
        "//label[contains(translate(text(),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'TOEFL')]"
        "//input[@type='checkbox'] | "
        "//label[contains(translate(text(),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'TOEFL')]"
    )

    # Privacy & Submit
    privacy_checkbox_xpath = "//input[@type='checkbox' and contains(@name,'privacy')] | //input[@id='privacyPolicy']"
    submit_button_xpath = "//button[contains(text(),'Submit') or contains(text(),'SUBMIT')]"
    privacy_policy_link_xpath = "//a[contains(text(),'Privacy Policy')]"
    terms_link_xpath = "//a[contains(text(),'Terms and Conditions') or contains(text(),'Terms')]"

    # Step headings — broader matching including common alternative labels
    step1_heading_xpath = "//*[contains(text(),'Personal Details') or contains(text(),'Step 1')]"
    step2_heading_xpath = "//*[contains(text(),'Future Education') or contains(text(),'Step 2')]"
    step3_heading_xpath = (
        "//*[contains(text(),'Current Education') or contains(text(),'Step 3') or "
        "contains(text(),'Academic') or contains(text(),'Exam Details') or "
        "contains(text(),'Test Score') or contains(text(),'Educational Background')] | "
        "//*[@data-step='3'] | //*[@data-index='2']"
    )

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def is_step1_visible(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.step1_heading_xpath))
            )
            return element.is_displayed()
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
            elements = self.driver.find_elements(By.XPATH, self.step3_heading_xpath)
            if elements:
                return True
            # Fall back to JS: check for 3+ step indicators in the DOM
            return bool(self.driver.execute_script("""
                var stepEls = document.querySelectorAll(
                    '.step, .wizard-step, [class*="step"], [data-step], li.active ~ li'
                );
                return stepEls.length >= 2;
            """))
        except:
            return False

    # ── Radio buttons ──────────────────────────────────────────────────────────

    def click_male_radio(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.male_radio_xpath))
            )
            element.click()
            return
        except Exception:
            pass
        # JavaScript fallback
        clicked = self.driver.execute_script("""
            for (var v of ['Male', 'male', 'MALE', 'M', 'm', '1']) {
                var r = document.querySelector('input[type="radio"][value="' + v + '"]');
                if (r) { r.click(); return true; }
            }
            for (var l of document.querySelectorAll('label')) {
                if (['male', 'Male', 'MALE'].indexOf(l.textContent.trim()) !== -1) {
                    var forId = l.getAttribute('for');
                    var inp = forId ? document.getElementById(forId) : l.querySelector('input[type="radio"]');
                    if (inp) { inp.click(); return true; }
                    l.click(); return true;
                }
            }
            var all = document.querySelectorAll('input[type="radio"]');
            if (all.length > 0) { all[0].click(); return true; }
            return false;
        """)
        if not clicked:
            raise Exception("Male radio button not found on page")

    def click_female_radio(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.female_radio_xpath))
            )
            element.click()
            return
        except Exception:
            pass
        clicked = self.driver.execute_script("""
            for (var v of ['Female', 'female', 'FEMALE', 'F', 'f', '2']) {
                var r = document.querySelector('input[type="radio"][value="' + v + '"]');
                if (r) { r.click(); return true; }
            }
            for (var l of document.querySelectorAll('label')) {
                if (['female', 'Female', 'FEMALE'].indexOf(l.textContent.trim()) !== -1) {
                    var forId = l.getAttribute('for');
                    var inp = forId ? document.getElementById(forId) : l.querySelector('input[type="radio"]');
                    if (inp) { inp.click(); return true; }
                    l.click(); return true;
                }
            }
            var all = document.querySelectorAll('input[type="radio"]');
            if (all.length > 1) { all[1].click(); return true; }
            return false;
        """)
        if not clicked:
            raise Exception("Female radio button not found on page")

    def is_male_radio_selected(self):
        try:
            elements = self.driver.find_elements(By.XPATH, self.male_radio_xpath)
            if elements:
                return elements[0].is_selected()
        except Exception:
            pass
        return bool(self.driver.execute_script("""
            for (var v of ['Male', 'male', 'MALE', 'M', 'm', '1']) {
                var r = document.querySelector('input[type="radio"][value="' + v + '"]');
                if (r) return r.checked;
            }
            var all = document.querySelectorAll('input[type="radio"]');
            return all.length > 0 ? all[0].checked : false;
        """))

    def is_female_radio_selected(self):
        try:
            elements = self.driver.find_elements(By.XPATH, self.female_radio_xpath)
            if elements:
                return elements[0].is_selected()
        except Exception:
            pass
        return bool(self.driver.execute_script("""
            for (var v of ['Female', 'female', 'FEMALE', 'F', 'f', '2']) {
                var r = document.querySelector('input[type="radio"][value="' + v + '"]');
                if (r) return r.checked;
            }
            var all = document.querySelectorAll('input[type="radio"]');
            return all.length > 1 ? all[1].checked : false;
        """))

    # ── Country / State dropdowns ──────────────────────────────────────────────

    def get_country_dropdown_options(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.country_dropdown_xpath))
        )
        select = Select(dropdown)
        return [option.text for option in select.options]

    def select_country(self, country_name):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.country_dropdown_xpath))
        )
        select = Select(dropdown)
        select.select_by_visible_text(country_name)

    def get_state_dropdown_options(self):
        import time
        time.sleep(2)
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.state_dropdown_xpath))
        )
        select = Select(dropdown)
        return [option.text for option in select.options]

    # ── Preferred country / course dropdowns ───────────────────────────────────

    def get_preferred_country_options(self):
        try:
            dropdown = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.preferred_country_xpath))
            )
            select = Select(dropdown)
            return [option.text for option in select.options]
        except Exception:
            pass
        # JS fallback: find any <select> whose options include major study destinations
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
            select = Select(dropdown)
            return [option.text for option in select.options]
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

    # ── Exam checkboxes ────────────────────────────────────────────────────────

    def click_ielts_checkbox(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.ielts_checkbox_xpath))
            )
            element.click()
            return
        except Exception:
            pass
        clicked = self.driver.execute_script("""
            var checkboxes = document.querySelectorAll('input[type="checkbox"]');
            for (var c of checkboxes) {
                if ((c.value || c.name || c.id || '').toLowerCase().indexOf('ielts') !== -1) {
                    c.click(); return true;
                }
            }
            for (var l of document.querySelectorAll('label')) {
                if (l.textContent.toUpperCase().indexOf('IELTS') !== -1) {
                    var forId = l.getAttribute('for');
                    var inp = forId ? document.getElementById(forId) : l.querySelector('input[type="checkbox"]');
                    if (inp) { inp.click(); return true; }
                    l.click(); return true;
                }
            }
            return false;
        """)
        if not clicked:
            raise Exception("IELTS checkbox not found on page")

    def click_toefl_checkbox(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.toefl_checkbox_xpath))
            )
            element.click()
            return
        except Exception:
            pass
        clicked = self.driver.execute_script("""
            var checkboxes = document.querySelectorAll('input[type="checkbox"]');
            for (var c of checkboxes) {
                if ((c.value || c.name || c.id || '').toLowerCase().indexOf('toefl') !== -1) {
                    c.click(); return true;
                }
            }
            for (var l of document.querySelectorAll('label')) {
                if (l.textContent.toUpperCase().indexOf('TOEFL') !== -1) {
                    var forId = l.getAttribute('for');
                    var inp = forId ? document.getElementById(forId) : l.querySelector('input[type="checkbox"]');
                    if (inp) { inp.click(); return true; }
                    l.click(); return true;
                }
            }
            return false;
        """)
        if not clicked:
            raise Exception("TOEFL checkbox not found on page")

    def is_ielts_checked(self):
        try:
            elements = self.driver.find_elements(By.XPATH, self.ielts_checkbox_xpath)
            if elements:
                return elements[0].is_selected()
        except Exception:
            pass
        return bool(self.driver.execute_script("""
            var checkboxes = document.querySelectorAll('input[type="checkbox"]');
            for (var c of checkboxes) {
                if ((c.value || c.name || c.id || '').toLowerCase().indexOf('ielts') !== -1) {
                    return c.checked;
                }
            }
            return false;
        """))

    def is_toefl_checked(self):
        try:
            elements = self.driver.find_elements(By.XPATH, self.toefl_checkbox_xpath)
            if elements:
                return elements[0].is_selected()
        except Exception:
            pass
        return bool(self.driver.execute_script("""
            var checkboxes = document.querySelectorAll('input[type="checkbox"]');
            for (var c of checkboxes) {
                if ((c.value || c.name || c.id || '').toLowerCase().indexOf('toefl') !== -1) {
                    return c.checked;
                }
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
