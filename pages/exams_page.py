from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExamsPage:

    url = "https://www.jeduka.com/exams"

    # Exam card locators
    ielts_xpath = "//*[contains(text(),'IELTS')]"
    toefl_xpath = "//*[contains(text(),'TOEFL')]"
    gmat_xpath = "//*[contains(text(),'GMAT')]"
    gre_xpath = "//*[contains(text(),'GRE')]"
    pte_xpath = "//*[contains(text(),'PTE')]"
    sat_xpath = "//*[contains(text(),'SAT')]"
    duolingo_xpath = "//*[contains(text(),'Duolingo')]"
    usmle_xpath = "//*[contains(text(),'USMLE')]"

    # IELTS sub-links
    ielts_about_xpath = "//a[contains(@href,'ielts') and contains(text(),'About')]"
    ielts_syllabus_xpath = "//a[contains(@href,'ielts') and (contains(text(),'Syllabus') or contains(@href,'syllabus'))]"
    ielts_pattern_xpath = "//a[contains(@href,'ielts') and (contains(text(),'Pattern') or contains(@href,'pattern'))]"
    ielts_preparation_xpath = "//a[contains(@href,'ielts') and (contains(text(),'Preparation') or contains(@href,'preparation'))]"
    ielts_registration_xpath = "//a[contains(@href,'ielts') and (contains(text(),'Registration') or contains(@href,'registration'))]"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def is_exam_visible(self, exam_name):
        try:
            xpath = f"//*[contains(text(),'{exam_name}')]"
            elements = self.driver.find_elements(By.XPATH, xpath)
            if elements:
                return any(el.is_displayed() for el in elements)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            elements = self.driver.find_elements(By.XPATH, xpath)
            return any(el.is_displayed() for el in elements)
        except:
            return False

    def get_ielts_sublinks(self):
        sublinks = self.driver.find_elements(By.XPATH, "//a[contains(@href,'ielts')]")
        return [link.get_attribute("href") for link in sublinks if link.get_attribute("href")]

    def navigate_to_exam_page(self, exam_slug):
        self.driver.get(f"https://www.jeduka.com/exams/{exam_slug}")

    def navigate_to_ielts_subpage(self, subpage_slug):
        self.driver.get(f"https://www.jeduka.com/exams/ielts/{subpage_slug}")
