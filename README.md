# xunit-wrapper
A command line tool to wrap shell calls and generate and xunit xml based on the returncode of the call.

## Example of usage
This will generate the testreport.xml xunit xml file from a passed test.
```
xunitwrap "echo hello"
```

This will generate the testreport.xml xunit xml file from a failed test.
```
xunitwrap foo
```

This will generate the mytestreport.xml xunit xml file instead of testreport.xml default.
```
xunitwrap --xunit-output-file=mytestreport.xml foo
```

This will set testsuite and testcase name
```
xunitwrap --suite-name="My suite" --test-name="My case" foo
```

## Requirements
The tool requires version 3.6 or higher of Python.