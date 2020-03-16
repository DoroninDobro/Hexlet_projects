from gendiff.parsers import parsers
from gendiff.formatters import write, plain, make_json


def starter(args):
    print(get_diff(args.first_file, args.second_file, format='string'))


def get_diff(first_file, second_file, format=''):
    before = parsers(first_file)
    after = parsers(second_file)
    new = diff(before, after)
    if format == 'plain':
        diffe = plain(new)
    elif format == 'json':
        diffe = make_json(new)
    else:
        diffe = write(new)
    return diffe


def diff(old, new):
    diffe = {}
    kold = old.keys()
    knew = new.keys()
    deleted = kold - knew
    for key in deleted:
        diffe[key] = ['deleted', old.get(key)]
    added = knew - kold
    for key in added:
        diffe[key] = ['added', new.get(key)]
    bothed = knew & kold
    for key in bothed:
        oldvalue = old.get(key)
        newvalue = new.get(key)
        if oldvalue != newvalue:
            if isinstance(oldvalue, dict) and isinstance(newvalue, dict):
                diffe[key] = ['changeddict', diff(oldvalue, newvalue)]
            else:
                diffe[key] = ['changed', oldvalue, newvalue]
        else:
            diffe[key] = ['unchanged', oldvalue]
    return(diffe)
