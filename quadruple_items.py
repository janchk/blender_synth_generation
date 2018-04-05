import os, fnmatch
from PIL import Image
import sys

path = "/home/jan/Documents/autovision/blender/images/real/excavator/"
dst_path = "/home/jan/Documents/autovision/blender/images/real/excavator_quadro/"


def bb_transform(boxes, fname):
    f = open(os.path.join(dst_path, fname + "_quadro" + ".txt"), "a")
    # f.write("\n")
    for box in boxes:
        st = box.split()
        st = [float(x) for x in st]
        f.write("\n%i %f %f %f %f" % (st[0], .5 * st[1], .5 * st[2], .5 * st[3], .5 * st[4]))
        f.write("\n%i %f %f %f %f" % (st[0], .5 * st[1] + 0.5, .5 * st[2], .5 * st[3], .5 * st[4]))
        f.write("\n%i %f %f %f %f" % (st[0], .5 * st[1], .5 * st[2] + 0.5, .5 * st[3], .5 * st[4]))
        f.write("\n%i %f %f %f %f" % (st[0], .5 * st[1] + 0.5, .5 * st[2] + 0.5, .5 * st[3], .5 * st[4]))
        # f.write(st[0] + " " + .5*st[1] + " " + .5*st[2] + .5*st[3] + .5*st[4])
    f.close()


pattern = "*.png"
files = os.listdir(path)
i = 1
val = len(files)/2
for file in files:
    if fnmatch.fnmatch(file, pattern):
        fname = file.split(".")[0]
        img = Image.open(os.path.join(path + file))
        w, h = (img.size[0], img.size[1])
        new_img = Image.new("RGB", (w * 2, h * 2))
        new_img.paste(img, (0, 0))
        new_img.paste(img, (w, 0))
        new_img.paste(img, (0, h))
        new_img.paste(img, (w, h))

        boxes = open(os.path.join(path + fname + ".txt")).readlines()
        bb_transform(boxes, fname)
        new_img.save(os.path.join(dst_path, fname + "_quadro" + ".png"))
        sys.stdout.write("\r %i of %i" % (i, val))
        sys.stdout.flush()
        i += 1
