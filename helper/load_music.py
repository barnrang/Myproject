from pydub import AudioSegment
import numpy as np
import os

def music_load(dir='../Music_sample',load_list=[],length=5000):
    if load_list == []:
        load_list = os.listdir(dir)
    all_file = os.listdir(dir)
    out_array = []
    load_list = list(filter(lambda x: x[-4:] == '.mp3',load_list))
    unload = 0
    for el in load_list:
        if el not in all_file:
            unload = 1
            print('Warning, file {} not found'.format(el))
            continue
        file_dir = os.path.join(dir,el)
        out_array.append(AudioSegment.from_mp3(file_dir)[:length].get_array_of_samples().tolist())
    return np.array(out_array)
