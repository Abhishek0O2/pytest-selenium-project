# pytest-selenium-project
# Overview
This repository contains a robust, educational automation framework using Selenium with Pytest in Python, targeting the SelectorsHub XPath Practice Page.

# Designed for:

Building solid automation skills via hands-on scenarios (UI, DOM, tables, modals).

Deepening Python concepts (list comprehensions, sets, lambda, iteration) by connecting each test case to a core language lesson.

Scalable Page Object Model structure—locators and actions live in page classes for maintainability.

# Scenarios Covered
# 1. Heading Assertion
Skills: Robust locator design, inheritance, page object basics

Actions:

Loads practice page

Locates page heading using flexible strategies (XPath with changing tags, context, or visible text)

Asserts heading text matches expected value

Python concepts:

Class inheritance for Page Object Model

The importance of constructor (__init__) for passing shared dependencies (driver)

Encapsulating locators and actions

# 2. Modal Popups and Tab Handling
Skills: Handling overlays, popups, tab/window context switching

Actions:

Scrolls and uses JS click for modal reliability

Waits for modal to appear

Locates and clicks link inside modal that opens in a new tab

Switches WebDriver context to new tab, asserts URL/content, then closes tab and returns

Python concepts:

Sets, set difference, and why we use them for tab detection

Lambda functions and list comprehensions for dynamic waits

Window handle management—robust extraction and switching

# 3. Data Table Extraction and Assertion
Skills: Semantic HTML table extraction, mapping UI columns to data

Actions:

Finds all table rows and columns

Extracts column or entire row data using list comprehensions

Asserts key details (e.g., user exists, role matches)

Python concepts:

Indexing in comprehensions, handling column mappings

List vs dict extraction for richer data mapping

Safe indexing, cleanup, and casing transformations

# 4. Dropdowns, Disabled Elements, Alerts, and Complex Element Handling
(Template section for you to fill as you encounter real cases!)

Skills: Select option interactions, toggling enabled/disabled, interacting with JS alerts, handling nested and dynamic DOM nodes

Actions:

Locates dropdowns and selects options programmatically

Identifies and interacts with disabled/enabled fields

Accepts, dismisses, and asserts JS alerts

Handles nested elements with parent/child context and shadow DOM as required

Python concepts:

Exception handling, assertions

Higher-order functions for flexible element waits

Generator expressions for data-driven validation

# 5. Frame, Shadow DOM, and Virtualization Challenges
(Advanced section, add as you reach these!)

Skills: Entering and switching frames, traversing shadow roots

Actions:

Switches WebDriver context to iframes

Grabs shadow DOM node references for deep selectors

Handles virtualization (rows/cells rendered only on scroll)

Python concepts:

Context managers (with for resource control)

Recursive data extraction

# Structure
text
/pages
    base_page.py   # shared helpers, driver reference
    main_page.py   # all locators and UI actions for practice page

/tests
    test_headings.py
    test_modals.py
    test_user_table.py

requirements.txt   # Selenium, Pytest, plus other dependencies
Getting Started
Install dependencies:

text
pip install -r requirements.txt
Run any test:

text
pytest tests/
Page Objects let you add/modify locators and actions centrally for all scenarios.

# Learning Approach
Every test case doubles as a Python lesson—see comments for:

List comprehensions and iteration tricks

Lambda and functional filtering

Set operations and window handle logic

Data modeling via dicts, rows, or custom classes

# How To Extend
Add scenarios by creating new test files and action methods in MainPage.

Try advanced UI features (alerts, shadow DOM, dropdowns, dynamic elements) and apply new Python features.

Use this repo as a template for real-world automation on evolving web pages.

# Contributing
Contributions welcome—open issues or PRs for new scenarios, page objects, or deeper Python integration examples!
