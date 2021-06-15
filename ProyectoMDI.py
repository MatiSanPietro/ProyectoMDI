import pandas as pd
import numpy as np
import OpenBlender
import json
import matplotlib.pyplot as plt

"""## Obtener los datos"""

token = '60b690829516291fe98257255sfBVoJ7MEjjfytjEuzDLsNiKIknjE'                #Genero el API token en OpenBlender 
action = 'API_getObservationsFromDataset'

# ANCHOR: 'Bitcoin vs USD'
  
parameters = { 
    'token' : token,
    'id_dataset' : '5d4c3af79516290b01c83f51',
    'date_filter':{"start_date" : "2020-01-01",
                   "end_date" : "2020-12-31"} 
} 

df = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)

df.reset_index(drop=True, inplace=True)
df['date'] = [OpenBlender.unixToDate(ts, timezone = 'GMT') for ts in df.timestamp]
df = df.drop('timestamp', axis = 1)

df.shape

df.head()
