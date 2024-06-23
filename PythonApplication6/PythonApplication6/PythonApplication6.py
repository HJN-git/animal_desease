#질병 발생 패턴 분석 - 시간적 패턴/ 공간적 패턴 / 가축 종류별 패턴/ 질병별
#위도-LAT, 경도-LOT

from cProfile import label
from calendar import month
from string import printable
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point
import numpy as np
from geopy.distance import distance

# 데이터 로드
disease_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication6/PythonApplication6/fulla.csv')
farm_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication6/PythonApplication6/fullb.csv')
sanitation_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication6/PythonApplication6/c.csv')
diseasefarm = pd.read_csv('C:/Users/user/source/repos/PythonApplication6/PythonApplication6/combined.csv')

#시간적 패턴 분석

# 날짜 데이터 타입 변환 및 년,월 추출

# diseasefarm['OCCRRNC_DE']= pd.to_datetime(diseasefarm['OCCRRNC_DE'].astype(str), format='%Y%m%d')

# diseasefarm['year']=diseasefarm['OCCRRNC_DE'].dt.year
# diseasefarm['month']=diseasefarm['OCCRRNC_DE'].dt.month

# grouped=diseasefarm.groupby(['year','month'])['OCCRRNC_LVSTCKCNT'].sum().reset_index()


# # 연도와 월을 합쳐서 datetime 형식으로 변환
# diseasefarm['date'] = pd.to_datetime(diseasefarm['year'].astype(str) + '-' + diseasefarm['month'].astype(str), format='%Y-%m')

# # 연도별 월별 농장 발병건수 시각화
# plt.figure(figsize=(10, 6))
# sns.lineplot(data=diseasefarm, x='date', y='OCCRRNC_LVSTCKCNT', hue='year', marker='o', markers=True, palette='tab20', alpha=1)
# plt.title('Year-Monthly Livestock Disease Occurrence')
# plt.xlabel('Date')
# plt.ylabel('Disease Count')
# plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')  # 범례 위치 조정
# plt.grid(True)
# plt.show()


# # 연도별 월별 농장 발병건수 시각화2-2
# years = diseasefarm['year'].unique()

# plt.figure(figsize=(10, 6))

# markers = ['o', 's', '^']  # 원, 사각형, 삼각형 마커

# for i, year in enumerate(years):
#     df_year = diseasefarm[diseasefarm['year'] == year]
#     sns.lineplot(data=df_year, x='month', y='OCCRRNC_LVSTCKCNT', label=year, marker=markers[i % len(markers)], ci=None)

# plt.title('Year-Monthly disease')
# plt.xlabel('Month')
# plt.ylabel('Disease Count')
# plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')  # 범례 위치 조정
# plt.grid(True)
# plt.show()

#공간적 패턴 분석

# import folium
# from folium.plugins import HeatMap

# # 한국의 중심 좌표 설정 (서울)
# map_center = [37.5665, 126.9780]

# # Folium 지도 생성
# m = folium.Map(location=map_center, zoom_start=8)

# # 질병 발생 위치 추가
# for idx, row in diseasefarm.iterrows():
#     folium.CircleMarker(
#         location=[row['LAT'], row['LOT']],
#         radius=1,
#         color='red',
#         fill=True,
#         fill_color='red',
#         fill_opacity=0.6,
#         popup=f"FARM_NM: {row['FARM_NM']}<br>LKNTS_NM: {row['LKNTS_NM']}<br>LVSTCKSPC_NM: {row['LVSTCKSPC_NM']}"
#     ).add_to(m)

# # 지도 저장 및 출력
# m.save('Location_red.html')

#가축 종류별 패턴 분석

# # 가축 종류별 질병 발생 수
# animal_pattern = diseasefarm['LVSTCKSPC_NM'].value_counts().reset_index()
# animal_pattern.columns = ['LVSTCKSPC_NM', 'OCCRRNC_LVSTCKCNT']

