#!/usr/bin/python
import time
import pandas as pd
import requests
import sys
def table_test(name1,name2,name3):
    df = pd.DataFrame([[name1,16,'BBA'],
                       [name2,19,'BTech'],
                       ['asd',18,'BSc']],
                      columns = ['Name','Age','Course'])
    js = df.to_json(orient = 'columns')
    print(js)
    return js
test
table_test(sys.argv[1], sys.argv[2] ,sys.argv[3])