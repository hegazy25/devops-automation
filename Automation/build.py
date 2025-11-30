import argparse
import os
import random
import sys
import time

parser = argparse.ArgumentParser(description='Build Automation Script')
parser.add_argument('--name', type=str, required=True, help='Name of the project')
parser.add_argument('--ver', type=str, required=True, help='Version of the project')
parser.add_argument('--dir', type=str,required=True, help='output directory for the build')
args = parser.parse_args()


def run_tests():
    print("Running tests...")
    test_names = ["test_functionality", "test_performance", "test_security"]
    test_passed = 0
    test_failed = 0
    total_tests = len(test_names)
    for test in test_names:
        print(f"Running {test}...")
        if random.choice([True, False]):
            print(f"{test} passed.")
            test_passed += 1
        else:
            print(f"{test} failed.")
            test_failed += 1
    print(f"Testing completed. {test_passed} tests passed, {test_failed} tests failed out of {total_tests} total tests.")
    return test_passed, test_failed, total_tests


def build_project(name, version, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        try :
            with open('source.txt', 'r') as src:
                content = src.read()
        except FileNotFoundError:
            print("Source file not found. Creating a dummy source file.")
            with open('source.txt', 'w') as src:
                src.write("This is a dummy source file for building the project.\n")
            with open('source.txt', 'r') as src:
                content = src.read()
    
        print("compiling source file...")
        
        build_file_path = os.path.join(output_dir, f"{name}_v{version}.txt")
        with open(build_file_path, 'w') as build_file:
            build_file.write("===============================================================================\n")
            build_file.write("=== Build Output ===\n")
            build_file.write("===============================================================================\n")
            build_file.write(f"Build started at : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            build_file.write("Build Details:\n")
            build_file.write(f"Project Name: {name}\n")
            build_file.write(f"Version: {version}\n")
            build_file.write("===============================================================================\n")
            build_file.write("source Content:\n")
            build_file.write(content)
            build_file.write("\n")
            build_file.write("===============================================================================\n")
            build_file.write("=== Compilation Details ===\n")
            build_file.write(f"Compiling starts {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            build_file.write("compiling done Successful!\n")
            build_file.write("===============================================================================\n")

            test_passed, test_failed, total_tests = run_tests()
            build_file.write("\n=== Test Results ===\n")
            build_file.write(f"Total Tests: {total_tests}\n")
            build_file.write(f"Tests Passed: {test_passed}\n")
            build_file.write(f"Tests Failed: {test_failed}\n")
            build_file.write("===============================================================================\n")
            if test_failed > 0:
                build_file.write("Build Status: Failed due to test failures.\n")
                build_file.write(f"Build completed at : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                build_file.write("===============================================================================\n")
                print(f"Build completed. Output located at: {build_file_path}")
                return 1
            else:
                build_file.write("Build Status: Successful!\n")
                build_file.write(f"Build completed at : {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                build_file.write("===============================================================================\n")
                print(f"Build completed. Output located at: {build_file_path}")
                return 0
            
    except Exception as e:
        print(f"An error occurred during the build process: {e}")
        return 1


exit_code = build_project(args.name, args.ver, args.dir)
sys.exit(exit_code)
