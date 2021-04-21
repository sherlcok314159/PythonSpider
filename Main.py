import csv
import matplotlib.pyplot as plt
import pandas as pd

#读取数据
with open("000001.csv",'r') as f:
    reader = csv.DictReader(f)
    Amplitude = [row['涨跌幅'] for row in reader]
    Price = [row['前收盘'] for row in reader]
    date= [row['日期'] for row in reader]

Prices_Higher_Days = 0
Prices_Lower_Days = 0
Prices_Higher_over_2_5_Days = 0
Prices_Lower_over_2_5_Days = 0

#计算上涨下跌天数
for i in Amplitude:
    if(float(i) > 0):Prices_Higher_Days+=1
    if(float(i) < 0):Prices_Lower_Days+=1
    if(float(i) > 2.5): Prices_Higher_over_2_5_Days+=1
    if(float(i) < -2.5):Prices_Lower_over_2_5_Days+=1
print("上涨天数："+str(Prices_Higher_Days))
print("下跌天数："+str(Prices_Lower_Days))
print("涨幅超过2.5%的天数："+str(Prices_Higher_over_2_5_Days))
print("跌幅超过2.5%的天数"+str(Prices_Lower_over_2_5_Days))


#通过pandas  matploylib 绘图
df = pd.read_csv('000001.csv',encoding='GBK')
df['日期'] = pd.to_datetime(df['日期'])
df.set_index('日期',inplace=True)
df['收盘价'].plot()
plt.title('上证指数近10年数据折线图')
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()

#后续目标：  1利用机器学习预测上证指数的走向
#          2从沪深300中挑选出最优投资组合