# Ecommerce-Automation
Automation framework to test Ecommerce Application
🛒 Ecommerce Automation Framework
Author: Kaustubh Thakare

An end-to-end automation framework for testing an e-commerce web application using Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern. This framework supports scalable test development, integrates with Jenkins for CI/CD, and generates detailed Allure Reports for test results.


**📌 FEATURES**

1. Modular Test Design: Implements the Page Object Model for maintainable and reusable code.

2. Test Coverage: Includes test cases for user registration, login, logout, product search, cart operations, and checkout processes.

3. Reporting: Integrates Allure for comprehensive and visually appealing test reports.

4. CI/CD Integration: Configured with Jenkins for automated test execution in continuous integration pipelines.

5. Configuration Management: Utilizes pytest.ini and config/ directory for managing test configurations and environment settings.


**📌 TECH STACK**

Programming Language: Python

Automation Tool: Selenium WebDriver

Testing Framework: Pytest

Design Pattern: Page Object Model (POM)

Continuous Integration: Jenkins

Reporting Tool: Allure

**📌 PROJECT STRUCTURE**

Ecommerce-Automation/

├── config/             # Configuration files and environment settings

├── pages/              # Page Object Model classes for web pages

├── tests/              # Test cases organized by functionality

├── utils/              # Utility functions and helper methods

├── reports/            # Generated test reports (e.g., Allure results)

├── requirements.txt    # Python dependencies

├── pytest.ini          # Pytest configuration

├── Jenkinsfile         # Jenkins pipeline configuration

└── README.md           # Project documentation



**🚀 GETTING STARTED**

**📌 PREREQUISITES**

Python 3.7 or higher

Google Chrome browser

Allure Commandline (for generating reports) - Setup and configured
Follow the official installation guide: https://allurereport.org/docs/#_installing_a_commandline


**📌 INSTALLATION**

Clone the repository:
1. git clone https://github.com/ThakareKaustubh/Ecommerce-Automation.git
2. cd Ecommerce-Automation

**Create and activate a virtual environment**
1. python -m venv venv
2. source venv/bin/activate  # On Windows: venv\Scripts\activate

**Install the required packages:**
1. pip install -r requirements.txt



**📌 RUNNING TESTS**
1. Execute All Tests
pytest

2. Run Specific Test Module
pytest tests/test_login.py

3. Run tests with Allure - Specify browser== chrome or firefox 
 pytest tests/test_user_registration.py --browser=chrome --alluredir=allure-results  
or if you want to run in headless mode use:
 pytest tests/test_user_registration.py --browser=chrome --headless --alluredir=allure-results  
Generate and open the report:

allure serve reports/




**📌 CONFIGURATION**
1. pytest.ini: Contains Pytest configurations.

2. config/: Directory for environment-specific settings and configurations.

**End of File**
