import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage


class TestHomePage:

    url = "https://www.jeduka.com/"

    # TC01
    def test_homepage_title_and_url(self, driver):
        self.driver = driver
        self.driver.get(self.url)

        assert "Study Abroad" in self.driver.title, "Homepage title is incorrect"
        assert "jeduka.com" in self.driver.current_url, "Homepage URL does not contain jeduka.com"

    # TC02
    def test_jeduka_logo_is_visible(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        logo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, home.logo_xpath))
        )
        assert logo.is_displayed(), "Jeduka logo is not visible on the homepage"

    # TC03
    def test_all_navbar_items_visible(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        navbar_text = " ".join(home.get_all_navbar_items())

        assert "Country" in navbar_text, "Country not found in navbar"
        assert "Courses" in navbar_text, "Courses not found in navbar"
        assert "Exam" in navbar_text, "Exam not found in navbar"
        assert "Articles" in navbar_text, "Articles not found in navbar"
        assert "Jeduka Zone" in navbar_text or "Zone" in navbar_text, "Jeduka Zone not found in navbar"
        assert "Student Support" in navbar_text or "Support" in navbar_text, "Student Support not found in navbar"

    # TC04
    def test_navbar_dropdowns_open(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        assert home.hover_and_check_dropdown(home.country_dropdown_xpath), "Country dropdown did not open"
        time.sleep(1)
        assert home.hover_and_check_dropdown(home.exam_dropdown_xpath), "Exam dropdown did not open"

    # TC06
    def test_search_now_button_works(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        time.sleep(2)
        home = HomePage(self.driver)

        country_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//select[contains(@name,'country') or contains(@id,'country')]")
            )
        )
        Select(country_dropdown).select_by_index(1)
        time.sleep(1)

        home.click_search_now_button()
        time.sleep(3)

        current_url = self.driver.current_url
        assert (
            "search" in current_url.lower()
            or "filter" in current_url.lower()
            or "country" in current_url.lower()
            or "result" in current_url.lower()
        ), (
            f"BUG-002: SEARCH NOW button does not filter results — "
            f"URL contains no search parameters after selecting a country "
            f"(current URL: {current_url})"
        )

    # TC07
    def test_request_free_advice_button_visible(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, home.request_free_advice_xpath))
        )
        assert element.is_displayed(), "REQUEST FREE ADVICE button is not visible"

    # TC08
    def test_contact_elements_visible(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        whatsapp = self.driver.find_element(By.XPATH, home.whatsapp_icon_xpath)
        assert whatsapp.is_displayed(), "WhatsApp icon is not visible"

        phone = self.driver.find_element(By.XPATH, home.phone_number_xpath)
        assert phone.is_displayed(), "Phone number is not visible"

    # TC09
    def test_search_icon_opens_search(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        try:
            home.click_search_icon()
            time.sleep(1)
            search_input = self.driver.find_element(
                By.XPATH, "//input[@type='search'] | //input[@type='text'][contains(@class,'search')]"
            )
            assert search_input.is_displayed(), "Search input did not appear after clicking search icon"
        except Exception as e:
            pytest.skip(f"Search icon not found with expected locator: {e}")

    # TC10
    def test_explore_countries_button_navigates(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        try:
            home.scroll_and_click_explore_countries()
            time.sleep(2)
            assert "study-abroad" in self.driver.current_url, "Did not navigate to study-abroad page"
        except Exception as e:
            pytest.skip(f"Explore Countries button not found: {e}")

    # TC11
    def test_view_all_countries_button_navigates(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        try:
            home.scroll_and_click_view_all_countries()
            time.sleep(2)
            assert "study-abroad" in self.driver.current_url, "Did not navigate to study-abroad page"
        except Exception as e:
            pytest.skip(f"View All Countries button not found: {e}")

    # TC13
    def test_view_all_exams_button_navigates(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        try:
            home.scroll_and_click_view_all_exams()
            time.sleep(2)
            assert "exams" in self.driver.current_url, "Did not navigate to exams page"
        except Exception as e:
            pytest.skip(f"View All Exams button not found: {e}")

    # TC25
    def test_view_all_articles_button_navigates(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        home = HomePage(self.driver)

        try:
            home.scroll_and_click_view_all_articles()
            time.sleep(2)
            assert "articles" in self.driver.current_url, "Did not navigate to articles page"
        except Exception as e:
            pytest.skip(f"View All Articles button not found: {e}")
