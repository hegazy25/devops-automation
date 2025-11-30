try :
    result = 10 / 0
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")

try:
    my_dict = {"name": "salah"}
    print(my_dict["age"])
except KeyError:
    print("Error: Key not found in dictionary.")

try:
    import non_existent_module
except ModuleNotFoundError:
    print("Error: Module not found.")

try:
    value = int("abc")
except ValueError:
    print("Error: Invalid value for conversion.")

try:
    result = 10 + "5"
except TypeError:
    print("Error: Incompatible types for operation.")

try:
    file = open("readonly_file.txt", "w")
    file.write("This is a test.")
    file.close()
except IOError:
    print("Error: I/O operation failed.")

status = "stopped"
try:
    if status != "running":
        raise ValueError("Service is not running")
except ValueError as e:
    print(f"Error: {e}")
