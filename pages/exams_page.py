from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExamsPage:

    # Each exam is an <h3> heading on the page
    # e.g. <h3>IELTS</h3>, <h3>TOEFL</h3> etc.
    ielts_xpath = "//h3[contains(text(),'IELTS')]"
    toefl_xpath = "//h3[contains(text(),'TOEFL')]"
    gmat_xpath = "//h3[contains(text(),'GMAT')]"
    gre_xpath = "//h3[contains(text(),'GRE')]"
    pte_xpath = "//h3[contains(text(),'PTE')]"
    sat_xpath = "//h3[contains(text(),'SAT')]"
    duolingo_xpath = "//h3[contains(text(),'Duolingo')]"
    usmle_xpath = "//h3[contains(text(),'USMLE')]"

    # IELTS sub-links — <a href="/exams/ielts/...">
    ielts_sublinks_xpath = "//a[contains(@href,'/exams/ielts')]"

    def __init__(self, driver):
        self.driver = driver

    def is_exam_visible(self, exam_name):
        xpath = f"//h3[contains(text(),'{exam_name}')]"
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            return element.is_displayed()
        except:
            return False

    def get_ielts_sublinks(self):
        sublinks = self.driver.find_elements(By.XPATH, self.ielts_sublinks_xpath)
        return [link.get_attribute("href") for link in sublinks if link.get_attribute("href")]
