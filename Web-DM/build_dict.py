import os

if __name__ == "__main__":
    proj_dir = os.path.abspath(os.curdir)
    raw_data = os.path.join(proj_dir, 'raw_data')
    files = os.listdir(raw_data)
    dict = {}
    for file in files:
        file_path = os.path.join(proj_dir, 'raw_data', file)
        with open(file_path, 'r') as f:
            text = f.readline()
            words = text.split(' ')
            for word in words:
                if word not in dict:
                    dict[word] = 1
                if word in dict:
                    dict[word] += 1
    result = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    dict_file = os.path.join(proj_dir, 'dict.txt')
    keywords_num = 300
    count = 0
    with open(dict_file, 'w') as f:
        for item in result:
            if count == keywords_num:
                break
            line = item[0] + ' ' + str(item[1]) + '\n'
            f.write(line)
            count += 1

