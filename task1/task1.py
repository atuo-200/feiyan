"""
本模块为爬虫模块，使用动态爬虫中的逆向分析法爬取疫情相关的数据，并保存成json文件
"""
import requests

#爬取数据
def spider_data(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
	}
	response = requests.get(url = url, headers = headers)
	data = response.json()["data"]
	return data

#保存数据以便数据预处理
def save_data(file_name,data):
	f = open(file_name,"w")
	f.write(str(data))
	f.close()

if __name__=='__main__':
	china_data = spider_data("https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5")
	overseas_data = spider_data("https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist")
	china_everday_data = spider_data("https://view.inews.qq.com/g2/getOnsInfo?name=disease_other")

	save_data("china_data.json",china_data)
	save_data("overseas_data.json",overseas_data)
	save_data("china_everday_data.json",china_everday_data)
