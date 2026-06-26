from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExamsPage:

    ielts_xpath = "//*[contains(text(),'IELTS')]"
    toefl_xpath = "//*[contains(text(),'TOEFL')]"
    gmat_xpath = "//*[contains(text(),'GMAT')]"
    gre_xpath = "//*[contains(text(),'GRE')]"
    pte_xpath = "//*[contains(text(),'PTE')]"
    sat_xpath = "//*[contains(text(),'SAT')]"
    duolingo_xpath = "//*[contains(text(),'Duolingo')]"
    usmle_xpath = "//*[contains(text(),'USMLE')]"

    # IELTS sub-links — <a href="/exams/ielts/...">
    ielts_sublinks_xpath = "//a[contains(@href,'/exams/ielts')]"

    def __init__(self, driver):
        self.driver = driver

    def is_exam_visible(self, exam_name):
        xpath = f"//*[contains(text(),'{exam_name}')]"
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            elements = self.driver.find_elements(By.XPATH, xpath)
            return any(el.is_displayed() for el in elements)
        except:
            return False

    def get_ielts_sublinks(self):
        sublinks = self.driver.find_elements(By.XPATH, self.ielts_sublinks_xpath)
        return [link.get_attribute("href") for link in sublinks if link.get_attribute("href")]
