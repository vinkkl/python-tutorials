import pandas as pd
import numpy as np
mydata_original = {'Crop': ['Rice', 'Wheat', 'Barley', 'Maize'],
    'Yield': [1010, 1025.2, 1404.2, 1251.7],
    'cost' : [102, np.nan, 20, 68],
    'Grade': ['A', 'B', 'A', 'C']       }

mydata_new ={
      'Crop':['Rice', 'Wheat', 'Barley', 'Maize'],
      'Img' :['http://example.com/img/rice.png',
              'http://example.com/img/wheat.png',
              'http://example.com/img/barley.png',
              'http://example.com/img/maize.png'
         ]
}
df_original= pd.DataFrame(mydata_original)
df_new= pd.DataFrame(mydata_new)
df_merge=pd.merge(df_original,df_new, on='Crop', how='left')
print(df_merge)
#crops = pd.DataFrame(mydata)
#crops.dropna(how = "any")
#crops.dropna(subset=["Yield", "cost"], how ='all').shape
#crops['cost'].fillna(value='unknown', inplace=True)
#print(crops)
#filt=crops[crops['cost'] > 20]
#print(crops[crops['Grade'] == 'A'])
#print(crops[(crops['Grade'] == 'A') | (crops['Grade'] == 'C')])
#print(crops.query("cost > 5.0"))
#print(filt)
#print(crops[crops.cost.isnull()])
#crops["cost"].fillna(value="1",inplace=True)
#print(crops)
# average_cost_by_crop =crops.groupby("Crop")["cost"].mean()
# print(average_cost_by_crop)
# highest_average_cost=average_cost_by_crop.idxmax()
# print(highest_average_cost)