import time
import pytest


class TestCoursePages:

    course_pages = [
        ("MBA", "https://www.jeduka.com/mba-colleges-universities-abroad"),
        ("Engineering", "https://www.jeduka.com/engineering-colleges-universities-abroad"),
        ("IT", "https://www.jeduka.com/information-technology-colleges-universities-abroad"),
        ("Medicine", "https://www.jeduka.com/medicine-and-healthcare-colleges-universities-abroad"),
        ("Hospitality & Tourism", "https://www.jeduka.com/hospitality-and-tourism-colleges-universities-abroad"),
        ("Management", "https://www.jeduka.com/management-colleges-universities-abroad"),
        ("Science", "https://www.jeduka.com/science-colleges-universities-abroad"),
        ("Arts", "https://www.jeduka.com/arts-colleges-universities-abroad"),
        ("Media Films", "https://www.jeduka.com/media-films-colleges-universities-abroad"),
        ("Law", "https://www.jeduka.com/law-colleges-universities-abroad"),
    ]

    # TC35
    def test_all_course_category_pages_load(self, driver):
        for course_name, url in self.course_pages:
            driver.get(url)
            time.sleep(1)

            assert "jeduka.com" in driver.current_url, \
                f"{course_name} course page did not load correctly"
            assert driver.current_url != "https://www.jeduka.com/", \
                f"{course_name} page redirected to homepage"
