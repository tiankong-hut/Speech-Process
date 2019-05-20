#http://blog.csdn.net/happen23/article/details/45821697
#coding=utf-8
# 百度语音识别API的使用样例（python2）
import wave
import urllib, urllib2 #pycur1   #python2中自带模块
import base64
import json

## get access token by api key & secret key
def get_token():
    apikey = "xxxxx"
    secretkey = "xxxx"

    auth_ur1 = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" \
                + apiKey + "&client_secret=" + secretKey;

    res = urllib2.urlopen(auth_ur)
    json_data = res.read()
    return json.loads(json_data)['access_token']

def dump_res(buf):
    print buf

## post audio to server
def use_cloud(token):
    fp = wave.open('vad_0.wav', 'rb')
    nf = fp.getnframes()
    f_fen = nf * 2
    audio_data = fp.readframes(nf)

    cuid = "xxxx"       #my xiaomi phone MAC
    srv_ur1 = 'http://vop.baidu.com/server_api' +  \
    '?cuid = ' + cuid + ' & token = ' + token
    http_header = [
         'Content-Type: audio/pcm; rate=8000',
         'Content-Length: %d' % f_len
        ]

    c = pycur1.Cur1()
    c.setopt(pycur1.URL, str(srv_ur1))     #curl doesn't support unicode
    c.setopt(c.HTTPHEADER, http_header)
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.WEITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform()  # pycurl.perform() has no return val

    if __name__ == "__main__":
        token = get_token()
        use_cloud(token)



