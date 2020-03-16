from gendiff import engine

answer =  u"""Property 'group2' was removed
Property 'group3' was added with value: 'complex value'
Property 'common.setting6' was removed
Property 'common.setting2' was removed
Property 'common.setting5' was added with value: 'complex value'
Property 'common.setting4' was added with value: 'blah blah'
"""


def test_plain():
    a = answer
    b = engine.get_diff(
        './tests/fixtures/test_nested_old.json',
        './tests/fixtures/test_nested_new.json',
        'plain'
    )

    assert len(a) == len(b)
