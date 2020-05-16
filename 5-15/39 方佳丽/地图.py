from pyecharts.charts import Map
from pyecharts import options as opts


value_1 = [155, 10, 66, 78, 44, 38, 88, 50, 20]
attr_1 = ["福建","山东","北京","上海","江西","新疆","内蒙古","云南","重庆"]
value_2 = [200, 100, 166, 78, 144, 38, 88, 150, 120]
attr_2 = ["辽宁","广东","广西","青海","甘肃","新疆","内蒙古","云南","重庆"]
def map_visualmap():
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(attr_1, value_1)],"china")
        .add("商家b", [list(z) for z in zip(attr_2, value_2)],"china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(max_=200,is_piecewise=True)
        )
    )
    return c
a = map_visualmap()
a.render(r"C:\Users\Administrator\中国地图.html")