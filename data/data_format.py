import os
import shutil

# ------ configuration zone ------
image_training_dir = '/home/huanlezhang/Data/KITTI/data_object_image_2/training/image_2/'
label_training_dir = '/home/huanlezhang/Data/KITTI/data_object_label_2/training/label_2/'
velodyne_training_dir = '/home/huanlezhang/Data/KITTI/pointCloudCropped/'

# ---- end of configuration ---

train_data_id_file = 'ImageSets/train.txt'
valid_data_id_file = 'ImageSets/val.txt'

SAVE_ROOT = 'DATA_DIR'

training_image_2 = os.path.join(SAVE_ROOT, 'training/image_2/')
training_label_2 = os.path.join(SAVE_ROOT, 'training/label_2/')
training_velodyne = os.path.join(SAVE_ROOT, 'training/velodyne/')
validation_image_2 = os.path.join(SAVE_ROOT, 'validation/image_2/')
validation_label_2 = os.path.join(SAVE_ROOT, 'validation/label_2/')
validation_velodyne = os.path.join(SAVE_ROOT, 'validation/velodyne')

if not os.path.exists(training_image_2):
    os.makedirs(training_image_2)
if not os.path.exists(training_label_2):
    os.makedirs(training_label_2)
if not os.path.exists(training_velodyne):
    os.makedirs(training_velodyne)
if not os.path.exists(validation_image_2):
    os.makedirs(validation_image_2)
if not os.path.exists(validation_label_2):
    os.makedirs(validation_label_2)
if not os.path.exists(validation_velodyne):
    os.makedirs(validation_velodyne)

with open(train_data_id_file, 'r') as train_data_f:
    for line in train_data_f:
        data_id = line.strip('\n\r')
        print('train ---' + data_id)
        image_2_src = os.path.join(image_training_dir, data_id + '.png')
        shutil.copy(image_2_src, training_image_2)
        label_2_src = os.path.join(label_training_dir, data_id + '.txt')
        shutil.copy(label_2_src, training_label_2)
        velodyne_src = os.path.join(velodyne_training_dir, data_id + '.bin')
        shutil.copy(velodyne_src, training_velodyne)

with open(valid_data_id_file, 'r') as valid_data_f:
    for line in valid_data_f:
        print('valid ---' + data_id)
        data_id = line.strip('\n\r')
        image_2_src = os.path.join(image_training_dir, data_id + '.png')
        shutil.copy(image_2_src, validation_image_2)
        label_2_src = os.path.join(label_training_dir, data_id + '.txt')
        shutil.copy(label_2_src, validation_label_2)
        velodyne_src = os.path.join(velodyne_training_dir, data_id + '.bin')
        shutil.copy(velodyne_src, validation_velodyne)

print('Done')
