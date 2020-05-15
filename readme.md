# 提交作业教程

## 第一步

登陆github账号

进入网址：https://github.com/xx299x/practice_pyecharts.git

点击右上角的`Fork`。

稍等一会儿会自动刷新。

刷新之后，找到`Clone or download`并点击，复制下面的地址。

## 第二步
打开 git bash 

输入以下代码

将后面的https地址换为你刚才复制的。
```bash
cd /d/
git clone https://github.com/xx299x/practice_pyecharts.git
cd practice_pyecharts
```
用资源管理器打开目录`D:/practice_pyecharts`
将作业目录移动到`5-15`文件夹下。
目录结构如下：
```
--practice_pyecharts
----5-15
-------01 张三
-------02 李四
-------03 王五
----
```


然后回到bash输入
```bash
git config --global user.email "example@example.com"
git config --global user.email "Author"
git add .
git commit -m '更新日志'
git push origin master
```
然后输入账号密码提交。
## 第三步
回到你的仓库，点击`new pull request`

到下一个页面继续点击`create pull request`

然后在`Title`文本框中填写你的`学号+姓名`后点击`create pull requset`即可。

## 其他问题

如果出现其他问题，请删除fork的仓库后重新按本教程操作。

删除步骤如下：

1. 进入你的仓库主页。
2. 点击`sitting`。
3. 拉到网页最下方，点击`Delete this repository`
4. 确认删除。
