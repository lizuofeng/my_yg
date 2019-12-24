class myargs:
    def __init__(self, url, output_dir, debug):
        self.URL = []
        if url is not None:
            self.URL.append(url)
        self.auto_rename = False
        self.cookies = None
        self.debug = debug
        self.extractor_proxy = None
        self.force = False
        self.format = None
        self.help = False
        self.http_proxy = None
        self.info = False
        self.input_file = None
        self.itag = None
        self.json = False
        self.no_caption = False
        self.no_merge = False
        self.no_proxy = False
        self.output_dir = output_dir
        self.output_filename = None
        self.password = None
        self.player = None
        self.playlist = False
        self.socks_proxy = None
        self.stream = None
        self.timeout = 600
        self.url = False
        self.version = False
