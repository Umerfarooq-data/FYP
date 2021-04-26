import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import sys
def make_record(user_data):
    return {
        'Virus name':user_data[0], # X
        'Virus family':user_data[1],
        'DNA(0)/RNA(1)':user_data[2],
        'Virus genus':user_data[3],
        'Average genome length (Nucleotides)':user_data[4],
        'Replication in the cytoplasm (True:1)':user_data[5],
        'Vector-borne or not (True:1)':user_data[6],
        'enveloped/non-enveloped (True:1)':user_data[7],
        'vSegmentedTF (True:1)':user_data[8],
        'Zoonotic or not (True:1)':user_data[9] # X
    }


data = pd.read_excel("Clean genomic dataset.xlsx")
# print(data.head(2))
# data = data.append(
#     make_record(['African_green_monkey_polyomavirus','Polyomaviridae',	0, 'Polyomavirus',5270	,1	,0	,1	,0	,1]), 
#     ignore_index=True)
# u_data = sys.argv[1:]

user_x = []
for arg in sys.argv[1:]:
    if(arg.isdigit()):
        user_x.append(int(arg))
    else:
        user_x.append(arg)


user_x.append(0)
# print(user_x)
# print(make_record(user_x))

data = data.append(make_record(user_x), ignore_index=True)
# data.loc[len(data.index)] = ['Adelaide_River_virus',	'Rhabdoviridae'	,1	,'Ephemerovirus'	,14627,	1,	1	,0,	0]
# print(data.tail(3))
data['Virus family'] = LabelEncoder().fit_transform(data['Virus family'])
X = data[['Virus family','vSegmentedTF (True:1)', 'Vector-borne or not (True:1)', 'enveloped/non-enveloped (True:1)', 
          'DNA(0)/RNA(1)', 'Replication in the cytoplasm (True:1)','Average genome length (Nucleotides)']].values
Y = data['Zoonotic or not (True:1)'].values
X= preprocessing.StandardScaler().fit(X).transform(X)
# x_train, x_test = train_test_split(X, shuffle = False, stratify = None)


risk_model = joblib.load('risk_model.sav')
zoonotic_model = joblib.load('zoonotic_model.sav')
# # data  = ['Adelaide_River_virus',	'Rhabdoviridae'	,1	,'Ephemerovirus'	,14627,	1,	1	,0,	0]
# # data['Virus family'] = LabelEncoder().fit_transform(data['Virus family'])
x1=risk_model.predict([X[-1]])
x2=zoonotic_model.predict([X[-1]])
# x = ['Adelaide_River_virus',	'Rhabdoviridae'	,1	,'Ephemerovirus'	,14627,	1,	1	,0,	0]
#print(X[-1])
print(x1[0], x2[0])
#print('First paramenter ', sys.argv[1])