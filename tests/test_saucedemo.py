# test_saucedemo.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


BASE_URL = "https://www.saucedemo.com/"


def login(driver, username, password):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def take_screenshot(driver, name):
    driver.save_screenshot(f"screenshots/{name}.png")


# 1. Invalid login (wrong password)
def test_invalid_login(driver):
    login(driver, "standard_user", "wrong_password")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Username and password do not match" in error.text
    take_screenshot(driver, "01_invalid_login")


# 2. Locked out user
def test_locked_out_user(driver):
    login(driver, "locked_out_user", "secret_sauce")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "locked out" in error.text.lower()
    take_screenshot(driver, "02_locked_out_user")


# 3. Valid login
def test_valid_login(driver):
    login(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
    take_screenshot(driver, "03_valid_login")


# 4. Page contains inventory items after login
def test_inventory_items_present(driver):
    login(driver, "standard_user", "secret_sauce")
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0
    take_screenshot(driver, "04_inventory_items_present")


# 5. Screenshot after successful login
def test_screenshot_after_login(driver):
    login(driver, "standard_user", "secret_sauce")
    take_screenshot(driver, "05_logged_in")
    assert driver.current_url.endswith("/inventory.html")
    # 6. Add product to cart
def test_add_to_cart(driver):
    login(driver, "standard_user", "secret_sauce")
    add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_button.click()
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"
    take_screenshot(driver, "06_add_to_cart")


# 7. Check cart badge shows 1 item
def test_cart_badge_shows_one(driver):
    login(driver, "standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"
    take_screenshot(driver, "07_cart_badge_one")


# 8. Remove item from cart
def test_remove_from_cart(driver):
    login(driver, "standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(1)  # slight delay to let DOM update
    elements = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(elements) == 0
    take_screenshot(driver, "08_remove_from_cart")


# 9. Navigate to cart page
def test_navigate_to_cart(driver):
    login(driver, "standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "/cart.html" in driver.current_url
    take_screenshot(driver, "09_navigate_to_cart")


# 10. Cart is empty after removing item
def test_cart_empty_after_removal(driver):
    login(driver, "standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0
    take_screenshot(driver, "10_cart_empty_after_removal")
    # 11. Sort products by name Z to A
def test_sort_name_z_to_a(driver):
    login(driver, "standard_user", "secret_sauce")
    sort_select = driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_select.click()
    sort_select.find_element(By.CSS_SELECTOR, "option[value='za']").click()
    time.sleep(1)
    take_screenshot(driver, "11_sort_name_z_to_a")


# 12. Sort products by price low to high
def test_sort_price_low_to_high(driver):
    login(driver, "standard_user", "secret_sauce")
    sort_select = driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_select.click()
    sort_select.find_element(By.CSS_SELECTOR, "option[value='lohi']").click()
    time.sleep(1)
    take_screenshot(driver, "12_sort_price_low_to_high")


# 13. Sort products by price high to low
def test_sort_price_high_to_low(driver):
    login(driver, "standard_user", "secret_sauce")
    sort_select = driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_select.click()
    sort_select.find_element(By.CSS_SELECTOR, "option[value='hilo']").click()
    time.sleep(1)
    take_screenshot(driver, "13_sort_price_high_to_low")


# 14. Add two items and go to checkout
def test_add_two_items_and_checkout(driver):
    login(driver, "standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    assert "/checkout-step-one.html" in driver.current_url
    take_screenshot(driver, "14_two_items_checkout")


# 15. Complete full checkout flow
def test_complete_checkout(driver):
    login(driver, "standard_user", "secret_sauce")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Step 1: user info
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Step 2: overview
    driver.find_element(By.ID, "finish").click()

    # Step 3: confirmation
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    complete_header = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "THANK YOU FOR YOUR ORDER" in complete_header.text.upper()
    take_screenshot(driver, "15_checkout_complete")
