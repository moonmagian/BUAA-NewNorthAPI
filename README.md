# 北航新北区查询 API
## 查询电费
查询可用的电量，必须使用 post。
- contentType: 'application/json; charset=utf-8'。
- url: http://weixin.lrgj.net.cn/ics/rest/wxdev/getlvalue
- data（以 json 传递）:
  - stucode: 个人学号
  - type: 1
- result（以 json 返回）:
    - success: 请求是否成功，true 成功。
    - msg: 请求相关的消息，成功为 "操作成功"。
    - data: 仅成功才会返回。
        - provalue: 剩余电量，字符串，格式为 "电量kWh"

## 查询水费
查询可用的水量，必须使用 post。
- contentType: 'application/json; charset=utf-8'。
- url: http://weixin.lrgj.net.cn/ics/rest/wxdev/getSurplusDegreeWaterMeter
- data（以 json 传递）:
  - stucode: 个人学号
- result（以 json 返回）:
    - success: 请求是否成功，true 成功。
    - msg: 请求相关的消息，成功为 "操作成功"。
    - data: 仅成功才会返回。
        - surplusDeg: 剩余水量，整数。

## 示例程序
- power.sh: 查询电费的 shell 脚本，需要安装 jq 与 curl，在使用 conky 或者配置各类 bar 时相当有用。
- water.sh: 查询水费的 shell 脚本，需要安装 jq 与 curl，在使用 conky 或者配置各类 bar 时相当有用。
- py3status_buaa_power.py: 用于 py3status 的示例 Python 脚本，使用前请使用 py3status 配置文件或直接修改脚本中的学号。

## 你是如何得到这些接口的
接口没上 https，burpsuite 很简单就能抓到请求了，https 普及，刻不容缓。