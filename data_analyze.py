import pandas as pd
from pyecharts.charts import Bar,Pie,Timeline
from pyecharts import options as opts
def count_rate():
	china_df = pd.read_csv("data\city_total_list.csv",index_col=0)

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
	province_data.to_csv("data\province_data.csv")

def overseas_deadRate():
	#海外死亡率前十的国家数据提取出来做可视化呈现
	data_all = pd.read_csv("data\world_deadrate10.csv")
	country = data_all['country']
	world_deadHead = data_all['deadRate']
	c = (
		Bar()
		.add_xaxis(list(country))
		.add_yaxis("死亡率", list(world_deadHead))
		.set_global_opts(
			xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
			title_opts=opts.TitleOpts(title="海外死亡比率top10")
		)
		.render("visual_html\海外死亡比率top10.html")
	)
def overseas_healRate():
	# 海外治愈率前十的国家数据提取出来做可视化呈现
	data_all = pd.read_csv("data\world_healrate10.csv")
	country = data_all['country']
	world_deadHead = data_all['healRate']
	c = (
		Bar()
		.add_xaxis(list(country))
		.add_yaxis("治愈率", list(world_deadHead))
		.set_global_opts(
			xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
			title_opts=opts.TitleOpts(title="海外治愈比率top10")
		)
		.render("visual_html\海外治愈比率top10.html")
	)
def plot_healDeadPie():
	data = pd.read_csv('data\chinaDayData.csv')
	df = pd.DataFrame(data)
	#数据
	date=df.iloc[:, 1].tolist()
	tl = Timeline()

	for i in range(len(data)):
		pie1 = (
			Pie()
			.add(
				"商家A",
				[list(z) for z in zip(["死亡","治愈"],df.iloc[i,3:].tolist())],
				radius=["30%", "55%"],
			)
			.set_global_opts(title_opts=opts.TitleOpts("中国{}日死亡率和治愈率比重".format(date[i])))
		)
		tl.add(pie1, "{}".format(date[i]))
	tl.render("visual_html\中国每日死亡人数与治愈人数比重饼图.html")
	return pie1

def run():
	count_rate()
	overseas_deadRate()
	overseas_healRate()
	plot_healDeadPie()
	
	
  
