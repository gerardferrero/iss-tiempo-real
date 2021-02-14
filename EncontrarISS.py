#!/usr/bin/env python3

import pandas as pd
import plotly as ply
import plotly.express as px

import time

url = 'http://api.open-notify.org/iss-now.json'

while True:
    df = pd.read_json(url)


    df['latitude'] = df.loc['latitude','iss_position']
    df['longitude'] = df.loc['longitude','iss_position']
    df.reset_index(inplace=True)
    #print(df)
    df = df.drop(['index','message'], axis=1)
    print(df)
    fig = px.scatter_geo(df, lat='latitude',
                        lon='longitude')
    #fig.show()
    ply.offline.plot(fig,filename="ISS.html",auto_open=False)
    time.sleep(45)
    
    