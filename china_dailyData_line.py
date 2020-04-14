import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

def plot_chinaDayData()-> Line:
	data = pd.read_csv('data\chinaDayData.csv')
	df = pd.DataFrame(data)
	#数据
	date=df.iloc[:, 1].tolist()
	nowconfirm=df.iloc[:, 1].tolist()
	confirm=df.iloc[:, 2].tolist()
	dead=df.iloc[:,3].tolist()
	heal=df.iloc[:, 4].tolist()
	date=[str(i) for i in date]

	line=(
		Line(init_opts=opts.InitOpts(width="1000px", height="500px"))
		.add_xaxis(date)
		.add_yaxis(
			"现确诊",
			nowconfirm,
			linestyle_opts=opts.LineStyleOpts(color='blue',width=1, type_="dashed"),
			yaxis_index=0,
			symbol_size=3,
			itemstyle_opts=opts.ItemStyleOpts(
			color="blue"
			),
		)
		.add_yaxis(
			"确诊",
			confirm,
			linestyle_opts=opts.LineStyleOpts(color='red',width=1, type_="dashed"),
			yaxis_index=0,
			symbol='circle',#','circle' 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
			symbol_size=3,
			 itemstyle_opts=opts.ItemStyleOpts(
			   color="red"
			),
		)
		.add_yaxis(
			"死亡",
			dead,
			linestyle_opts=opts.LineStyleOpts(color='lightsalmon',width=1, type_="dashed"),
			yaxis_index=1,
			symbol='diamond',
			symbol_size=5,
			itemstyle_opts=opts.ItemStyleOpts(
			color="lightsalmon"
			),
		)
		.add_yaxis(
			"治愈",
			heal,
			linestyle_opts=opts.LineStyleOpts(color='green',width=1, type_="dashed"),
			yaxis_index=1,
			symbol='triangle',
			symbol_size=5,
			itemstyle_opts=opts.ItemStyleOpts(
			color="green"
			),
		)
		.extend_axis(
			yaxis=opts.AxisOpts(
				type_="value",
				name='死亡/治愈',
				position="right",
			)
		)
		.extend_axis(
			yaxis=opts.AxisOpts(
				type_="value",
				split_number=10,
				min_=2000,
				name='现确诊/累计确诊',
				position="left",

			)
		)
		.set_global_opts(
			title_opts=opts.TitleOpts(title="中国每日疫情数据"),
			xaxis_opts=opts.AxisOpts(name='日期',name_location='end',name_rotate=-30),
			yaxis_opts=opts.AxisOpts(
				axistick_opts=opts.AxisTickOpts(is_show=True),
				splitline_opts=opts.SplitLineOpts(is_show=True),), #y网格线
			tooltip_opts=opts.TooltipOpts(trigger="axis"),  #交互
			datazoom_opts=opts.DataZoomOpts(
				is_show=True,
				type_="slider",
				is_realtime=True,
				range_start=20,
				range_end=80,
				orient="horizontal" #"vertical"
			)  #x轴值缩放
			)
			.set_series_opts(
			label_opts=opts.LabelOpts(is_show=False),#去掉线上的数字
		)
			)

	line.render(path='visual_html\中国每日疫情数据折线图.html')
	return line
