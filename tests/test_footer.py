import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFooter:

    url = "https://www.jeduka.com/"

    privacy_policy_xpath = "//a[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'privacy policy') or contains(@href,'privacy-policy')]"
    terms_xpath = "//a[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'terms and conditions') or contains(@href,'terms-and-conditions') or contains(@href,'terms')]"
    footer_xpath = "//footer | //div[contains(@class,'footer')] | //section[contains(@class,'footer')] | //*[@id='footer']"
    # Footer has Facebook, X (Twitter), LinkedIn, Pinterest, Instagram — no YouTube, no Newsletter section
    social_media_xpath = "//a[contains(@href,'facebook') or contains(@href,'instagram') or contains(@href,'twitter') or contains(@href,'x.com') or contains(@href,'linkedin') or contains(@href,'pinterest')]"

    # TC36
    def test_footer_visible_with_key_sections(self, driver):
        driver.get(self.url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        footer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.footer_xpath))
        )
        assert footer.is_displayed(), "Footer is not visible"

        privacy_links = driver.find_elements(By.XPATH, self.privacy_policy_xpath)
        assert len(privacy_links) > 0, "Privacy Policy link not found in footer"
        assert privacy_links[0].is_displayed(), "Privacy Policy link is not visible"

        terms_links = driver.find_elements(By.XPATH, self.terms_xpath)
        assert len(terms_links) > 0, "Terms and Conditions link not found in footer"
        assert terms_links[0].is_displayed(), "Terms and Conditions link is not visible"

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