# # 한글 폰트 설정 (Windows 기준, MacOS 및 Linux는 다를 수 있음)
# plt.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정

# # 시각화
# plt.figure(figsize=(12, 6))
# sns.barplot(data=animal_pattern, x='LVSTCKSPC_NM', y='OCCRRNC_LVSTCKCNT')
# plt.title('livestock types')
# plt.xlabel('LVSTCKSPC_NM')
# plt.ylabel('OCCRRNC_LVSTCKCNT')
# plt.xticks(rotation=45)
# plt.show()

#질병별 패턴 분석

# # 질병별 질병 발생 수
# animal_pattern = diseasefarm['LKNTS_NM'].value_counts().reset_index()
# animal_pattern.columns = ['LKNTS_NM', 'OCCRRNC_LVSTCKCNT']

# # 한글 폰트 설정
# plt.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정

# # 시각화
# plt.figure(figsize=(12, 6))
# sns.barplot(data=animal_pattern, x='LKNTS_NM', y='OCCRRNC_LVSTCKCNT')
# plt.title('livestock types')
# plt.xlabel('LKNTS_NM')
# plt.ylabel('OCCRRNC_LVSTCKCNT')
# plt.xticks(rotation=45)
# plt.show()

#공간 분석 - 농가와 질병 발생 위치 간 거리 계산/ 방역시설과 농가 간 거리 계산


# 먼저 각 데이터 프레임을 지리적 데이터 프레임으로 변환합니다 (Point 객체 생성)
geometry_disease = [Point(xy) for xy in zip(disease_data['LOT'], disease_data['LAT'])]
gdisease_data = gpd.GeoDataFrame(disease_data, geometry=geometry_disease, crs='EPSG:4326')

geometry_farm = [Point(xy) for xy in zip(farm_data['LOT'], farm_data['LAT'])]
gfarm_data = gpd.GeoDataFrame(farm_data, geometry=geometry_farm, crs='EPSG:4326')

geometry_veterinary = [Point(xy) for xy in zip(sanitation_data['LOT'], sanitation_data['LAT'])]
gsanitation_data = gpd.GeoDataFrame(sanitation_data, geometry=geometry_veterinary, crs='EPSG:4326')

# 공간 분석을 위해 인덱스를 설정합니다 (선택 사항)

gdisease_data = gdisease_data.set_index('LKNTS_NM')
gfarm_data = gfarm_data.set_index('ROW_NUM')
gsanitation_data = gsanitation_data.set_index('PSTN_DSNF_PLC_NM')

print(gdisease_data.columns) 질병명이 사라졌다..


# # 예시로 유클리드 거리 계산 함수를 정의합니다
# def calculate_distance(row):
#     dist = distance((row['LAT_x'], row['LOT_x']), (row['LAT_y'], row['LOT_y'])).km
#     return dist

# # 1. 가축질병 데이터와 농가 위치 데이터 간의 거리 계산
# distance_df = gpd.sjoin(gdisease_data, gfarm_data, how="inner", op='intersects')
# print(distance_df.columns)
#distance_df.to_csv("distance_df.csv", index=False)
# distance_df['distance(km)'] = distance_df.apply(lambda x: calculate_distance(x), axis=1)


# # 2. 방역시설과 농가 간의 거리 계산
# distance_veterinary_df = gpd.sjoin(gsanitation_data, gfarm_data, how="inner", op='intersects')[['PSTN_DSNF_PLC_NM', 'ROW_NUM', 'geometry']]
# distance_veterinary_df['거리(km)'] = distance_veterinary_df.apply(lambda x: calculate_distance(x), axis=1)

# # 1,2 결과 출력
# print("가축질병 데이터와 농가 위치 데이터 간의 거리:")
# print(distance_df)

# print("\n방역시설과 농가 간의 거리:")
# print(distance_veterinary_df)

##파일저장 코드 farm_data.to_csv("b.csv", index=False)
