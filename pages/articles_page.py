from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ArticlesPage:

    url = "https://www.jeduka.com/articles-updates"

    article_cards_xpath = "//article | //div[contains(@class,'article')] | //div[contains(@class,'card')]//a[contains(@href,'article')]"
    first_article_xpath = "(//article | //div[contains(@class,'article-card')] | //div[contains(@class,'card')]//a)[1]"
    article_h1_xpath = "//h1"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

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
