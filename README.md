# 🧪 Saucedemo UI Automation — Python + Selenium + Pytest

This repository contains automated UI tests for the [saucedemo.com](https://www.saucedemo.com) demo shop, implemented in **Python** using **Selenium WebDriver** and **Pytest**.  
Each test is validated and followed by a screenshot stored in `/screenshots/`.

---

## 📌 Description

The test suite covers the following UI scenarios:

- ✅ Login (valid, invalid, locked user)
- 🛒 Cart operations (add, remove, badge counter)
- 📦 Checkout process (form, overview, confirmation)
- 🧭 Navigation and product sorting

Each test saves a screenshot by name in `/screenshots/`.

---

## 🛠 Tech Stack

- Python  
- Pytest  
- Selenium WebDriver  
- ChromeDriver  
- GitHub

---

## ✅ Test Cases

| #  | Test Case                                | Status |
|----|-------------------------------------------|--------|
| 1  | Invalid login (wrong password)            | ✅     |
| 2  | Locked out user login                     | ✅     |
| 3  | Valid login                                | ✅     |
| 4  | Inventory items visible after login       | ✅     |
| 5  | Screenshot after successful login         | ✅     |
| 6  | Add item to cart                          | ✅     |
| 7  | Cart badge shows 1                        | ✅     |
| 8  | Remove item from cart                     | ✅     |
| 9  | Navigate to cart page                     | ✅     |
| 10 | Cart is empty after removal               | ✅     |
| 11 | Sort products: Name (Z to A)              | ✅     |
| 12 | Sort products: Price (Low to High)        | ✅     |
| 13 | Sort products: Price (High to Low)        | ✅     |
| 14 | Add two items and go to checkout          | ✅     |
| 15 | Complete full checkout process            | ✅     |

---

## 📂 Project Structure

```
qa-login-saucedemo-pytest/
├── conftest.py
├── requirements.txt
├── README.md
├── screenshots/
│   └── 01_invalid_login.png ... 15_checkout_complete.png
└── tests/
    └── test_saucedemo.py
```

---

## 🖼 Screenshots

### ❌ 01 – Invalid Login  
![01_invalid_login](screenshots/01_invalid_login.png)

### ❌ 02 – Locked Out User  
![02_locked_out_user](screenshots/02_locked_out_user.png)

### ✅ 03 – Valid Login  
![03_valid_login](screenshots/03_valid_login.png)

### ✅ 04 – Inventory Items Present  
![04_inventory_items_present](screenshots/04_inventory_items_present.png)

### 📸 05 – Logged In Screenshot  
![05_logged_in](screenshots/05_logged_in.png)

### 🛒 06 – Add to Cart  
![06_add_to_cart](screenshots/06_add_to_cart.png)

### 🛒 07 – Cart Badge Shows 1  
![07_cart_badge_one](screenshots/07_cart_badge_one.png)

### 🔄 08 – Remove from Cart  
![08_remove_from_cart](screenshots/08_remove_from_cart.png)

### 📦 09 – Navigate to Cart  
![09_navigate_to_cart](screenshots/09_navigate_to_cart.png)

### 📦 10 – Cart Empty After Removal  
![10_cart_empty_after_removal](screenshots/10_cart_empty_after_removal.png)

### 🔤 11 – Sort Name Z→A  
![11_sort_name_z_to_a](screenshots/11_sort_name_z_to_a.png)

### 💲 12 – Sort Price Low→High  
![12_sort_price_low_to_high](screenshots/12_sort_price_low_to_high.png)

### 💲 13 – Sort Price High→Low  
![13_sort_price_high_to_low](screenshots/13_sort_price_high_to_low.png)

### 🧾 14 – Two Items to Checkout  
![14_two_items_checkout](screenshots/14_two_items_checkout.png)

### ✅ 15 – Checkout Complete  
![15_checkout_complete](screenshots/15_checkout_complete.png)

---

## 🚀 Run Locally

1. Install Python 3.x and Chrome
2. Clone this repository
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run tests:

```bash
pytest tests/
```

5. Screenshots will be saved automatically to `/screenshots/`
