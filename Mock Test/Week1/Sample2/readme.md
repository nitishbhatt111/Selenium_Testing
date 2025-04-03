# Selenium Test Cases for Practice Page

## Prerequisites
- Install Python
- Install Selenium (`pip install selenium`)
- Download ChromeDriver (or any required WebDriver) and set the path

## Test Cases

### 1. Verify Page Title
**Steps:**
1. Open the browser and navigate to the page.
2. Get the title of the page.
3. Verify that the title is "Selenium Practice Page".

**Expected Result:** The page title should match.

---

### 2. Login Button Presence
**Steps:**
1. Locate the login button using `id="loginBtn"`.
2. Verify if the button is displayed.

**Expected Result:** The login button should be visible.

---

### 3. Enter Username and Password
**Steps:**
1. Locate the username input field using `id="username"`.
2. Enter a sample username.
3. Locate the password input field using `id="password"`.
4. Enter a sample password.

**Expected Result:** The entered values should be present in the fields.

---

### 4. Click on Example Link
**Steps:**
1. Locate the link using `id="exampleLink"`.
2. Click on the link.

**Expected Result:** The browser should navigate to "https://example.com".

---

### 5. Select Dropdown Option
**Steps:**
1. Locate the dropdown using `id="dropdown"`.
2. Select "Option 2".

**Expected Result:** "Option 2" should be selected.

---

### 6. Select Checkbox
**Steps:**
1. Locate the checkbox using `id="agree"`.
2. Click to check the box.
3. Verify if the checkbox is selected.

**Expected Result:** The checkbox should be checked.

---

### 7. Select Radio Button
**Steps:**
1. Locate the radio button using `id="male"`.
2. Click to select the radio button.
3. Verify if the radio button is selected.

**Expected Result:** The male radio button should be selected.

---

### 8. Verify Table Data
**Steps:**
1. Locate the table using the `<table>` tag.
2. Verify if the second row contains "Jane" and age "25".

**Expected Result:** The table data should match.

---

### 9. Verify Element by Class Name
**Steps:**
1. Locate the paragraph using `class="info"`.
2. Verify that the text matches "This is a practice page for Selenium locators.".

**Expected Result:** The paragraph text should match.

---

### 10. Verify Element by Tag Name
**Steps:**
1. Locate the first button on the page using the `<button>` tag.
2. Verify that the button text is "Login".

**Expected Result:** The button text should match.

---

### 11. Verify Partial Link Text
**Steps:**
1. Locate the "Contact Us" link using partial link text "Contact".
2. Click the link.

**Expected Result:** The browser should navigate to the contact page.

---

### 12. Verify CSS Selector
**Steps:**
1. Locate the email input field using `.email-input`.
2. Enter a sample email.
3. Verify that the email is entered correctly.

**Expected Result:** The input field should contain the entered email.

---

### 13. Verify XPath Locator
**Steps:**
1. Locate the second list item using XPath.
2. Verify that the text matches "Item 2".

**Expected Result:** The text should match "Item 2".

---

### 14. Verify Form Submission
**Steps:**
1. Enter a username and password.
2. Click the login button.
3. Verify if the user is redirected to a new page or a message is displayed.

**Expected Result:** A successful login message or redirection should occur.

---

### 15. Verify Alert Handling
**Steps:**
1. Trigger an alert box (if available).
2. Accept the alert.
3. Verify that the alert is dismissed.

**Expected Result:** The alert should be dismissed successfully.

---

### 16. Verify Browser Navigation
**Steps:**
1. Click a link to navigate to another page.
2. Use the browser back button.
3. Verify that the user is back on the original page.

**Expected Result:** The user should return to the original page.

---

### 17. Verify Keyboard Actions
**Steps:**
1. Locate the username field.
2. Use the keyboard shortcut to select all text and delete it.
3. Verify that the field is empty.

**Expected Result:** The field should be cleared.

---

### 18. Verify Mouse Hover
**Steps:**
1. Hover over an element (if available).
2. Verify if a tooltip or dropdown appears.

**Expected Result:** The expected UI element should appear.

---

### 19. Verify Window Handles
**Steps:**
1. Click on a link that opens a new tab.
2. Switch to the new tab.
3. Verify that the correct page is opened.

**Expected Result:** The expected page should be loaded in the new tab.

---

### 20. Verify File Upload
**Steps:**
1. Locate the file input field.
2. Upload a sample file.
3. Verify that the file is uploaded successfully.

**Expected Result:** The uploaded file should be processed successfully.

