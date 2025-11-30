# Define valid services
valid_services = ["nginx", "docker", "ssh", "mysql"]

def restart_service(service_name, valid_list):
    if service_name not in valid_list:
        raise ValueError(f"Service '{service_name}' does not exist.")
    
    print(f"Restarting {service_name} service...")
    print(f"{service_name} service restarted successfully.")


# Test services (includes valid and invalid ones)
services_to_restart = ["nginx", "salah", "web", "docker", "ssh", "mysql"]

print("=" * 50)
print("Service Restart Process")
print("=" * 50)

# Loop through services and restart them
for svc in services_to_restart:
    try:
        restart_service(svc, valid_services)
    except ValueError as e:
        print(f"Error: {e}")
    print()  # Blank line for readability

print("=" * 50)
print("Restart process completed.")
print("=" * 50)
