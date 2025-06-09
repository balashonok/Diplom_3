from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.general_page_locators import GeneralPageLocators

class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def get_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility_of_element(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_overlaying_element_disappeared(self):
        self.wait_for_invisibility_of_element(GeneralPageLocators.OVERLAY)

    def find_element_with_wait(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    def is_displayed(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator).is_displayed()

    def click_to_element_with_wait(self, locator):
        self.wait_overlaying_element_disappeared()
        self.wait_for_clickable(locator)
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def _scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_and_scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return self._scroll_to_element(element)

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    def drag_and_drop_element(self, element_locator, destination_locator):
        from_element = self.find_element_with_wait(element_locator)
        to_element = self.find_element_with_wait(destination_locator)
        self.driver.execute_script("""
                const [from_element, to_element] = arguments;
                const dataTransfer = new DataTransfer();

                // Эмуляция событий drag-and-drop
                ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
                    const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
                    (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
                });
            """, from_element, to_element)
