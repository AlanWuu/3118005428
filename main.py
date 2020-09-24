import re
import sys
from math import sqrt
import jieba
  
def file_reader(filename,filename2):
    file_words = {}
    ignore_list = ['<','>','?','!','.',',','=','&','，','。'] #设置停用词
    accepted_chars = re.compile(u"[a-zA-Z0-9\u4e00-\u9fa5]") #限定只匹配中文
    file_object = open(filename,encoding='UTF-8')
    #分词  
    try:
        all_the_text = file_object.read()
        seg_list = jieba.cut(all_the_text, cut_all=True)
        for s in seg_list:
            if accepted_chars.match(s) and s not in ignore_list:
                if s not in file_words.keys():
                    file_words[s] = [1,0]
                else:
                    file_words[s][0] += 1
    finally:
        file_object.close()
  
    file_object2 = open(filename2,encoding='UTF-8')
  
    try:
        all_the_text = file_object2.read()
        seg_list = jieba.cut(all_the_text, cut_all=True)
        for s in seg_list:
            if accepted_chars.match(s) and s not in ignore_list:
                if s not in file_words.keys():
                    file_words[s] = [0,1]
                else:
                    file_words[s][1] += 1
    finally:
        file_object2.close()
    #利用余弦相似性算法计算相似性
    sum_2 = 0
    sum_file1 = 0
    sum_file2 = 0
    for word in file_words.values():
        sum_2 += word[0]*word[1]
        sum_file1 += word[0]**2
        sum_file2 += word[1]**2
  
    rate = sum_2/(sqrt(sum_file1*sum_file2))
    #保留两位小数并输出答案文件
    file=open(sys.argv[3],'w')
    file.write(str(int(rate * 100) / 100))
    file.close()
    

file_reader(sys.argv[1],sys.argv[2]) #从命令行获取文件地址
