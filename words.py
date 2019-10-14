from collections import Counter
def cal_char(str1):
    count = 0
    for char in str1:
        if char >= ' ' and char <= '~':
            count+=1
    return count


def cal_alp(str1):
    count = 0
    for char in str1:
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
            count += 1
    return count

def cal_num(str1):
    count = 0
    for char in str1:
        if char >= '0' and char <= '9':
            count += 1
    return count


def list_add(str1=''):
    list1 = []
    str2 = " "
    str3 = ""
    for i in range(len(str1)):
        if str2 == ' ':
            if (str1[i] >= 'a' and str1[i] <= 'z') or (str1[i] >= 'A' and str1[i] <= 'Z'):
                str3 += str1[i]
                str2 = 'Y'
        elif str2 == 'Y':
            if (str1[i] == ' '):
                list1.append(str3)
                str3 = ''
                str2 == ' '
            elif (str1[i] >= 'a' and str1[i] <= 'z') or (str1[i] >= 'A' and str1[i] <= 'Z'):
                str3 += str1[i]
    if str3 != '':
        list1.append(str3)
    return list1


def list_addplus(list1,length):
    list3=[]
    i=0
    l = len(list1)
    if l<length:
        print("词组长度过大\n")
        return None
    else:
        while i+length<=len(list1):
            list2=[]
            for j in range(length):
                list2.append(list1[i+j])
            list3.append(list2)
            i+=1
        return list3

def buhash(list3):
    d = {}
    seen = set()
    for item in list3:
        val = tuple(item)
        if val not in seen:
            seen.add(val)
            d.setdefault(val,1)
        else:
            for get_l in d.keys():
                if tuple(item) == get_l:
                    d[get_l]+=1
                    break
    return d


def file_line(str1):
    count=0
    if str1 =='':
        return count
    count = 1
    for item in str1:
        if item=="\n":
            count+=1
    return count


def Count_words(str1):
    words = list_add(str1.lower())
    words_counts = Counter(words)
    return len(words_counts)

def cal_words(str1, num):
    words = list_add(str1.lower())
    words_counts = Counter(words)
    if len(words_counts) < num:
        print("单词数不足%d，所有单词词频为:"%(num))
        top = words_counts.most_common(len(words_counts))
    else:
        top = words_counts.most_common(num)
        print("词频最高的%d个单词为:"%num)
        for item in top:
            print("%s:%d" % (item[0], item[1]))
    return top
