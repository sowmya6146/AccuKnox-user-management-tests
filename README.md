# AccuKnox-user-management-tests

## Project Overview
Automated test suite for OrangeHRM User Management module using Playwright Python.

## Application Under Test
- **URL:** https://opensource-demo.orangehrmlive.com
- **Module:** Admin > User Management

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Project Setup

### 1. Clone the repository
```bash
git clone https://github.com/sowmya6146/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests
```

### 2. Install dependencies
```bash
pip install playwright pytest-playwright
playwright install
```

### 3. Run the test cases
```bash
pytest test_user_management.py -v
```

## Playwright Version
- Playwright: 1.43.0
- pytest-playwright: 0.5.0

## Test Cases Covered
1. Login verification
2. Navigate to User Management
3. Add new user
4. Search created user
5. Edit user role
6. Edit user status
7. Validate updated details
8. Delete user
9. Negative - password mismatch
10. Negative - duplicate username
