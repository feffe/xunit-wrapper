import re
from unittest.mock import Mock

import pytest
from freezegun import freeze_time

from xunitwrapper import process_to_xml


@pytest.fixture
def passed_process():
    return Mock(communicate=lambda: ("stdout".encode(), "".encode()), returncode=0)


@pytest.fixture
def failed_process():
    return Mock(communicate=lambda: ("".encode(), "stderr".encode()), returncode=1)


def process_to_xml_(process):
    return process_to_xml(process=process, test_name="test", suite_name="suite")


def test_suite_name(passed_process):
    assert re.search(
        '<testsuite .*name="suite" .*>',
        process_to_xml_(process=passed_process)
    )


def test_test_name(passed_process):
    assert re.search(
        '<testcase .*name="test" .*>',
        process_to_xml_(process=passed_process)
    )


def test_passed_process(passed_process):
    assert re.search(
        '<testsuite .*failures="0" .*>',
        process_to_xml_(process=passed_process)
    )


def test_failed_process(failed_process):
    assert re.search(
        '<testsuite .*failures="1" .*>',
        process_to_xml_(process=failed_process)
    )
    assert re.search(
        '<testcase .*>\n.*<failure',
        process_to_xml_(process=failed_process)
    )


@freeze_time("2020-01-12")
def test_zero_duration(passed_process):
    assert re.search(
        '<testsuites .*time="0.0">',
        process_to_xml_(process=passed_process)
    )
    assert re.search(
        '<testsuite .*time="0">',
        process_to_xml_(process=passed_process)
    )


def test_duration(passed_process):
    xml = process_to_xml_(process=passed_process)
    m = re.search('<testsuites .*time="(.*)">', xml)
    assert float(m.group(1)) > 0
    m = re.search('<testsuite .*time="(.*)">', xml)
    assert float(m.group(1)) > 0


def test_stdout(passed_process):
    assert re.search(
        '<testcase .*>\n.*<system-out>stdout</system-out>',
        process_to_xml_(process=passed_process)
    )


def test_stderr(failed_process):
    assert re.search(
        '<testcase .*>\n.*\n.*<system-err>stderr</system-err>',
        process_to_xml_(process=failed_process)
    )
