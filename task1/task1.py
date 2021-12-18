import re


def task1_use_regular(input_str):
    result_str = input_str
    res = re.search(r'\([^\)]*$', input_str)
    if res:
        result_str = input_str[:res.start()]
    return result_str


def task1_use_foreach(input_str):
    last_open = -1
    need_remove = False
    ix = 0
    for x in input_str:
        if '(' == x:
            if not need_remove:
                last_open = ix
            need_remove = True
        if ')' == x:
            need_remove = False
        ix += 1
    result_str = input_str[0:last_open if need_remove else ix]

    return result_str


if __name__ == '__main__':
    print(task1_use_foreach('esdfd((esdf)(esdf'))
