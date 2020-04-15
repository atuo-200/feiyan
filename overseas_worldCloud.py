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
