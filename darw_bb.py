import os
import xml.etree.ElementTree as ET
import cv2
annot_path = "/media/jan/ubuntuHD/YOLO/yolo_dataset/yolo_quadro/people_car_quad_annot/"
img_path = "/media/jan/ubuntuHD/YOLO/yolo_dataset/yolo_quadro/people_car_quad_ds/"


def draw(img, x_annot):
    for child in x_annot:
        if child.tag == "object":
            name = child[0].text
            xmin = int(child[1][0].text)
            ymin = int(child[1][1].text)
            xmax = int(child[1][2].text)
            ymax = int(child[1][3].text)
            cv2.rectangle(img, (xmin,ymin), (xmax, ymax), (0,255,0))
    cv2.imshow("DRAWED", img)
    cv2.waitKey(-1)


files = os.listdir(annot_path)

for file in files:
    annot_json = open(os.path.join(annot_path + file))
    annot_xml = open(os.path.join(annot_path + file.split(".")[0] + ".xml"))
    img = cv2.imread(os.path.join(img_path + file.split(".")[0] + ".png"))
    # jstring = annot_json.readline()
    tree = ET.parse(annot_xml)
    root = tree.getroot()
    draw(img, root)