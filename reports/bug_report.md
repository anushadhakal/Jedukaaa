# Bug Report — Jeduka.com QA Automation Testing

**Project:** Jeduka.com Automation Testing
**Prepared by:** QA Automation Intern
**Date:** June 2026
**Tool Used:** Selenium + Pytest

---

## BUG-001

| Field        | Details |
|--------------|---------|
| **Bug ID**   | BUG-001 |
| **Summary**  | Homepage search widget "SEARCH NOW" button does not filter results when only Country is selected |
| **Module**   | Homepage Search |
| **Severity** | High |
| **Priority** | High |
| **Steps to Reproduce** | 1. Go to https://www.jeduka.com/ <br> 2. Select "USA" from "Select Your Preferred Country" dropdown <br> 3. Leave "Select Course" and "Select Course Type" blank <br> 4. Click the yellow "SEARCH NOW" button |
| **Expected** | Page should navigate to a filtered results page showing universities/courses in USA |
| **Actual**   | Page reloads or no visible filter is applied. Results do not change based on country selection. |
| **Screenshot** | search_no_filter.png |

---

## BUG-002

| Field        | Details |
|--------------|---------|
| **Bug ID**   | BUG-002 |
| **Summary**  | Register form Step 3 — State dropdown does not update dynamically after selecting Nepal |
| **Module**   | Register Page |
| **Severity** | Medium |
| **Priority** | High |
| **Steps to Reproduce** | 1. Go to https://www.jeduka.com/register.html <br> 2. Scroll to Step 1 <br> 3. Click "Country You Are Currently Living In" dropdown <br> 4. Select "Nepal" <br> 5. Observe the State dropdown |
| **Expected** | State dropdown should update and show states/provinces of Nepal (e.g., Bagmati, Koshi, Lumbini) |
| **Actual**   | State dropdown remains empty or shows default placeholder without updating |
| **Screenshot** | state_not_updating.png |

---

## BUG-003

| Field        | Details |
|--------------|---------|
| **Bug ID**   | BUG-003 |
| **Summary**  | Clicking "REQUEST FREE ADVICE" button does not open counselling form or navigate to register page |
| **Module**   | Homepage |
| **Severity** | High |
| **Priority** | High |
| **Steps to Reproduce** | 1. Go to https://www.jeduka.com/ <br> 2. Locate the orange "REQUEST FREE ADVICE" button <br> 3. Click the button |
| **Expected** | Should navigate to /register.html or open a counselling pop-up form |
| **Actual**   | Button click does nothing or navigates to an unrelated section of the page |
| **Screenshot** | request_advice_broken.png |

---

## BUG-004

| Field        | Details |
|--------------|---------|
| **Bug ID**   | BUG-004 |
| **Summary**  | Register form allows submission without accepting Privacy Policy and Terms checkbox |
| **Module**   | Register Page |
| **Severity** | Critical |
| **Priority** | Critical |
| **Steps to Reproduce** | 1. Go to https://www.jeduka.com/register.html <br> 2. Fill all required fields in Step 1, Step 2, Step 3 <br> 3. Leave the "I accept Privacy Policy and T&C" checkbox unchecked <br> 4. Click "Submit To Get Call Back" |
| **Expected** | Error message "Please accept the Privacy Policy and T&C" should appear. Form should NOT be submitted. |
| **Actual**   | Form gets submitted even without accepting Privacy Policy. User data is saved without consent. |
| **Screenshot** | privacy_bypass.png |

---

## BUG-005

| Field        | Details |
|--------------|---------|
| **Bug ID**   | BUG-005 |
| **Summary**  | "Apply Now" button missing on university detail pages for France and Germany |
| **Module**   | Country Pages — Universities |
| **Severity** | High |
| **Priority** | High |
| **Steps to Reproduce** | 1. Go to https://www.jeduka.com/france/universities <br> 2. Click on any university listing <br> 3. Look for "Apply Now" button on the detail page <br> 4. Repeat for https://www.jeduka.com/germany/universities |
| **Expected** | "Apply Now" button should be visible on all university detail pages |
| **Actual**   | Button is missing on France and Germany university detail pages. Only USA and UK pages have it. |
| **Screenshot** | apply_now_missing.png |

---

## BUG-006

| Field        | Details |
|--------------|---------|
| **Bug ID**   | BUG-006 |
| **Summary**  | Homepage takes more than 10 seconds to fully load on first visit |
| **Module**   | Performance |
| **Severity** | Medium |
| **Priority** | Medium |
| **Steps to Reproduce** | 1. Open browser in a fresh session (clear cache) <br> 2. Navigate to https://www.jeduka.com/ <br> 3. Start timer and wait for document.readyState to be "complete" |
| **Expected** | Full page load should complete in under 10 seconds |
| **Actual**   | Page takes 12–14 seconds to fully load on first visit due to large image assets and third-party scripts |
| **Screenshot** | performance_slow.png |

---

*Total Bugs Found: 6*
*Critical: 1 | High: 4 | Medium: 1*
