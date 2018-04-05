import os, fnmatch
from shutil import copyfile

path = "/media/jan/ubuntuHD/YOLO/yolo_dataset/exported_dataset/"
path_to_exp = "/media/jan/ubuntuHD/YOLO/yolo_dataset/choosed_dataset/"

cts = {"bulldozer": 0, "excavator": 0, "backhoe": 0,
              "tractor": 0, "truck": 0, "grader": 0, "loader": 0, "car": 0, "person": 0}
ctspt = {"bulldozer": 0, "excavator": 0, "backhoe": 0,
              "tractor": 0, "truck": 0, "grader": 0, "loader": 0, "car": 0, "person": 0}


def pt_calc():
    all = cts["bulldozer"] + cts["excavator"] \
          + cts["backhoe"] + cts["tractor"] + cts["truck"] + \
          cts["grader"] + cts["loader"] + cts["car"] + cts["person"]

    ctspt["bulldozer"] = round(cts["bulldozer"]/all, 3)
    ctspt["excavator"] = round(cts["excavator"]/all, 3)
    ctspt["backhoe"] = round(cts["backhoe"]/all, 3)
    ctspt["tractor"] = round(cts["tractor"]/all, 3)
    ctspt["truck"] = round(cts["truck"]/all, 3)
    ctspt["grader"] = round(cts["grader"]/all, 3)
    ctspt["loader"] = round(cts["loader"]/all, 3)
    ctspt["car"] = round(cts["car"]/all, 3)
    ctspt["person"] = round(cts["person"]/all, 3)


def export(file):
    file = file.split(".")[0]
    txtf = open(os.path.join(path + file + ".txt"))
    dsttxt = os.path.join(path_to_exp + file + ".txt")
    dstimg = os.path.join(path_to_exp + file + ".png")
    lines = txtf.readlines()
    for line in lines:
        cat = int(line.split(" ")[0])
        if cat == 1:
            try:
                copyfile(os.path.join(path + file + ".png"), dstimg)
                copyfile(txtf.name, dsttxt)
            except:
                print('no such image: ', file)





def calc(file):
    lines = file.readlines()
    for line in lines:
        cat = int(line.split(" ")[0])
        if cat == 0:
            cts["bulldozer"] += 1
        elif cat == 1:
            cts["excavator"] += 1
        elif cat == 2:
            cts["backhoe"] += 1
        elif cat == 3:
            cts["tractor"] += 1
        elif cat == 4:
            cts["truck"] += 1
        elif cat == 5:
            cts["grader"] += 1
        elif cat == 6:
            cts["loader"] += 1
        elif cat == 7:
            cts["car"] += 1
        elif cat == 8:
            cts["person"] += 1



pattern = "*.txt"
files = os.listdir(path)

for file in files:
    if fnmatch.fnmatch(file, pattern):
        export(file)
        txtf = open(os.path.join(path + file))
        calc(txtf)

pt_calc()
print(cts)
