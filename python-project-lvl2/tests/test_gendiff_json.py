from gendiff import engine


answer = u'''{
    host: hexlet.io
  - timeout: 50
  + timeout: 20
  - proxy: 123.234.53.22
  + verbose: True
}'''


def test_flat_json():
    a = answer
    b = engine.get_diff(
        './tests/fixtures/test_flat_before.json',
        './tests/fixtures/test_flat_after.json',
        'string'
    )

    assert len(a) == len(b)
