from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:

    url = "https://www.jeduka.com/"

    # Locators
    logo_xpath = "//a[contains(@class,'logo') or contains(@href,'/')]//img"
    navbar_country_xpath = "//nav//a[contains(text(),'Country')]"
    navbar_courses_xpath = "//nav//a[contains(text(),'Courses')]"
    navbar_exam_xpath = "//nav//a[contains(text(),'Exam')]"
    navbar_articles_xpath = "//nav//a[contains(text(),'Articles')]"
    navbar_jeduka_zone_xpath = "//nav//a[contains(text(),'Jeduka Zone')]"
    navbar_student_support_xpath = "//nav//a[contains(text(),'Student Support')]"

    country_dropdown_xpath = "//a[contains(text(),'Country')]"
    courses_dropdown_xpath = "//a[contains(text(),'Courses')]"
    exam_dropdown_xpath = "//a[contains(text(),'Exam')]"
    articles_dropdown_xpath = "//a[contains(text(),'Articles')]"

    search_country_dropdown_xpath = "//select[contains(@name,'country') or contains(@id,'country')] | //div[contains(text(),'Select Your Preferred Country')]"
    search_course_dropdown_xpath = "//div[contains(text(),'Select Course')]"
    search_course_type_dropdown_xpath = "//div[contains(text(),'Select Course Type')]"
    search_now_button_xpath = "//button[contains(text(),'SEARCH NOW') or contains(@class,'search')]"

    request_free_advice_xpath = (
        "//a[contains(text(),'REQUEST FREE ADVICE') or contains(text(),'Request Free Advice') or "
        "contains(text(),'Free Advice') or contains(text(),'FREE ADVICE') or "
        "contains(text(),'Get Free Advice') or contains(text(),'Book Free Advice')] | "
        "//button[contains(text(),'REQUEST FREE ADVICE') or contains(text(),'Request Free Advice') or "
        "contains(text(),'Free Advice') or contains(text(),'FREE ADVICE') or "
        "contains(text(),'Get Free Advice')] | "
        "//*[contains(@class,'free-advice') or contains(@class,'free_advice') or "
        "contains(@href,'free-advice') or contains(@href,'free_advice')]"
    )
    whatsapp_icon_xpath = "//a[contains(@href,'whatsapp') or contains(@href,'wa.me')]"
    phone_number_xpath = (
        "//*[contains(@href,'tel:')] | "
        "//*[contains(text(),'+91 8347742297') or contains(text(),'8347742297') or "
        "contains(text(),'+91-8347742297') or contains(text(),'+918347742297')]"
    )
    search_icon_xpath = "//button[contains(@class,'search')] | //i[contains(@class,'search')] | //span[contains(@class,'search')]"

    explore_countries_xpath = "//a[contains(text(),'Explore Countries')] | //button[contains(text(),'Explore Countries')]"
    view_all_countries_xpath = "//a[contains(text(),'View All Countries')] | //button[contains(text(),'View All Countries')]"
    view_all_exams_xpath = "//a[contains(text(),'View All Exams')] | //button[contains(text(),'View All Exams')]"
    view_all_articles_xpath = "//a[contains(text(),'View All Articles')] | //button[contains(text(),'View All Articles')]"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def is_logo_visible(self):
        try:
            logo = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.logo_xpath))
            )
            return logo.is_displayed()
        except:
            return False

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

    def is_request_free_advice_visible(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.request_free_advice_xpath))
            )
            return element.is_displayed()
        except:
            return False

    def click_request_free_advice(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.request_free_advice_xpath))
        )
        element.click()

    def is_whatsapp_icon_visible(self):
        try:
            element = self.driver.find_element(By.XPATH, self.whatsapp_icon_xpath)
            return element.is_displayed()
        except:
            return False

    def is_phone_number_visible(self):
        try:
            element = self.driver.find_element(By.XPATH, self.phone_number_xpath)
            return element.is_displayed()
        except:
            return False

    def click_search_icon(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_icon_xpath))
        )
        element.click()

    def scroll_and_click_explore_countries(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.explore_countries_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def scroll_and_click_view_all_countries(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.view_all_countries_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def scroll_and_click_view_all_exams(self):
        self.driver.execute_script("window.scrollBy(0, 800);")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.view_all_exams_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def scroll_and_click_view_all_articles(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.view_all_articles_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
