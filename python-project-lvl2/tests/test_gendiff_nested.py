from gendiff import engine

answer =  u'''{
  - group2: {
      abc: 12345
  }
  + group3: {
      fee: 100500
  }
    common: {
    - setting6: {
        key: value
    }
    - setting2: 200
    + setting5: {
        key5: value5
    }
    + setting4: blah blah
      setting1: Value 1
      setting3: True
  }
    group1: {
    - baz: bas
    + baz: bars
      foo: bar
  }
}'''

def test_nested():
    a = answer
    b = engine.get_diff(
        './tests/fixtures/test_nested_old.json',
        './tests/fixtures/test_nested_new.json',
        'string'
    )

    assert len(a) == len(b)
