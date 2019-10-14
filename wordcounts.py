from words import *


while 1:
    str0 = input("命令行:")
    list_str = str0.split()
    for item in list_str:
        if item != '-m' and item != 'wordCounts.exe' and item != '-i' and item != '-n' and item != '-o' and item != '-q':
            loc = list_str.index(item)
            if loc == 0 or loc == 1:
                print("命令有误!")
                break
            else:
                if list_str[loc-1] != '-m' and list_str[loc-1] != '-i' and list_str[loc-1] != '-n' and list_str[loc-1] != '-o':
                    print("命令有误!")
                    break
    if list_str[0] == 'wordCounts.exe':
        if '-i' in list_str:
            add = list_str.index('-i')
            try:
                fp = open(list_str[add+1], 'r+')
            except IOError:
                print("Error: 没有找到文件或读取文件失败")
            else:
                str1 = fp.read()
                str2 = "characters:\nalphabet:\nnum:\nwords:\nlines:"
                list_word = str2.split("\n")
                print(list_word[0], cal_char(str1))
                print(list_word[1], cal_alp(str1))
                print(list_word[2], cal_num(str1))
                print(list_word[3], Count_words(str1))
                print(list_word[4], file_line(str1))
                list1 = list_add(str1)
                mark1 = 0
                mark2 = 0
                if '-m' in list_str:
                    add1 = list_str.index('-m')
                    char = list_str[add1+1]
                    if char.isdigit():
                        list2 = list_addplus(list1, int(char))
                        print(buhash(list2))
                        mark1 = 1
                    else:
                        print("命令错误!")
                        fp.close()
                        continue
                if '-n' in list_str:
                    add2 = list_str.index('-n')
                    char = list_str[add2+1]
                    if char.isdigit():
                        list3 = cal_words(str1, int(char))
                        mark2 = 1
                    else:
                        print("命令错误!")
                        fp.close()
                        continue
                fp.close()
                if '-o' in list_str:
                    add3 = list_str.index('-o')
                    str3 = list_str[add3+1]
                    try:
                        fp = open(str3, 'a+')
                    except IOError:
                        print("Error: 写入文件失败!")
                    else:
                        fp.write(list_word[0]+str(cal_char(str1))+'\n')
                        fp.write(list_word[1]+str(cal_alp(str1))+'\n')
                        fp.write(list_word[2]+str(cal_num(str1))+'\n')
                        fp.write(list_word[3]+str(Count_words(str1))+'\n')
                        fp.write(list_word[4]+str(file_line(str1))+'\n')
                        if mark1 == 1:
                            for item in buhash(list2):
                                fp.write(str(item)+'\n')
                        if mark2 == 1:
                            for item in list3:
                                fp.write(str(item)+'\n')
                        fp.close()
                if '-q' in list_str:
                    print("结束!")
                    break

        else:
            print("错误命令!")


