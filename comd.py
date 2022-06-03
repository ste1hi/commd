
# 引用库
import os,run,gettext
from init import Init

class Show_Command:

    # 初始化全局设置
    def __init__(self):
        ini = Init()
        self.language,self.langpath = ini.read()
        self.run = run.run()
        self.runc = run.run_cn()
        
        gettext.install("lang",self.langpath,codeset="utf-8")
        gettext.translation("lang",self.langpath,languages=[self.language])
        self._ = gettext.gettext
        
    
    # set命令
    def set0(self,len):     # 避免重名命名set0
        if len == 2:
            if self.com[1] == "Chinese" or self.com[1] == "zh_CN":
                self.language = "zh_CN"
                print("中文设置成功")
                gettext.translation("lang",self.langpath,languages=[self.language])
                self._ = gettext.gettext
            elif self.com[1] == "English" or self.com[1] == "en_US":
                self.language = "en_US"
                print("English setting successful")
                gettext.translation("lang",self.langpath,languages=[self.language])
                self._ = gettext.gettext
        else:
            print(self._("Command is not find"))

    def host(self,len):
        if len == 3:
            if self.language == "en_US":
                self.rune.chage_hosts(com=self.com[1],ip=self.com[2])
            elif self.language == "zh_CN":
                self.runc.chage_hosts(com=self.com[1],ip=self.com[2])        
        else:
            print(self._("Command is not find"))


    def web(self,len):
        if len == 3:
            if self.com[1] == "-u":
                response = self.rune.url(text=self.com[2])
                if response == "Command is not find":
                    print(self._("url is wrong"))
        elif len == 5:
            if self.com[1] == "-u":
                if self.com[3] == "-b":
                    if self.language == "en_US":
                        self.rune.url_in_browser(browser=self.com[4], url=self.com[2])
                    elif self.language == "zh_CN":
                        self.runc.url_in_browser(browser=self.com[4], url=self.com[2])
        else:
            print(self._("Command is not find"))


    def img(self,len):
        if len == 1:
            if self.language == "en_US":
                self.rune.img_help()
            elif self.language == "zh_CN":
                self.runc.img_help()
        elif len == 2:
            if self.com[1] == "-help":
                if self.language == "en_US":
                    self.rune.img_help()
                elif self.language == "zh_CN":
                    self.runc.img_help()
            else:
                print(self._("Command is not find"))
        elif len == 3:
            if self.com[1] == "-o":
                if self.language == "en_US":
                    self.rune.img_open(name=self.com[2])
                elif self.language == "zh_CN":
                    self.runc.img_open(name=self.com[2])
            elif self.com[1] == "-g":
                if self.language == "en_US":
                    self.rune.img_gray(name=self.com[2])
                elif self.language == "zh_CN":
                    self.runc.img_gray(name=self.com[2])
            elif self.com[1] == "-l":
                if self.language == "en_US":
                    self.rune.img_line(name=self.com[2])
                elif self.language == "zh_CN":
                    self.runc.img_line(name=self.com[2])
            else:
                print(self._("Command is not find"))
        else:
            print(self._("Command is not find"))


    def lf(self,len):
        if len == 1:
            print(os.listdir())
        elif len == 2:
            if self.com[1] == "?":
                if self.language == "en_US":
                    self.rune.lf_help()
                elif self.language == "zh_CN":
                    self.runc.lf_help()
            elif self.com[1] == "-m":
                self.rune.lf_m()
            elif self.com[1] == "-f":
                self.rune.lf_f()
            else:
                print(self._("Command is not find"))
        elif len == 3:
            if self.com[1] == "-p":
                try:
                    print(os.listdir(self.com[2]))
                except FileNotFoundError:
                    print(self._("Please enter true path"))
        elif len == 4:
            if self.com[1] == "-m":
                if self.com[2] == "-p":
                    self.rune.lf_mp(path=self.com[3])
                else:
                    print(self._("Command is not find"))
            elif self.com[1] == "-f":
                if self.com[2] == "-p":
                    self.rune.lf_fp(path=self.com[3])
            else:
                print(self._("Command is not find"))
        else:
            print(self._("Command is not find"))
            

    def file(self,len):
        if len == 1:
            if self.language == "en_US":
                self.rune.file_help()
            elif self.language == "zh_CN":
                self.runc.file_help()
        elif len == 2:
            if self.com[1] == "?":
                if self.language == "en_US":
                    self.rune.file_help()
                elif self.language == "zh_CN":
                    self.runc.file_help()
            else:
                print(self._("Command is not find"))
        elif len == 3:
            if self.com[1] == "cat":
                if self.language == "en_US":
                    self.rune.file_cat(self.com[2])
                elif self.language == "zh_CN":
                    self.runc.file_cat(self.com[2])
            elif self.com[1] == "rm":
                if self.language == "en_US":
                    self.rune.file_rm(self.com[2])
                elif self.language == "zh_CN":
                    self.runc.file_rm(self.com[2])
            elif self.com[1] == "new":
                if self.language == "en_US":
                    self.rune.file_new(self.com[2])
                elif self.language == "zh_CN":
                    self.runc.file_new(self.com[2])
            elif self.com[1] == "append":
                if self.language == "en_US":
                    self.rune.file_append(self.com[2])
                elif self.language == "zh_CN":
                    self.runc.file_append(self.com[2])
            else:
                print(self._("Command is not find"))
        else:
            print(self._("Command is not find"))


    def cd(self,len):
        if len == 1:
            if self.language == "en_US":
                print("cd [PATH]:Change working directory")
            elif self.language == "zh_CN":
                print("cd [PATH]:改变工作路径")
        elif len == 2:
            if self.com[1] == "?":
                if self.language == "en_US":
                    print("cd [PATH]:Change working directory")
                elif self.language == "zh_CN":
                    print("cd [PATH]:改变工作路径")
            else:
                try:
                    os.chdir(self.com[1])
                except FileNotFoundError:
                    print(self._("Please enter true path"))
        else:
            print(self._("Command is not find"))


    def command(self):
        print(os.getcwd(), ">>", end="")
        self.cmd = input()
        self.com = self.cmd.split()
        self.com_len = len(self.com)
        if self.com_len > 0:
            if self.com[0] == "exit" or self.com[0] == "quit" or self.com[0] == "bye":
                print(self._("bye"))
                exit()
            elif self.com[0] == "cd":
                self.cd(self.com_len)
            elif self.com[0] == "lf":
                self.lf(self.com_len)
            elif self.com[0] == "web":
                self.web(self.com_len)  
            elif self.com[0] == "set":
                self.set0(self.com_len)    
            elif self.com[0] == "host":
                self.host(self.com_len) 
            elif self.com[0] == "img":
                self.img(self.com_len) 
            elif self.com[0] == "file":
                self.file(self.com_len)     
            else:

                # if self.language == "en_US":
                #     print(self.rune.url(text=self.com[0]))
                # elif self.language == "zh_CN":
                #     print(self.runc.url(text=self.com[0]))

                print(self._("Command is not find"))





if __name__ == "__main__":
    show_command = Show_Command()
    while True:
        try:
            while True:
                show_command.command()
        except Exception as e:
            print("\n"+str(e))