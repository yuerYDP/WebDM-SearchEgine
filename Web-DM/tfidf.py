import os
import math
from reverseindex import read_dict

def getFileKeysFre(src, dst, dict):
    dict_tmp = dict
    for item in dict_tmp:
        dict_tmp[item] = 0
    dict_keys = dict_tmp.keys()

    with open(src, 'r') as f:
        text = f.readline()
        words = text.strip().split(' ')
        for word in words:
            if word in dict_keys:
                dict_tmp[word] += 1

    with open(dst, 'w') as f:
        for item in dict_tmp:
            line = item + ' ' + str(dict_tmp[item]) + '\n'
            f.write(line)

    return dict_tmp.values()

def tf_idf(dst, database, keywords_num):
    # refer to: https://blog.csdn.net/zhaomengszu/article/details/81452907
    total_documents_num = len(database)
    idf_documents_num =[]
    for i in range(keywords_num):
        idf_documents_num.append(0)
    for item in database:
        frequency = list(database[item])
        for index, val in enumerate(idf_documents_num):
            if frequency[index] > 0:
                idf_documents_num[index] = val + 1
    tf_idf_dict = {}
    for item in database:
        tf_idf = []
        for i in range(keywords_num):
            tf_idf.append(0.0)
        item_frequency = list(database[item])
        for i in range(keywords_num):
            maxval = max(item_frequency)
            tf = item_frequency[i] / (maxval + 1)
            idf = math.log(total_documents_num / (idf_documents_num[i] + 1))
            tf_idf_val = tf * idf
            tf_idf[i] = tf_idf_val
        tf_idf_dict[item] = tf_idf

    with open(dst, 'w') as f:
        for item in tf_idf_dict:
            line = item + ' * ' + ' '.join([str(i) for i in tf_idf_dict[item]]) + '\n'
            f.write(line)

if __name__ == "__main__":
    proj_dir = os.path.abspath(os.curdir)
    dict_path = os.path.join(proj_dir, 'dict.txt')
    dict = read_dict(dict_path)

    # 获得每篇文章的关键字频率
    raw_data = os.path.join(proj_dir, 'raw_data')
    files = os.listdir(raw_data)
    database = {}
    for file in files:
        file_path = os.path.join(proj_dir, 'raw_data', file)
        save_path = os.path.join(proj_dir, 'keywords_data', file)
        frequency = getFileKeysFre(file_path, save_path, dict)
        database[file] = frequency

    # 算tf-idf,并写到文件
    tf_idf_info_path = os.path.join(proj_dir, 'tf-idf.txt')
    keywords_num = len(dict)
    tf_idf(tf_idf_info_path, database, keywords_num)


