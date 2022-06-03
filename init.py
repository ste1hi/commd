'''
Author: ste1hi 1874076121@qq.com
Date: 2022-06-02 22:48:27
LastEditors: ste1hi 1874076121@qq.com
LastEditTime: 2022-06-03 08:47:51
FilePath: \commnd\init.py
Description: 
读取配置文件
Copyright (c) 2022 by ste1hi 1874076121@qq.com, All Rights Reserved. 
'''
import os
from configparser import ConfigParser
class Init :
    
    def __init__(self):

        # 定义配置文件位置
        self.gl_filename = "C:/Users/{0}/.comd/config.ini".format(os.getlogin())
        self.gl_directory = "C:/Users/{0}/.comd".format(os.getlogin())

        # 定义配置变量
        self.gl_language = ""

        # 新建配置文件
        if not os.path.exists(self.gl_filename):
            if not os.path.exists(self.gl_directory):
                os.mkdir(self.gl_directory)
            with open(self.gl_filename,"w") as f:   # 创建配置文件并写入内容
                f.write("[LANGUAGE]\nlanguage=zh_CN\npath=C:\\Users\\{0}\\.comd\\locale".format((os.getlogin())))


    def read(self):
    
        conn = ConfigParser()   # 定义读取对象
        conn.read(self.gl_filename)
        self.gl_language = conn.get("LANGUAGE","language")
        self.gl_langpath = conn.get("LANGUAGE","path")
        return self.gl_language,self.gl_langpath





