import datadotworld as dw
import pandas as pd
ds = dw.load_dataset('makeovermonday/2020w16', auto_update=True)
print(ds.dataframes)
#print(ds)
#print(ds.describe())
data = ds.tables['ghg_emissions_by_life_cycle_stage_ourworldindata_upload']
df = pd.DataFrame(data)
print(df)
#print(data)