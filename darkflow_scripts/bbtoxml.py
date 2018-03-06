# translates original bounding box representation
# which describes on DARKNET site to DARKFLOW

from PIL import Image
import os, fnmatch
from xml.etree.cElementTree import Element, SubElement, Comment, tostring
import xml.etree.cElementTree as ET

path = "/media/jan/ubuntuHD/YOLO/yolo_dataset/exported_dataset/"
dst_path = "/media/jan/ubuntuHD/YOLO/darkflow/df_anotations/"
annotation_path = "/media/jan/ubuntuHD/YOLO/darknet/data/autovision.names"


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

    tree = ET.ElementTree(annotation)
    tree.write(file)
    # with open(file, "w") as f:
    #     f.write(annotation)


def processing():
    with open(annotation_path) as f:
        annotations = f.readlines()

    pattern = "*.png"
    files = os.listdir(path)
    for file in files:
        if fnmatch.fnmatch(file, pattern):
            fname = file.split(".")[0]
            img = Image.open(os.path.join(path + file))
            width, height = img.size
            boxes = open(os.path.join(path + fname + ".txt")).readlines()
            genxml(fname, width, height, boxes, annotations)


processing()


