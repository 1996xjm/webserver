# coding=utf-8
import pandas as pd
import numpy as np

import calendar

def createExcel(year,month,data_arr):
    day_num =calendar.monthrange(year,month)[1]

    df = pd.DataFrame(data_arr)
    df['date'] = pd.to_numeric(df['date'].str.split('-',expand = True)[2])
    df = df.set_index('date')
    df = df.T
    new_columns = list(set(range(1,day_num+1)).difference(set(df.columns)))
    sum_data = pd.DataFrame(df.sum(axis=1),columns=["汇总"])
    sum_data["汇总"] =sum_data["汇总"]*10
    df[df==1] = "√"
    index = df.index
    value = df.values
    new_data = np.zeros((len(index),day_num-len(value[0]))).astype(int)
    new_df = pd.DataFrame(new_data,index=index,columns=new_columns)

    df= df.join(new_df).sort_index(axis=1)
    df[df==0] = np.nan
    finall_data = df.join(sum_data)
    finall_data.to_excel("./static/lunchexcel/{}-{}.xlsx".format(year,month))
    print(finall_data)





