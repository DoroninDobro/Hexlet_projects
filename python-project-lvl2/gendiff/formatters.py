import json


def write(dic):
    diffe = '{\n'
    dicstr = write_dic(dic)
    indent = ' ' * 2
    dicstr = indent + dicstr.replace('\n', '\n' + indent)
    diffe += dicstr
    diffe = diffe[:-3] + diffe[-1]
    return diffe


def write_dic(dic):
    variable = ('changed', 'added', 'deleted', 'unchanged', 'changeddict')
    diffe = ''
    for item in dic.items():
        if isinstance(item[1][1], dict):
            value = write(item[1][1])
        else:
            value = item[1][1]
        if item[1][0] not in variable:
            diffe += f'  {item[0]}: {item[1]}\n'
            return diffe + '}'
        if item[1][0] == 'changed':
            diffe += f"- {item[0]}: {item[1][1]}\n"
            diffe += f"+ {item[0]}: {item[1][2]}\n"
        if item[1][0] == 'added':
            diffe += f"+ {item[0]}: {value}\n"
        if item[1][0] == 'deleted':
            diffe += f"- {item[0]}: {value}\n"
        if item[1][0] == 'unchanged' or item[1][0] == 'changeddict':
            diffe += f"  {item[0]}: {value}\n"
    return diffe + '}'


def plain(dic, addon='', lines=''):
    start = "Property '" + addon
    ldic = list(dic)
    for key in ldic:
        value = dic.get(key)
        if value[0] == 'deleted':
            lines += f"{start}{key}' was removed\n"
        if value[0] == 'added':
            if isinstance(value[1], dict):
                finish = "'complex value'"
            else:
                finish = f"'{value[1]}'"
            lines += f"{start}{key}' was added with value: {finish}\n"
        if value[0] == 'changeddict':
            if isinstance(value[-1], dict):
                lines = plain(value[-1], key+'.', lines)
            else:
                lines += f"{start}{key}' was changed from '{value[1]}' to '{value[2]}'\n"  # noqa: E501
    return lines


def make_json(new):
    diffe = json.dumps(new)
    return diffe
