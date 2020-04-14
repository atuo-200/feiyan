import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

def plot_overseasBar()-> Bar:
	data = pd.read_csv('data\overseas_data.csv')
	df = pd.DataFrame(data)

	country=df.iloc[:, 1].tolist()
	newconfirm=df.iloc[:, 2].tolist()
	confirm=df.iloc[:, 3].tolist()
	heal=df.iloc[:, 4].tolist()
	dead=df.iloc[:,5].tolist()

	bar=(
		Bar(init_opts=opts.InitOpts(width="1000px", height="500px"))
		.add_xaxis(country)
		.add_yaxis(
			"新增确诊",
			newconfirm,

		)
		.add_yaxis(
			"累计确诊",
			confirm,

		)

		.add_yaxis(
			"治愈",
			heal,
		)
		.add_yaxis(
			"死亡",
			dead,
			)
		.extend_axis(
			yaxis=opts.AxisOpts(
				type_="value",
				name='人数/人',
				position="left",
			)
		)
		.set_global_opts(
			title_opts=opts.TitleOpts(title="国外疫情数据"),
			tooltip_opts=opts.TooltipOpts(trigger="axis"),
			xaxis_opts=opts.AxisOpts(name='国家'),
			yaxis_opts=opts.AxisOpts(
				axistick_opts=opts.AxisTickOpts(is_show=True),
				splitline_opts=opts.SplitLineOpts(is_show=False)),

			#滚动条
			datazoom_opts=opts.DataZoomOpts(
				is_show=True,
				type_="slider",
				is_realtime=True,
				range_start=30,
				range_end=90,
				orient="horizontal"
			)
		)
	)
	bar.render(path='visual_html\海外疫情数据条形图.html')
	return bar
