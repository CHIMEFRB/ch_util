import pandas as pd
from ch_util.andata import HKPData
import requests
from mpi4py import MPI


def worker(metric):
    print('starting worker')

    url = 'http://bao.chimenet.ca:3308/api/v1/import/prometheus'
    f = HKPData.from_acq_h5("/home/anja/scratch/hkp_prom_20200801.h5", metrics=[metric])
    df = f.select(metric)


    for time, row in df.iterrows():
        prom_metric = f"{metric}{{"
        for col in df.columns:
            # value is placed at the end of the metric
            if col == 'value' or row[col] == "-":
                continue
            prom_metric += f"{col}=\"{row[col]}\", "
        prom_metric = prom_metric[:-2]
        prom_metric += f"}} "
        # get the unix timestamp out of the pd.Timestamp object
        prom_metric += f"{row['value']} {(time - pd.Timestamp('1970-01-01')) // pd.Timedelta('1ms')}"
        params=f"upload_file={prom_metric}"
        requests.post(url, params=params)
    print(f'Finished {metric}')

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    metrics = HKPData.metrics("/home/anja/scratch/hkp_prom_20200801.h5")
else:
    metrics = []

metrics = comm.bcast(list(metrics), root=0)

worker(metrics[rank])

