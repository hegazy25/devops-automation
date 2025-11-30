#basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("DevOps"))

#function with default parameters
def power(base, exponent=2):
    return base ** exponent
print(power(3))
print(power(3, 3))

#function with variable-length arguments

def summarize(*args):
    return sum(args)
print(summarize(1, 2, 3, 4, 5))
my_list = [10, 20, 30]
print(summarize(*my_list)) # Correctly calls summarize(10, 20, 30)


#function with keyword arguments
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="salah", age=30, city="Cairo")