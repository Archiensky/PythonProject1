# Task 1: User age group lookup
users = {
    "Olena": "Adults",
    "Ivan": "Teenagers",
    "Maria": "Children",
    "Andriy": "Adults"
}

name = input("Enter the user's name: ")

if name in users:
    print(f"{name} belongs to the age group: {users[name]}")
else:
    print("User not found.")

print("\n---\n")

# Task 2: Convert input to integer with error handling
try:
    number = int(input("Enter a number: "))
    print(f"You entered the integer: {number}")
except ValueError:
    print("Error: The input is not a valid number.")

print("\n---\n")

# Task 3: Read file content with exception handling
file_path = input("Enter the path to the file: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")

print("\n---\n")

# Task 4: Import module and call a function with error handling
module_name = input("Enter the name of the module to import: ")
function_name = input("Enter the function name to call from the module: ")

try:
    module = __import__(module_name)
    func = getattr(module, function_name)
    print(f"Calling function {function_name} from module {module_name}...")
    func()
except ImportError:
    print(f"Error: Module '{module_name}' could not be imported.")
except AttributeError:
    print(f"Error: Function '{function_name}' not found in module '{module_name}'.")
