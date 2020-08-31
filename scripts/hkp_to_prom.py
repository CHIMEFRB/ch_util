import glob
import os
import re

from datetime import datetime
import pandas as pd
from caput import mpiutil
from ch_util.andata import HKPData
from mpi4py import MPI


def worker(h5file):
    print(f'starting {h5file}')

    with open(f'/home/anja/scratch/prom-{rank}.txt', 'a') as fp:
        fp.write(f'{h5file}')

    url = 'http://bao.chimenet.ca:3308/api/v1/import/prometheus'
    metrics = HKPData.metrics(h5file)
    prom_metrics = []
    f = HKPData.from_acq_h5(h5file, metrics=metrics)
    for metric in metrics:
        df = f.select(metric)

        for time, row in df.iterrows():
            prom_metric = f"{metric}{{"
            label_value_pairs = [f"{col}=\"{row[col]}\"" for col in df.columns if col != 'value' and row[col] != '-']
            prom_metric += ", ".join(label_value_pairs)
            prom_metric += f"}} "
            # get the unix timestamp out of the pd.Timestamp object
            prom_metric += f"{row['value']} {(time - pd.Timestamp('1970-01-01')) // pd.Timedelta('1ms')}"
            prom_metrics.append(prom_metric)

        with open(f'/home/anja/scratch/prom-{rank}.txt', 'a') as fp:
            fp.write('\n'.join(prom_metrics))
        prom_metrics = []
    print(f'finished {h5file}')
    return True

def find_files(start_time, end_time):
    glob_str = os.path.join(
            '/home/anja/projects/rpp-krs/chime/chime_online/', '*_chime_hkp', '*.h5'
            )
    list_of_files = sorted(glob.glob(glob_str))
    final_list_of_files = []
    for f in list_of_files:
        folder_datetime = re.search("(\d*T\d*)Z.*", f).groups()[0]
        folder_datetime = datetime.strptime(folder_datetime, "%Y%m%dT%H%M%S")
        if folder_datetime >= start_time and folder_datetime <= end_time:
            final_list_of_files.append(f)
    return final_list_of_files


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

list_of_files = find_files(datetime.strptime('20170701', '%Y%m%d'), datetime.strptime('20170801', '%Y%m%d'))


success = mpiutil.parallel_map(worker, list_of_files, root=0)
