from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait

link = "https://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 20).until(
        text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element(By.ID, "book").click()

    x = int(browser.find_element(By.ID, "input_value").text)
    y = str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.ID, "answer").send_keys(str(y))

    solve_button = browser.find_element(By.ID, "solve")
    solve_button.click()
finally:
    time.sleep(30)
    browser.quit()
