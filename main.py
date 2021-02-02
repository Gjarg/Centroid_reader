import os
import concurrent.futures
import numpy as np
import matplotlib.pyplot as plt
import cv2
import h5py
from functions import get_centroid

if __name__ == '__main__':

    os.chdir('images')
    beam_liste = os.listdir()
    array_centroid = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(get_centroid, beam_liste)
        for r in results:
            array_centroid.append(r)
    os.chdir("..")
    f = h5py.File("centroid.hdf5", "w")
    f.create_dataset("centroid", data=array_centroid)
    print(array_centroid)
