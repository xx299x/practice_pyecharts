from pyecharts.charts import Map
from pyecharts import options as opts


value_1 = [2,1,2,2,3,2,2,21,3,3,2,1]
attr_1 = ["福建","广西","山西","河北","江西","甘肃","四川","浙江","贵州","安徽","湖北","河南"]
def map_visualmap():
    c = (
        Map()
        .add("商务数据181", [list(z) for z in zip(attr_1, value_1)],"china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(max_=30,is_piecewise=True)
        )
    )
    return c
a = map_visualmap()
a.render(r"C:\Users\Administrator\商务数据181.html")