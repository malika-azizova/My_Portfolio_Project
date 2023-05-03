import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from faker import Faker

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import unittest


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_wordpress_chrome(self):
        fake = Faker()

        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        waits = WebDriverWait(driver, 3)
        driver.maximize_window()

        print(driver.title)
        print(driver.current_url)

        driver.find_element(By.PARTIAL_LINK_TEXT, "California Real Estate").click()
        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("California Real Estate Page Title is: ", driver.title)

        # Page down for search invisible element

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30 size-full"]')))
        time.sleep(2)

        # filling in the form
        name = driver.find_element(By.ID, "g2-name")
        name.send_keys(fake.first_name())
        time.sleep(1)
        name.clear()
        time.sleep(1)
        name.send_keys(fake.first_name())

        # random email with no Faker lib
        random_email = str(random.randint(0, 99999)) + "myemail" + "@example.com"

        email = driver.find_element(By.ID, "g2-email")
        # email.send_keys(random_email)
        email.send_keys(fake.email())
        time.sleep(1)
        email.clear()
        time.sleep(1)
        email.send_keys(fake.email())

        # Text message "Hello!"
        Message = driver.find_element(By.ID, "contact-form-comment-g2-message")
        Message.send_keys("Hello My Friend!")

        WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))

        # Push button "Submit"
        submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        submit.click()

        time.sleep(2)

        try:
            WebDriverWait(driver, 4) \
                .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))
            print("Registration complete!")
        except TimeoutException:
            print("Registration not complete!")

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()

        print(driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").get_attribute("type"))

        pageTitle = "California Real Estate – QA at Silicon Valley Real Estate"
        assert driver.title == pageTitle


    def test_wordpress_chrome_1120_850(self):
        fake = Faker()

        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        waits = WebDriverWait(driver, 3)
        driver.set_window_size(1120, 850)

        print(driver.title)
        print(driver.current_url)

        driver.find_element(By.PARTIAL_LINK_TEXT, "California Real Estate").click()
        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("California Real Estate Page Title is: ", driver.title)

        # Page down for search invisible element

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30 size-full"]')))
        time.sleep(2)

        # filling in the form
        name = driver.find_element(By.ID, "g2-name")
        name.send_keys(fake.first_name())
        name.clear()
        name.send_keys(fake.first_name())

        # random email with no Faker lib
        random_email = str(random.randint(0, 99999)) + "myemail" + "@example.com"

        email = driver.find_element(By.ID, "g2-email")
        # email.send_keys(random_email)
        email.send_keys(fake.email())
        email.clear()
        email.send_keys(fake.email())

        # Text message
        Message = driver.find_element(By.ID, "contact-form-comment-g2-message")
        Message.send_keys("Hello My Friend!")

        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()

        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))

        # Push button "Submit"
        submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        submit.click()

        time.sleep(2)

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()

        print(driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").get_attribute("type"))

        pageTitle = "California Real Estate – QA at Silicon Valley Real Estate"
        assert driver.title == pageTitle

    def tearDown(self):
        self.driver.quit()



class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_wordpress_Edge(self):
        fake = Faker()

        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        waits = WebDriverWait(driver, 4)
        driver.maximize_window()

        print(driver.title)
        print(driver.current_url)

        driver.find_element(By.PARTIAL_LINK_TEXT, "California Real Estate").click()
        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("California Real Estate Page Title is: ", driver.title)

        # Page down for search invisible element

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30 size-full"]')))
        time.sleep(2)

        # filling in the form
        name = driver.find_element(By.ID, "g2-name")
        name.send_keys(fake.first_name())
        name.clear()
        name.send_keys(fake.first_name())

        # random email with no Faker lib
        random_email = str(random.randint(0, 99999)) + "myemail" + "@example.com"

        email = driver.find_element(By.ID, "g2-email")
        # email.send_keys(random_email)
        email.send_keys(fake.email())
        email.clear()
        email.send_keys(fake.email())

        # Text message
        Message = driver.find_element(By.ID, "contact-form-comment-g2-message")
        Message.send_keys("Hello My Friend!")

        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))

        # Push button "Submit"
        submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        submit.click()

        time.sleep(2)

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()

        print(driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").get_attribute("type"))

        pageTitle = "California Real Estate – QA at Silicon Valley Real Estate"
        assert driver.title == pageTitle

    def test_wordpress_Edge_1120_850(self):
        fake = Faker()

        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        waits = WebDriverWait(driver, 3)
        driver.set_window_size(1120, 850)

        print(driver.title)
        print(driver.current_url)

        driver.find_element(By.PARTIAL_LINK_TEXT, "California Real Estate").click()
        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("California Real Estate Page Title is: ", driver.title)

        # Page down for search invisible element

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30 size-full"]')))
        time.sleep(2)

        # filling in the form
        name = driver.find_element(By.ID, "g2-name")
        name.send_keys(fake.first_name())
        name.clear()
        name.send_keys(fake.first_name())

        # random email with no Faker lib
        random_email = str(random.randint(0, 99999)) + "myemail" + "@example.com"

        email = driver.find_element(By.ID, "g2-email")
        # email.send_keys(random_email)
        email.send_keys(fake.email())
        email.clear()
        email.send_keys(fake.email())

        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.ID, "contact-form-comment-g2-message")))

        # Text message
        Message = driver.find_element(By.ID, "contact-form-comment-g2-message")
        Message.send_keys("Today is a great day!")

        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()

        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))

        # Push button "Submit"
        submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        submit.click()

        time.sleep(2)

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()

        print(driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").get_attribute("type"))

        pageTitle = "California Real Estate – QA at Silicon Valley Real Estate"
        assert driver.title == pageTitle

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()

    def test_wordpress_Firefox(self):
        fake = Faker()

        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        waits = WebDriverWait(driver, 4)
        self.driver.fullscreen_window()

        print(driver.title)
        print(driver.current_url)

        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()

        driver.find_element(By.PARTIAL_LINK_TEXT, "California Real Estate").click()
        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("California Real Estate Page Title is: ", driver.title)

        # Page down for search invisible element

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30 size-full"]')))
        time.sleep(2)
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)

        # filling in the form
        name = driver.find_element(By.ID, "g2-name")
        name.send_keys(fake.first_name())
        name.clear()
        name.send_keys(fake.first_name())

        # random email with no Faker lib
        random_email = str(random.randint(0, 99999)) + "myemail" + "@example.com"

        email = driver.find_element(By.ID, "g2-email")
        # email.send_keys(random_email)
        email.send_keys(fake.email())
        email.clear()
        email.send_keys(fake.email())

        # Text message
        Message = driver.find_element(By.ID, "contact-form-comment-g2-message")
        Message.send_keys("Thank you for your patience!")

        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))

        # Push button "Submit"
        submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        submit.click()

        time.sleep(2)

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()

        print(driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").get_attribute("type"))

        pageTitle = "California Real Estate – QA at Silicon Valley Real Estate"
        assert driver.title == pageTitle

    def test_wordpress_Firefox_1250_550(self):
        fake = Faker()

        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        waits = WebDriverWait(driver, 3)
        driver.set_window_size(1250, 550)

        print(driver.title)
        print(driver.current_url)

        driver.find_element(By.PARTIAL_LINK_TEXT, "California Real Estate").click()
        time.sleep(2)
        assert "California Real Estate" in driver.title
        print("California Real Estate Page Title is: ", driver.title)

        driver.find_element(By.XPATH, '//*[@value="Close and accept"]').click()

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56 size-full"]')))
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30 size-full"]')))
        time.sleep(2)

        # filling in the form
        name = driver.find_element(By.ID, "g2-name")
        name.send_keys(fake.first_name())
        name.clear()
        name.send_keys(fake.first_name())

        # random email with no Faker lib
        random_email = str(random.randint(0, 99999)) + "myemail" + "@example.com"

        email = driver.find_element(By.ID, "g2-email")
        # email.send_keys(random_email)
        email.send_keys(fake.email())
        email.clear()
        email.send_keys(fake.email())

        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.ID, "contact-form-comment-g2-message")))

        # Text message "Hello!"
        Message = driver.find_element(By.ID, "contact-form-comment-g2-message")
        Message.send_keys("Thank you!")

        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))

        # Push button "Submit"
        submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        submit.click()

        time.sleep(2)

        driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()

        print(driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").get_attribute("type"))

        pageTitle = "California Real Estate – QA at Silicon Valley Real Estate"
        assert driver.title == pageTitle

    def tearDown(self):
        self.driver.quit()