import os
import random

base_dirs = '/home/yxyl/share/train/fireworks/'

xml_list = base_dirs + 'Annotations'
train_txt = base_dirs + 'ImageSets/Main/train.txt'
test_txt = base_dirs + 'ImageSets/Main/test.txt'
test_num = 10
path_folder = os.listdir(xml_list)
path_folder.sort()
total_list = []
train_list = []
for path_folder_list in path_folder:
    # path_xml_list = xml_list + '/' + path_folder_list
    filename = os.path.splitext(os.path.split(path_folder_list)[1])[0]
    # print(filename)
    total_list.append(filename)
test_list = random.sample(total_list,test_num)
print(test_list)
print(len(total_list))
train_list = list(set(total_list) - set(test_list))
print(len(train_list))

with open(train_txt, "w") as text_file:
    for i in range(len(train_list)):
        text_file.write('%s\n' % (train_list[i]))
with open(test_txt, "w") as test_file:
    for i in range(len(test_list)):
        test_file.write('%s\n' % (test_list[i]))

