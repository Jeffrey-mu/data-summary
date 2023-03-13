import pandas as pd


def concant_data(path, start_data, end_data, type='normal'):
  if type == 'normal':
    column = ['Dimension.AD_UNIT_NAME','Dimension.DATE','Dimension.HOUR','Dimension.SITE_NAME','Dimension.AD_UNIT_ID','Column.AD_EXCHANGE_TOTAL_REQUESTS','Column.AD_EXCHANGE_MATCH_RATE','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_IMPRESSIONS','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CLICKS','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CTR','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_AVERAGE_ECPM','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE','Column.AD_EXCHANGE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS_RATE']
    result_column = ['Dimension.AD_UNIT_NAME','Dimension.DATE','Dimension.SITE_NAME','Dimension.AD_UNIT_ID','Column.AD_EXCHANGE_TOTAL_REQUESTS','Column.AD_EXCHANGE_MATCH_RATE','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_IMPRESSIONS','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CLICKS','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CTR','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_AVERAGE_ECPM','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE','Column.AD_EXCHANGE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS_RATE']
    concant_column = ['Dimension.AD_UNIT_NAME', 'Dimension.DATE', 'Dimension.AD_UNIT_ID', 'Dimension.SITE_NAME']
  elif type == 'country':
    column = ['Dimension.AD_UNIT_NAME','Dimension.COUNTRY_NAME','Dimension.DATE','Dimension.HOUR','Dimension.SITE_NAME','Dimension.AD_UNIT_ID','Dimension.COUNTRY_CRITERIA_ID','Column.AD_EXCHANGE_TOTAL_REQUESTS','Column.AD_EXCHANGE_MATCH_RATE','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_IMPRESSIONS','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CLICKS','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CTR','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_AVERAGE_ECPM','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE','Column.AD_EXCHANGE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS_RATE']
    result_column = ['Dimension.AD_UNIT_NAME','Dimension.COUNTRY_NAME','Dimension.DATE','Dimension.SITE_NAME','Dimension.AD_UNIT_ID','Dimension.COUNTRY_CRITERIA_ID','Column.AD_EXCHANGE_TOTAL_REQUESTS','Column.AD_EXCHANGE_MATCH_RATE','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_IMPRESSIONS','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CLICKS','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CTR','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_AVERAGE_ECPM','Column.AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE','Column.AD_EXCHANGE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS_RATE']
    concant_column = ['Dimension.AD_UNIT_NAME','Dimension.COUNTRY_NAME','Dimension.DATE','Dimension.SITE_NAME','Dimension.AD_UNIT_ID','Dimension.COUNTRY_CRITERIA_ID',]
  # 读取csv文件，并指定使用的列
  df = pd.read_csv(path, usecols=column)

  # 筛选出前一天16点之后的数据
  yesterday_after_4pm = df[(df['Dimension.DATE'] == start_data) & (df['Dimension.HOUR'] >= 16)]

  # 筛选出今天16点之前的数据
  today_before_4pm = df[(df['Dimension.DATE'] == end_data) & (df['Dimension.HOUR'] < 16)]
  # 将两个数据集合并起来
  df_filtered['Column.AD_EXCHANGE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS_RATE'] = df_filtered['Column.AD_SERVER_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS'] / df_filtered['Column.TOTAL_ACTIVE_VIEW_MEASURABLE_IMPRESSIONS']
  # 将两个数据集合并起来，并选择需要的列
  df_filtered = pd.concat([yesterday_after_4pm, today_before_4pm])[result_column]

  # 按照AD_UNIT_NAME，AD_UNIT_ID和DATE进行分组，并对分组后的数据进行求和
  df_sum = df_filtered.groupby(concant_column).sum()

  # 保存到csv文件
  df_sum.to_csv(path)
    # Dimension.AD_UNIT_NAME,Dimension.COUNTRY_NAME,Dimension.DATE,Dimension.HOUR,Dimension.SITE_NAME,Dimension.AD_UNIT_ID,Dimension.COUNTRY_CRITERIA_ID,Column.AD_EXCHANGE_TOTAL_REQUESTS,Column.AD_EXCHANGE_MATCH_RATE,Column.AD_EXCHANGE_LINE_ITEM_LEVEL_IMPRESSIONS,Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CLICKS,Column.AD_EXCHANGE_LINE_ITEM_LEVEL_CTR,Column.AD_EXCHANGE_LINE_ITEM_LEVEL_AVERAGE_ECPM,Column.AD_EXCHANGE_LINE_ITEM_LEVEL_REVENUE,Column.AD_EXCHANGE_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS_RATE
concant_data('./data/topfun-2023-03-12:20:47:08-2023-03-06~2023-03-07 copy.csv', '2023-03-06', '2023-03-07')
