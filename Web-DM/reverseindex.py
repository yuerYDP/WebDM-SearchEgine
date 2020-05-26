import os

def read_dict(dict_path):
    dict = {}
    with open(dict_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            item = line.strip().split(' ')
            if len(item) == 2:
                dict[item[0]] = item[1]
    return dict

def getFileKeys(file_path):
    with open(file_path) as f:
        text = f.readline()
        words = text.strip().split(' ')
        keys = set(words)
        return keys


if __name__ == "__main__":
    proj_dir = os.path.abspath(os.curdir)
    dict_path = os.path.join(proj_dir, 'dict.txt')
    dict = read_dict(dict_path)
    reverse_dict = {}
    for item in dict:
        reverse_dict[item] = ''
    dict_keys_set = reverse_dict.keys()

    raw_data = os.path.join(proj_dir, 'raw_data')
    files = os.listdir(raw_data)
    for file in files:
        file_path = os.path.join(proj_dir, 'raw_data', file)
        keys = getFileKeys(file_path)
        for key in keys:
            if key in dict_keys_set:
                reverse_dict[key] = reverse_dict[key] + ' ' + file

    reverseindex_file = 'reverseindex.txt'
    reverseindex_file_path = os.path.join(proj_dir, reverseindex_file)
    with open(reverseindex_file_path, 'w') as f:
        for item in reverse_dict:
            line = item + ' * ' + reverse_dict[item] + '\n'
            f.write(line)

