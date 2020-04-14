import data_spider
import data_analyze
import china_dailyData_line
import china_map
import overseas_map
import overseas_bar
import china_pie
import overseas_worldCloud
from pyecharts.charts import Bar, Grid, Line, Pie, Tab

#数据爬取及分析
data_spider.run()
data_analyze.run()

#数据可视化呈现
tab = Tab()
tab.add(china_map.plot_china_provinces(), "中国疫情数据地图")
tab.add(china_dailyData_line.plot_chinaDayData(),"中国每日疫情数据折线图")
tab.add(china_pie.plot_chinaPie(),"国内城市死亡/治愈人数饼图")
tab.add(overseas_bar.plot_overseasBar(), "海外疫情数据条形图")

tab.add(overseas_map.plot_overseasMap(),"海外疫情数据地图")
tab.add(overseas_worldCloud.plot_countryWordCloud(),"海外疫情国家词云图")
#tab.add(china_ratePie.plot_healDeadPie(), "pie-example")
tab.render("data_view.html")
