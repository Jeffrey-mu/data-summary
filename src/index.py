import pandas as pd
df = pd.read_csv('./data/topfun-2023-03-12:20:47:08-2023-03-06~2023-03-07.csv')
# df = pd.read_csv('./data//topfun-2023-03-12:20:31:53-2023-03-05~2023-03-06.csv')
# 将日期列和小时列合并为datetime格式

# 按条件筛选数据
income_3_5 = df[(df['Dimension.DATE'] == '2023-03-06') & (df['Dimension.HOUR'] >= 16)]['Column.AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE'].sum()
income_3_6 = df[(df['Dimension.DATE'] == '2023-03-07') & (df['Dimension.HOUR'] < 16)]['Column.AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE'].sum()

# 输出结果
print('3.5汇总：',income_3_5 + income_3_6)
# print('3.6汇总：',income_3_5 + income_3_6)



