#注意，该代码只能用于个人短信发送
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC0ee04fe3c38078c9912dacdde6df5d91"
# Your Auth Token from twilio.com/console
auth_token  = "733968de791842633a2fed93c4fba552"
client = Client(account_sid, auth_token)
message = client.messages.create(
    # to="+86xxxxxxxxxxx,替换成注册的手机号，也就是要接收短信的手机号，中国区是+86",
    # from_="+15017250604，替换成你的twilio phone number，twilio分配给你的",
    to="+8619834521692",#要发给的人
    from_="18135444627",
    body="张伟是个王八蛋")#要发送的内容
print("短信发送成功")
