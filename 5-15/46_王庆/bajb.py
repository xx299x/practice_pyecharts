from pyecharts.charts import Map
from pyecharts import options as opts
value_1 = [2,3,2,21,3,2,2,2,1,3,1,2]
attr_1 = ["福建","江西","四川","浙江","贵州","山西"]
value_2 = [2,2,1,3,1,2]
attr_2 = ["甘肃","河北","河南","安徽","广西","湖北"]
def map_visualmap():
    c = (
        Map()
        .add("商务181", [list(z) for z in zip(attr_1, value_1)],"china")
        .add("商务181", [list(z) for z in zip(attr_2, value_2)],"china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(max_=25,is_piecewise=True)
        )
    )
    return c
a = map_visualmap()
a.render(r"C:\Users\Administrator\wq1111.html")

#from pyecharts import options as opts
#from pyecharts.charts import Map
#from pyecharts.faker import Faker

#c = (
 #   Map()
  #  .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
   # .set_global_opts(
    #    title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）"),
     #   visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
    #)
    #.render("map_visualmap_piecewise.html")
#)
