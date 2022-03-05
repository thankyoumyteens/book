import os
import re

path1 = r'C:\Users\ILove\Downloads\论语译注\OPS/'
path2 = r'C:\Users\ILove\Downloads\论语译注\out/'

# [1]
# <a href="chapter315.html#comment1" id="comment1b">*</a>


def do_jk():
    for line in f:
        line = re.sub('\n', '', line)
        cm = re.search(r'校\s*勘', line)
        if cm:
            comment_flag = True
        while True:
            regexp = r'\((\d*)\)'
            m = re.search(regexp, line)
            if m:
                comment_no = m.group(1)
                if comment_flag:
                    line = re.sub(regexp, '<a href="' + simple_path + '#jk_back\\1" id="jk\\1">[\\1]</a>',
                                  line)
                else:
                    line = re.sub(regexp, '<a href="' + simple_path + '#jk\\1" id="jk_back\\1">[\\1]</a>',
                                  line)
            else:
                break
        print(line)
        f2.write(line)
        f2.flush()


def do_comment():
    for line in f:
        line = re.sub('\n', '', line)
        cm = re.search(r'注\s*解', line)
        if cm:
            comment_flag = True
        if not comment_flag:
            cm = re.search(r'注\s*释', line)
            if cm:
                comment_flag = True
        while True:
            regexp = r'\[(\d*)\]'
            m = re.search(regexp, line)
            if m:
                comment_no = m.group(1)
                if comment_flag:
                    line = re.sub(regexp, '<a href="' + simple_path + '#comment_back\\1" id="comment\\1">[\\1]</a>',
                                  line)
                else:
                    line = re.sub(regexp, '<a href="' + simple_path + '#comment\\1" id="comment_back\\1">[\\1]</a>',
                                  line)
            else:
                break
        print(line)
        f2.write(line)
        f2.flush()


path_array = os.listdir(path1)
for simple_path in path_array:
    if os.path.isfile(path1 + simple_path) and simple_path.endswith('html'):
        f = open(path1 + simple_path, "r", encoding="utf-8")
        f2 = open(path2 + simple_path, "w", encoding="utf-8")
        comment_flag = False
        do_jk()
        do_comment()
        f2.close()
        f.close()
