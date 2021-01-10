#muse

import pandas as pd
import numpy as  np
import os
#os.chdir('J:\\爬虫高跟鞋')
'''
df = pd.read_csv('data.csv',header=None,
                names=['商品名称','价格名称','付款人数','店铺名称','发货地址'],
                encoding='unicode_escape')
                '''
df = pd.read_csv('data.csv',header=0,encoding='gbk')
for row in df.values:
    print(row)


