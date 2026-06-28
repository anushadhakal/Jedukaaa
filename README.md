Jeduka.com — Web Automation Testing

Automation testing project for jeduka.com, a study abroad platform.
Built using Selenium + Pytest + Page Object Model (POM) as part of an internship task at MindRisers Institute of Technology.

Prepared by: Anusha Dhakal


Test Summary

Total Test CasesPassedFailedPass RateBugs Found4239392.9%2


Tools Used

ToolPurposePythonProgramming languageSelenium WebDriverBrowser automationPytest + pytest-htmlTest runner and HTML outputPage Object ModelCode organization patternApache JMeterPerformance and load testing


Project Structure

jeduka_automation/
│
├── pages/               # One file per page — locators and methods
├── tests/               # One file per feature — test functions
├── conftest.py          # Browser setup and teardown
├── pytest.ini           # Pytest settings
└── requirements.txt     # Python packages needed


Installation and Running

Install dependencies:

pip install -r requirements.txt

Run all tests:

pytest -v

Run a specific file:

pytest tests/test_homepage.py -v

Generate HTML output (saved to reports/):

pytest --html=reports/report.html --self-contained-html -v


Bugs Found

Bug IDSeverityDescriptionBUG-JEDUKA-001HIGHAll country FAQ pages return HTTP 404BUG-JEDUKA-002MEDIUMQuiz widget on article page shows unavailable message instead of quiz