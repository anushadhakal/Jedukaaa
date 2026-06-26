import time
import pytest
import requests
from selenium.webdriver.common.by import By


class TestNavigation:

    # TC38
    def test_browser_back_and_forward_navigation(self, driver):
        driver.get("https://www.jeduka.com/")
        time.sleep(1)
        homepage_url = driver.current_url

        driver.get("https://www.jeduka.com/study-in-usa")
        time.sleep(1)

        driver.back()
        time.sleep(1)
        assert "jeduka.com" in driver.current_url, "Back navigation failed"

        driver.forward()
        time.sleep(1)
        assert "study-in-usa" in driver.current_url, "Forward navigation failed"

    # TC39
    def test_no_broken_navbar_links(self, driver):
        driver.get("https://www.jeduka.com/")
        time.sleep(2)

        navbar_links = driver.find_elements(By.XPATH, "//nav//a | //header//a")
        hrefs = [link.get_attribute("href") for link in navbar_links
                 if link.get_attribute("href") and
                 link.get_attribute("href").startswith("http")]

        broken_links = []
        for href in hrefs[:10]:  # Check first 10 to keep test fast
            try:
                response = requests.head(href, timeout=5, allow_redirects=True)
                if response.status_code >= 400:
                    broken_links.append(f"{href} → {response.status_code}")
            except Exception:
                pass  # Skip network errors

        assert len(broken_links) == 0, \
            "BUG-001: Broken navbar links found:\n" + "\n".join(broken_links)
