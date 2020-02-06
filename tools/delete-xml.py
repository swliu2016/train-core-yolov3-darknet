import os
import shutil

base_dir='/home/yxyl/share/train/fireworks/'

if __name__ == '__main__':
    xml_dirs = base_dir + 'JPEGImages/'
    test_image =base_dir +  'Annotations/'
    # print(data[0].split(';', 6))
    for image in os.listdir(test_image):
        print(image)
        filename = os.path.splitext(os.path.split(image)[1])[0]
        if not os.path.exists(xml_dirs + filename + '.jpg'):
            print('delete:',image)
            os.remove(test_image + image)
    print('over')
