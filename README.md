# my_yg
对you_get进行修改从而提出对外开放的接口
参数类:
```
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
```
接口:
```
from my_yg.common import yg
yg(URL = None, output_dir = '.', debug = False)
``` 
  其中URL为视频播放页URL,output_dir为视频文件输出路径,debug为是否进行调试的标志
