import argparse
import os
import random
import sys
import time

parser = argparse.ArgumentParser(description='Build Automation Script')
parser.add_argument('--logfile', type=str, required=True, help='path to the deployment log file')
parser.add_argument('--output', type=str, required=True, help='output directory for processed logs')
args = parser.parse_args()

def check_log_file(logfile):
    if not os.path.exists(logfile):
        print(f"Error: Log file '{logfile}' does not exist.")
        sys.exit(1)
    print(f"Log file '{logfile}' found.")
    return True

def check_for_errors(logfile):
    check_log_file(logfile)
    errors = []
    warnings = []
    infos = []
    debugs = []
    with open(logfile, 'r') as log_file:
        log_lines = log_file.readlines()
    errors = [line for line in log_lines if "Error" in line or "Failed" in line]
    warnings = [line for line in log_lines if "Warning" in line]
    infos = [line for line in log_lines if "Info" in line]
    debugs = [line for line in log_lines if "Debug" in line]
    return errors , warnings , infos , debugs



def process_deployment_log(logfile, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        errors, Warning , infos , debug = check_for_errors(logfile)
        output_file_path = os.path.join(output_dir, f"processed_{os.path.basename(logfile)}")
        with open(output_file_path, 'w') as output_file:
            output_file.write("===============================================================================\n")
            output_file.write("=== Processed Deployment Log ===\n")
            output_file.write("===============================================================================\n")
            output_file.write(f"Processing started at : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            output_file.write(f"Total Errors Found: {len(errors)}\n")
            output_file.write(f"Total Warning Found: {len(Warning)}\n")
            output_file.write(f"Total infos Found: {len(infos)}\n")
            output_file.write(f"Total debug Found: {len(debug)}\n")
            output_file.write("===============================================================================\n")
            if len(errors) > 0:
                output_file.write("Error Details:\n")
                for line in errors:
                    output_file.write(line)
            else:
                output_file.write("No errors found in the deployment log.\n")

            if len(Warning) > 0:
                output_file.write("\nWarning Details:\n")
                for line in Warning:
                    output_file.write(line)
            else:
                output_file.write("No warnings found in the deployment log.\n")

            if len(infos) > 0:
                output_file.write("\nInfo Details:\n")
                for line in infos:
                    output_file.write(line)
            else:
                output_file.write("No infos found in the deployment log.\n")


            if len(debug) > 0:
                output_file.write("\nDebug Details:\n")
                for line in debug:
                    output_file.write(line)
            else:
                output_file.write("No debug found in the deployment log.\n")

            output_file.write("===============================================================================\n")
            output_file.write(f"Processing completed at : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            output_file.write("===============================================================================\n")
            print(f"Processed log saved to: {output_file_path}")
        return 0
    except Exception as e:
        print(f"An error occurred while processing the log: {e}")
        return 1
    

if __name__ == "__main__":
  exit_code = process_deployment_log(args.logfile, args.output)
  sys.exit(exit_code)