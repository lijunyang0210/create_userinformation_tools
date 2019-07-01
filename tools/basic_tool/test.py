import string

import random


def get_pwd():
    # 生成一个包含所有a-z英文大小写的字符串
    string1 = string.ascii_letters
    # 生成一个包换所有标点符号的字符串
    string2 = string.punctuation
    # 生成一个所有数字的字符串0123456789
    string3 = string.digits
    # 三个字符串拼接
    src = string1 + string2 + string3
    # 随机从拼接后的字符串取一个有五个元素的list子集，
    pwd = random.sample(src, 5)
    print(pwd)
    # 生成一个A-Z大写字符串
    string4 = string.ascii_uppercase
    # 生成一个a-z小写字符串
    string5 = string.ascii_lowercase
    #
    # pwd.extend(random.sample(string4, 1))
    # pwd.extend(random.sample(string5, 1))
    pwd.extend([random.choice(string4), random.choice(string5)])

    # random.sample(string4, 1), random.sample(string5, 1)
    print(pwd)
    random.shuffle(pwd)
    pwd = ''.join(pwd)
    print(pwd)
    return pwd


get_pwd()
