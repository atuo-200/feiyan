import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType

def plot_china_provinces()-> Map:
	data = pd.read_csv('data\province_data.csv')
	df = pd.DataFrame(data)

	Province = df.iloc[:, 0].tolist()
	Confirm = df.iloc[:, 2].tolist()
	data = [list(i) for i in zip(Province, Confirm)]

	#背景颜色和主题
	map = (Map(init_opts=opts.InitOpts(bg_color='#eee', theme=ThemeType.ROMA))
		   .add('确诊病例', data, 'china', is_map_symbol_show=False)
		   .set_series_opts(textStyle_opts=opts.TextStyleOpts(font_size=12))
		   .set_global_opts(title_opts=opts.TitleOpts(title='全国各省确诊案例',pos_left='center'),
							#分段显示的设置
							visualmap_opts=opts.VisualMapOpts(
								is_piecewise= True,
								#自定义分段
								pieces=[
									{'min': 10000, 'label': '>=10000人', 'color': '#BC8F8F'},
									{'min': 1000, 'max': 9999, 'label': '1000-9999人', 'color': '#FFDEAD'},
									{'min': 500, 'max': 999, 'label': '500-999人', 'color': '#FFA500'},
									{'min': 100, 'max': 499, 'label': '100-499人', 'color': '#B22222'},
									{'min': 10, 'max': 99, 'label': '10-99人', 'color': '#D2691E'},
									{'min': 1, 'max': 9, 'label': '1-9人', 'color': '#E9967A'}
								],
							),
							legend_opts=opts.LegendOpts(
								is_show=False
							),




							)
		   
		   )
	map.render(path='visual_html\中国省份疫情数据地图.html')
	return map







