# coding:utf-8
# -----------------------------------------------------------------------------
# Comments  : 创建yolo3所需的train.txt,val.txt,test.txt
# Developer : SWLIU
# Date      : 2019-12-23
# -----------------------------------------------------------------------------
import os
import random
from config import cfg

# # trainval集占整个数据集的百分比,剩下的就是test集所占的百分比
trainval_percent = cfg.ROOT.TRAIN_VAL_PERCENT
# train集占trainval集的百分比, 剩下的就是val集所占的百分比
train_percent = cfg.ROOT.TRAIN_PERCENT
rootPath = cfg.ROOT.PATH
xmlfilepath = os.path.join(rootPath, 'Annotations')
txtsavepath = 'ImageSets'
total_xml = os.listdir(os.path.join(rootPath, xmlfilepath))

# 总数据集个数
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

#用来训练和验证的图片文件的文件名列表
ftrainval = open(os.path.join(rootPath, 'ImageSets/Main/trainval.txt'), 'w')
#用来测试的图片文件的文件名列表
ftest = open(os.path.join(rootPath, 'ImageSets/Main/test.txt'), 'w')
#是用来训练的图片文件的文件名列表
ftrain = open(os.path.join(rootPath, 'ImageSets/Main/train.txt'), 'w')
#是用来验证的图片文件的文件名列表
fval = open(os.path.join(rootPath, 'ImageSets/Main/val.txt'), 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        # 写到训练和验证集
        ftrainval.write(name)
        if i in train:
            # 在训练集里的写到测试集里
            ftest.write(name)
        else:
            # 不在训练集里，写到验证集
            fval.write(name)
    else:
        # 写到训练集
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
