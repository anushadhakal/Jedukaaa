from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ArticlesPage:

    article_cards_xpath = "//a[contains(@href,'/articles-updates/')]"
    article_h1_xpath = "//h1"

    def __init__(self, driver):
        self.driver = driver

    def get_article_cards(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.article_cards_xpath))
        )
        return self.driver.find_elements(By.XPATH, self.article_cards_xpath)

    def click_first_article(self):
        cards = self.get_article_cards()
        if cards:
            cards[0].click()

    def get_article_detail_h1(self):
        h1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.article_h1_xpath))
        )
        return h1.text
