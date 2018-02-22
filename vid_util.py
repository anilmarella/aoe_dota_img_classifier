import cv2, os
import numpy as np

def generate_frames_from_video(video_path, target_dir, k=100):
    vidcap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    count=0
    flg = True
    while flg:
        flg, image = vidcap.read()
        if count % k == 0:
            cv2.imwrite(os.path.join(target_dir, "frame{}.jpg".format(count/k)), image)
        count += 1
    
    return os.listdir(target_dir)

def load_images_from_dir(images_dir, image_res, label):
    image_files = os.listdir(images_dir)
    m = len(image_files)
    x = np.ndarray(shape=[m, image_res[0], image_res[1], image_res[2]])
    y = np.full(shape=[m,1], fill_value=label)
    ix = 0
    for f in image_files:
        img_data = cv2.imread(os.path.join(images_dir, f))
        x[ix, :] = cv2.resize(img_data, (image_res[1], image_res[0]), interpolation=cv2.INTER_CUBIC)
        ix += 1
    
    return x, y

def shuffle(X, Y):
    shuff = np.arange(Y.shape[0])
    np.random.shuffle(shuff)
    
    return X[shuff], Y[shuff]

def load_dataset(file_label, image_res):
    list_x = []
    list_y = []
    for k in file_label:
        x, y = load_images_from_dir(file_label[k], image_res, k)
        list_x.append(x)
        list_y.append(y)
    X = np.concatenate(tuple(list_x), axis=0)
    Y = np.concatenate(tuple(list_y), axis=0)
    
    return shuffle(X, Y)

def load_data(image_res=(72,128,3)):
    game_1_path = os.path.join(os.path.curdir, 'data', 'images', 'aoe')
    game_2_path = os.path.join(os.path.curdir, 'data', 'images', 'dota')
    file_label = {1:game_1_path, 0:game_2_path}
    X, Y = load_dataset(file_label, image_res)

    return X, Y