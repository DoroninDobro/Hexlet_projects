from gendiff import engine

answer = u'''{
    constant: yep
  - test: bar
  + test: foo
  - foo: bar
  + bar: foo
}'''


def test_flat_yml():
    a = answer
    b = engine.get_diff(
        './tests/fixtures/test_flat_before.yml',
        './tests/fixtures/test_flat_after.yml',
        'string'
    )

    assert len(a) == len(b)
