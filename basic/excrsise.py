config = {
    "Database": {"host": "localhost", "port": 5432},
    "API": {"endpoint": "/api/v1", "timeout": 30}
}

def get_config(section, key):
    try :
        return config[section][key]
    except KeyError:
        return "config not found"
print(get_config("Database", "host"))  # Output: localhost


def check_servers(server_list):
    for server in server_list:
        status = "running" if server.startswith("web") else "stopped"
        print(f"Server {server} is {status}.")

servers = ["web01", "web02", "db01", "db02"]
check_servers(servers)







def process_numbers(num_list):
    result = []
    for num in num_list:
        try:
            processed = 100 / num
            result.append(processed)
        except ZeroDivisionError:
            result.append("undefined")
    return result

numbers = [10, 0, 25, 50]
print(process_numbers(numbers))  # Output: [10.0, 'undefined', 4.0, 2.0]
