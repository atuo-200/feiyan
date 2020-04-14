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
            title_opts=opts.TitleOpts(title="国内城市死亡/治愈人数饼图"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_top="20%", pos_left="90%", orient="vertical"),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

    )
    c.render(path = "visual_html\国内城市死亡及治愈人数饼图.html")
    return c
