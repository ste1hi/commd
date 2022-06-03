from init import Init
import gettext

class run():  
    def __init__(self):
        ini = Init()
        self.language,self.langpath = ini.read()
        gettext.install("lang",self.langpath,codeset="utf-8")
        gettext.translation("lang",self.langpath,languages=[self.language])
        self._ = gettext.gettext

    def new_method(self, sys):
        sys.setdefaultencoding('utf8')

    def file_help(self):
        print(self._("\nfile  = file ?:Query help"))
        print(self._("file cat [FILE_NAME]:Displays the file read-only (the file must exist)"))
        print(self._("file rm [FILE_NAME]:Deletes the specified file (file must exist)"))
        print(self._("file new [FILE_NAME]:New file"))
        print(self._("file append [ADDITIONAL_CONTENT] [FILE_NAME]:Appends the specified content to the end of the file (the file may not exist)\n"))


    def lf_help(self):
        print(self._("\nlf ：View the files and folders in the current directory"))
        print(self._("lf ?：See the help"))
        print(self._("lf -m：View the folder in the current directory"))
        print(self._("lf -f：View the files in the current directory"))
        print(self._("lf -m -p [PATH]：View the folder under the path"))
        print(self._("lf -p [PATH]：View the files and folders under the path"))
        print(self._("lf -f -p [PATH]：View the file under the path\n"))


    def file_cat(self,file_name):
        try:
            f = open(file_name, "r", encoding="utf_8")
            print(self._(f.read()))
            f.close()
        except BaseException:
            print(self._("\nError opening file\n"))


    def file_rm(self,file_name):
        import os
        os.remove(file_name)


    def file_new(self,file_name):
        try:
            f = open(file_name, "r")  #以只读模式打开，判断文件是否存在
        except FileNotFoundError:
            f1 = open(file_name, "a+")
            f1.close()
        else:
            f.close()
            print(self._("\nFile already exists\n"))


    def file_append(self,file_name):
        f = open(file_name, "a")
        f.write(input("Please enter append text>>>"))
        f.close()

    def lf_m(self):
        import os
        all_file = os.listdir()
        j = []
        for each_file in all_file:
            if os.path.isdir(each_file):
                j.append(each_file)
        print(j)

    def lf_f(self):
        import os
        all_file = os.listdir()
        j = []
        for each_file in all_file:
            if os.path.isfile(each_file):
                j.append(each_file)
        print(j)

    def lf_mp(self,path):
        import os
        all_file = os.listdir(path)
        j = []
        for each_file in all_file:
            if os.path.isdir(os.path.join(path, each_file)):
                j.append(each_file)
        print(j)

    def lf_fp(self,path):
        import os
        all_file = os.listdir(path)
        j = []
        for each_file in all_file:
            if os.path.isfile(os.path.join(path, each_file)):
                j.append(each_file)
        print(j)

    def img_help(self):
        pass

    def img_open(self,name):
        import os, cv2
        img = cv2.imread(os.path.join(os.getcwd(), name))
        cv2.namedWindow(name, 0)
        cv2.imshow(name, img)
        print(self._("\nThe picture is open\n"))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def img_gray(self,name):
        import os, cv2
        img = cv2.imread(os.path.join(os.getcwd(), name),0)
        cv2.namedWindow(name, 0)
        cv2.imshow(name, img)
        print(self._("\nThe picture is open\n"))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def img_line(self,name):
        import os, cv2
        img = cv2.imread(os.path.join(os.getcwd(), name), 0)
        e = cv2.Canny(img, 50, 150, apertureSize=3)
        cv2.namedWindow(name,0)
        cv2.imshow(name, e)
        print(self._("\nThe picture is open\n"))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def chage_hosts(self,com,ip):
        import os
        path = r"C:\Windows\System32\drivers\etc\hosts"
        print(self._(os.system("ping "+ip)))
        confirm = input("\nConfirm to add {0} to  the hosts file(y/n)".format(ip))
        while True:
            if confirm == "y":
                with open(path, "a", encoding="utf-8") as f:
                    f.writelines("\n" + ip + " " + com)
                    return 0
            elif confirm == "n":
                return 0
            else:
                print(self._("Please enter either y or n"))

    def url(self,text):
        import webbrowser
        url_list = text.split("/")
        p = 0
        for j in url_list:
            url_2 = j.split(".")
            for i in url_2:
                if i == "com" or i == "cn" or i == "org":
                    webbrowser.open(text)
                    p = 1
        if p == 0:
            return "Command is not find"

    def url_in_browser(self,browser,url):
        import os,webbrowser
        if not browser:
            print(self._("Please enter true path"))
        else:
            # 判断浏览器路径是否存在
            if not os.path.exists(browser):
                print(self._("Please enter true path"))
            else:
                browser_task_name = browser.split('\\')[-1]  # 结束任务的名字
                browser_name = browser_task_name.split('.')[0]  # 自定义的浏览器代号
                webbrowser.register(browser_name, None, webbrowser.BackgroundBrowser(browser))
                url_list = url.split("/")
                p = 0
                for j in url_list:
                    url_2 = j.split(".")
                    for i in url_2:
                        if i == "com" or i == "cn" or i == "org":
                            webbrowser.get(browser_name).open_new_tab(url)  # 使用新注册的浏览器打开网页
                            p = 1
                if p == 0:
                    print(self._("url is wrong"))
