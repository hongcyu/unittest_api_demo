## unittest_api_demo
### 项目框架

![image-20201025222533960](https://gitee.com/hongcyu/image/raw/master/images/image-20201025222533960.png)

tree:

![](https://cdn.jsdelivr.net/gh/hongcyu/image/images/test_tree1.png)

### 效果图

![](https://cdn.jsdelivr.net/gh/hongcyu/image/images/test_report3.png)

### v1.1

1. 添加自动识别行列属性

2. report的views不能点击：

   ```
   打开\Lib\site-packages\HtmlTestRunner\template\report_template.html
   修改地址换成国内能连的地址：
   比如：http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js
   ```

   ![](https://cdn.jsdelivr.net/gh/hongcyu/image/images/test_report1.png)

3. report不能显示中文：

   ```
   修改\Lib\site-packages\HtmlTestRunner\result.py下的generate_file
   加上encoding='utf-8'
   ```

   ![](https://cdn.jsdelivr.net/gh/hongcyu/image/images/test_report4.png)





### v1.0

1. 引入了单元测试、html测试报告以及断言结果
3. 引入了ddt数据驱动
4. 实现用例的可配置
5. 实现路径的可配置



### 参考资料：

ddt官方文档：https://ddt.readthedocs.io/en/latest/

### 第三方模块:

1. ddt
2. openpyxl
3. requests
4. html-testRunner

