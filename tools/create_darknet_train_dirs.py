# coding:utf-8
# -----------------------------------------------------------------------------
# Comments  : 创建darknet-yolo3训练所需的文件夹
# Developer : SWLIU
# Date      : 2019-12-23
# -----------------------------------------------------------------------------
import os
from config import cfg

def mkdir(path):

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

if __name__=='__main__':
    rootPath = cfg.ROOT.PATH
    mkdir(os.path.join(rootPath, 'Annotations'))
    mkdir(os.path.join(rootPath,'ImageSets'))
    mkdir(os.path.join(rootPath,'JPEGImages'))
    mkdir(os.path.join(rootPath,'labels'))
    mkdir(os.path.join(rootPath,'Self'))
    mkdir(os.path.join(rootPath,'ImageSets/Main'))
    mkdir(os.path.join(rootPath,'Self/DarknetLabel'))
    mkdir(os.path.join(rootPath,'Self/DarknetModel'))
    mkdir(os.path.join(rootPath,'Self/Test'))