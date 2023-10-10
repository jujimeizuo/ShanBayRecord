# ShanBay Record

用 iOS 快捷指令配合 Actions 实现自动打卡

## setup secrets

- G_T
- SHANBAY_USERNAME
- TELE_TOKEN
- TELE_CHAT_ID

## Shortcuts

1. Get actions id（need to apply token）

```shell
curl https://api.github.com/repos/jujimeizuo/running_page/actions/workflows -H "Authorization: token d8xxxxxxxxxx" # change to your config
```
<center><img src="https://cdn.jujimeizuo.cn/blog/2023/10/get-action-id.jpg" alt="get-action-id"></center>

2. Binding shortcut instruction

    1. Get it via icloud [ShanBayRecord-Shortcuts-Template](https://www.icloud.com/shortcuts/4ab9336490574538847ec9f04681aea4)

    2. Modify the dictionary parameters in the following figure
   <center> <img src="https://cdn.jujimeizuo.cn/blog/2023/10/ShabayRecord-Template.png"> </center>

3. automatic：when close ShanBay App

<center>
<img src="https://cdn.jujimeizuo.cn/blog/2023/10/new-automation.png" width=20% height=20%>
<img src="https://cdn.jujimeizuo.cn/blog/2023/10/select-close.png" width=20% height=20%>
<img src="https://cdn.jujimeizuo.cn/blog/2023/10/select-shortcut.png" width=20% height=20%>
<img src="https://cdn.jujimeizuo.cn/blog/2023/10/finish-automation.png" width=20% height=20%>
</center>

## Appreciation

Thank you, that's enough. Just enjoy it.