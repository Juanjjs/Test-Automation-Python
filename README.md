# Purchase automation

## Test Automation Project: Negative Test Case for Renfe Ticket Purchase
This repository contains an automated test case using Python and Selenium to simulate a negative test scenario on Renfe's website. The test case involves attempting to purchase a train ticket with an invalid bank card, following specific instructions and best practices.

### Overview
The goal of this project is to create a complete automated test case from scratch, using the Selenium framework to interact with Renfe's website and validate that the system correctly handles invalid payment information. Adhering to the Page Object Model (POM) design pattern.

This repository simulates the purchase of a ticket in an automated way on the Renfe website. [Renfe website](https://www.renfe.com/es/es)

### Web Automation Project with Selenium and Python

This project uses **Selenium** to automate interactions with a web page, following the **Page Object Model (POM)** design pattern in Python.

## Project Structure

The code is organized as follows:

- **drivers/**: Contains the drivers needed to run automated tests in different browsers.

- **pages/**: Defines classes representing the different web pages under test. Each `.py` file within this directory corresponds to a specific page, encapsulating page elements and possible actions:
  - `DataPage.py`: Data entry page.
  - `DetailsPayPage.py`: Payment details page.
  - `HomePage.py`: Home page.
  - `PayPage.py`: Payment page.
  - `train_selection.py`: Train selection page.

- **tests/**: Contains the automated test cases that validate the application's functionalities.
  - `test_booking.py`: Runs tests to verify the ticket booking flow.

- **utils/**: Includes support utilities for automation.
  - `webdriver_setup.py`: WebDriver setup and management.

- **pytest.ini**: Configuration file for Pytest, defining how the tests should be executed.

- **README.md**: Project documentation.

- **requirements.txt**: List of project dependencies.

## Important
A virtual environment is used to run the test using Pytest.