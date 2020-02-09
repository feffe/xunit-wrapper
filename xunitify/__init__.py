import argparse
from subprocess import Popen, PIPE
from time import time

from junit_xml import TestSuite, TestCase


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--xunit-output-file", help="Xunit result file name", default="testreport.xml")
    parser.add_argument("--suite-name", help="Xunit suite name", default="Xunit wrapped test suite")
    parser.add_argument("--test-name", help="Xunit suite name", default="Xunit wrapped test case")
    parser.add_argument("command")
    return parser.parse_args()


def wrap_shell_command():
    args = parse_args()
    print(f"Calling following command with xunit wrapper: {args.command}")
    p = Popen(args.command, shell=True, stdout=PIPE, stderr=PIPE)
    with open(args.xunit_output_file, "w") as f:
        f.write(process_to_xml(process=p, test_name=args.test_name, suite_name=args.suite_name))


def process_to_xml(process, test_name, suite_name):
    t0 = time()
    stdout, stderr = process.communicate()
    duration = time() - t0
    tc = TestCase(name=test_name, elapsed_sec=duration, stdout=stdout.decode(), stderr=stderr.decode(),)
    if process.returncode != 0:
        tc.add_failure_info(stderr.decode())
    return TestSuite.to_xml_string([TestSuite(name=suite_name, test_cases=[tc])])
