#������ ��ó��

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from pandas.io.formats.style_render import Subset

# ������ �ε�
disease_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication5/PythonApplication5/fulla.csv')
farm_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication5/PythonApplication5/fullb.csv')
sanitation_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication5/PythonApplication5/c.csv')

#������ Ȯ��

# disease_data.info()
# farm_data.info()
# sanitation_data.info()

# #����ġ Ȯ��
#print(disease_data.isnull().sum())
# print(farm_data.isnull().sum())
#print(sanitation_data.isnull().sum())

# ����ġ ó�� (����ġ�� �ִ� ���� ����)
a=disease_data.dropna(subset=['LAT'])
b=farm_data.dropna(subset=['LAT'])
c=sanitation_data.dropna()

# #��
# print(disease_data.size)
# print(farm_data.size)
# print(sanitation_data.size)
# #��
# print(a.size)
# print(b.size)
# print(c.size)

 # ������ ����
# combined_data = pd.merge(a, b, on=['LAT', 'LOT'], how='inner')
# combined_data.to_csv("combined.csv", index=False)
combined_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication5/PythonApplication5/combined.csv')


# �м�
# ��: ���� ���� ���� �߻� �м�
combined_data['�߻���'] = pd.to_datetime(combined_data['�߻�����']).dt.month
monthly_disease_stats = combined_data.groupby(['�߻���', '����']).size().unstack().fillna(0)

##�������� �ڵ� farm_data.to_csv("b.csv", index=False)