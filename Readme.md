# MyBridge 资产库更新日志

## v0.0.0.0.1
- 完成基本功能
## v0.0.0.0.2
- 资产导入页面在资产导入过程中添加进度条防止窗口卡住
- 主页搜索框,使用回车键执行搜索
- 修复资产导入页面左侧待导入资产队列当当前导入的资产是队列第一个资产,导入完成后,不会自动选中下一个的问题
- 修复在导入资产后,切换回主页,不更新资产列表的问题
- 在打包时将资源文件打包到exe文件中
- 修正窗口左侧导航栏宽度
- 给软件添加启动页面
## v0.0.0.0.3
- 加载资产多线程优化
- UI效果优化
- 导入资产时检测数据库是否被占用,在占用时等待,防止出现多个实例同时写入数据库的情况
## v0.0.0.0.4
- 