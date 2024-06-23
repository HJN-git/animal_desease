#���� �߻� ���� �м� - �ð��� ����/ ������ ���� / ���� ������ ����/ ������
#����-LAT, �浵-LOT

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

# ������ �ε�
disease_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication6/PythonApplication6/fulla.csv')
farm_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication6/PythonApplication6/fullb.csv')
sanitation_data = pd.read_csv('C:/Users/user/source/repos/PythonApplication6/PythonApplication6/c.csv')
diseasefarm = pd.read_csv('C:/Users/user/source/repos/PythonApplication6/PythonApplication6/combined.csv')

#�ð��� ���� �м�

# ��¥ ������ Ÿ�� ��ȯ �� ��,�� ����

# diseasefarm['OCCRRNC_DE']= pd.to_datetime(diseasefarm['OCCRRNC_DE'].astype(str), format='%Y%m%d')

# diseasefarm['year']=diseasefarm['OCCRRNC_DE'].dt.year
# diseasefarm['month']=diseasefarm['OCCRRNC_DE'].dt.month

# grouped=diseasefarm.groupby(['year','month'])['OCCRRNC_LVSTCKCNT'].sum().reset_index()


# # ������ ���� ���ļ� datetime �������� ��ȯ
# diseasefarm['date'] = pd.to_datetime(diseasefarm['year'].astype(str) + '-' + diseasefarm['month'].astype(str), format='%Y-%m')

# # ������ ���� ���� �ߺ��Ǽ� �ð�ȭ
# plt.figure(figsize=(10, 6))
# sns.lineplot(data=diseasefarm, x='date', y='OCCRRNC_LVSTCKCNT', hue='year', marker='o', markers=True, palette='tab20', alpha=1)
# plt.title('Year-Monthly Livestock Disease Occurrence')
# plt.xlabel('Date')
# plt.ylabel('Disease Count')
# plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')  # ���� ��ġ ����
# plt.grid(True)
# plt.show()


# # ������ ���� ���� �ߺ��Ǽ� �ð�ȭ2-2
# years = diseasefarm['year'].unique()

# plt.figure(figsize=(10, 6))

# markers = ['o', 's', '^']  # ��, �簢��, �ﰢ�� ��Ŀ

# for i, year in enumerate(years):
#     df_year = diseasefarm[diseasefarm['year'] == year]
#     sns.lineplot(data=df_year, x='month', y='OCCRRNC_LVSTCKCNT', label=year, marker=markers[i % len(markers)], ci=None)

# plt.title('Year-Monthly disease')
# plt.xlabel('Month')
# plt.ylabel('Disease Count')
# plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')  # ���� ��ġ ����
# plt.grid(True)
# plt.show()

#������ ���� �м�

# import folium
# from folium.plugins import HeatMap

# # �ѱ��� �߽� ��ǥ ���� (����)
# map_center = [37.5665, 126.9780]

# # Folium ���� ����
# m = folium.Map(location=map_center, zoom_start=8)

# # ���� �߻� ��ġ �߰�
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

# # ���� ���� �� ���
# m.save('Location_red.html')

#���� ������ ���� �м�

# # ���� ������ ���� �߻� ��
# animal_pattern = diseasefarm['LVSTCKSPC_NM'].value_counts().reset_index()
# animal_pattern.columns = ['LVSTCKSPC_NM', 'OCCRRNC_LVSTCKCNT']

# # �ѱ� ��Ʈ ���� (Windows ����, MacOS �� Linux�� �ٸ� �� ����)
# plt.rcParams['font.family'] = 'Malgun Gothic'  # '���� ���'���� ����

# # �ð�ȭ
# plt.figure(figsize=(12, 6))
# sns.barplot(data=animal_pattern, x='LVSTCKSPC_NM', y='OCCRRNC_LVSTCKCNT')
# plt.title('livestock types')
# plt.xlabel('LVSTCKSPC_NM')
# plt.ylabel('OCCRRNC_LVSTCKCNT')
# plt.xticks(rotation=45)
# plt.show()

#������ ���� �м�

# # ������ ���� �߻� ��
# animal_pattern = diseasefarm['LKNTS_NM'].value_counts().reset_index()
# animal_pattern.columns = ['LKNTS_NM', 'OCCRRNC_LVSTCKCNT']

# # �ѱ� ��Ʈ ����
# plt.rcParams['font.family'] = 'Malgun Gothic'  # '���� ���'���� ����

# # �ð�ȭ
# plt.figure(figsize=(12, 6))
# sns.barplot(data=animal_pattern, x='LKNTS_NM', y='OCCRRNC_LVSTCKCNT')
# plt.title('livestock types')
# plt.xlabel('LKNTS_NM')
# plt.ylabel('OCCRRNC_LVSTCKCNT')
# plt.xticks(rotation=45)
# plt.show()

#���� �м� - �󰡿� ���� �߻� ��ġ �� �Ÿ� ���/ �濪�ü��� �� �� �Ÿ� ���


# ���� �� ������ �������� ������ ������ ���������� ��ȯ�մϴ� (Point ��ü ����)
geometry_disease = [Point(xy) for xy in zip(disease_data['LOT'], disease_data['LAT'])]
gdisease_data = gpd.GeoDataFrame(disease_data, geometry=geometry_disease, crs='EPSG:4326')

geometry_farm = [Point(xy) for xy in zip(farm_data['LOT'], farm_data['LAT'])]
gfarm_data = gpd.GeoDataFrame(farm_data, geometry=geometry_farm, crs='EPSG:4326')

geometry_veterinary = [Point(xy) for xy in zip(sanitation_data['LOT'], sanitation_data['LAT'])]
gsanitation_data = gpd.GeoDataFrame(sanitation_data, geometry=geometry_veterinary, crs='EPSG:4326')

# ���� �м��� ���� �ε����� �����մϴ� (���� ����)

gdisease_data = gdisease_data.set_index('LKNTS_NM')
gfarm_data = gfarm_data.set_index('ROW_NUM')
gsanitation_data = gsanitation_data.set_index('PSTN_DSNF_PLC_NM')

print(gdisease_data.columns) �������� �������..


# # ���÷� ��Ŭ���� �Ÿ� ��� �Լ��� �����մϴ�
# def calculate_distance(row):
#     dist = distance((row['LAT_x'], row['LOT_x']), (row['LAT_y'], row['LOT_y'])).km
#     return dist

# # 1. �������� �����Ϳ� �� ��ġ ������ ���� �Ÿ� ���
# distance_df = gpd.sjoin(gdisease_data, gfarm_data, how="inner", op='intersects')
# print(distance_df.columns)
#distance_df.to_csv("distance_df.csv", index=False)
# distance_df['distance(km)'] = distance_df.apply(lambda x: calculate_distance(x), axis=1)


# # 2. �濪�ü��� �� ���� �Ÿ� ���
# distance_veterinary_df = gpd.sjoin(gsanitation_data, gfarm_data, how="inner", op='intersects')[['PSTN_DSNF_PLC_NM', 'ROW_NUM', 'geometry']]
# distance_veterinary_df['�Ÿ�(km)'] = distance_veterinary_df.apply(lambda x: calculate_distance(x), axis=1)

# # 1,2 ��� ���
# print("�������� �����Ϳ� �� ��ġ ������ ���� �Ÿ�:")
# print(distance_df)

# print("\n�濪�ü��� �� ���� �Ÿ�:")
# print(distance_veterinary_df)

##�������� �ڵ� farm_data.to_csv("b.csv", index=False)
