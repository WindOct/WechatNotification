import requests
import json
class WechatMessagePush:
    def __init__(self, appid, appsecret, temple_id):
        self.appid = appid
        self.appsecret = appsecret
        # 模板id,参考公众号后面的模板消息接口 -> 模板ID(用于接口调用):IG1Kwxxxx
        self.temple_id = temple_id
        self.token = self.get_Wechat_access_token()

    def get_Wechat_access_token(self):
        '''
        获取微信的access_token： 获取调用接口凭证
        :return:
        '''
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.appid}&secret={self.appsecret}"
        response = requests.get(url)
        res = response.json()
        if "access_token" in res:
            token = res["access_token"]
            return token

    def get_wechat_accout_fans_count(self):
        '''
        获取微信公众号所有粉丝的openid
        '''
        next_openid = ''
        url = f"https://api.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&next_openid={next_openid}"
        response = requests.get(url)
        res = response.json()['data']['openid']

    def send_wechat_temple_msg(self, content):
        '''
        发送微信公众号的模板消息'''
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.token}"

        # fan_open_id = self.get_wechat_accout_fans_count()
        # for open_id in fan_open_id:
        body = {
            "touser":'opM8V6Ygh0w7TPo-_BiGAa03-ySc',
            'template_id': self.temple_id,
            "topcolor": "#667F00",
            "data": {
                "key": {'value':content}
            }
        }
        headers = {"Content-type": "application/json"}
        data = json.JSONEncoder().encode(body)
        print(data)
        res = requests.post(url=url, data=data, headers=headers)


    def send_wechat_temple_msg1(self, content):
        '''
        发送微信公众号的模板消息'''
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.token}"

        # fan_open_id = self.get_wechat_accout_fans_count()
        # for open_id in fan_open_id:
        #取消这两行的注释，就可将body中的touser进行替换，从而给每个关注用户推送消息
        print (content)
        body = {
            "touser":'opM8V6Ygh0w7TPo-_BiGAa03-ySc',
            'template_id': self.temple_id,
            "topcolor": "#667F00",
            "data": content
        }
        headers = {"Content-type": "application/json"}
        data = json.JSONEncoder().encode(body)
        print(data)
        res = requests.post(url=url, data=data, headers=headers)
if __name__ == '__main__':
    #fill the parameters here
    appid = ""
    screct = ""
    template_id = ''
    with open('wechatannouncement.txt','r',encoding='utf-8') as f1:
        with open('upwechatannouncement.txt','r',encoding='utf-8') as f2:
            str1=f1.read()
            str2=f2.read()
            if str1!=str2:
                WechatMessagePush(appid, screct, template_id).send_wechat_temple_msg(str1)
                f2.close()
                with open('upwechatannouncement.txt','w',encoding='utf-8') as f3:
                    f3.write(str1)

    with open('wechatdekt.json','r') as fi1:
        li1=fi1.read()
        list1=json.loads(li1)
        print(list1)
    with open('upwechatdekt.json','r', encoding='utf-8') as fi2:
        li2=fi2.read()
        list2 = json.loads(li2)
        print (list2)
    result=[i for i in list1 if i not in list2]
    print(result)
    if result:
        rec={
            'title':{'value':'化学化工学院挑战营1'},
            'time':{'value':'2023/07/16 14:00 -\n2023/07/20 14:00'}
        }
        for item in result:
            rec['title']={'value':item[0]}
            rec['time']={"value":item[2]}
            WechatMessagePush(appid, screct, temple_id).send_wechat_temple_msg1(rec)
        with open('upwechatdekt.json','w',encoding='utf-8') as f3:
            json.dump(list1,f3)