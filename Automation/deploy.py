import argparse
import os
import random
import sys
import time

parser = argparse.ArgumentParser(description='Build Automation Script')
parser.add_argument('--app', type=str, required=True, help='App name to deploy')
parser.add_argument('--env', type=str, required=True, help='environment to deploy to')
parser.add_argument('--server', type=str,required=True, help='server address for deployment')
parser.add_argument('--port', type=str, required=True, help='port number for deployment')
args = parser.parse_args()

def validate_environment(env):
    valid_envs = ['staging', 'production']
    if env not in valid_envs:
        raise ValueError(f"Invalid environment '{env}'. Choose from {valid_envs}.")
    print(f"Environment '{env}' validated.")
    return True

    

def validate_package(app_name):
    if not os.path.exists('./packages'):
        os.makedirs('./packages')
    
    package_path = f"./packages/{app_name}.txt"
    try:
        with open(package_path, 'r') as pkg:
            content = pkg.read()
            print(f"Package '{package_path}' found.")
            return content
    except FileNotFoundError:
        print(f"Package not found. Creating dummy package...")
        with open(package_path, 'w') as pkg:
            pkg.write(f"Application: {app_name}\nVersion: 1.0.0\nBuild: stable\n")
        with open(package_path, 'r') as pkg:
            content = pkg.read()
            return content


def deploy_application(app, env, server, port):
    try:
        validate_environment(env)
        package_content = validate_package(app)
        
        print(f"Deploying '{app}' to {env} environment on server {server}:{port}...")
        time.sleep(0.5)  # Simulate deployment time
        print("Deployment in progress...")
        time.sleep(0.5)  # Simulate deployment time
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        deploy_log_path = f"./deployments/{app}_deployment_{env}_{timestamp}.txt"
        if not os.path.exists('./deployments'):
            os.makedirs('./deployments')
        
        with open(deploy_log_path, 'w') as log_file:
            log_file.write("===============================================================================\n")
            log_file.write("=== Deployment Log ===\n")
            log_file.write("===============================================================================\n")
            log_file.write(f"Deployment started at : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            log_file.write(f"App Name: {app}\n")
            log_file.write(f"Environment: {env}\n")
            log_file.write(f"Server: {server}\n")
            log_file.write(f"Port: {port}\n")
            log_file.write("===============================================================================\n")
            log_file.write("Package Content:\n")
            log_file.write(package_content)
            log_file.write("\n===============================================================================\n")
            log_file.write("Stopping current service...\n")
            time.sleep(0.5)  # Simulate deployment time
            log_file.write("Backing up current version...\n")
            time.sleep(0.5)  # Simulate deployment time
            log_file.write("Deploying new version..\n")
            time.sleep(0.5)  # Simulate deployment time
            log_file.write("Starting new service...\n")
            time.sleep(0.5)  # Simulate deployment time
            log_file.write("===============================================================================\n")
            log_file.write("Running health checks..\n")
            #running dummy health checks
            health_check_passed = random.choice([True, True, False])  # Higher chance to pass
            if health_check_passed:
                log_file.write("Health checks passed successfully.\n")
                log_file.write("Deployment Status: Successful!\n")
                log_file.write(f"Deployment completed at : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                log_file.write("===============================================================================\n")
                print(f"Deployment completed successfully. Log located at: {deploy_log_path}")
                return 0
            else:
                log_file.write("Health checks failed!\n")
                log_file.write("Deployment Status: Failed due to health check failure.\n")
                log_file.write(f"Deployment completed at : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                log_file.write("===============================================================================\n")
                print(f"Deployment failed. Log located at: {deploy_log_path}")
                return 1
            
    except Exception as e:
        print(f"Deployment error: {e}")
        return 1
    
if __name__ == "__main__":
  exit_code = deploy_application(args.app, args.env, args.server, args.port)
  sys.exit(exit_code)