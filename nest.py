import sys
import json
from nested_dict import nested_dict
from copy import deepcopy


def nest(dicts: list, levels: list) -> dict:
    '''given a list of dicts returns a nested dict with the provided levels of nesting'''
    result = nested_dict()
    dicts_copy = deepcopy(dicts)  # copy to not mutate the data
    for data in dicts_copy:
        path = []
        for argument in levels:
            path.append(data[argument])
            data.pop(argument)
        exec('result["' + '"]["'.join(path) + '"]= [' + str(data) + ']', locals())
    return result.to_dict()


if __name__ == "__main__":
    if '--help' in sys.argv:
        print(
            'A program that given a json file will return a nested dictionary of dictionaries of arrays, with keys '
            'specified in command line arguments. Use example: \n'
            'cat input.json | python nest.py currency country city')
        sys.exit(0)
    input_json = json.loads(sys.stdin.read())
    levels = sys.argv[1:]
    print(json.dumps(nest(input_json, levels)))
