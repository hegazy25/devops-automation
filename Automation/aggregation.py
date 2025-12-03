import argparse
import fnmatch
import os
import random
import sys
import time


parser = argparse.ArgumentParser(description='Build Automation Script')
parser.add_argument('--test-dir', type=str, required=True, help='path to test result')
parser.add_argument('--output', type=str, required=True, help='output directory for aggregation')
parser.add_argument('--format', type=str,required=True, help='aggregation format: summary or detailed')
args = parser.parse_args()

def scan_test_results(test_dir):
    tests = []
    try :
        test_files = [f for f in os.listdir(test_dir) if fnmatch.fnmatch(f, 'test_results_*.txt')]
        if not test_files:
            print("No test result files found.")
            return []
        else:
            for test_file in test_files:
                with open(os.path.join(test_dir, test_file), 'r') as f:
                    content = f.read()
                    for line in content.splitlines():
                        if line.startswith("Test:"):
                            parts = [p.strip() for p in line.split(',')]

                            test_name = parts[0].replace("Test:", "").strip()
                            test_status = parts[1].replace("Status:", "").strip()
                            test_time = parts[2].replace("Time:", "").strip()

                            err_msg = ""
                            if len(parts) > 3:
                                err_msg = parts[3].replace("Error:", "").strip()
                            
                            tests.append({
                                'name': test_name,
                                'status': test_status,
                                'timestamp': test_time,
                                'error': err_msg,
                                'file': test_file
                                })
        print(f"Found {len(tests)} tests in total.")
        return tests
    except Exception as e:
        print(f"Error reading test result: {e}")
        return []


def aggregate_test_results(tests):
    try:
        summary = {
            'total': len(tests),
            'passed': sum(1 for t in tests if t['status'] == 'PASSED'),
            'failed': sum(1 for t in tests if t['status'] == 'FAILED'),
        }
        success_rate = (summary['passed'] / summary['total'] * 100) if summary['total'] > 0 else 0

        group_by_file = {}
        for test in tests:
            if test['file'] not in group_by_file:
                group_by_file[test['file']] = []
            group_by_file[test['file']].append(test)
        
        group_by_status = {'PASSED': [], 'FAILED': []}
        for test in tests:
            group_by_status[test['status']].append(test)


        failed_tests = [t for t in tests if t['status'] == 'FAILED']


        aggregated_data = {
            'summary': summary,
            'success_rate': success_rate,
            'group_by_file': group_by_file,
            'group_by_status': group_by_status,
            'failed_tests': failed_tests
        }
        return aggregated_data
    except Exception as e:
        print(f"Error aggregating test results: {e}")
        return None

def generate_summary_report(aggregated_data, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        report_path = os.path.join(output_dir, 'summary_report.txt')
        with open(report_path, 'w') as f:
            f.write("=================================================================\n")
            f.write("Test Aggregation Report\n")
            f.write("=================================================================\n")
            f.write(time.strftime("Generated on: %Y-%m-%d %H:%M:%S\n"))
            f.write("=================================================================\n")
            f.write(f"Total Tests: {aggregated_data['summary']['total']}\n")
            f.write(f"Passed Tests: {aggregated_data['summary']['passed']}\n")
            f.write(f"Passed precentage: {aggregated_data['success_rate']:.2f}%\n")
            f.write(f"Failed Tests: {aggregated_data['summary']['failed']}\n")
            f.write("Failed percentage: {:.2f}%\n".format(100 - aggregated_data['success_rate']))
            f.write("=================================================================\n")
            f.write(f"Tests Grouped by File:\n")
            for file, tests in aggregated_data['group_by_file'].items():
                f.write(f"  {file}: {len(tests)} tests\n")
            f.write("=================================================================\n")
            f.write("Failed Tests Details:\n")
            for test in aggregated_data['failed_tests']:
                f.write(f"  Test Name: {test['name']}, File: {test['file']}, Time: {test['timestamp']}, Error: {test['error']}\n")
            f.write("=================================================================\n")
            f.write("Recommendations:\n")
            if aggregated_data['summary']['failed'] > 0:
                f.write("  - Review failed tests and fix issues.\n")
            else:
                f.write("  - All tests passed successfully. No action needed.\n")
            f.write("=================================================================\n")
            f.write("End of Report\n")
            f.write(time.strftime("Generated on: %Y-%m-%d %H:%M:%S\n"))
            f.write("=================================================================\n")
            print(f"Summary report generated at: {report_path}")
        return 0
    except Exception as e:
        print(f"Error generating summary report: {e}")
        return 1


if __name__ == "__main__":
    tests = scan_test_results(args.test_dir)
    aggregated_data = aggregate_test_results(tests)
    if aggregated_data is None:
        sys.exit(1)
    else:
        print("successfully aggregated test results.")

    if args.format == 'summary':
        exit_code = generate_summary_report(aggregated_data, args.output)
    # elif args.format == 'detailed':
    #     exit_code = generate_detailed_report(aggregated_data, args.output)
    else:
        print("Invalid format. Choose 'summary' or 'detailed'.")
        exit_code = 1

    sys.exit(exit_code)
