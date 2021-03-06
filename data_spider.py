"""
本模块为爬虫模块，使用动态爬虫中的逆向分析法爬取疫情相关的数据，并保存成csv文件
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
	
def run():
	spider_overseas()
	spider_china()
	spider_chinaDayData()
	spider_rate()
	

