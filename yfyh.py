import random #:1
import requests #:2
from loguru import logger #:3
'''
频道链接:https://t.me/maomaoalal  交流群:https://t.me/+5xDWXXg-Ug03ZGI1
鸾凤玉华 小程序
抓包 api.luanfengyuhua.cn 域名
变量：sessionkey  
签到10天大概20缘值 价值20块钱
也可以兑换实物
corn 一天一次
'''
# 账号配置
sessionkey_list =['sessionkey']# 多账号配置 ['session1','session2']
info ='''
频道链接:https://t.me/maomaoalal  交流群:https://t.me/+5xDWXXg-Ug03ZGI1
鸾凤玉华 小程序账号配置
抓包 api.luanfengyuhua.cn 域名
变量：sessionkey  
签到10天大概20缘值 价值20块钱
也可以兑换实物
corn 一天一次
'''#:25
def get_ua ():#:26
    OOO0OO0O00000OOOO =random .randint (55 ,62 )#:27
    O00OOO0OO00OOO0OO =random .randint (0 ,3200 )#:28
    O0O000OO000OOO0OO =random .randint (0 ,140 )#:29
    OOOOOO00OO0O00O00 =['(Windows NT 6.1; WOW64)','(Windows NT 10.0; WOW64)','(X11; Linux x86_64)','(Macintosh; Intel Mac OS X 10_12_6)']#:33
    OOOOOOO000OOO0000 ='Chrome/{}.0.{}.{}'.format (OOO0OO0O00000OOOO ,O00OOO0OO00OOO0OO ,O0O000OO000OOO0OO )#:34
    O000OO0OO0O000O0O =' '.join (['Mozilla/5.0',random .choice (OOOOOO00OO0O00O00 ),'AppleWebKit/537.36','(KHTML, like Gecko)',OOOOOOO000OOO0000 ,'Safari/537.36'])#:38
    return O000OO0OO0O000O0O #:39
def Sign (OO00OO00O0O00O000 ,O0O0000OO0OO000OO ):#:42
    try :#:43
        OO0OOOOO0O00O00O0 ='https://api.luanfengyuhua.cn/Api/Signin/submit'#:44
        OO0OO0O000OO00OOO ={'crypt':'563ed8d6cc76e33bc5cd03ea95bc200c-1653397581000','sessionkey':O0O0000OO0OO000OO ,'User-Agent':OO00OO00O0O00O000 ,'content-type':'application/json','Accept-Encoding':'gzip,compress,br,deflate','Referer':'https://servicewechat.com/wx0a33ac3ad3f4c06c/44/page-frame.html',}#:52
        O0OO000OOO0OOOOOO =requests .post (url =OO0OOOOO0O00O00O0 ,headers =OO0OO0O000OO00OOO ).json ()#:53
        if O0OO000OOO0OOOOOO ['status']==200 :#:54
            return '签到成功'#:55
        elif O0OO000OOO0OOOOOO ['status']==100 :#:56
            return '今日已签到'#:57
        else :#:58
            return '未知错误'+O0OO000OOO0OOOOOO #:59
    except Exception as O0000OOOOOO000OOO :#:60
        return O0000OOOOOO000OOO #:61
if __name__ =='__main__':#:64
    logger .info (info )#:65
    logger .info (f'当前共{len(sessionkey_list)}个账号')#:66
    my_ua =get_ua ()#:67
    for sessionkey in sessionkey_list :#:68
        Sign_result =Sign (my_ua ,sessionkey )#:69
        logger .info (Sign_result )#:70
