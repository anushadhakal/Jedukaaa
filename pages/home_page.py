from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    # Logo — <a href="/"><img alt="logo"></a>
    logo_xpath = "//img[@alt='logo']"

    # Navbar — <ul><li><a>Country</a></li>...
    navbar_country_xpath = "//nav//a[contains(text(),'Country')]"
    navbar_courses_xpath = "//nav//a[contains(text(),'Courses')]"
    navbar_exam_xpath = "//nav//a[contains(text(),'Exam')]"
    navbar_articles_xpath = "//nav//a[contains(text(),'Articles')]"
    navbar_jeduka_zone_xpath = "//nav//a[contains(text(),'Jeduka Zone')]"
    navbar_student_support_xpath = "//nav//a[contains(text(),'Student Support')]"

    country_dropdown_xpath = "//nav//a[contains(text(),'Country')]"
    exam_dropdown_xpath = "//nav//a[contains(text(),'Exam')]"

    # Search form dropdowns — <select> elements
    search_country_dropdown_xpath = "//select[contains(@name,'country') or contains(@id,'country')]"
    search_course_dropdown_xpath = "//select[./option[text()='Select Course']]"
    search_now_button_xpath = "//button[contains(text(),'Search Now') or contains(text(),'SEARCH NOW')]"

    # Request FREE Advice — <a href="/register.html">Request FREE Advice</a>
    request_free_advice_xpath = "//a[contains(text(),'Request FREE Advice')]"

    # Contact — <a href="https://wa.me/+918347742297"> and <a href="tel:+918347742297">
    whatsapp_icon_xpath = "//a[contains(@href,'wa.me')]"
    phone_number_xpath = "//a[@href='tel:+918347742297']"

    # Search icon
    search_icon_xpath = "//button[@id='submit_google_search']"

    # View All buttons — exact text from page inspection
    explore_countries_xpath = "//a[contains(text(),'Explore Countries')]"
    view_all_countries_xpath = "//a[contains(text(),'View All Countries')]"
    view_all_exams_xpath = "//a[contains(text(),'View All Exams')]"
    view_all_articles_xpath = "//a[contains(text(),'view all articles')]"

    def __init__(self, driver):
        self.driver = driver

    def get_all_navbar_items(self):
        navbar_links = self.driver.find_elements(By.XPATH, "//nav//a | //header//a")
        return [link.text.strip() for link in navbar_links if link.text.strip()]

    def hover_and_check_dropdown(self, dropdown_xpath):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, dropdown_xpath))
        )
        ActionChains(self.driver).move_to_element(element).perform()
        return True

    def click_search_now_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_now_button_xpath))
        )
        button.click()

    def click_request_free_advice(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.request_free_advice_xpath))
        )
        element.click()

    def click_search_icon(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_icon_xpath))
        )
        element.click()

    def _scroll_to_bottom_and_find(self, xpath):
        # Scroll to bottom first to trigger lazy-loaded content, then find element
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return element

    def scroll_and_click_explore_countries(self):
        element = self._scroll_to_bottom_and_find(self.explore_countries_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_and_click_view_all_countries(self):
        element = self._scroll_to_bottom_and_find(self.view_all_countries_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_and_click_view_all_exams(self):
        element = self._scroll_to_bottom_and_find(self.view_all_exams_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_and_click_view_all_articles(self):
        element = self._scroll_to_bottom_and_find(self.view_all_articles_xpath)
        self.driver.execute_script("arguments[0].click();", element)
