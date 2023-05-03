from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_NBC_chrome(self):

        driver = self.driver
        driver.get("https://google.com")
        driver.maximize_window()

        # wait max 5 sec for page loading
        driver.implicitly_wait(5)

        # this method is depreciated in Selenium4
        driver.find_element(By.NAME, "q").send_keys("NBC")
        driver.find_element(By.NAME, "btnK").click()

        print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image

        # Same code, but with XPath locator
        print(driver.find_element(By.XPATH, '//*[@alt="Google"]').get_attribute("src"))  # Google logo image

        # Find and click on the NBC link
        driver.find_element(By.PARTIAL_LINK_TEXT, "NBC TV Network").click()
        assert "NBC TV Network - Shows, Episodes, Schedule" in driver.title
        print("NBC Page Title is: ", driver.title)
        if not "NBC TV Network - Shows, Episodes, Schedule" in driver.title:
            raise Exception("Title for NBC page is wrong!")

        driver.set_page_load_timeout(5)

        # Find and click on "Browse"
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.ESCAPE)
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)

        # Find el The kelly Clarkson Show
        driver.find_element(By.LINK_TEXT, 'The Kelly Clarkson Show').click()

        time.sleep(3)
        assert "The Kelly Clarkson Show - Official Website - NBC.com" in driver.title
        driver.find_element(By.XPATH, '//title[contains(text(),"The Kelly Clarkson Show - Official Website - NBC.c")]')
        print(driver.find_element(By.XPATH, "//img[@alt='The Kelly Clarkson Show']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@alt='The Kelly Clarkson Show']").get_attribute("src"))

        # Find element value, then store this value to variable "KellyPageLogo"
        KellyPageLogo = driver.find_element(By.XPATH, "(//img[@alt='The Kelly Clarkson Show'])[2]")

        # Find KellyShowURL
        KellyShowURL = "https://www.nbc.com/the-kelly-clarkson-show"
        assert KellyShowURL == driver.current_url
        if KellyShowURL != driver.current_url:
            print("Current The Kelly Clarkson Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Show URL is OK: ", driver.current_url)

        # Same element verification for "Kelly Page Logo"
        if KellyPageLogo:
            print("The Kelly Clarkson Show Page Logo is OK")
        else:
            print("NO The Kelly Clarkson Show Page Logo")

        # View Show Tickets
        driver.find_element(By.XPATH, "//span[contains(.,'Tickets')]").click()
        time.sleep(3)
        KellyShowTicketsTitle = "The Kelly Clarkson Show "
        assert KellyShowTicketsTitle in driver.title
        if KellyShowTicketsTitle:
            print("The Kelly Clarkson Show tickets are available")
        else:
            print("The Kelly Clarkson Show tickets are unavailable")
        time.sleep(3)
        driver.back()

    def tearDown(self):
        # quit from browser
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_NBC_Edge(self):

        driver = self.driver
        driver.get("https://google.com")
        driver.maximize_window()

        # wait max 5 sec for page loading
        driver.implicitly_wait(5)

        # this method is depreciated in Selenium4
        driver.find_element(By.NAME, "q").send_keys("NBC")
        driver.find_element(By.NAME, "btnK").click()
        time.sleep(3)

        print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image

        # Same code, but with XPath locator
        print(driver.find_element(By.XPATH, '//*[@alt="Google"]').get_attribute("src"))  # Google logo image

        # Find and click on the NBC link
        driver.get("https://www.nbc.com/")
        assert "NBC TV Network - Shows, Episodes, Schedule" in driver.title
        print("NBC Page Title is: ", driver.title)
        if not "NBC TV Network - Shows, Episodes, Schedule" in driver.title:
            raise Exception("Title for NBC page is wrong!")

        driver.set_page_load_timeout(5)

        # Find and click on "Browse"
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.ESCAPE)
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)

        # Find el The kelly Clarkson Show
        driver.find_element(By.LINK_TEXT, 'The Kelly Clarkson Show').click()

        time.sleep(3)
        assert "The Kelly Clarkson Show - Official Website - NBC.com" in driver.title
        driver.find_element(By.XPATH,
                            '//title[contains(text(),"The Kelly Clarkson Show - Official Website - NBC.c")]')
        print(driver.find_element(By.XPATH, "//img[@alt='The Kelly Clarkson Show']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@alt='The Kelly Clarkson Show']").get_attribute("src"))

        # Find element value, then store this value to variable "KellyPageLogo"
        KellyPageLogo = driver.find_element(By.XPATH, "(//img[@alt='The Kelly Clarkson Show'])[2]")

        # Find KellyShowURL
        KellyShowURL = "https://www.nbc.com/the-kelly-clarkson-show"
        assert KellyShowURL == driver.current_url
        if KellyShowURL != driver.current_url:
            print("Current The Kelly Clarkson Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Show URL is OK: ", driver.current_url)

        # Same element verification for "Kelly Page Logo"
        if KellyPageLogo:
            print("The Kelly Clarkson Show Page Logo is OK")
        else:
            print("NO The Kelly Clarkson Show Page Logo")

        # View Show Tickets
        driver.find_element(By.XPATH, "//span[contains(.,'Tickets')]").click()
        time.sleep(3)
        KellyShowTicketsTitle = "The Kelly Clarkson Show "
        assert KellyShowTicketsTitle in driver.title
        if KellyShowTicketsTitle:
            print("The Kelly Clarkson Show tickets are available")
        else:
            print("The Kelly Clarkson Show tickets are unavailable")
        time.sleep(3)
        driver.back()

    def tearDown(self):

        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()

    def test_NBC_Firefox(self):

        driver = self.driver
        driver.get("https://google.com")
        driver.maximize_window()

        # wait max 5 sec for page loading
        driver.implicitly_wait(5)

        # this method is depreciated in Selenium4
        driver.find_element(By.NAME, "q").send_keys("NBC")
        driver.find_element(By.NAME, "btnK").click()

        print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image

        # Same code, but with XPath locator
        print(driver.find_element(By.XPATH, '//*[@alt="Google"]').get_attribute("src"))  # Google logo image

        # Find and click on the NBC link
        driver.get("https://www.nbc.com/")
        assert "NBC TV Network - Shows, Episodes, Schedule" in driver.title
        print("NBC Page Title is: ", driver.title)
        if not "NBC TV Network - Shows, Episodes, Schedule" in driver.title:
            raise Exception("Title for NBC page is wrong!")

        driver.set_page_load_timeout(5)

        # Find and click on "Browse"
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.ESCAPE)
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Browse").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)

        # Find el The kelly Clarkson Show
        driver.find_element(By.LINK_TEXT, 'The Kelly Clarkson Show').click()

        time.sleep(3)
        assert "The Kelly Clarkson Show - Official Website - NBC.com" in driver.title
        driver.find_element(By.XPATH,
                            '//title[contains(text(),"The Kelly Clarkson Show - Official Website - NBC.c")]')
        print(driver.find_element(By.XPATH, "//img[@alt='The Kelly Clarkson Show']").get_attribute("title"))
        print(driver.find_element(By.XPATH, "//img[@alt='The Kelly Clarkson Show']").get_attribute("src"))

        # Find element value, then store this value to variable "KellyPageLogo"
        KellyPageLogo = driver.find_element(By.XPATH, "(//img[@alt='The Kelly Clarkson Show'])[2]")

        # Find KellyShowURL
        KellyShowURL = "https://www.nbc.com/the-kelly-clarkson-show"
        assert KellyShowURL == driver.current_url
        if KellyShowURL != driver.current_url:
            print("Current The Kelly Clarkson Show URL is different and it is: ", driver.current_url)
        else:
            print("Current Show URL is OK: ", driver.current_url)

        # Same element verification for "Kelly Page Logo"
        if KellyPageLogo:
            print("The Kelly Clarkson Show Page Logo is OK")
        else:
            print("NO The Kelly Clarkson Show Page Logo")

        # View Show Tickets
        driver.find_element(By.XPATH, "//span[contains(.,'Tickets')]").click()
        time.sleep(3)
        KellyShowTicketsTitle = "The Kelly Clarkson Show "
        assert KellyShowTicketsTitle in driver.title
        if KellyShowTicketsTitle:
            print("The Kelly Clarkson Show tickets are available")
        else:
            print("The Kelly Clarkson Show tickets are unavailable")
        time.sleep(3)
        driver.back()

    def tearDown(self):
        # quit from browser
        self.driver.quit()
