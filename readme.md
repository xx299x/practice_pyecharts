# 作业清单

共有4个文件夹

1. `1-7_practice` 1-7的作业。
2. `5-15\`，5月15的作业
3. `6-5\`6-5号的作业
4. `期中_practice\`期中测试的作业

第一个是

# 提交作业教程

**注意**：如果有`fork`我的仓库，请拉到最后看`其他问题`。


## 第一步

登陆github账号

进入网址：https://github.com/xx299x/practice_pyecharts.git

点击右上角的`Fork`。

稍等一会儿会自动刷新。

刷新之后，找到`Clone or download`并点击，复制下面的地址。

## 第二步
打开 git bash 

输入以下代码

**将后面的https地址换为你刚才复制的。**
```bash
cd /d/
git clone https://github.com/yourId/practice_pyecharts.git
cd practice_pyecharts
```
用资源管理器打开目录`D:/practice_pyecharts`
将作业目录移动到`5-15`文件夹下。
目录结构如下：
```
--practice_pyecharts
----5-15
-------01_张三
-------02_李四
-------03_王五
----
```
如果是第一次使用github 上传文件，先设置 邮箱和用户名
```
git config --global user.email "example@example.com"
git config --global user.name "Author"
```
如果已经设置过用户名继续下面的步骤。
回到bash输入
```bash
git add .
git commit -m '更新日志'
git push origin master
```
然后输入账号密码提交。
## 第三步
回到`fork的仓库`，点击`new pull request`

到下一个页面继续点击`create pull request`

然后在`Title`文本框中填写你的`学号+姓名`后点击`create pull requset`即可。

## 其他问题

如果出现其他问题，请删除`fork的仓库`和删除`d盘`的`practice_pyecharts`文件夹后重新按本教程操作。

删除步骤如下：

1. 进入你的`fork的仓库`主页。
2. 点击`sitting`。
3. 拉到网页最下方，点击`Delete this repository`
4. 确认删除。
