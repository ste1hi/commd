class Show_Command:

    def __init__(self):
        import os
        print(os.getcwd(), ">>", end="")
        self.cmd = input()
        self.com = self.cmd.split()
        self.com_len = len(self.com)



    def command(self):
        import os
        # 判断命令长度
        if self.com_len == 0:
            print("命令未找到")
        # 命令长度为1
        elif self.com_len == 1:
            # 命令为file
            if self.com[0] == "file":
                print("file 无参 = file ?:查询帮助")
                print("file cat 文件名:以只读方式显示文件(文件必须存在)")
                print("file rm 文件名:删除指定文件(文件必须存在)")
                print("file new 文件名:新建文件")
                print("file append 追加内容 文件名:向文件的最后追加指定内容(文件不一定存在)\n")

            elif self.com[0] == "exit":
                print("再见")
                exit()
            elif self.com[0] == "cd":
                print("请输入cd 目录；来改变工作目录")

            elif self.com[0] == "lf":
                print(os.listdir())
            elif self.com[0] == "find":
                print("find 无参 = find ?:查询帮助")
                print("find 搜索内容:用百度搜索")
                print("find -b 搜索内容：用百度搜索=find 搜索内容")
                print("find -s 搜索内容：用搜狗搜索")
                print("fi")
            else:
                print("命令未找到")
        # 命令长度为2
        elif self.com_len == 2:
            # 命令第一节为file
            if self.com[0] == "file":
                # 命令第2节为?
                if self.com[1] == "?":
                    print("file 无参 = file ?:查询帮助")
                    print("file cat 文件名:以只读方式显示文件(文件必须存在)")
                    print("file rm 文件名:删除指定文件(文件必须存在)")
                    print("file new 文件名:新建文件")
                    print("file append 文件名:向文件的最后追加指定内容(文件不一定存在)\n")

                else:
                    print("命令未找到")
            elif self.com[0] == "cd":
                if self.com[1] == "?":
                    print("请输入cd 目录；来改变工作目录")
                else:
                    try:
                        os.chdir(self.com[1])
                    except FileNotFoundError:
                        print("请输入正确的路径")
            elif self.com[0] == "lf":
                if self.com[1] == "?":
                    print("lf 无参：查看当前目录下的文件和文件夹")
                    print("lf ?：查看帮助")
                    print("lf -m：查看当前目录下的文件夹")
                    print("lf -f：查看当前目录下的文件")
                    print("lf -m -p 路径：查看路径下的文件夹")
                    print("lf -p 路径：查看路径下的文件和文件夹")
                    print("lf -f -p 路径：查看路径下的文件")

                elif self.com[1] == "-m":
                    all_file = os.listdir()
                    j = []
                    for each_file in all_file:
                        if os.path.isdir(each_file):
                            j.append(each_file)
                    print(j)

                elif self.com[1] == "-f":
                    all_file = os.listdir()
                    j = []
                    for each_file in all_file:
                        if os.path.isfile(each_file):
                            j.append(each_file)
                    print(j)

                else:
                    print("命令未找到")
            else:
                print("命令未找到")
        # 命令长度为3
        elif self.com_len == 3:
            # 命令第一节为file
            if self.com[0] == "file":

                if self.com[1] == "cat":
                    file_cat(self.com[2])
                elif self.com[1] == "rm":
                    file_rm(self.com[2])
                elif self.com[1] == "new":
                    file_new(self.com[2])
                elif self.com[1] == "append":
                    file_append(self.com[2])
                else:
                    print("命令未找到")
            elif self.com[0] == "lf":
                if self.com[1] == "-p":
                    try:
                        print(os.listdir(self.com[2]))
                    except FileNotFoundError:
                        print("请输入正确的路径")

            else:
                print("命令未找到")
        elif self.com_len == 4:
            if self.com[0] == "lf":
                if self.com[1] == "-m":
                    if self.com[2] == "-p":
                        all_file = os.listdir(self.com[3])
                        j = []
                        for each_file in all_file:
                            if os.path.isdir(each_file):
                                j.append(each_file)
                        print(j)
                    else:
                        print("命令未找到")

                elif self.com[1] == "-f":
                    if self.com[2] == "-p":
                        all_file = os.listdir(self.com[3])
                        j = []
                        for each_file in all_file:
                            if os.path.isfile(each_file):
                                j.append(each_file)
                        print(j)
                else:
                    print("命令未找到")
            else:
                print("命令未找到")
        else:
            print("命令未找到")


def file_cat(file_name):
    try:
        f = open(file_name, "r", encoding="utf_8")
        print(f.read())
        f.close()
    except BaseException:
        print("打开文件出错")


def file_rm(file_name):
    import os
    os.remove(file_name)

def file_new(file_name):
    try:
        f = open(file_name, "r")  #以只读模式打开，判断文件是否存在
    except FileNotFoundError:
        f1 = open(file_name, "a+")
        f1.close()
    else:
        f.close()
        print("文件已存在")

def file_append(file_name):
    f = open(file_name, "a")
    f.write(input("请输入追加文本>>>"))
    f.close()



if __name__ == "__main__":
    while True:
        show_command = Show_Command()
        show_command.command()
