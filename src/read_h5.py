import h5py
import numpy as np
import os

script_dir = os.path.dirname(__file__) 

rel_path = '../data/msd_summary_file.h5'
abs_file_path = os.path.join(script_dir, rel_path)

with h5py.File(abs_file_path, 'r+') as hdf:
    ls = list(hdf.keys())
    print('number of datasets: \n', ls)
    data = hdf.get('musicbrainz')
    dataset = np.array(data)
