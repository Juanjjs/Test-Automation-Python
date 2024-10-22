# Purchase automation

## Test Automation Project: Negative Test Case for Renfe Ticket Purchase
This repository contains an automated test case using Python and Selenium to simulate a negative test scenario on Renfe's website. The test case involves attempting to purchase a train ticket with an invalid bank card, following specific instructions and best practices.

### Overview
The goal of this project is to create a complete automated test case from scratch, using the Selenium framework to interact with Renfe's website and validate that the system correctly handles invalid payment information. Adhering to the Page Object Model (POM) design pattern.

### Project Setup
#### Tools & Technologies Used
- **Repository:** GitHub
- **Programming Language:** Python
- **Test Framework:** Selenium WebDriver
- **Design Pattern:** Page Object Model (POM)

### Test Scenario
The automated test case is a negative scenario where a user attempts to purchase a one-way train ticket with invalid payment information. The specific test case details are as follows:

1. **Website:** [Renfe Official Website](https://www.renfe.com/es/es)
2. **Route:** From VALENCIA JOAQUÍN SOROLLA to BARCELONA-SANTS
3. **Journey Type:** One-way trip
4. **Passenger Details:** Non-real data is used for the passenger information
5. **Payment:** An invalid credit card number (e.g., `0000 0000 0000 0000`) is provided
6. **Expected Result:** A banner message should appear indicating that the provided card details are invalid

### Key Considerations
The project evaluates the following criteria:

- **Data Structures:** Correct use of Python data structures for managing test data and logic.
- **Test Duration and Wait Handling:** Tests are optimized for duration and make appropriate use of implicit waits in Selenium.
- **Git Usage:** Proper use of Git for version control, with clear commit messages and branching where necessary.
- **Page Object Model (POM):** Implementation of the POM pattern to separate page interactions from test logic for better maintainability.

### Key Steps in the Test Case:
**1.** Navigate to the Renfe homepage.\
**2.** Search for available train tickets from VALENCIA JOAQUÍN SOROLLA to BARCELONA-SANTS on a selected date.\
**3.** Choose the first available ticket option.\
**4.** Fill in the passenger details with dummy data.\
**5.** Attempt to pay using an invalid credit card `(0000 0000 0000 0000)`.\
**6.** Verify that an error banner or message appears, indicating that the card is invalid.