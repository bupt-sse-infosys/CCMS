# CCMS
高校课程管理系统

## 注意事项

1. 提交的时候只提交py文件和页面，其他别提交

2. 冲突的时候注意一下，别给覆盖了

3. python项目整个传上来貌似也不能down下来就直接运行，暂时先这样吧

## 导入项目

1. 从git上check out，如图：

	![](https://i.imgur.com/XazdErX.png)
	![](https://i.imgur.com/6DDMtdn.png)

	URL: `https://github.com/bupt-sse-infosys/CCMS.git`

2. File -> Settings... 进入设置， Project: CCMS -> Project Interpreter， 点击设置选择add，如图：

	![](https://i.imgur.com/BHKmJM0.png)

	弹出如下图，会在项目下新建一个venv，点击ok，完成后如图：

	![](https://i.imgur.com/SU2gYQb.png)

3. 下载依赖：点击`+`号

	![](https://i.imgur.com/2iImRDe.png)

	【注意】配置国内镜像下的快，点击`Manage Repositories`，点`+`号输入`https://pypi.douban.com/simple/`(豆瓣镜像--传说最好用)，ok。可以继续添加，不加也ok，其他镜像可以自行百度：`http://mirrors.aliyun.com/pypi/simple/`（阿里云的）。

	![](https://i.imgur.com/wwPf4eC.png)

	- 安装flask：搜索框搜索flask，选中flask，install package

		![](https://i.imgur.com/rBx0yeU.png)

		安装成功后如图：

		![](https://i.imgur.com/0woPwIw.png)

	- 安装flask-sqlalchemy，方法同上

	- 安装pymysql，方法同上

4. 配置数据库，打开setting.py，修改成自己的数据库

	![](https://i.imgur.com/6tA6IYp.png)

5. 运行db_create.py是构建数据库，运行后可见数据库创建了表。运行之后，控制台会有一个警告，网上说貌似是编码的问题，不过我怎么改编码还是会报，不过目前没有什么影响，就先这样吧。
6. 修改编码：File -> Settings -> Editor -> File Encodings，改成UTF-8，如图：

	![](https://i.imgur.com/aRap921.png)
		