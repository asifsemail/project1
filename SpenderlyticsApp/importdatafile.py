import pandas as pd

def importdata(f):
    importdata.data = pd.DataFrame(pd.read_csv(f))
