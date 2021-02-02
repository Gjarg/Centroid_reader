from PIL import Image, ImageDraw
import numpy as np
import cv2
import matplotlib.pyplot as plt


def get_heighest_zone(filename):

    beam = Image.open(filename)
    beam_bw = beam.convert('L')
    arr = np.asarray(beam_bw).T
    zone_size = 50
    max_sum = float("-inf")
    row_idx, col_idx = 0, 0
    for row in range(arr.shape[0]-zone_size):
        for col in range(arr.shape[1]-zone_size):
            curr_sum = np.sum(arr[row:row+zone_size, col:col+zone_size])
            if curr_sum > max_sum:
                row_idx, col_idx = row, col
                max_sum = curr_sum
    col_center = col_idx + zone_size/2
    row_center = row_idx + zone_size/2
    return row_center, col_center

def get_centroid(filename):
    beam = np.copy(cv2.imread(filename))
    bw_beam = cv2.cvtColor(beam, cv2.COLOR_BGR2GRAY)
    val = cv2.minMaxLoc(bw_beam)
    col_center = val[3][0]
    row_center = val[3][1]
    return col_center, row_center, bw_beam.shape[0], bw_beam.shape[1]

def get_centroid_mask(filename):
    beam = np.copy(cv2.imread(filename))
    bw_beam = cv2.cvtColor(beam, cv2.COLOR_BGR2GRAY)
    print(bw_beam.shape)
    plt.imshow(bw_beam[250:960, 550:1280])
    val = cv2.minMaxLoc(bw_beam[250:960, 550:1280])
    max_x = val[3][0]
    max_y = val[3][1]
    s = 20
    cord1 = (max_x + s, max_y + s)
    cord2 = (max_x-s, max_y-s)
    color = (255, 0, 0)
    t = 5
    rocket_box = np.copy(beam)
    print(rocket_box.shape)
    rocket_box = cv2.rectangle(
        rocket_box[250:960, 550:1280], cord1, cord2, color, t)
    plt.imshow(rocket_box)
    plt.show()
