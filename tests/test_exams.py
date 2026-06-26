import time
from pages.exams_page import ExamsPage


class TestExamsPage:

    url = "https://www.jeduka.com/exams"
    base_url = "https://www.jeduka.com"

    # TC14
    def test_exams_page_shows_all_exam_categories(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        time.sleep(2)
        exams = ExamsPage(self.driver)

        exam_list = ["IELTS", "TOEFL", "Duolingo", "GMAT", "GRE", "PTE", "SAT", "USMLE"]
        for exam in exam_list:
            assert exams.is_exam_visible(exam), f"{exam} is not visible on the exams page"

    # TC15
    def test_ielts_sublinks_present(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        time.sleep(2)
        exams = ExamsPage(self.driver)

        sublinks = exams.get_ielts_sublinks()
        assert len(sublinks) >= 5, f"Expected at least 5 IELTS sub-links, found {len(sublinks)}"
        assert "ielts" in " ".join(sublinks).lower(), "No IELTS links found in sub-links"

    # TC33
    def test_all_exam_main_pages_load(self, driver):
        self.driver = driver
        exam_slugs = ["ielts", "toefl", "gre", "gmat", "pte", "sat",
                      "duolingo", "usmle", "usmle-step-1", "usmle-step-2"]

        for slug in exam_slugs:
            self.driver.get(f"{self.base_url}/exams/{slug}")
            time.sleep(1)
            assert slug in self.driver.current_url, f"Exam page for '{slug}' did not load correctly"

    # TC34
    def test_ielts_subpages_load(self, driver):
        self.driver = driver
        subpages = ["", "eligibility", "syllabus", "pattern", "preparation", "registration"]

        for subpage in subpages:
            if subpage == "":
                self.driver.get(f"{self.base_url}/exams/ielts")
            else:
                self.driver.get(f"{self.base_url}/exams/ielts/{subpage}")
            time.sleep(1)
            assert "ielts" in self.driver.current_url, f"IELTS subpage '{subpage}' did not load"
