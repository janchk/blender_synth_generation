import json
import os
import xml.etree.ElementTree as ET

annot_path = "/home/jan/ADAS-server/home/user/darknet2.0/yolo_dataset/val_anotations/"
out_path = "/home/jan/ADAS-server/home/user/darknet2.0/yolo_dataset/val_dataset/out/"


def compare(j_annot, x_annot):
    for child in x_annot:
        if child.tag == "object":
            name = child[0].text
            xmin = int(child[1][0].text)
            ymin = int(child[1][1].text)
            xmax = int(child[1][2].text)
            ymax = int(child[1][3].text)
            for bbox in j_annot:
                print('olo')

files = os.listdir(out_path)

for file in files:
    annot_json = open(os.path.join(out_path + file))
    annot_xml = open(os.path.join(annot_path + file.split(".")[0] + ".xml"))
    jstring = annot_json.readline()
    tree = ET.parse(annot_xml)
    root = tree.getroot()
    box = json.loads(jstring)
    compare(box, root)