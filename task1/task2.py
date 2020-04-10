import pandas as pd
import matplotlib.pyplot as plt
def count_rate():
	china_df = pd.read_csv("./city_total_list.csv",index_col=0)

	#把各省份的数据加起来
	province_data = china_df.groupby('省份').sum()


	#计算死亡率和治愈率
	province_data.columns.tolist().insert(4,"治愈率")
	province_data.columns.tolist().insert(5,"死亡率")
	province_data["治愈率"] = province_data["heal"] / province_data["confirm"]

	province_data["死亡率"] = province_data["dead"] / province_data["confirm"]


	"""
	按治愈率对数据进行降序排序，数据显示宁夏、西藏、青海的治愈率最高为100%，当然
	这也得益于地处偏远，输入病例少，疫情可控。
	"""
	print(province_data.sort_values(by = "治愈率",ascending = False))

	"""
	按致死率对数据进行排序，数据显示湖北的死亡率最高，因为地处疫情爆发中心点。
	"""
	print(province_data.sort_values(by = "死亡率",ascending = False))

	#把治愈率和死亡率转为百分比的形式，再把数据存储成csv文件
	province_data["死亡率"] = province_data["死亡率"].apply(lambda x:'%.2f%%'%(x*100))
	province_data["治愈率"] = province_data["治愈率"].apply(lambda x:'%.2f%%'%(x*100))
	province_data.to_csv("province_data.csv")

"""
分析全国的日期序列数据,因为数据太多，只绘制3月份到4月份的数据，从图中可以看出3月份和4月份
的确诊人数和死亡人数趋向平缓，治愈人数大幅增加，疫情得到了控制
"""
def daily_change():
	# 获取每日疫情数据，日期，确诊，疑似，死亡，治愈
	(date_list, everyday_confirm,everyday_dead, everyday_heal) = pd.read_csv("./chinaDayData.csv",index_col=0).values.T.tolist()
	
	plt.rcParams['font.sans-serif'] = ['SimHei']
	
	fig, ax1 = plt.subplots(figsize=(10, 8))
	plt.xlabel('日期')
	plt.ylabel('人数')


	ax1.plot(everyday_confirm[48:],color='red',linewidth=1.0,linestyle='--',label = '确诊人数')
	
	ax1.plot(everyday_heal[48:],color='yellow',linewidth=1.0,linestyle='-.',label = '治愈人数')
	ax1.set_xticks(range(0,len(date_list[48:]),1))
	ax1.set_xticklabels(date_list[48:], rotation=40)
	ax1.set_ylabel(r"确诊及治愈人数", fontsize=16)
	plt.legend(loc='upper left')
	plt.grid(which='major', axis='both', color='grey', linestyle='--', alpha=0.2)
	#图2
	ax2 = ax1.twinx()

	ax2.set_ylabel(r"死亡人数", fontsize=16)
	ax2.set_ylim(0, 3500)
	ax2.plot(everyday_dead[48:],color='blue',linewidth=1.0,linestyle='-.',label = '死亡人数')

	plt.grid(which='major', axis='both', color='grey', linestyle='--', alpha=0.2)
	plt.legend(loc='upper right')
	plt.title("2019-nCoV疫情变化时间图", fontsize=16)

	plt.savefig('2019-nCoV疫情变化时间图.png', bbox_inches='tight')
	plt.show()
	

if __name__ == "__main__":
	count_rate()
	daily_change()
	
	
  
