from voc_eval import voc_eval 
print voc_eval('results/{}.txt', 'VOCdevkit/VOC2007/Annotations/{}.xml', 'VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'q', '.') 

