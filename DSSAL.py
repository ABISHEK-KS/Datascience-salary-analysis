import pandas as pd
import numpy as np 
import pandas_profiling as pp 
fil=pd.read_excel(r'C:/Users/ksabi/OneDrive/Desktop/upload to github/DS salaries/DataWithPVTT.xlsx')
df=pd.DataFrame
print(fil) 
prof=pp.ProfileReport(fil)
prof.to_file('DSSAL.html')