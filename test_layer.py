import json
import pandas as pd
import numpy as np
import paramiko
import pysftp


def lambda_handler(event, context):
    # test for pandas
    data = {'name':["Tom", "John", "Andre", "Sam"], 
        'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
        'score':[90, 40, 80, 98]} 
  
    df = pd.DataFrame(data) 
    print(df.head())
    print('----------------')
    # test for paramiko
    client = paramiko.SSHClient()
    print(client)
    print('----------------')
    # test for pysftp
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    print(cnopts)
    print('----------------')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }