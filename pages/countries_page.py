from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CountriesPage:

    # Each country card header is ALL CAPS text e.g. "USA", "CANADA"
    # The links inside each card have mixed case e.g. "Study In USA", "Universities In Canada"
    h1_xpath = "//h1"
    university_cards_xpath = "//div[contains(@class,'university')] | //div[contains(@class,'card')] | //article"
    apply_now_button_xpath = "//a[contains(text(),'Apply Now')] | //button[contains(text(),'Apply Now')]"

    def __init__(self, driver):
        self.driver = driver

    def get_h1_text(self):
        h1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.h1_xpath))
        )
        return h1.text

    def is_country_section_visible(self, country_name):
        # Country name appears in link texts e.g. "Study In Canada", "Universities In France"
        # so mixed-case search works even though the card header is ALL CAPS
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

    def get_country_card_links(self, country_name):
        # Returns all links inside a specific country's card
        # e.g. "Study In USA", "Universities In USA" etc.
        xpath = f"//a[contains(text(),'{country_name}')]"
        links = self.driver.find_elements(By.XPATH, xpath)
        return [link.get_attribute("href") for link in links if link.get_attribute("href")]
