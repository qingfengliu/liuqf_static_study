import pandas as pd
# import difflib
# #
# # # 创建一个示例的 pandas 数据框
# # data_from=pd.read_excel(r'D:\信科\项目\ai\低碳\物资与碳排因子匹配\物资类型.xls')
# # data_aim=pd.read_excel(r'D:\信科\项目\ai\低碳\物资与碳排因子匹配\碳因子.xls')  # 假设数据存储在 'data.xlsx' 文件中
# #
# # data_from=data_from[['物资类型分组','资源编码','资源名称']]
# # data_aim=data_aim[['名称','来源类别','来源','代号','排放因子(kgCO₂)','碳因子过程','碳因子库名称']]
# #
# # #求data_from的资源名称与data_aim的名称的相似度，并且将两个数据框合并，并且转换为pandas的DataFrame格式
# # def similar(a, b):
# #     return difflib.SequenceMatcher(None, a, b).ratio()
# #
# # def match_all_similarities(data_from, data_aim):
# #     all_matches = []
# #     for index_from, row_from in data_from.iterrows():
# #         for index_aim, row_aim in data_aim.iterrows():
# #             similarity = similar(row_from['资源名称'], row_aim['名称'])
# #             match_row = {
# #                 '物资类型分组': row_from['物资类型分组'],
# #                 '资源编码': row_from['资源编码'],
# #                 '资源名称': row_from['资源名称'],
# #                 '匹配名称': row_aim['名称'],
# #                 '来源类别': row_aim['来源类别'],
# #                 '来源': row_aim['来源'],
# #                 '代号': row_aim['代号'],
# #                 '排放因子(kgCO₂)': row_aim['排放因子(kgCO₂)'],
# #                 '碳因子过程': row_aim['碳因子过程'],
# #                 '碳因子库名称': row_aim['碳因子库名称'],
# #                 '相似度': similarity
# #             }
# #             all_matches.append(match_row)
# #     return pd.DataFrame(all_matches)
# #
# #
# # data_all_similarities = match_all_similarities(data_from, data_aim)
# # data_all_similarities.to_csv(r'D:\信科\项目\ai\低碳\物资与碳排因子匹配\物资与碳因子所有相似度.csv')

#data=pd.read_csv(r'D:\信科\项目\ai\低碳\物资与碳排因子匹配\物资与碳因子所有相似度.csv')
#看一下相似度的分布情况

#取3/4分位的所有数据
#data2=data[data['相似度']>data['相似度'].quantile(0.75)]
#print(data2.shape)
#data2.to_csv(r'D:\信科\项目\ai\低碳\物资与碳排因子匹配\物资与碳因子所有相似度_3_4分位.csv', index=False)

data3=pd.read_csv(r'D:\信科\项目\ai\低碳\物资与碳排因子匹配\物资与碳因子所有相似度_3_4分位.csv')

data4=data3[data3['相似度']>0.5]
data4.to_excel(r'D:\信科\项目\ai\低碳\物资与碳排因子匹配\物资与碳因子所有相似度_0.5以上.xlsx', index=False)



