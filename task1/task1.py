"""
本模块为爬虫模块，使用动态爬虫中的逆向分析法爬取疫情相关的数据，并保存成json文件
"""
import json
import requests
import pandas
#爬取数据
def spider_data(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
	}
	response = requests.get(url = url, headers = headers)
	data = response.json()["data"]
	return data

#爬取海外疫情数据
overseas_data = spider_data("https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist")
overseas_data= [(i["name"],i["confirmAdd"],i["confirm"],i["dead"],i["heal"]) for i in overseas_data]
overseas_data = pandas.DataFrame(overseas_data)
new_cols1 = ['国家', '新增确诊','累计确诊','治愈', '死亡']
overseas_data.columns = new_cols1
overseas_data.to_csv('overseas_data.csv', encoding='utf-8')

#爬取国内疫情数据
china_data = spider_data("https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5")
china_data = json.loads(china_data)

#国内疫情数据初步预处理
china_city_data = china_data["areaTree"][0]["children"]
city_total_list = []
for i in range(len(china_city_data)):
	province = china_city_data[i]['name']
	province_list = china_city_data[i]['children']
	city_list = [(a["name"],province,a["total"],a["today"])for a in province_list]
	city_total_list.extend(city_list)
city_total_list = pandas.DataFrame(city_total_list)
new_cols2 = ['城市', '省份','共计','新增']
city_total_list.columns = new_cols2
city_total_list.to_csv('city_total_list.csv', encoding='utf-8')

#爬取中国每日疫情情况数据
china_everday_data = spider_data("https://view.inews.qq.com/g2/getOnsInfo?name=disease_other")
chinaDayList = json.loads(china_everday_data)["chinaDayList"]

chinaDayData = [(i["date"],i["confirm"],i["dead"],i["heal"]) for i in chinaDayList]
chinaDayData = pandas.DataFrame(chinaDayData)
new_cols3 = ['日期', '确诊','死亡','痊愈']
chinaDayData.columns = new_cols3
chinaDayData.to_csv('chinaDayData.csv', encoding='utf-8')


