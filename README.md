📌 Project Overview

This project demonstrates automated testing of the Urban Routes web application using Selenium WebDriver with Pytest and the Page Object Model (POM) design pattern.
The goal is to validate core user journeys, improve test maintainability, and ensure reliable, efficient test execution.

🎯 Objectives

Automate user flows for Urban Routes

Apply the Page Object Model (POM) to keep code modular and maintainable

Use Pytest for test execution and reporting

Ensure tests run efficiently without unnecessary delays

Showcase professional test automation practices for portfolio and interviews

🛠️ Tools & Technologies

Language: Python

Framework: Pytest

Automation: Selenium WebDriver

Design Pattern: Page Object Model (POM)



📂 Project Structure
urban-scooter/
│── data/             # Test data files   
│── pages/            # Page Object Model (POM) classes  
│── main/            # Pytest test cases  
│── helpers/          # Utility functions     
│── README.md         # Project documentation  

📑 Code & Naming Guidelines

Variables → snake_case with descriptive names


Comments → Explain important logic concisely

Modularity → Reusable POM classes and helpers

Efficiency → Avoid unnecessary wait functions

Test Naming → Start with test_ + clear scenario (e.g., test_user_can_book_scooter)

✅ Sample Test Case

Scenario: Verify user can successfully book a taxi

Precondition: User is logged in

Steps:

Enter pickup and drop-off locations

Select Custom option

Expected Result: Route is displayed with correct details

Automated Test Example (Pytest + POM):

    
    def test_set_route(self):
       self.driver.get(data.URBAN_ROUTES_URL)
       urban_routes_page = pages.UrbanRoutesPage(self.driver)
       urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

       actual_value_from = urban_routes_page.get_value_in_from()
       expected_value_from = data.ADDRESS_FROM

       actual_value_to = urban_routes_page.get_value_in_to()
       expected_value_to = data.ADDRESS_TO

       assert actual_value_from in expected_value_from, f'Expected: {expected_value_from} Actual: {actual_value_from}'
       assert actual_value_to in expected_value_to, f'Expected: {expected_value_to} Actual: {actual_value_to}'

📊 Results

Automated core scenarios: Ride booking, and booking confirmation

Improved test readability and maintainability with POM

Achieved faster execution with Pytest parallel runs
