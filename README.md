# api_test_framework

接口自动化测试

# To-Do
- Hamcrest改造用例断言
- 测试报告生成

# Done
- 配置相关的数据驱动
- log打印
- jsonpath的封装
- post接口所传body的yaml数据驱动
- yaml中参数可以传入变量（应用场景如取出创建出来的实例id，传给删除接口的param）
- 检查实例状态时的重试增加超时机制
- 使用TestBase或fixture封装通用测试用例（创建主机和删除主机）
- 日志输入到log文件中