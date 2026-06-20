from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CountriesPage:

    study_abroad_url = "https://www.jeduka.com/study-abroad"

    country_pages = {
        "usa": "https://www.jeduka.com/study-in-usa",
        "canada": "https://www.jeduka.com/study-in-canada",
        "uk": "https://www.jeduka.com/study-in-uk",
        "australia": "https://www.jeduka.com/study-in-australia",
        "france": "https://www.jeduka.com/study-in-france",
        "germany": "https://www.jeduka.com/study-in-germany",
    }

    university_pages = {
        "usa": "https://www.jeduka.com/usa/universities",
        "uk": "https://www.jeduka.com/uk/universities",
        "canada": "https://www.jeduka.com/canada/universities",
        "australia": "https://www.jeduka.com/australia/universities",
        "france": "https://www.jeduka.com/france/universities",
        "germany": "https://www.jeduka.com/germany/universities",
    }

    visa_pages = {
        "usa": "https://www.jeduka.com/usa/student-visa-for-usa",
        "uk": "https://www.jeduka.com/uk/student-visa-for-uk",
        "canada": "https://www.jeduka.com/canada/student-visa-for-canada",
        "australia": "https://www.jeduka.com/australia/student-visa-for-australia",
        "france": "https://www.jeduka.com/france/student-visa-for-france",
        "germany": "https://www.jeduka.com/germany/student-visa-for-germany",
    }

    scholarship_pages = {
        "usa": "https://www.jeduka.com/scholarships-in-usa",
        "canada": "https://www.jeduka.com/scholarships-in-canada",
        "uk": "https://www.jeduka.com/scholarships-in-uk",
        "australia": "https://www.jeduka.com/scholarships-in-australia",
        "france": "https://www.jeduka.com/scholarships-in-france",
        "germany": "https://www.jeduka.com/scholarships-in-germany",
    }

    # Study Abroad page country sections
    country_sections = ["USA", "Canada", "France", "Germany", "Netherlands",
                        "UK", "Australia", "New Zealand", "Switzerland", "Spain"]

    # USA sub-nav tabs
    usa_subnav_create_user_xpath = "//a[contains(@href,'study-in-usa') and contains(text(),'Study in USA')]"
    usa_subnav_cost_xpath = "//a[contains(@href,'cost-of-study-in-usa')]"
    usa_subnav_universities_xpath = "//a[contains(@href,'usa/universities')]"
    usa_subnav_scholarships_xpath = "//a[contains(@href,'scholarships-in-usa')]"
    usa_subnav_intakes_xpath = "//a[contains(@href,'intakes-in-usa')]"
    usa_subnav_faq_xpath = "//a[contains(@href,'faq-usa')]"

    university_cards_xpath = "//div[contains(@class,'university')] | //div[contains(@class,'card')] | //article"
    apply_now_button_xpath = "//a[contains(text(),'Apply Now')] | //button[contains(text(),'Apply Now')]"
    h1_xpath = "//h1"

    def __init__(self, driver):
        self.driver = driver

    def open_study_abroad(self):
        self.driver.get(self.study_abroad_url)

    def open_country_page(self, country):
        self.driver.get(self.country_pages[country])

    def open_university_page(self, country):
        self.driver.get(self.university_pages[country])

    def open_visa_page(self, country):
        self.driver.get(self.visa_pages[country])

    def open_scholarship_page(self, country):
        self.driver.get(self.scholarship_pages[country])

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def get_h1_text(self):
        h1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.h1_xpath))
        )
        return h1.text

    def is_country_section_visible(self, country_name):
        try:
            xpath = f"//*[contains(text(),'{country_name}')]"
            elements = self.driver.find_elements(By.XPATH, xpath)
            if elements:
                return any(el.is_displayed() for el in elements)
            # Wait briefly for dynamic content then retry
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            elements = self.driver.find_elements(By.XPATH, xpath)
            return any(el.is_displayed() for el in elements)
        except:
            return False

    def get_university_cards(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.university_cards_xpath))
        )
        return self.driver.find_elements(By.XPATH, self.university_cards_xpath)

    def click_first_university(self):
        cards = self.get_university_cards()
        if cards:
            cards[0].click()

    def is_apply_now_button_visible(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.apply_now_button_xpath))
            )
            return element.is_displayed()
        except:
            return False

    def get_all_subnav_links(self):
        links = self.driver.find_elements(By.XPATH, "//nav//a | //ul[contains(@class,'sub')]//a")
        return [link.get_attribute("href") for link in links if link.get_attribute("href")]
