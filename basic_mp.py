import multiprocessing as mp
from multiprocessing import Pool
import tqdm

pool_size = mp.cpu_count()

def do_job(item):

    #Do Something or return [item,false]

    return [item,False]


def batch_start(itemlist):
    
    with Pool(processes=pool_size) as pool:

        results = list(tqdm.tqdm(pool.imap(do_job,itemlist)))

        return results


if __name__ == '__main__':
    itemlist = []
    res = batch_start(itemlist)


