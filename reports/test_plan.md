# Test Plan — Jeduka.com QA Automation Project

**Document Version:** 1.0
**Prepared by:** QA Automation Intern
**Date:** June 2026
**Project:** Jeduka.com Website Automation Testing

---

## 1. Introduction

This test plan describes the approach and scope for automated testing of the Jeduka.com website — a study abroad platform that provides information on universities, courses, exams, and scholarships for international students.

The automation project uses Selenium with Pytest following a Page Object Model (POM) architecture, similar to the BBC School Management System automation project.

---

## 2. Objective

- Verify that all major website features function correctly
- Ensure forms validate user input properly
- Check navigation between all pages works without broken links
- Validate page load performance is within acceptable limits
- Identify and report bugs found during test execution

---

## 3. Scope

### In Scope
- Homepage (title, logo, navbar, search widget, buttons)
- Register Page (3-step form, dropdowns, checkboxes, submission)
- Exams Page (exam categories, sub-links, individual exam pages)
- Articles Page (listing page, article detail pages)
- Country Pages (Study Abroad, Study In pages, University listings, Visa pages, Scholarship pages)
- Course Pages (all 10 course category pages)
- Footer (links, social media icons)
- Navigation (back/forward, broken links)
- Performance (page load time, Navigation Timing API)

### Out of Scope
- Admin backend or CMS
- Payment gateway or transaction testing
- Email/SMS notification testing
- Mobile responsiveness (not automated in this project)
- Load testing / stress testing

---

## 4. Test Environment

| Item | Details |
|------|---------|
| Website | https://www.jeduka.com/ |
| Browser | Google Chrome (latest) |
| OS | Windows 10/11 |
| Automation Tool | Selenium 4.x |
| Test Framework | Pytest |
| Language | Python 3.x |
| Reporting | pytest-html |
| ChromeDriver | Matching Chrome version |

---

## 5. Test Strategy

- Follow **Page Object Model (POM)** — page classes in `/pages/`, test scripts in `/tests/`
- Use **explicit waits** (WebDriverWait) for all dynamic elements
- Keep code **simple and readable** — written at intern/junior level
- Group tests by feature module into separate test files
- Use `conftest.py` for shared driver fixture
- Generate HTML report after every test run

---

## 6. Test Types

### 6.1 Functional Testing
Verify all features work as expected — forms, buttons, dropdowns, navigation links, exam pages, article listings, university listings.

### 6.2 UI Testing
Verify that all key UI elements (logo, navbar, footer, buttons) are visible and displayed correctly.

### 6.3 Navigation Testing
Verify that clicking links/buttons navigates to the correct pages, and browser back/forward buttons work correctly.

### 6.4 Performance Testing
Measure page load time using Python's `time` module and the browser's Navigation Timing API.

---

## 7. Entry Criteria

- The Jeduka.com website is accessible and live
- ChromeDriver is installed and matches Chrome version
- Python 3.x is installed
- All dependencies are installed via `pip install -r requirements.txt`
- All test files and page classes are written and reviewed

---

## 8. Exit Criteria

- All 41 test cases have been executed
- Test execution report is generated
- All Critical and High severity bugs are documented
- HTML report is saved in `/reports/` folder
- Pass rate is at least 85%

---

## 9. Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Website layout changes | High — locators may break | Use stable locators (text-based XPath) |
| Slow network/page load | Medium — tests may time out | Use 10-second explicit waits |
| Dynamic content (AJAX) | Medium — elements may not be ready | Use WebDriverWait before all interactions |
| ChromeDriver version mismatch | High — tests won't run | Use webdriver-manager to auto-manage driver |
| Form submission may send real data | Low — test data used | Use clearly fake test data (e.g. "123456789") |

---

## 10. Deliverables

- `jeduka_automation/` — Full automation project folder
- `reports/report.html` — HTML test execution report
- `reports/bug_report.md` — Bug report document
- `reports/test_plan.md` — This document
- `reports/execution_report.md` — Test execution summary
- `README.md` — Project documentation

---

## 11. Schedule

| Task | Duration |
|------|----------|
| Understand website and test cases | 1 day |
| Set up project structure | 0.5 day |
| Write page classes (POM) | 1 day |
| Write all 41 test scripts | 2 days |
| Execute tests and fix issues | 1 day |
| Prepare bug report and reports | 0.5 day |
| Final review and submission | 0.5 day |
| **Total** | **~6.5 days** |

---

*Prepared by: QA Automation Intern*
*Reviewed by: QA Lead / Project Manager*
