from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.faker import Faker
import pandas as pd 

def plot_healDeadPie() -> Pie:
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



