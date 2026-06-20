# Jeduka.com QA Automation Project

**Prepared by:** QA Automation Intern
**Framework:** Selenium + Pytest + Page Object Model (POM)
**Website:** https://www.jeduka.com/

---

## Project Overview

This project automates 41 test cases for the Jeduka.com website — a study abroad platform. It covers homepage, register form, exam pages, article pages, country pages, course pages, footer, navigation, and performance testing.

The project follows the same style as the BBC School Management System automation project — simple, clean, beginner-friendly code using POM structure.

---

## Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.x | Programming language |
| Selenium 4.x | Browser automation |
| Pytest | Test runner and framework |
| pytest-html | HTML test report generation |
| WebDriverWait | Explicit waits for dynamic content |
| Page Object Model | Code organization pattern |

---

## Folder Structure

```
jeduka_automation/
│
├── pages/                         # Page Object classes
│   ├── home_page.py               # HomePage — locators + methods for homepage
│   ├── register_page.py           # RegisterPage — locators + methods for register form
│   ├── exams_page.py              # ExamsPage — exam listing and sub-pages
│   ├── articles_page.py           # ArticlesPage — article listing and detail
│   ├── countries_page.py          # CountriesPage — study abroad, university, visa, scholarship
│   └── apply_now_page.py          # ApplyNowPage — apply now page check
│
├── tests/                         # Test scripts
│   ├── test_homepage.py           # TC01–TC13, TC25 — Homepage tests
│   ├── test_register.py           # TC16–TC23 — Register form tests
│   ├── test_exams.py              # TC14, TC15, TC33, TC34 — Exam page tests
│   ├── test_articles.py           # TC25, TC26 — Articles tests
│   ├── test_country_pages.py      # TC12, TC27–TC32 — Country page tests
│   ├── test_courses.py            # TC35 — Course category page tests
│   ├── test_footer.py             # TC36, TC37 — Footer tests
│   ├── test_navigation.py         # TC24, TC38, TC39 — Navigation tests
│   └── test_performance.py        # TC40, TC41 — Performance tests
│
├── utilities/                     # Helper files
│   ├── driver_setup.py            # Chrome driver setup function
│   ├── waits.py                   # Reusable wait helper functions
│   └── screenshot.py              # Screenshot utility
│
├── reports/                       # Reports and documentation
│   ├── report.html                # Auto-generated HTML test report
│   ├── bug_report.md              # Bug report with 6 sample bugs
│   ├── test_plan.md               # Full QA test plan document
│   └── execution_report.md        # Test execution summary
│
├── conftest.py                    # Pytest fixture — Chrome driver setup and teardown
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## Installation

### Step 1 — Clone or download the project
```
git clone <your-repo-url>
cd jeduka_automation
```

### Step 2 — Install dependencies
```
pip install -r requirements.txt
```

### Step 3 — Make sure Google Chrome is installed
ChromeDriver is managed automatically.

---

## Run Tests

### Run all tests
```
pytest -v
```

### Run a specific test file
```
pytest tests/test_homepage.py -v
```

### Run a specific test
```
pytest tests/test_homepage.py::TestHomePage::test_homepage_title_and_url -v
```

### Run tests by module marker
```
pytest -m homepage -v
pytest -m performance -v
```

---

## Generate HTML Report

```
pytest --html=reports/report.html --self-contained-html -v
```

Open `reports/report.html` in your browser to view the full test report.

---

## How It Works

### conftest.py
- Contains the `driver` fixture
- Automatically opens Chrome before each test and closes it after
- All test functions receive `driver` as a parameter

### Page Classes (POM)
- Each page of the website has its own class in `/pages/`
- Locators (XPath, ID) are stored as class-level variables
- Methods perform actions like clicking, typing, reading text
- Tests import these classes and call their methods

### Test Files
- Each test file covers one module (homepage, register, exams, etc.)
- Tests call page class methods and use `assert` to verify results
- Simple and readable — no complex logic inside test functions

### Example
```python
def test_homepage_title_and_url(self, driver):
    home = HomePage(driver)
    home.open()
    assert "Study Abroad" in home.get_title()
    assert "jeduka.com" in home.get_current_url()
```

---

## Test Results Summary

| Total | Passed | Failed | Skipped |
|-------|--------|--------|---------|
| 41    | 36     | 3      | 2       |

Pass Rate: **87.8%**

---

## Author

**QA Automation Intern**
Certified from: MindRisers Institute of Technology
Project: Jeduka.com Internship Task
Framework: Selenium + Pytest + POM
