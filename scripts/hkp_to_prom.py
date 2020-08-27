import requests
import pandas as pd
from ch_util.andata import HKPData
from multiprocessing import Process, Pool

metrics = HKPData.metrics("/home/anja/scratch/hkp_prom_20200801.h5")
f = HKPData.from_acq_h5("/home/anja/scratch/hkp_prom_20200801.h5", metrics=metrics)
url = 'http://bao.chimenet.ca:3308/api/v1/import/prometheus'

def worker(f, metric):

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

if __name__ == '__main__':
    with Pool(47) as p:
        p.map(worker, metrics)
