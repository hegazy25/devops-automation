import argparse
import os
import random
import sys
import time
import yaml


parser = argparse.ArgumentParser(description='Build Automation Script')
parser.add_argument('--config', type=str, required=True, help='path to configuration file')
parser.add_argument('--env', type=str, required=True, help='environment: dev, staging, prod')
parser.add_argument('--action', type=str,required=True, help='validate, report , apply')
args = parser.parse_args()


def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Error loading configuration file: {e}")
        sys.exit(1)

def validate_config(config, env):
    errors = []
    required_keys = ['build_steps', 'deploy_steps', 'notifications']
    
    # Check required keys exist
    for key in required_keys:
        if key not in config.get(env, {}):
            errors.append(f"Missing required key: {key}")
    
    # Validate data types
    if 'build_steps' in config[env]:
        if not isinstance(config[env]['build_steps'], list):
            errors.append(f"'build_steps' must be a list, got {type(config[env]['build_steps'])}")
    
    if 'deploy_steps' in config[env]:
        if not isinstance(config[env]['deploy_steps'], list):
            errors.append(f"'deploy_steps' must be a list, got {type(config[env]['deploy_steps'])}")
    
    # Validate value ranges (example for port if it exists)
    if 'port' in config[env]:
        port = config[env]['port']
        if not isinstance(port, int) or port < 1 or port > 65535:
            errors.append(f"Port must be integer between 1-65535, got {port}")
    
    return errors

    

def generate_report(config, env, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        report_path = os.path.join(output_dir, f"config_report_{env}_{time.strftime('%Y%m%d_%H%M%S')}.txt")
        with open(report_path, 'w') as f:
            f.write("="*70 + "\n")
            f.write(f"Configuration Report - {env.upper()} Environment\n")
            f.write("="*70 + "\n")
            f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Build Steps: {config[env]['build_steps']}\n")
            f.write(f"Deploy Steps: {config[env]['deploy_steps']}\n")
            f.write(f"Notifications: {config[env]['notifications']}\n")

        print(f"Report saved to: {report_path}")
        return 0
    except Exception as e:
        print(f"Error generating report: {e}")
        return 1




def apply_config(config, env, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Execute steps
    for step in config[env]['build_steps']:
        print(f"Executing build step: {step}")
        time.sleep(random.uniform(0.5, 1.5))
    
    # Save applied config
    applied_config_path = os.path.join(output_dir, f"{env}_config_applied.yaml")
    with open(applied_config_path, 'w') as f:
        yaml.dump(config[env], f)
    
    print(f"Configuration applied and saved to: {applied_config_path}")
    return 0


if __name__ == "__main__":
    config = load_config(args.config)
    env = args.env
    action = args.action

    if env not in config:
        print(f"Environment '{env}' not found in configuration.")
        sys.exit(1)

    if action == 'validate':
        errors = validate_config(config, env)
        if errors:
            print(f"Validation failed with {len(errors)} error(s):")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)  
        else:
            print("Configuration is valid")
            sys.exit(0)  
    
    elif action == 'report':
        exit_code = generate_report(config, env, './reports')  
        sys.exit(exit_code)
    
    elif action == 'apply':
        exit_code = apply_config(config, env, './configs')
        sys.exit(exit_code)
    
    else:
        print(f"Unknown action '{action}'. Valid actions are: validate, report, apply.")
        sys.exit(1)
