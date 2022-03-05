from api import api_blue
from flask import *
import requests, json
import time


class BingImg:
    def __init__(self):
        self.Update()

    def Update(self):
        self.cont = requests.get("https://api.xygeng.cn/Bing/").content
        self.date = time.strftime("%Y-%m-%d", time.localtime())
    
    def Get(self):
        date = time.strftime("%Y-%m-%d", time.localtime())
        if date == self.date:
            return self.cont
        else:
            self.Update()
            return self.cont


BING = BingImg()


@api_blue.route('/bing', methods=['GET'])
def Bing():
    return BING.Get()