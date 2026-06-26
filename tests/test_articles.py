import time
from pages.articles_page import ArticlesPage


class TestArticlesPage:

    url = "https://www.jeduka.com/articles-updates"

    # TC25
    def test_articles_page_loads_with_correct_title(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        time.sleep(2)

        assert "articles" in self.driver.current_url.lower(), "URL does not contain 'articles'"
        assert "Article" in self.driver.title or "jeduka" in self.driver.title.lower(), \
            "Articles page title is incorrect"

    # TC26
    def test_articles_page_shows_cards_and_clicking_opens_detail(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        time.sleep(2)
        articles = ArticlesPage(self.driver)

        cards = articles.get_article_cards()
        assert len(cards) >= 1, "No article cards found on the articles listing page"

        articles.click_first_article()
        time.sleep(2)

        h1 = articles.get_article_detail_h1()
        assert h1 != "", "Article detail page has an empty H1 heading"
        assert len(h1) > 3, "Article detail H1 heading is too short"
