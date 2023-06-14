# This program is used to illustrate timeit module
import timeit
setup='''
import numpy as np 
import pandas as pd 
import pandas as pd
df = pd.read_csv("C:/Users/adity/Pandas files/tips.csv")

def quality(total_bill,tip):
    
    if tip/total_bill> 0.25:
        return 'Generous'
    else:
        return 'Others'
'''

stmt1='''df['Quality']=df[['total_bill','tip']].apply(lambda df:quality(df['total_bill'],df['tip']),axis=1)'''
stmt2='''np.vectorize(quality)(df['total_bill'],df['tip'])'''

print('Time taken by stmt1:',timeit.timeit(setup=setup,stmt=stmt1,number=1000))
print('Time taken by stmt2:',timeit.timeit(setup=setup,stmt=stmt2,number=1000))