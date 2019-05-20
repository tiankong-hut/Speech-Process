# coding=UTF-8
# http://www.360doc.com/content/16/0410/21/3852985_549560441.shtml
# 用Python编程实现语音控制电脑
# 电脑面前的你，是否也希望能让电脑听命于你？当你累的时候，只需说一声“我累了”，电脑就会放着优雅的轻音乐来让你放松。
# 或许你希望你在百忙之中，能让电脑郎读最新的NBA比分赛况….一切都是那么惬意。
# SAPI是微软Speech API , 是微软公司推出的语音接口
# 先进行一个简单的环境调试： 启动语音识别器，同时系统将会重复你所录入的语音，当遇到“turn off”时，就会自动关闭识别系统。
while True:
    phrase = speech.input()             #speech（）
    speech.say("You said %s" %phrase)
    if phrase == "turn off":
        break












