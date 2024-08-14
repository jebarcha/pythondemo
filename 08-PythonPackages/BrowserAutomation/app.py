from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
browser = webdriver.Chrome()

# Navigate to GitHub
browser.get("https://github.com")

# Find the 'Sign in' link and click it
signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

username_box = browser.find_element(By.ID, "login_field")
print(username_box)
# username_box.send_keys("jebarcha")

# password_box = browser.find_element(By.ID, "password")
# password_box.send_keys("Libertad1974$")
# password_box.submit()

# assert "jebarcha" in browser.page_source
# # make a more specific assertion:
# profile_link = browser.find_element(By.CLASS_NAME, "user-profile-link")
# link_label = profile_link.get_attribute("innerHTML")
# assert "jebarcha" in link_label, f"Expected 'jebarcha' to be in '{link_label}'"

input("Press Enter to close the browser...")
browser.quit()
