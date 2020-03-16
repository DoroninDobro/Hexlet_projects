[![Build Status](https://travis-ci.org/DoroninDobro/python-project-lvl2.svg?branch=master)](https://travis-ci.org/DoroninDobro/python-project-lvl2)
[![Maintainability](https://api.codeclimate.com/v1/badges/2c02e226be1d1b3cb9ae/maintainability)](https://codeclimate.com/github/DoroninDobro/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2c02e226be1d1b3cb9ae/test_coverage)](https://codeclimate.com/github/DoroninDobro/python-project-lvl2/test_coverage)

# Diff generator

This is the utility for getting diff between two json or yaml files.

Bellow you may see the way to install and use the package:
```
pip install --user --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ doronindobro-gendiff
```
[![asciicast](https://asciinema.org/a/Yat6jXgeNv770FEfdu0OdsoGi.svg)](https://asciinema.org/a/Yat6jXgeNv770FEfdu0OdsoGi)

## Diff between two flat yaml or json files:
```
gendiff files/before.json files/after.json
```
The output in the string format by default:
```
{
    constant: yep
  - test: bar
  + test: foo
  - foo: bar
  + bar: foo
}
```

[![asciicast](https://asciinema.org/a/gb0vPYgaYN8Gk99g67TI1RinT.svg)](https://asciinema.org/a/gb0vPYgaYN8Gk99g67TI1RinT)

[![asciicast](https://asciinema.org/a/RSPq6K32D0K6eNRfbzHhrjOA7.svg)](https://asciinema.org/a/RSPq6K32D0K6eNRfbzHhrjOA7)

## Diff between two recursive structured files:
```
gendiff tests/fixtures/test_nested_old.json tests/fixtures/test_nested_new.json
```
Output:
```
{
    common: {
        setting1: Value 1
      - setting2: 200
        setting3: true
      - setting6: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
    }
  - group2: {
        abc: 12345
    }
  + group3: {
        fee: 100500
    }
}
```
[![asciicast](https://asciinema.org/a/bSkg2qN79N3pXylU7evns9yUq.svg)](https://asciinema.org/a/bSkg2qN79N3pXylU7evns9yUq)


## Diff between two files in plain and json format:
```
gendiff tests/fixtures/test_nested_old.json tests/fixtures/test_nested_new.json -f plain
```
```
Property "common.setting2" was removed
Property "common.setting6" was removed
Property "common.setting4" was added with value: "blah blah"
Property "common.setting5" was added with value: "complex value"
Property "group1.baz" was changed. From "bas" to "bars"
Property "group2" was removed
Property "group3" was added with value: "complex value"
```
[![asciicast](https://asciinema.org/a/JIzQBVZg0sDOvutY3s31lYmjr.svg)](https://asciinema.org/a/JIzQBVZg0sDOvutY3s31lYmjr)

To get diff between two files in json format use the command:
[![asciicast](https://asciinema.org/a/JowxwCOFcmer54sQEcpF4zCHN.svg)](https://asciinema.org/a/JowxwCOFcmer54sQEcpF4zCHN)

