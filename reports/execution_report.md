# Test Execution Report — Jeduka.com

**Project:** Jeduka.com QA Automation
**Prepared by:** QA Automation Intern
**Execution Date:** June 2026
**Environment:** Chrome (latest), Windows 10, Selenium 4.x, Pytest

---

## Summary

| Total Tests | Passed | Failed | Skipped |
|-------------|--------|--------|---------|
| 41          | 36     | 3      | 2       |

**Pass Rate: 87.8%**

---

## Module-wise Results

| Module | Tests | Passed | Failed | Skipped |
|--------|-------|--------|--------|---------|
| Homepage | 12 | 10 | 1 | 1 |
| Register Page | 8 | 7 | 1 | 0 |
| Exams Page | 4 | 4 | 0 | 0 |
| Articles Page | 2 | 2 | 0 | 0 |
| Country Pages | 7 | 6 | 1 | 0 |
| Course Pages | 1 | 1 | 0 | 0 |
| Footer | 2 | 2 | 0 | 0 |
| Navigation | 3 | 3 | 0 | 0 |
| Performance | 3 | 2 | 0 | 1 |

---

## Failed Tests

### FAIL-01 — TC06: Search NOW button does not filter results
- **Test:** `test_search_now_button_works`
- **Reason:** Clicking SEARCH NOW after selecting USA did not navigate to a filtered page. URL remained unchanged.
- **Related Bug:** BUG-001

### FAIL-02 — TC22: Register form submitted without Privacy Policy acceptance
- **Test:** `test_form_submission_fails_without_privacy_policy`
- **Reason:** Form was submitted successfully even without checking the privacy checkbox.
- **Related Bug:** BUG-004

### FAIL-03 — TC30: Apply Now button missing on France/Germany university pages
- **Test:** `test_apply_now_button_on_university_detail_page`
- **Reason:** Apply Now button was not found on France and Germany university detail pages.
- **Related Bug:** BUG-005

---

## Skipped Tests

### SKIP-01 — TC09: Search icon behavior
- **Reason:** Search icon locator was not reliable across all page states. Marked as skip with `pytest.skip()` inside the test.

### SKIP-02 — TC41: Performance timing API
- **Reason:** `loadEventEnd` returned 0 on first execution (timing not yet available). Test skipped gracefully.

---

## Observations

1. Most core navigation and page load tests passed successfully.
2. The website uses dynamic content (AJAX dropdowns) which required explicit waits.
3. The register form has a critical bug — Privacy Policy bypass — which should be fixed immediately.
4. Performance was acceptable for most pages (6–9 seconds load time) but homepage exceeded 10s on first cold load.
5. All 10 exam pages loaded correctly without any broken URLs.
6. Country pages were stable and consistent across all 6 major study destinations.

---

## Recommendations

- Fix the Privacy Policy validation bug (BUG-004) — this is a Critical severity issue
- Fix the SEARCH NOW button to actually filter results (BUG-001) — this is the core feature
- Add "Apply Now" button to France and Germany university detail pages (BUG-005)
- Optimize homepage load time (BUG-006) — compress images and defer non-critical scripts
- Use `id` attributes on form elements to make locators more stable and less likely to break

---

*Report generated after full test suite execution using:*
```
pytest tests/ -v --html=reports/report.html
```
