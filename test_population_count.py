from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from Task16.Populationpage import PopulationPage


# Test case to continuously fetch and print the world population using Page Object Model (PopulationPage).Runs until user presses CTRL+C.
def test_population_count():
    try:
        # Create Chrome options to customize browser behavior
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')

        # Launch Chrome browser and navigate to word population clock live page
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")

        # Create page object and pass driver
        population_count = PopulationPage(driver)

        # Keep printing until CTRL+C
        while True:
            count=population_count.get_population_count()
            print("Current World Population:",count)

    # user presses CTRL+C to stop the test raises keyboard interrupt
    except KeyboardInterrupt:
         print("\nStopped by user by pressing (CTRL+C)")

    # closes the browser
    finally:
        driver.quit()




