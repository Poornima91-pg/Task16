from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage():

    # Initialize the Populationpage object with Selenium WebDriver instance and define element locators for the page.
    def __init__(self, driver):
        self.driver = driver

        # Locators for Population count element
        self.population_xpath = "//div[@class='counter-ticker is-size-2-mobile']"

    # Wait until the population counter is visible and return its text
    def get_population_count(self):
        wait = WebDriverWait(self.driver, 10)
        population = wait.until(EC.visibility_of_element_located((By.XPATH, self.population_xpath)))
        return population.text

