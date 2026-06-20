import time
import pytest
from pages.exams_page import ExamsPage


class TestExamsPage:

    # TC14
    def test_exams_page_shows_all_exam_categories(self, driver):
        exams = ExamsPage(driver)
        exams.open()
        time.sleep(2)

        exam_list = ["IELTS", "TOEFL", "Duolingo", "GMAT", "GRE", "PTE", "SAT", "USMLE"]

        for exam in exam_list:
            assert exams.is_exam_visible(exam), f"{exam} is not visible on the exams page"

    # TC15
    def test_ielts_sublinks_present(self, driver):
        exams = ExamsPage(driver)
        exams.open()
        time.sleep(2)

        sublinks = exams.get_ielts_sublinks()
        assert len(sublinks) >= 5, f"Expected at least 5 IELTS sub-links, found {len(sublinks)}"

        sublinks_text = " ".join(sublinks)
        assert "ielts" in sublinks_text.lower(), "No IELTS links found in sub-links"

    # TC33
    def test_all_exam_main_pages_load(self, driver):
        exam_slugs = ["ielts", "toefl", "gre", "gmat", "pte", "sat",
                      "duolingo", "usmle", "usmle-step-1", "usmle-step-2"]

        exams = ExamsPage(driver)

        for slug in exam_slugs:
            exams.navigate_to_exam_page(slug)
            time.sleep(1)
            assert slug in driver.current_url, f"Exam page for '{slug}' did not load correctly"

    # TC34
    def test_ielts_subpages_load(self, driver):
        subpages = ["", "eligibility", "syllabus", "pattern", "preparation", "registration"]

        exams = ExamsPage(driver)

        for subpage in subpages:
            if subpage == "":
                driver.get("https://www.jeduka.com/exams/ielts")
            else:
                exams.navigate_to_ielts_subpage(subpage)
            time.sleep(1)
            assert "ielts" in driver.current_url, f"IELTS subpage '{subpage}' did not load"
