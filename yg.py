'''
Created on 2018.4.11

@author: Administrator
'''
from my_yg.common import yg


class myargs():
    def __init__(self, URL, output_dir, debug):
        self.URL = []
        if URL != None:
            self.URL.append(URL)
        self.auto_rename=False
        self.cookies=None
        self.debug=debug
        self.extractor_proxy=None
        self.force=False
        self.format=None
        self.help=False
        self.http_proxy=None
        self.info=False
        self.input_file=None
        self.itag=None
        self.json=False
        self.no_caption=False
        self.no_merge=False
        self.no_proxy=False
        self.output_dir=output_dir
        self.output_filename=None
        self.password=None
        self.player=None
        self.playlist=False
        self.socks_proxy=None
        self.stream=None
        self.timeout=600
        self.url=False
        self.version=False
        
url = 'http://news.cctv.com/2018/04/12/VIDEbl9oWTyX1lUIgEVvvKT7180412.shtml'
output_dir = '.'
debug = True      
        
if __name__ == '__main__':
    yg(URL = url, output_dir = output_dir, debug = debug)
