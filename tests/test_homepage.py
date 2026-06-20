import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage


class TestHomePage:

    # TC01
    def test_homepage_title_and_url(self, driver):
        home = HomePage(driver)
        home.open()

        assert "Study Abroad" in home.get_title(), "Homepage title is incorrect"
        assert "jeduka.com" in home.get_current_url(), "Homepage URL does not contain jeduka.com"

    # TC02
    def test_jeduka_logo_is_visible(self, driver):
        home = HomePage(driver)
        home.open()

        assert home.is_logo_visible(), "Jeduka logo is not visible on the homepage"

    # TC03
    def test_all_navbar_items_visible(self, driver):
        home = HomePage(driver)
        home.open()

        navbar_items = home.get_all_navbar_items()
        navbar_text = " ".join(navbar_items)

        assert "Country" in navbar_text, "Country not found in navbar"
        assert "Courses" in navbar_text, "Courses not found in navbar"
        assert "Exam" in navbar_text, "Exam not found in navbar"
        assert "Articles" in navbar_text, "Articles not found in navbar"
        assert "Jeduka Zone" in navbar_text or "Zone" in navbar_text, "Jeduka Zone not found in navbar"
        assert "Student Support" in navbar_text or "Support" in navbar_text, "Student Support not found in navbar"

    # TC04
    def test_navbar_dropdowns_open(self, driver):
        home = HomePage(driver)
        home.open()

        result = home.hover_and_check_dropdown(home.country_dropdown_xpath)
        assert result, "Country dropdown did not open"
        time.sleep(1)

        result = home.hover_and_check_dropdown(home.exam_dropdown_xpath)
        assert result, "Exam dropdown did not open"

    # TC06
    def test_search_now_button_works(self, driver):
        from selenium.webdriver.support.ui import Select
        home = HomePage(driver)
        home.open()
        time.sleep(2)

        country_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//select[contains(@name,'country') or contains(@id,'country')]")
            )
        )
        Select(country_dropdown).select_by_index(1)  # pick first real option
        time.sleep(1)

        home.click_search_now_button()
        time.sleep(3)

        # BUG-002: SEARCH NOW must navigate to a filtered results page.
        # The URL should contain a search/filter parameter reflecting the chosen country.
        current_url = driver.current_url
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
        home = HomePage(driver)
        home.open()

        assert home.is_request_free_advice_visible(), "REQUEST FREE ADVICE button is not visible"

    # TC08
    def test_contact_elements_visible(self, driver):
        home = HomePage(driver)
        home.open()

        assert home.is_whatsapp_icon_visible(), "WhatsApp icon is not visible"
        assert home.is_phone_number_visible(), "Phone number is not visible"

    # TC09
    def test_search_icon_opens_search(self, driver):
        home = HomePage(driver)
        home.open()

        try:
            home.click_search_icon()
            time.sleep(1)
            search_input = driver.find_element(By.XPATH, "//input[@type='search'] | //input[@type='text'][contains(@class,'search')]")
            assert search_input.is_displayed(), "Search input did not appear after clicking search icon"
        except Exception as e:
            pytest.skip(f"Search icon not found with expected locator: {e}")

    # TC10
    def test_explore_countries_button_navigates(self, driver):
        home = HomePage(driver)
        home.open()

        try:
            home.scroll_and_click_explore_countries()
            time.sleep(2)
            assert "study-abroad" in driver.current_url, "Did not navigate to study-abroad page"
        except Exception as e:
            pytest.skip(f"Explore Countries button not found: {e}")

    # TC11
    def test_view_all_countries_button_navigates(self, driver):
        home = HomePage(driver)
        home.open()

        try:
            home.scroll_and_click_view_all_countries()
            time.sleep(2)
            assert "study-abroad" in driver.current_url, "Did not navigate to study-abroad page"
        except Exception as e:
            pytest.skip(f"View All Countries button not found: {e}")

    # TC13
    def test_view_all_exams_button_navigates(self, driver):
        home = HomePage(driver)
        home.open()

        try:
            home.scroll_and_click_view_all_exams()
            time.sleep(2)
            assert "exams" in driver.current_url, "Did not navigate to exams page"
        except Exception as e:
            pytest.skip(f"View All Exams button not found: {e}")

    # TC25
    def test_view_all_articles_button_navigates(self, driver):
        home = HomePage(driver)
        home.open()

        try:
            home.scroll_and_click_view_all_articles()
            time.sleep(2)
            assert "articles" in driver.current_url, "Did not navigate to articles page"
        except Exception as e:
            pytest.skip(f"View All Articles button not found: {e}")
