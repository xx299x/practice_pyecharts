from pyecharts.charts import Map
from pyecharts import options as opts

#用Excel数据透视表统计出全班分布人数
value_1 = [3,1,2,1,3,1,1,2,3,2,2,21,1]
attr_1 = ["安徽","福建","甘肃","广西","贵州","河北","河南","湖北","江西","山西","四川","浙江"]
def map_visualmap():
    c = (
        Map()
        .add("商数181", [list(z) for z in zip(attr_1, value_1)],"china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(max_=21,is_piecewise=True)
        )
    )#max数值决定地区块的颜色
    return c
a = map_visualmap()
a.render(r"D:\33\sw181.html") #设置存储路径