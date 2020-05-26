import os
import jieba
from reverseindex import read_dict

def read_tfidf_database(path):
    tfidf_database = {}
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split('*')
            document = parts[0].strip()
            tfidf_str = parts[1]
            tfidf_singles = tfidf_str.strip().split(' ')
            vals = []
            for single in tfidf_singles:
                vals.append(float(single))
            tfidf_database[document] = vals
    return tfidf_database

def inner_product(a, b):
    sum = 0.0001
    for x, y in zip(a, b):
        sum += x * y
    return sum


def cosin_distance(database, vector):
    similarity = {}
    for item in database:
        tfidf = list(database[item])
        distance = inner_product(tfidf, vector) / (inner_product(tfidf, tfidf) * inner_product(vector, vector))
        similarity[item] = distance
    return similarity

if __name__ == "__main__":
    proj_path = os.path.abspath(os.curdir)
    tfidf_path = os.path.join(proj_path, 'tf-idf.txt')
    tfidf_database = read_tfidf_database(tfidf_path)

    dict_path = os.path.join(proj_path, 'dict.txt')
    dict = read_dict(dict_path)
    dict_keys = dict.keys()

    search_sentence = "叶辰在昆仑虚的时候就喜欢上了孙怡吗？"
    search_keywords = jieba.cut(search_sentence)
    vector = {}
    for item in dict:
        vector[item] = 0
    for word in search_keywords:
        if word in dict_keys:
            vector[word] += 1
    item = list(vector.values())
    similar_result = cosin_distance(tfidf_database, item)
    sorted_result = sorted(similar_result.items(), key=lambda x: x[1], reverse=True)
    results = sorted_result[:10]
    for item in results:
        print(item[0])