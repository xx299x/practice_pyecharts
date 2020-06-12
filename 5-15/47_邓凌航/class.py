from pyecharts.charts import Map
from pyecharts import options as opts


value_1 = [2, 1, 1, 1, 1, 1, 1, 2, 2,1,13]
attr_1 = ["安徽","福建","甘肃","广西","贵州","河南","湖北","江西","山西","四川","浙江"]
value_2 = [1,0,1,1,0,2,0,1,1,0,1,8]
attr_2 = ["安徽","福建","甘肃","河北","广西","贵州","河南","湖北","江西","山西","四川","浙江"]
def map_visualmap():
    c = (
        Map()
        .add("男", [list(z) for z in zip(attr_1, value_1)],"china")
        .add("女", [list(z) for z in zip(attr_2, value_2)],"china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(max_=200,is_piecewise=True)
        )
    )
    return c
a = map_visualmap()
a.render(r"D:\zg\3.html")