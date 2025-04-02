# Selenium Practice Questions

This document contains a set of Selenium test scenarios designed to help you practice various locators (ID, Name, CSS, XPath) and common Selenium interactions. Use the provided HTML template (`index.html`) to test your scripts. Each question includes a scenario, target element, and expected locator to guide your answers.

---

## Questions

### 1. ID Locator
**Scenario**: Write a Selenium script to enter "testuser" in the username field using the ID locator.  
**Target Element**:
```html
<input type="text" id="username" name="username" class="form-input" />
```

### 2. Name Locator 
**Scenario**: Write a Selenium script to enter "password123" in the password field using the Name locator.
**Target Element**:
```html
<input type="password" id="password" name="password" class="form-input" />
```

### 3. CSS Selector
**Scenario**: Click the "Login" button using a CSS Selector. 
**Target Element**:
```html
<button type="submit" id="submitBtn" class="btn">Login</button>
```

### 4. XPath Locator 
**Scenario**: Click the "Forgot Password?" link using an XPath locator. 
**Target Element**:
```html
<a href="#" id="forgotLink" class="link">Forgot Password?</a>
```
### 5. Multiple Elements with CSS 
**Scenario**: Retrieve all product names from the product list using a CSS Selector and print them. 
**Target Elements**:
```html
<span class="product-name">Laptop</span>,
<span class="product-name">Phone</span>
```
### 6. XPath with Attributes
**Scenario**: Find the price of the product with data-product-id="p2" using XPath.
**Target Element**: 
```html
<span class="price">$499</span> inside
<div class="product-item" data-product-id="p2">
```

### 7. Handling Hidden Elements 
**Scenario**: Check if the "Tablet" product is hidden using a CSS Selector and print its display status.
**Target Element**:
```html
  <div class="product-item hidden-element" data-product-id="p3">
```

### 8.Combined Locators 
**Scenario**: Enter text in the username field and click the submit button using a combination of ID and CSS locators. 
**Target Elements**:
```html
    Username input (id="username") and Submit button (class="btn")
```

### 9. XPath with Parent-Child Relationship 
**Scenario**: Find the footer text using an XPath that navigates through the parent <footer> element. 
**Target Element**:
```html
<p class="footer-text">© 2025 Selenium Practice</p>
```

### 10.  Dynamic Scenario
**Scenario**: Write a script to verify that entering a username and password, then clicking the login button, does not throw an error (assuming no real submission logic). 
**Target Elements**: 
```html
Username field, Password field, and Login button.
```

---

### Notes
- You can copy this content into a `README.md` file in your project folder.
- The questions are formatted to be clear and concise, with code blocks for target elements and expected locators.
- Feel free to tweak the scenarios or add more complexity (e.g., waiting for elements, handling alerts) to challenge each other further! Let me know if you need help with anything else.
