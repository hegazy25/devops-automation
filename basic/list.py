# List operations
servers = ["web1", "web2", "db1"]
servers.append("cache1")  # Add element
servers.remove("db1")      # Remove element
print(servers[0])          # Access by index
print(len(servers))        # Length

# List comprehension (powerful shorthand)
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]  # [1, 4, 9, 16, 25]

# Filtering with list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]  # [2, 4]
print(squared)
print(even_numbers)


# Dictionary operations
config = {"host": "localhost", "port": 8080}
config["user"] = "admin"  # Add key-value
print(config["host"])      # Access value
config.update({"debug": True})  # Update multiple
print(config)

# Iterating dictionaries
for key, value in config.items():
    print(f"{key}: {value}")

# Dictionary comprehension
ports = {f"service{i}": 8000 + i for i in range(1, 4)}
# {"service1": 8001, "service2": 8002, "service3": 8003}
