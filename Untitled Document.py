import os

train = os.path.join("/media/jan/My Files/autovision/train.txt")
validate = os.path.join("/media/jan/My Files/autovision/validate.txt")
with open(train, "w") as file:
    for i in range(0, 22752):
        file.write(("/media/jan/My Files/autovision/dataset_export/" + "%06d" + ".png\n") % i)

with open(validate, "w") as file:
    for i in range(22752, 23752):
        file.write(("/media/jan/My Files/autovision/dataset_export/" + "%06i" + ".png\n") % i)
