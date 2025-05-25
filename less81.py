import logging
from datetime import datetime

# === Logging Configuration ===
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


# === Task 1: Log current date with INFO level ===
def log_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    logging.info(f"Current date: {current_date}")


# === Task 2: Error handling with logging ===
def simulate_error():
    try:
        result = 10 / 0
    except Exception as e:
        logging.error(f"An error occurred: {e}")


# === Task 3: Login check using assert ===
def login(username, password):
    correct_username = "admin"
    correct_password = "12345"
    try:
        assert username == correct_username and password == correct_password, \
            "Invalid username or password"
        print("Login successful")
    except AssertionError as e:
        print(e)


# === Task 4: Age check using assert ===
def check_age(age):
    try:
        assert age >= 18, "You must be 18 or older"
        print("You may use this service")
    except AssertionError as e:
        print(e)


# === Task 5: List length check using assert ===
def process_list(input_list):
    try:
        assert len(input_list) >= 3, "The list must contain at least 3 elements"
        print(f"The list contains {len(input_list)} elements")
    except AssertionError as e:
        print(e)


# === Run All Tasks ===
if __name__ == "__main__":
    log_current_date()
    simulate_error()
    login("admin", "12345")         # Valid login
    login("user", "wrongpass")      # Invalid login
    check_age(20)                   # Valid age
    check_age(15)                   # Invalid age
    process_list([1, 2, 3])         # Valid list
    process_list([1])               # Invalid list
