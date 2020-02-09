# xunitify
A command line tool to wrap shell calls and generate and xunit xml based on the returncode of the call.

## Example of usage
This will generate the testreport.xml xunit xml file from a passed test.
```
xunitfy "echo hello"
```

This will generate the testreport.xml xunit xml file from a failed test.
```
xunitfy foo
```

This will generate the mytestreport.xml xunit xml file instead of testreport.xml default.
```
xunitfy --xunit-output-file=mytestreport.xml foo
```

This will set testsuite and testcase name
```
xunitfy --suite-name="My suite" --test-name="My case" foo
```

## Requirements
The tool requires version 3.6 or higher of Python.