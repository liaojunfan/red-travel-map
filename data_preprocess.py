import pandas as pd

# 黔南红色点位测试数据集
site_data = [
    {"name":"猴场会议会址","lon":107.48,"lat":27.05,"category":"会议遗址"},
    {"name":"邓恩铭故居","lon":107.37,"lat":26.58,"category":"名人故居"},
    {"name":"红七军过黔南旧址","lon":107.80,"lat":25.90,"category":"行军遗址"}
]

df = pd.DataFrame(site_data)

# 数据清洗、处理
print("====黔南红色点位数据集====")
print(df)

# 导出处理完成的点位csv文件
df.to_csv("red_site_dataset.csv",index=False,encoding="utf‑8‑sig")
print("点位数据文件 red_site_dataset.csv 导出成功！")