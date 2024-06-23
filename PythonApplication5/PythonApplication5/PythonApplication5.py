#데이터 전처리

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from pandas.io.formats.style_render import Subset

# 데이터 로드
disease_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication5/PythonApplication5/fulla.csv')
farm_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication5/PythonApplication5/fullb.csv')
sanitation_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication5/PythonApplication5/c.csv')

#데이터 확인

# disease_data.info()
# farm_data.info()
# sanitation_data.info()

# #결측치 확인
#print(disease_data.isnull().sum())
# print(farm_data.isnull().sum())
#print(sanitation_data.isnull().sum())

# 결측치 처리 (결측치가 있는 행을 제거)
a=disease_data.dropna(subset=['LAT'])
b=farm_data.dropna(subset=['LAT'])
c=sanitation_data.dropna()

# #전
# print(disease_data.size)
# print(farm_data.size)
# print(sanitation_data.size)
# #후
# print(a.size)
# print(b.size)
# print(c.size)

 # 데이터 결합
# combined_data = pd.merge(a, b, on=['LAT', 'LOT'], how='inner')
# combined_data.to_csv("combined.csv", index=False)
combined_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication5/PythonApplication5/combined.csv')


# 분석
# 예: 월별 가축 질병 발생 분석
combined_data['발생월'] = pd.to_datetime(combined_data['발생일자']).dt.month
monthly_disease_stats = combined_data.groupby(['발생월', '지역']).size().unstack().fillna(0)

##파일저장 코드 farm_data.to_csv("b.csv", index=False)