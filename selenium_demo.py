from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://www.bfr.bund.de/de/start.html")
driver.implicitly_wait(0.5)

# Find search field
element = driver.find_element(By.ID, "autocomplete-search")
element.send_keys('Campylobacter')

# Simulate pressing the Enter key
element.send_keys(Keys.RETURN)
driver.implicitly_wait(0.5)

# find dropdown and select "show 100 items"
dropdown = driver.find_element(By.ID, "search_rows")
select = Select(dropdown)
select.select_by_visible_text("50 Treffer pro Seite")

driver.implicitly_wait(0.5)

# Find all the links on the page
links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Campylobacter")
text_list = []
for i in range(len(links)):
    # Re-find the links on each iteration
    links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Campylobacter")

    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView();", links[i])

    try:
        links[i].click()
        # Retrieve the text from the clicked link
        #print(driver.find_element(By.CLASS_NAME, "textArea").text)
        #print(driver.find_element(By.TAG_NAME, "body").text)
        #print(driver.find_element(By.ID, "main").text)

        # Retrieve the text from the clicked link
        text = driver.find_element(By.TAG_NAME, "body").text

        # Store the text in the list
        text_list.append(text)

    except StaleElementReferenceException:
        continue

    # Go back to the previous page
    driver.execute_script('window.history.go(-1)')

driver.quit()

print(text_list)