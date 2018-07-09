'''
Translates original bounding box representation
which describes on DARKNET site to DARKFLOW(same as VOC dataset)
also can be using for choosing sub-datasets by categories
defined by "choosed_cat" variable
'''

from PIL import Image
import os, fnmatch
from xml.etree.cElementTree import Element, SubElement, Comment, tostring
import xml.etree.cElementTree as ET
from shutil import copyfile
import sys
path = "/home/jan/Documents/autovision/blender/images/real/all/"
# path = "/media/jan/ubuntuHD/YOLO/yolo_dataset/yolo_fish/"
img_dst_path = "/home/jan/ADAS-server/home/user/darknet2.0/yolo_dataset/autovision_fish_ds/"
dst_path = "/home/jan/ADAS-server/home/user/darknet2.0/yolo_dataset/autovision_fish_annot/"
annotation_path = "/media/jan/ubuntuHD/YOLO/darknet/data/autovision.names"
choosed_cat = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def genxml(fname, fwidth, fheight, objects, annotations):

    file = os.path.join(dst_path + fname + ".xml")
    annotation = Element('annotation')

    folder = SubElement(annotation, "folder")
    folder.text = 'exported_dataset'
    filename = SubElement(annotation, "filename")
    filename.text = fname + ".png"

    size = SubElement(annotation, "size")
    width = SubElement(size, "width")
    width.text = str(fwidth)

    height = SubElement(size, "height")
    height.text = str(fheight)

    depth = SubElement(size, "depth")
    depth.text = "3"

    for obj in objects:
        try:
            if int(obj.split()[0]) in choosed_cat:
                obj = obj[:-1]
                object = Element("object")
                name = SubElement(object, "name")
                name.text = annotations[int(obj.split()[0])][:-1]

                bndbox = SubElement(object, "bndbox")
                xmin = SubElement(bndbox, "xmin")
                xmin.text = str(int(fwidth*(float(obj.split()[1]) - float(obj.split()[3])/2)))

                ymin = SubElement(bndbox, "ymin")
                ymin.text = str(int(fheight*(float(obj.split()[2]) - float(obj.split()[4])/2)))

                xmax = SubElement(bndbox, "xmax")
                xmax.text = str(int(fwidth*(float(obj.split()[1]) + float(obj.split()[3])/2)))

                ymax = SubElement(bndbox, "ymax")
                ymax.text = str(int(fheight*(float(obj.split()[2]) + float(obj.split()[4])/2)))

                annotation.append(object)
        except: pass

    if len(list(annotation)) > 3:
        tree = ET.ElementTree(annotation)
        tree.write(file)
        copyfile(os.path.join(path + fname + ".png"), os.path.join(img_dst_path + fname + ".png"))


def processing():
    with open(annotation_path) as f:
        annotations = f.readlines()
    i = 1
    pattern = "*.png"
    files = os.listdir(path)
    val = len(files)/2
    for file in files:
        if fnmatch.fnmatch(file, pattern):
            fname = file.split(".")[0]
            img = Image.open(os.path.join(path + file))
            width, height = img.size
            boxes = open(os.path.join(path + fname + ".txt")).readlines()
            genxml(fname, width, height, boxes, annotations)
            sys.stdout.write("\r %i of %i" % (i, val))
            sys.stdout.flush()
            i += 1

processing()


