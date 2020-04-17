## python爬虫助力疫情数据追踪项目报告

#### 项目概述

​		2019新型冠状病毒（2019-nCoV），因2019年武汉病毒性肺炎病例而被发现，2020年1月12日被世界卫生组织命名。冠状病毒是一个大型病毒家族，已知可引起感冒以及中东呼吸综合征和严重急性呼吸综合征等较严重疾病。新型冠状病毒是以前从未在人体中发现的冠状病  毒新毒株。

​		2020年新型冠状病毒在全球肆虐，确诊人数快速攀升，全世界确诊病例突破两百万，各地的景区以及娱乐场所封闭，街道上空无一人。随着疫情的严重化，人们对疫情的关注度也越来越高。在疫情期间，随时了解疫情的情况成为人们每天必不可少的习惯之一。而在互联网作用下，中国将准确、实时的疫情数据公布于网上，并且疫情数据的透明化以及往后的发展趋势对于全国人民以及全世界人民来说都极为重要。在这样的背景下，我们身为大数据专业的学生，通过运用所学技术对公开出来的疫情数据进行分析，进行探索，从对疫情数据的探索分析中找出蕴含在疫情期间的发展态势，也希望能通过这一次项目的学习，能让我们更好地理解数据，从数据中摸索出事物发展的规律；加深对数据技术的理解，加深对数据分析流程的理解。

**学习目标**

1. 关注疫情新闻以及了解疫情数据
2. 掌握爬取疫情数据的基本思路和方法
3. 掌握数据预处理的基本思路和方法
4. 掌握数据分析的基本思路和方法
5. 掌握数据可视化的基本思路和方法

**使用到的工具和第三方库**

| 工具/第三方库 |                    应用                    |
| :-----------: | :----------------------------------------: |
|    pycharm    |               编写python代码               |
|   requests    |                爬取疫情数据                |
|    pandas     | 对爬取下来的疫情数据进行数据预处理及其分析 |
|   pyecharts   |     对获取的疫情数据进行数据可视化展示     |
|      git      | 对最终的可视化图表部署到GitHub page上展示  |
|               |                                            |

**项目程序实现逻辑**

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas10.PNG)

#### 1、了解疫情数据

