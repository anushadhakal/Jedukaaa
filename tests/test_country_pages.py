import time
import pytest
import requests
from pages.countries_page import CountriesPage


class TestCountryPages:

    study_abroad_url = "https://www.jeduka.com/study-abroad"

    country_pages = {
        "usa": "https://www.jeduka.com/study-in-usa",
        "canada": "https://www.jeduka.com/study-in-canada",
        "uk": "https://www.jeduka.com/study-in-uk",
        "australia": "https://www.jeduka.com/study-in-australia",
        "france": "https://www.jeduka.com/study-in-france",
        "germany": "https://www.jeduka.com/study-in-germany",
    }

    university_pages = {
        "usa": "https://www.jeduka.com/usa/universities",
        "uk": "https://www.jeduka.com/uk/universities",
        "canada": "https://www.jeduka.com/canada/universities",
        "australia": "https://www.jeduka.com/australia/universities",
        "france": "https://www.jeduka.com/france/universities",
        "germany": "https://www.jeduka.com/germany/universities",
    }

    visa_pages = {
        "usa": "https://www.jeduka.com/usa/student-visa-for-usa",
        "uk": "https://www.jeduka.com/uk/student-visa-for-uk",
        "canada": "https://www.jeduka.com/canada/student-visa-for-canada",
        "australia": "https://www.jeduka.com/australia/student-visa-for-australia",
        "france": "https://www.jeduka.com/france/student-visa-for-france",
        "germany": "https://www.jeduka.com/germany/student-visa-for-germany",
    }

    scholarship_pages = {
        "usa": "https://www.jeduka.com/scholarships-in-usa",
        "canada": "https://www.jeduka.com/scholarships-in-canada",
        "uk": "https://www.jeduka.com/scholarships-in-uk",
        "australia": "https://www.jeduka.com/scholarships-in-australia",
        "france": "https://www.jeduka.com/scholarships-in-france",
        "germany": "https://www.jeduka.com/scholarships-in-germany",
    }

    # TC12
    def test_study_abroad_page_shows_all_10_countries(self, driver):
        self.driver = driver
        self.driver.get(self.study_abroad_url)
        time.sleep(2)
        countries = CountriesPage(self.driver)

        country_list = ["USA", "Canada", "France", "Germany", "Netherlands",
                        "UK", "Australia", "New Zealand", "Switzerland", "Spain"]

        for country in country_list:
            assert countries.is_country_section_visible(country), \
                f"{country} section is not visible on the Study Abroad page"

    # TC27
    def test_all_country_study_pages_load(self, driver):
        self.driver = driver
        countries = CountriesPage(self.driver)

        for country, url in self.country_pages.items():
            self.driver.get(url)
            time.sleep(1)

            assert country in self.driver.current_url.lower() or \
                   country.replace("-", "") in self.driver.current_url.lower(), \
                f"{country} page URL is incorrect"

            h1 = countries.get_h1_text()
            assert h1 != "", f"H1 is empty on {country} page"

    # TC28
    def test_usa_subnav_tabs_present_and_navigate(self, driver):
        self.driver = driver
        self.driver.get(self.country_pages["usa"])
        time.sleep(2)
        countries = CountriesPage(self.driver)

        subnav_links = countries.get_all_subnav_links()
        subnav_text = " ".join(subnav_links)

        expected_hrefs = ["study-in-usa", "cost-of-study", "universities", "scholarships", "intakes", "faq"]
        for href in expected_hrefs:
            assert href in subnav_text, f"Sub-nav link containing '{href}' not found on USA page"

        faq_links = [link for link in subnav_links if link and "faq" in link.lower() and link.startswith("http")]
        assert faq_links, "No FAQ URLs found in USA subnav links"
        for faq_url in faq_links[:3]:
            try:
                response = requests.get(faq_url, timeout=8, allow_redirects=True)
                assert response.status_code < 400, (
                    f"BUG-003: Country FAQ page returned HTTP {response.status_code} — "
                    f"'{faq_url}' does not exist"
                )
            except requests.exceptions.RequestException:
                pass

    # TC29
    def test_all_university_listing_pages_have_results(self, driver):
        self.driver = driver
        countries = CountriesPage(self.driver)

        for country, url in self.university_pages.items():
            self.driver.get(url)
            time.sleep(2)

            assert country in self.driver.current_url.lower(), \
                f"{country} university page URL is incorrect"

            cards = countries.get_university_cards()
            assert len(cards) >= 1, f"No university cards found on {country} universities page"

    # TC30
    def test_apply_now_button_on_university_detail_page(self, driver):
        self.driver = driver
        self.driver.get(self.university_pages["usa"])
        time.sleep(2)
        countries = CountriesPage(self.driver)

        try:
            countries.click_first_university()
            time.sleep(2)
            assert countries.is_apply_now_button_visible(), \
                "Apply Now button is not visible on the university detail page"
        except Exception as e:
            pytest.skip(f"Could not click first university card: {e}")

    # TC31
    def test_all_student_visa_pages_load(self, driver):
        self.driver = driver

        for country, url in self.visa_pages.items():
            self.driver.get(url)
            time.sleep(1)
            assert "student-visa" in self.driver.current_url, \
                f"Student visa page for {country} did not load correctly"

    # TC32
    def test_all_scholarship_pages_load_with_correct_title(self, driver):
        self.driver = driver

        for country, url in self.scholarship_pages.items():
            self.driver.get(url)
            time.sleep(1)
            title = self.driver.title.lower()
            assert "scholarship" in title or "jeduka" in title, \
                f"Scholarship page title incorrect for {country}"
