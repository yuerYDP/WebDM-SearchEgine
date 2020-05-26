import os
import jieba

def stopwordslist(file):
    with open(file, 'r') as f:
        stopwords = [line.strip() for line in f.readlines()]
        stopwords.append(' ')
        stopwords.append('  ')
        stopwords.append('\t')
    return stopwords

def splitword(src, dst, stopwords):
    with open(src, 'r') as f:
        text = f.readline()
        result = jieba.cut(text.strip())
        output_str = ''
        for word in result:
            if word not in stopwords and word.strip() != '':
                output_str += word
                output_str += ' '
    with open(dst, 'w') as f:
        f.write(output_str)

if __name__ == "__main__":
    # 获取停用词表
    proj_dir = os.path.abspath(os.curdir)
    stopwords_file = os.path.join(proj_dir, 'stopwords.txt')
    stopwords = stopwordslist(stopwords_file)

    # 去停用词
    crawl_data = os.listdir(os.path.join(proj_dir, 'crawl_data'))
    for data in crawl_data:
        file_path = os.path.join(proj_dir, 'crawl_data', data)
        save_path = os.path.join(proj_dir, 'raw_data', data)
        splitword(file_path, save_path, stopwords)

    # 建立字典

    # 获取关键字表

    # 统计每条项目的关键字向量


