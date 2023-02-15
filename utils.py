# @Date    : 2023/2/14
# @Author  : CAgAG
# @Version : 1.0
# @Function:

import os
import re

import kNN


def rename_file(old, new):
    # 重命名文件
    src = './{}'.format(old)
    if os.path.exists(src):
        dst = './{}'.format(new)
        os.rename(src, dst)


def check():
    # 检查文件夹是否正确
    rename_file('testDigits', 'test_temp')
    rename_file('testDigits(process)', 'testDigits')
    test_number, error_sum, mistakes_num, total_time, result_list, testFileList = kNN.main()
    rename_file('testDigits', 'testDigits(process)')
    rename_file('test_temp', 'testDigits')
    return test_number, error_sum, mistakes_num, total_time, result_list, testFileList


def file_dir(num, path='testDigits/'):
    # 指定数字的数据量
    dir_list = os.listdir(path)
    dir_str = '-'.join(dir_list)
    gate = re.findall(r'{}_\d+\.txt'.format(str(num)), dir_str)
    # print(type(gate))
    return len(gate) + 1


if __name__ == '__main__':
    print(file_dir(6))
