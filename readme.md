## 浙江大学电气学院学术讲座自动报名脚本

## 配置环境

Python>=3.9 （Python=3.11 经测试可完美运行）

```
pip install selenium
pip install webdriver-manager
```

## 运行脚本

填入浙大通行证的账号和密码（代码开源，保护个人隐私）

```
python main.py
```

**注意**：请将打开的窗口最大化！否则将会闪退！

## TODO

* [X] 取消GoogleDriver的驱动需求，一键适配
* [ ] 通过github actions来实现全自动抢讲座以及订阅消息功能
