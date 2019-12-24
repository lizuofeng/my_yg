"""
Created on 2018.4.11

@author: zfli
"""
from my_yg.common import yg

url = 'http://news.cctv.com/2018/04/12/VIDEbl9oWTyX1lUIgEVvvKT7180412.shtml'
output_dir = '.'
debug = True      
        
if __name__ == '__main__':
    yg(url=url, output_dir=output_dir, debug=debug)
