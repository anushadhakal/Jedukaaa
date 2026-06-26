import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFooter:

    url = "https://www.jeduka.com/"

    privacy_policy_xpath = "//footer//a[contains(text(),'Privacy Policy')] | //a[contains(@href,'privacy-policy')]"
    terms_xpath = "//footer//a[contains(text(),'Terms')] | //a[contains(@href,'terms')]"
    newsletter_xpath = "//*[contains(text(),'newsletter') or contains(text(),'Newsletter')]"
    footer_xpath = "//footer | //div[contains(@class,'footer')] | //section[contains(@class,'footer')] | //*[@id='footer']"
    social_media_xpath = "//a[contains(@href,'facebook') or contains(@href,'instagram') or contains(@href,'twitter') or contains(@href,'linkedin') or contains(@href,'youtube')]"

    # TC36
    def test_footer_visible_with_key_sections(self, driver):
        driver.get(self.url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        footer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.footer_xpath))
        )
        assert footer.is_displayed(), "Footer is not visible"

        privacy_link = driver.find_element(By.XPATH, self.privacy_policy_xpath)
        assert privacy_link.is_displayed(), "Privacy Policy link not found in footer"

        terms_link = driver.find_element(By.XPATH, self.terms_xpath)
        assert terms_link.is_displayed(), "Terms and Conditions link not found in footer"

        newsletter = driver.find_element(By.XPATH, self.newsletter_xpath)
        assert newsletter.is_displayed(), "Newsletter section not found in footer"

    # TC37
    def test_footer_social_media_links_valid(self, driver):
        driver.get(self.url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        social_links = driver.find_elements(By.XPATH, self.social_media_xpath)
        assert len(social_links) >= 1, "No social media links found in footer"

        for link in social_links:
            href = link.get_attribute("href")
            assert href and href != "#", f"Social media link has invalid href: {href}"
