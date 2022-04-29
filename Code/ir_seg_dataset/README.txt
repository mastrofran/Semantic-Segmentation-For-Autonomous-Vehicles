anno_json: Original annotation files. Objects were annotated by polygon, so for each object, the format of annotation is a sequence of points (each point contains x and y).

images: All images in this dataset (all:1569, day:820, night:749)

labels: We parsed json annotation into ground truth images. (0:unlabeled, 1:car, 2:person, 3:bike, 4:curve, 5:car_stop, 6:guardrail, 7:color_cone, 8:bump)

black_list.txt: contains some images without any annotation.

make_flip.py: make flipped images before training.


test.txt
train.txt
val.txt
text_night.txt
text_day.txt: are the list of test set, training set, validation set, night test set, day test set, respectively.
