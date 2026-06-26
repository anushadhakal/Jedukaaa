from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CountriesPage:

    country_sections = ["USA", "Canada", "France", "Germany", "Netherlands",
                        "UK", "Australia", "New Zealand", "Switzerland", "Spain"]

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

    def get_h1_text(self):
        h1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.h1_xpath))
        )
        return h1.text

    def is_country_section_visible(self, country_name):
        xpath = f"//*[contains(text(),'{country_name}')]"
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
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