​		本次要爬取的疫情数据来源是 [https://news.qq.com/zt2020/page/feiyan.htm#/global](https://news.qq.com/zt2020/page/feiyan.htm#/global) 我们进入相应的页面可以获取相应的每日更新的实时疫情数据，我们本次爬虫的目的就是获取这些数据。如下图，我们可以得到国内各个地区以及海外各个国家的确诊人数、治愈人数和死亡人数等数据。

​		**国内省份及其城市的疫情数据**

![image](https://github.com/atuo-200/feiyan/blob/master/image/image-20200417002121584.png)

​		**海外国家的疫情数据**

![image](https://github.com/atuo-200/feiyan/blob/master/image/image-20200417001910548.png)

#### 2、疫情数据爬虫

##### 2.1   了解Python获取网络数据的方法

​		使用Python对网络数据进行爬取，首先我们要学会判断网页是静态网页还是动态网页。可以通过在网页源代码中查找我们想要爬取的数据，如果找得到则说明网页是静态的，找不到则说明网页是动态的。在这里需要注意的是，浏览器开发者工具元素面板上显示的是浏览器执行Javascript之后生成的HTML代码，鼠标右键的查看源代码才是真正的网页源代码。

​		第二是要了解用python实现网络爬虫的基本知识，我们所熟知的静态爬虫方法是最常见的一种爬虫方法，其使用的前提是我们爬取的网页是静态的，也就是所需要的数据都包含在网页源代码里，我们可以通过对网页源数据进行解析提取，得到我们所需的数据。但是这种方法又有局限性，它对于很多做了反爬措施，其中数据是通过JS与服务器进行请求得到的动态网站来说束手无措。在这个基础上，根据动态网页，我们引申出动态爬虫的方法，其中动态爬虫又分为动态页面逆向分析爬取和模拟浏览器爬取。在本次项目中，我们所用到的是动态页面逆向分析爬取方法，以这种方式进行动态页面的爬取实质就是对页面进行逆向分析，其核心就是跟踪页面的交互行为 JS 触发调度，分析出有价值、有意义的核心调用（一般都是通过 JS 发起一个 HTTP 请求），然后我们使用 Python 直接访问逆向得到的链接获取需要的数据。

##### 2.2  了解本项目数据获取的方法

我们进入网页https://news.qq.com/zt2020/page/feiyan.htm，通过查看网页源代码发现这个网页是动态网页。我们选择借助火狐浏览器的Web开发者工具找到相应疫情数据存放的位置。打开【网络（Network）】面板，重新刷新网页，监听网络信息，可以看到从网络请求下载资源的实时信息。

![image](https://github.com/atuo-200/feiyan/blob/master/image/image-20200417132103528.png)

在这里我们需要关注的重点是js、json类型的数据，逐个点击查看，会在右侧响应标签下显示该资源的内容。

![image](https://github.com/atuo-200/feiyan/blob/master/image/image-20200417132412989.png)

想要更加仔细的查看该资源的信息，可以右键单击该资源，选择新建标签页打开。

在一系列的查找下，我们找到了以下几个数据链接，里面包含的都是json类型的数据。

海外国家疫情数据： [https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist](https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist)

国内疫情数据：[https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5](https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5)

国内每日疫情情况数据：[https://view.inews.qq.com/g2/getOnsInfo?name=disease_other](https://view.inews.qq.com/g2/getOnsInfo?name=disease_other)

海外疫情治愈率和死亡率top10的国家数据：[https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryWeekCompRank,FAutoContinentConfirmStatis,FAutoConfirmMillionRankList,FAutoHealDeadRateRankList](https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryWeekCompRank,FAutoContinentConfirmStatis,FAutoConfirmMillionRankList,FAutoHealDeadRateRankList)

我们选择对这几个数据链接发起爬虫请求，获取信息。

#### 3、数据预处理

利用requests库爬取疫情数据之后，我们获得的是json形式的数据，可以利用json库对json数据进行解析，利用列表推导式对json里面的数据提取出来，组合成pandas库里的DataFrame数据格式，再调用pandas库的to_csv方法，把数据保存成csv文件。从json文件中提取数据的复杂度与json文件组织数据的复杂度相关，其中对国内疫情数据进行提取的时候，可能稍显繁琐，但只要我们学会稍稍转换思维，利用pandas库的常见方式，还是能轻松地把数据提取出来。

同时也由于疫情数据是经官方进行处理之后再公布到互联网上的，不存在什么异常值、非空值、数据格式错误的异常值，数据是比较干净的，所以这次项目的数据预处理部分的代码不涉及对于异常值的处理。

**数据爬虫和数据预处理结合后的代码**

```python
"""
本模块为爬虫和数据预处理模块，使用动态爬虫中的逆向分析法爬取疫情相关的数据，并从中提取需要的数据保存成csv文件
"""
import json
import requests
import pandas as pd
#爬虫代码
def spider_data(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
	}
	response = requests.get(url = url, headers = headers)
	data = response.json()["data"]
	return data

def spider_overseas():	
	#爬取海外疫情数据
	overseas_data = spider_data("https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist")
	overseas_data= [(i["name"],i["confirmAdd"],i["confirm"],i["dead"],i["heal"]) for i in overseas_data]
	overseas_data = pd.DataFrame(overseas_data)
	new_cols1 = ['国家', '新增确诊','累计确诊','治愈', '死亡']
	overseas_data.columns = new_cols1
	overseas_data.to_csv('data\overseas_data.csv', encoding='utf-8')

def spider_china():	
	#爬取国内疫情数据
	china_data = spider_data("https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5")
	china_data = json.loads(china_data)

	#国内疫情数据初步预处理
	china_city_data = china_data["areaTree"][0]["children"]
	city_total_list = []
	for i in range(len(china_city_data)):
		province = china_city_data[i]['name']
		province_list = china_city_data[i]['children']
		city_list = [(province,a["name"],a["total"])for a in province_list]
		city_total_list.extend(city_list)
	city_total_list = pd.DataFrame(city_total_list)
	new_cols2 = ['省份', '城市','共计']
	city_total_list.columns = new_cols2

	#国内疫情数据二次预处理
	total_data = pd.DataFrame(city_total_list["共计"].values.tolist())[["nowConfirm","confirm","dead","heal"]]
	city_total_list = pd.concat([city_total_list,total_data],axis = 1)
	city_total_list.drop('共计',axis=1, inplace=True)

	#保存数据
	city_total_list.to_csv('data\city_total_list.csv', encoding='utf-8')

def spider_chinaDayData():
	#爬取中国每日疫情情况数据
	china_everday_data = spider_data("https://view.inews.qq.com/g2/getOnsInfo?name=disease_other")
	chinaDayList = json.loads(china_everday_data)["chinaDayList"]

	chinaDayData = [(i["date"],i["confirm"],i["nowConfirm"],i["dead"],i["heal"]) for i in chinaDayList]
	chinaDayData = pd.DataFrame(chinaDayData)
	chinaDayData.columns = ['日期', '累计确诊','现有确诊','死亡','痊愈']
	chinaDayData.to_csv('data\chinaDayData.csv', encoding='utf-8')
def spider_rate():
	#爬取海外疫情治愈率和死亡率前10的国家数据并保存成csv文件
	rate_data = spider_data("https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryWeekCompRank,FAutoContinentConfirmStatis,FAutoConfirmMillionRankList,FAutoHealDeadRateRankList")
	rate_data = rate_data['FAutoHealDeadRateRankList']

	#将死亡率前10，和治愈率前十的数据取出并保存成csv文件
	world_deadHead = rate_data['deadHead']
	world_healHead = rate_data['healHead']

	pd.DataFrame(world_deadHead).to_csv("data\world_deadrate10.csv")
	pd.DataFrame(world_healHead).to_csv("data\world_healrate10.csv")
	
#总的运行函数
def run():
	spider_overseas()
	spider_china()
	spider_chinaDayData()
	spider_rate()
```

代码运行后会在项目目录下的data目录中生成几个数据文件，这就是我们数据爬虫和数据预处理的最终结果，我们可以拿这些数据进行疫情数据分析和疫情数据可视化。

![image](https://github.com/atuo-200/feiyan/blob/master/image/image1.PNG)

#### 4、疫情数据分析

疫情数据分析这部分我们分为三个方面来探索数据，一是根据国内省份死亡率和治愈率，分析死亡率和治愈率和地区之间的关系；二是对海外治愈率和死亡率前十的国家数据做可视化呈现，分析哪些国家对疫情的应对更好和更糟糕；三是对中国每日死亡人数治愈人数所占的比重进行可视化呈现，从而分析国内疫情的发展规律是向好还是向坏。

##### 4.1 疫情数据分析整体代码

```python
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
    #绘制中国每日死亡人数与治愈人数比重饼图，从而分析国内疫情的发展规律是向好还是向坏
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
```

上面是疫情数据分析的整体代码，下面我们分部分对整体代码进行解析，分维度探讨数据。

##### 4.2 探讨国内省份死亡率和治愈率

count_rate()函数中，我们对city_total_list.csv中的数据进行治愈率和死亡率的计算，先根据治愈率进行降序排序，得到以下结果。

![image-20200417160146594](https://github.com/atuo-200/feiyan/blob/master/image/image-20200417160146594.png)

数据显示宁夏、西藏、青海的治愈率最高为100%，既得益于抗疫措施的部署恰当，也得益于地处偏远，输入病例少，疫情可控。

除宁夏、西藏、青海的治愈率为100%，江西湖南也非常的高，达到99.5%以上。

江西省注重集中治疗和个体治疗相结合，坚持中西医并重，充分发挥中西医治疗协同作用，注重在院治疗和出院管理想结合，建立出院患者复查病毒核酸阳性情况报告制度，将出院患者复发，复阳情况控制在最低，得益于这一系列医护措施，使江西省的治愈率名列全国前列。

湖南省起处湖北邻近，在严控病例输入的同时，还能把治愈率控制在这么高的比例，在这背后是全省得鼎力支持，湖南14个省级疾控和诊治专家组“下沉”市州，指导新型冠状病毒感染的肺炎救治工作；湖南省领导多次前往医院等抗疫一线看望慰问医务工作者，并大力呼吁民众佩戴一般医用防护口罩即可，把N95口罩特别是医用N95口罩、防护服等医疗物资留给救治一线的医务人员等等。数据证明，这一系列的抗疫措施采取得非常有效。可以戳这一链接详细了解湖南在新冠肺炎抗疫战中采取的硬核举措：[这次疫情，我们欠湖南人一个热搜](https://zhuanlan.zhihu.com/p/107935796?utm_source=wechat_session&utm_medium=social&utm_oi=1021410697481248768)

再根据死亡率进行降序排序

![image](https://github.com/atuo-200/feiyan/blob/master/image/image-20200417160924315.png)

数据显示湖北的死亡率达到约6.6%，是死亡率第二名的省份的两倍，因为其地处疫情爆发中心点，也因为早期抗疫措施不全面，疫情扩散快，医护物资和医护人员短缺，造成一些令人惋惜的悲剧。

除湖南以外，新疆和海南的死亡率分别位列第二名和第三名，死亡率分别在3.9%和3.5%左右。我们小组探究出了以下原因：1、相对于其他省份，由于海南和新疆的经济较为落后，导致现有的医疗人员和设备及技术跟不上；2、并且海南旅游业较发达，人流量比较大，而医疗力量方面平平；3、海南和新疆的确诊患者绝大多数是患有其他疾病高龄老人。

##### 4.3 从死亡率和治愈率探讨海外国家的疫情应对情况

先来看看海外国家死亡率的top10，overseas_deadRate() 函数中我们对海外死亡率前十的国家数据提取出来做可视化呈现，得到如下图表。

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas5.png)

从上图我们可以得出死亡率最高的是阿尔及利亚，其地处非洲，科技水平和医疗水平落后，人民生活缺乏卫生观念，造成疫情扩散，死亡率居高。

而海外国家死亡率top10中，比利时、英国、意大利、法国、荷兰、瑞典、西班牙、匈牙利均为欧洲国家，在海外国家死亡率top10中，欧洲国家占比80%，这是一个不小的比重，我们小组对这一数据呈现得出以下结论：

+ 欧洲地区人口老龄化，而新冠病毒在老龄人中更易感染；
+ 政府低估了新冠肺炎的威力，在中国爆发疫情时，并没有引起西方国家足够的重视，还不以为然，认为不会构成太大影响，导致准备不足，宣传不足；
+ 民众认知不够，上面说到，西方国家政府在疫情来临时，还在甩锅和指责，不向民众宣称新冠肺炎的危害性，结果就是误导了群众，使得感染人数有增不减，医院人满为患，医疗系统瘫痪，医疗物资难以自足，经验不足，导致死亡率较高。

再来看看海外国家治愈率的top10，overseas_healRate()函数中，我们对海外国家治愈率前十的国家数据提取出来做可视化呈现，得到如下图表。

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas6.png)

由图可以看出海外国家治愈率最高的为韩国，比治愈率第二名的国家高出大约10%的百分比，我们小组总结了以下原因：

+ 韩国有着强大的医疗物资生产能力与检测能力；
+ 韩国从中央到地方的立体防疫指挥体系很快被建立；
+ 韩国政府参考中国抗击疫情的经验，建立韩版方舱医院，进行分级治疗，重症患者住院治疗，轻症患者接受隔离观察，确诊患者间没有造成交叉感染；

##### 4.4 从国内每日死亡及治愈人数的比重变化探索疫情的发展

plot_healDeadPie()函数中我们绘制中国每日死亡及治愈人数比重的饼图，我们往图表中加了TimeLine组件，点击图表下方的时间轴，图表就能执行动态交互功能，显示出对应日期的数据；点击图表下方的播放按钮，图表能自动按照时间轴顺序变换相应的数据。

可以戳链接 https://atuo-200.github.io/china_deadHeal_pie.html 点击图表下方的播放按钮，我们可以看到中国治愈率占死亡率的比重是逐渐加大，这说明我国的疫情发展是向好发展的。这得益于中国全党和全人民对抗击疫情采取的一系列举措，使中国成为全世界疫情控制得最好的国家。

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas9.png)

#### 5、疫情数据可视化

在数据可视化阶段，我们对数据爬虫和数据预处理阶段获取的数据进行可视化呈现，下面分图表对绘图过程做简要的概述和图表呈现，并附上相应代码。

绘图的主要流程为：

+ 导入所需要的库（pandas读取文件数据，pyecharts绘图）；

+ pandas读取需绘图的数据，并将数据转化成列表格式，整合在一起；
+ 将数据添加到图框中，然后根据需要添加图形的设置；
+ 最后生成html格式的文件；

##### 5.1 中国每日疫情数据折线图

**绘图代码**

```python
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

def plot_chinaDayData()-> Line:
	data = pd.read_csv('data\chinaDayData.csv')
	df = pd.DataFrame(data)
	#数据
	date=df.iloc[:, 1].tolist()
	nowconfirm=df.iloc[:, 3].tolist()
	confirm=df.iloc[:, 2].tolist()
	dead=df.iloc[:,4].tolist()
	heal=df.iloc[:, 5].tolist()
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
```

**图表展示**

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas7.png)

##### 5.2 中国省份疫情数据地图

**绘图代码**

```python
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
```

**图表展示**

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas8.png)

##### 5.3 海外疫情数据地图

**绘图代码**

```python
import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType

def plot_overseasMap()-> Map:
	data = pd.read_csv('data\overseas_data.csv')
	df = pd.DataFrame(data)

	Province = df.iloc[:, 1].tolist()
	Confirm = df.iloc[:, 3].tolist()

	data = [list(i) for i in zip(Province, Confirm)]


	map = (Map(init_opts=opts.InitOpts(bg_color='#eee', theme=ThemeType.ROMA))
		   .add('确诊病例', data, 'world', is_map_symbol_show=False,name_map={
			'Singapore Rep.':'新加坡',
			'Dominican Rep.':'多米尼加',
			'Palestine':'巴勒斯坦',
			'Bahamas':'巴哈马',
			'Timor-Leste':'东帝汶',
			'Afghanistan':'阿富汗',
			'Guinea-Bissau':'几内亚比绍',
			"Côte d'Ivoire":'科特迪瓦',
			'Siachen Glacier':'锡亚琴冰川',
			"Br. Indian Ocean Ter.":'英属印度洋领土',
			'Angola':'安哥拉',
			'Albania':'阿尔巴尼亚',
			'United Arab Emirates':'阿联酋',
			'Argentina':'阿根廷',
			'Armenia':'亚美尼亚',
			'French Southern and Antarctic Lands':'法属南半球和南极领地',
			'Australia':'澳大利亚',
			'Austria':'奥地利',
			'Azerbaijan':'阿塞拜疆',
			'Burundi':'布隆迪',
			'Belgium':'比利时',
			'Benin':'贝宁',
			'Burkina Faso':'布基纳法索',
			'Bangladesh':'孟加拉国',
			'Bulgaria':'保加利亚',
			'The Bahamas':'巴哈马',
			'Bosnia and Herz.':'波斯尼亚和黑塞哥维那',
			'Belarus':'白俄罗斯',
			'Belize':'伯利兹',
			'Bermuda':'百慕大',
			'Bolivia':'玻利维亚',
			'Brazil':'巴西',
			'Brunei':'文莱',
			'Bhutan':'不丹',
			'Botswana':'博茨瓦纳',
			'Central African Rep.':'中非共和国',
			'Canada':'加拿大',
			'Switzerland':'瑞士',
			'Chile':'智利',
			'China':'中国',
			'Ivory Coast':'象牙海岸',
			'Cameroon':'喀麦隆',
			'Dem. Rep. Congo':'刚果（金）',
			'Congo':'刚果（布）',
			'Colombia':'哥伦比亚',
			'Costa Rica':'哥斯达黎加',
			'Cuba':'古巴',
			'N. Cyprus':'北塞浦路斯',
			'Cyprus':'塞浦路斯',
			'Czech Rep.':'捷克',
			'Germany':'德国',
			'Djibouti':'吉布提',
			'Denmark':'丹麦',
			'Algeria':'阿尔及利亚',
			'Ecuador':'厄瓜多尔',
			'Egypt':'埃及',
			'Eritrea':'厄立特里亚',
			'Spain':'西班牙',
			'Estonia':'爱沙尼亚',
			'Ethiopia':'埃塞俄比亚',
			'Finland':'芬兰',
			'Fiji':'斐',
			'Falkland Islands':'福克兰群岛',
			'France':'法国',
			'Gabon':'加蓬',
			'United Kingdom':'英国',
			'Georgia':'格鲁吉亚',
			'Ghana':'加纳',
			'Guinea':'几内亚',
			'Gambia':'冈比亚',
			'Guinea Bissau':'几内亚比绍',
			'Eq. Guinea':'赤道几内亚',
			'Greece':'希腊',
			'Greenland':'格陵兰',
			'Guatemala':'危地马拉',
			'French Guiana':'法属圭亚那',
			'Guyana':'圭亚那',
			'Honduras':'洪都拉斯',
			'Croatia':'克罗地亚',
			'Haiti':'海地',
			'Hungary':'匈牙利',
			'Indonesia':'印度尼西亚',
			'India':'印度',
			'Ireland':'爱尔兰',
			'Iran':'伊朗',
			'Iraq':'伊拉克',
			'Iceland':'冰岛',
			'Israel':'以色列',
			'Italy':'意大利',
			'Jamaica':'牙买加',
			'Jordan':'约旦',
			'Japan':'日本',
			'Japan':'日本本土',
			'Kazakhstan':'哈萨克斯坦',
			'Kenya':'肯尼亚',
			'Kyrgyzstan':'吉尔吉斯斯坦',
			'Cambodia':'柬埔寨',
			'Korea':'韩国',
			'Kosovo':'科索沃',
			'Kuwait':'科威特',
			'Lao PDR':'老挝',
			'Lebanon':'黎巴嫩',
			'Liberia':'利比里亚',
			'Libya':'利比亚',
			'Sri Lanka':'斯里兰卡',
			'Lesotho':'莱索托',
			'Lithuania':'立陶宛',
			'Luxembourg':'卢森堡',
			'Latvia':'拉脱维亚',
			'Morocco':'摩洛哥',
			'Moldova':'摩尔多瓦',
			'Madagascar':'马达加斯加',
			'Mexico':'墨西哥',
			'Macedonia':'马其顿',
			'Mali':'马里',
			'Myanmar':'缅甸',
			'Montenegro':'黑山',
			'Mongolia':'蒙古',
			'Mozambique':'莫桑比克',
			'Mauritania':'毛里塔尼亚',
			'Malawi':'马拉维',
			'Malaysia':'马来西亚',
			'Namibia':'纳米比亚',
			'New Caledonia':'新喀里多尼亚',
			'Niger':'尼日尔',
			'Nigeria':'尼日利亚',
			'Nicaragua':'尼加拉瓜',
			'Netherlands':'荷兰',
			'Norway':'挪威',
			'Nepal':'尼泊尔',
			'New Zealand':'新西兰',
			'Oman':'阿曼',
			'Pakistan':'巴基斯坦',
			'Panama':'巴拿马',
			'Peru':'秘鲁',
			'Philippines':'菲律宾',
			'Papua New Guinea':'巴布亚新几内亚',
			'Poland':'波兰',
			'Puerto Rico':'波多黎各',
			'Dem. Rep. Korea':'朝鲜',
			'Portugal':'葡萄牙',
			'Paraguay':'巴拉圭',
			'Qatar':'卡塔尔',
			'Romania':'罗马尼亚',
			'Russia':'俄罗斯',
			'Rwanda':'卢旺达',
			'W. Sahara':'西撒哈拉',
			'Saudi Arabia':'沙特阿拉伯',
			'Sudan':'苏丹',
			'S. Sudan':'南苏丹',
			'Senegal':'塞内加尔',
			'Solomon Is.':'所罗门群岛',
			'Sierra Leone':'塞拉利昂',
			'El Salvador':'萨尔瓦多',
			'Somaliland':'索马里兰',
			'Somalia':'索马里',
			'Serbia':'塞尔维亚',
			'Suriname':'苏里南',
			'Slovakia':'斯洛伐克',
			'Slovenia':'斯洛文尼亚',
			'Sweden':'瑞典',
			'Swaziland':'斯威士兰',
			'Syria':'叙利亚',
			'Chad':'乍得',
			'Togo':'多哥',
			'Thailand':'泰国',
			'Tajikistan':'塔吉克斯坦',
			'Turkmenistan':'土库曼斯坦',
			'East Timor':'东帝汶',
			'Trinidad and Tobago':'特里尼达和多巴哥',
			'Tunisia':'突尼斯',
			'Turkey':'土耳其',
			'Tanzania':'坦桑尼亚',
			'Uganda':'乌干达',
			'Ukraine':'乌克兰',
			'Uruguay':'乌拉圭',
			'United States':'美国',
			'Uzbekistan':'乌兹别克斯坦',
			'Venezuela':'委内瑞拉',
			'Vietnam':'越南',
			'Vanuatu':'瓦努阿图',
			'West Bank':'西岸',
			'Yemen':'也门',
			'South Africa':'南非',
			'Zambia':'赞比亚',
			'Zimbabwe':'津巴布韦'
		})
		   .set_series_opts(textStyle_opts=opts.TextStyleOpts(font_size=12),label_opts=opts.LabelOpts(is_show=False))
		   .set_global_opts(title_opts=opts.TitleOpts(title='国外累计确诊病例',pos_left='center'),
							#分段显示的设置
							visualmap_opts=opts.VisualMapOpts(
								is_piecewise= True,
								#自定义分段
								pieces=[
									{'min': 200000, 'label': '>=200000人', 'color': '#300000'},
									{'min': 100000, 'max': 199999, 'label': '100000-199999人', 'color': '#580000'},
									{'min': 10000, 'max': 99999, 'label': '10000-99999人', 'color': '#880000'},
									{'min': 5000, 'max': 9999, 'label': '5000-9999人', 'color': '#F80000'},
									{'min': 1000, 'max': 4999, 'label': '1000-4999人', 'color': '#FF6633'},
									{'min': 100, 'max': 999, 'label': '100-999人', 'color': '#FF9966'},
									{'min': 1, 'max': 99, 'label': '1-99人', 'color': '#FFCC00'}
								],
							),
							legend_opts=opts.LegendOpts(
								is_show=False
							),
							)
		   )
	map.render(path='visual_html\海外疫情数据地图.html')
	return map
```

**图表展示**

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas1.png)

##### 5.4 海外疫情数据条形图

**绘图代码**

```python
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
```

**图表展示**

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas2.png)

##### 5.5 国内省份死亡/治愈人数饼图

**绘图代码**

```python
from pyecharts import options as opts
from pyecharts.charts import Pie
import pandas as pd

def plot_chinaPie() -> Pie:
    #导入数据
    data = pd.read_csv('data\province_data.csv')
    df = pd.DataFrame(data)
    columns = df.iloc[:, 0].tolist()
    heal = df.iloc[:, 4].tolist()
    dead = df.iloc[:, 3].tolist()

    c = (
        Pie()
        .add(
            "死亡人数",
            [list(z) for z in zip(columns, dead)],
            radius=["25%", "50%"],
            center=["20%", "70%"]
        )
        .add(
            "治愈人数",
            [list(z) for z in zip(columns, heal)],
            radius=["25%", "50%"],
            center=["60%", "70%"]
            )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="国内省份死亡/治愈人数饼图"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_top="20%", pos_left="90%", orient="vertical"),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

    )
    c.render(path = "visual_html\国内省份死亡及治愈人数饼图.html")
    return c
```

**图表展示**

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas3.png)

##### 5.6 海外疫情国家词云图

**绘图代码**

```python
from pyecharts.charts import WordCloud
from pyecharts import options as opts
import pandas as pd

def plot_countryWordCloud() -> WordCloud:
    data_all = pd.read_csv("data\overseas_data.csv")
    data_confirm = data_all['累计确诊']
    data_country = data_all['国家']
    data = [list(i) for i in zip(data_country, data_confirm)]
    c = (
        WordCloud()
        .add(series_name="疫情热点", data_pair=data, word_size_range=[15, 80])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="疫情重灾国家分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
            )
    )
    c.render("visual_html\海外疫情国家词云图.html")
    return c
```

**图表展示**

![image](https://github.com/atuo-200/feiyan/blob/master/image/canvas4.png)

根据词云可以看出，其中“美国”、“意大利”、“西班牙”等词最为突出，因此我们初步判断这几个国家是海外的疫情重灾国家。

#### 6、项目收尾工作

**代码整理**

+ 在完成以上数据爬虫、数据分析和数据可视化的代码编写工作后，我们对总代码进行整理，即是把实现各个功能的代码块用函数封装起来，创建一个main.py文件，把实现各个功能（如数据爬虫、数据预处理、数据分析和数据可视化）的代码运行都集成到main.py文件里，这样能让我们只要一次运行main.py文件，便可一次性地获取数据，把数据保存在相应的目录下，一次性地生成可视化图表，减少运行项目代码的复杂度。
+ 并且我们在main.py文件中我们用pyecharts中的分页组件把各个可视化部分的图表串连起来，用一个html文件展示，也就是show_view.html文件。

main.py代码

```python
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
tab.add(china_pie.plot_chinaPie(),"国内省份死亡/治愈人数饼图")
tab.add(overseas_bar.plot_overseasBar(), "海外疫情数据条形图")

tab.add(overseas_map.plot_overseasMap(),"海外疫情数据地图")
tab.add(overseas_worldCloud.plot_countryWordCloud(),"海外疫情国家词云图")
#tab.add(china_ratePie.plot_healDeadPie(), "pie-example")
tab.render("show_view.html")
```

**把可视化图表部署到GitHub page上**

接下来我们把生成的show_view.html文件部署到GitHub page，使得图表可以联网查看，把html文件部署到GitHub page也很简单，只需要到GitHub上新建一个特殊的仓库，在本地用git命令把show_view.html上传到仓库上，再在仓库的setting上开启GitHub page功能，即可让GitHub page托管我们的html文件，使得最终集成的可视化图表能联网查看。

可戳链接 [https://atuo-200.github.io/feiyan/show_view.html](https://atuo-200.github.io/feiyan/show_view.html) 查看最终集成的可视化图表。

![image](https://github.com/atuo-200/feiyan/blob/master/image/image2.PNG)

#### 总结

本项目报告展示了如何使用Python爬取疫情数据，如何利用pandas对爬取到的疫情数据进行预处理操作，并保存成csv文件，如何从获取的疫情数据中探索数据背后的疫情情况及发展，如何使用pyecharts对获取的数据进行可视化绘图展示，并把最终的可视化图表部署到GitHub page上，使得图表可以联网呈现。



