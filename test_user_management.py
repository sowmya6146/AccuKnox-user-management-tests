import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://opensource-demo.orangehrmlive.com"
USERNAME = "Admin"
PASSWORD = "admin123"
TEST_USERNAME = "testuser_sowmya"
TEST_PASSWORD = "Test@12345"


def login(page: Page):
    page.goto(f"{BASE_URL}/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/dashboard**")


def navigate_to_user_management(page: Page):
    page.get_by_role("link", name="Admin").click()
    page.get_by_role("menuitem", name="Users").click()
    expect(page.get_by_role("heading", name="System Users")).to_be_visible()


# TC_UM_001
def test_login(page: Page):
    page.goto(f"{BASE_URL}/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(re.compile(".*dashboard.*"))


# TC_UM_002
def test_navigate_to_user_management(page: Page):
    login(page)
    navigate_to_user_management(page)
    expect(page.get_by_role("heading", name="System Users")).to_be_visible()


# TC_UM_003
def test_add_new_user(page: Page):
    login(page)
    navigate_to_user_management(page)
    page.get_by_role("button", name="Add").click()
    page.locator("form").get_by_role("combobox").nth(0).select_option(label="Admin")
    page.locator("form").get_by_role("combobox").nth(1).select_option(label="Enabled")
    page.get_by_placeholder("Type for hints...").fill("Paul")
    page.wait_for_selector(".oxd-autocomplete-dropdown")
    page.locator(".oxd-autocomplete-option").first.click()
    page.get_by_placeholder("Username").fill(TEST_USERNAME)
    page.locator("input[type='password']").nth(0).fill(TEST_PASSWORD)
    page.locator("input[type='password']").nth(1).fill(TEST_PASSWORD)
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Successfully Saved")).to_be_visible()


# TC_UM_004
def test_search_user(page: Page):
    login(page)
    navigate_to_user_management(page)
    page.get_by_placeholder("Username").fill(TEST_USERNAME)
    page.get_by_role("button", name="Search").click()
    expect(page.get_by_role("cell", name=TEST_USERNAME)).to_be_visible()


# TC_UM_005
def test_edit_user_role(page: Page):
    login(page)
    navigate_to_user_management(page)
    page.get_by_placeholder("Username").fill(TEST_USERNAME)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="Edit").click()
    page.locator("form").get_by_role("combobox").nth(0).select_option(label="ESS")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Successfully Updated")).to_be_visible()


# TC_UM_006
def test_edit_user_status(page: Page):
    login(page)
    navigate_to_user_management(page)
    page.get_by_placeholder("Username").fill(TEST_USERNAME)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="Edit").click()
    page.locator("form").get_by_role("combobox").nth(1).select_option(label="Disabled")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Successfully Updated")).to_be_visible()


# TC_UM_007
def test_validate_updated_details(page: Page):
    login(page)
    navigate_to_user_management(page)
    page.get_by_placeholder("Username").fill(TEST_USERNAME)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="Edit").click()
    expect(page.locator("form").get_by_role("combobox").nth(0)).to_have_value("ESS")


# TC_UM_008
def test_delete_user(page: Page):
    login(page)
    navigate_to_user_management(page)
    page.get_by_placeholder("Username").fill(TEST_USERNAME)
    page.get_by_role("button", name="Search").click()
    page.get_by_role("checkbox").nth(1).check()
    page.get_by_role("button", name="Delete Selected").click()
    page.get_by_role("button", name="Yes, Delete").click()
    expect(page.get_by_text("Successfully Deleted")).to_be_visible()


# TC_UM_009 - Negative
def test_password_mismatch(page: Page):
    login(page)
    navigate_to_user_management(page)
    page.get_by_role("button", name="Add").click()
    page.locator("input[type='password']").nth(0).fill("Test@12345")
    page.locator("input[type='password']").nth(1).fill("Test@99999")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Passwords do not match")).to_be_visible()


# TC_UM_010 - Negative
def test_duplicate_username(page: Page):
    login(page)
    navigate_to_user_management(page)
    page.get_by_role("button", name="Add").click()
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Already exists")).to_be_visible()
