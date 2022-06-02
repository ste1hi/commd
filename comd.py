class Show_Command:

    def __init__(self):
        self.language = "en"



    def command(self):
        import os
        import run
        print(os.getcwd(), ">>", end="")
        self.cmd = input()
        self.com = self.cmd.split()
        self.com_len = len(self.com)
        # 判断命令长度

        rune = run.run_en()
        runc = run.run_cn()


        if self.com_len == 0:
            if self.language == "en":
                print("Command is not find")
            elif self.language == "cn":
                print("命令未找到")

        # 命令长度为1
        elif self.com_len == 1:
            # 命令为file
            if self.com[0] == "file":
                if self.language == "en":
                    rune.file_help()
                elif self.language == "cn":
                    runc.file_help()


            elif self.com[0] == "exit" or self.com[0] == "quit" or self.com[0] == "bye":
                if self.language == "en":
                    print("bye")
                elif self.language == "cn":
                    print("再见")
                exit()
            elif self.com[0] == "cd":
                if self.language == "en":
                    print("cd [PATH]:Change working directory")
                elif self.language == "cn":
                    print("cd [PATH]:改变工作路径")


            elif self.com[0] == "lf":
                print(os.listdir())

            elif self.com[0] == "img":
                if self.language == "en":
                    rune.img_help()
                elif self.language == "cn":
                    runc.img_help()

            else:
                if self.language == "en":
                    print(rune.url(text=self.com[0]))
                elif self.language == "cn":
                    print(runc.url(text=self.com[0]))

        # 命令长度为2
        elif self.com_len == 2:
            # 命令第一节为file
            if self.com[0] == "file":
                # 命令第2节为?
                if self.com[1] == "?":
                    if self.language == "en":
                        rune.file_help()
                    elif self.language == "cn":
                        runc.file_help()

                else:
                    if self.language == "en":
                        print("Command is not find")
                    elif self.language == "cn":
                        print("命令未找到")
            elif self.com[0] == "cd":
                if self.com[1] == "?":
                    if self.language == "en":
                        print("cd [PATH]:Change working directory")
                    elif self.language == "cn":
                        print("cd [PATH]:改变工作路径")
                else:
                    try:
                        os.chdir(self.com[1])
                    except FileNotFoundError:
                        if self.language == "en":
                            print("Please enter true path")
                        elif self.language == "cn":
                            print("请输入正确的路径")

            elif self.com[0] == "lf":
                if self.com[1] == "?":
                    if self.language == "en":
                        rune.lf_help()
                    elif self.language == "cn":
                        runc.lf_help()

                elif self.com[1] == "-m":
                    rune.lf_m()

                elif self.com[1] == "-f":
                    rune.lf_f()

                else:
                    print("Command is not find")
            elif self.com[0] == "img":
                if self.com[1] == "-help":
                    if self.language == "en":
                        rune.img_help()
                    elif self.language == "cn":
                        runc.img_help()
                else:
                    if self.language == "en":
                        print("Command is not find")
                    elif self.language == "cn":
                        print("命令未找到")
            elif self.com[0] == "set":
                if self.com[1] == "Chinese" or self.com[1] == "cn":
                    self.language = "cn"
                    print("中文设置成功")
                elif self.com[1] == "English" or self.com[1] == "en":
                    self.language = "en"
                    print("English setting successful")
            else:
                if self.language == "en":
                    print("Command is not find")
                elif self.language == "cn":
                    print("命令未找到")
        # 命令长度为3
        elif self.com_len == 3:
            # 命令第一节为file
            if self.com[0] == "file":

                if self.com[1] == "cat":

                    if self.language == "en":
                        rune.file_cat(self.com[2])
                    elif self.language == "cn":
                        runc.file_cat(self.com[2])
                elif self.com[1] == "rm":
                    if self.language == "en":
                        rune.file_rm(self.com[2])
                    elif self.language == "cn":
                        runc.file_rm(self.com[2])

                elif self.com[1] == "new":
                    if self.language == "en":
                        rune.file_new(self.com[2])
                    elif self.language == "cn":
                        runc.file_new(self.com[2])

                elif self.com[1] == "append":
                    if self.language == "en":
                        rune.file_append(self.com[2])
                    elif self.language == "cn":
                        runc.file_append(self.com[2])

                else:
                    if self.language == "en":
                        print("Command is not find")
                    elif self.language == "cn":
                        print("命令未找到")
            elif self.com[0] == "lf":
                if self.com[1] == "-p":
                    try:
                        print(os.listdir(self.com[2]))
                    except FileNotFoundError:
                        if self.language == "en":
                            print("Please enter true path")
                        elif self.language == "cn":
                            print("请输入正确的路径")

            elif self.com[0] == "img":
                if self.com[1] == "-o":

                    if self.language == "en":
                         rune.img_open(name=self.com[2])
                    elif self.language == "cn":
                        runc.img_open(name=self.com[2])

                elif self.com[1] == "-g":
                    if self.language == "en":
                        rune.img_gray(name=self.com[2])
                    elif self.language == "cn":
                        runc.img_gray(name=self.com[2])

                elif self.com[1] == "-l":
                    if self.language == "en":
                         rune.img_line(name=self.com[2])
                    elif self.language == "cn":
                        runc.img_line(name=self.com[2])

            elif self.com[0] == "host":

                if self.language == "en":
                    rune.chage_hosts(com=self.com[1],ip=self.com[2])
                elif self.language == "cn":
                    runc.chage_hosts(com=self.com[1],ip=self.com[2])
            elif self.com[0] == "web":
                if self.com[1] == "-u":
                    response = rune.url(text=self.com[2])
                    if response == "Command is not find":

                        if self.language == "en":
                            print("url is wrong")
                        elif self.language == "cn":
                            print("地址是错误的")
            else:
                if self.language == "en":
                    print("Command is not find")
                elif self.language == "cn":
                    print("命令未找到")
        elif self.com_len == 4:
            if self.com[0] == "lf":
                if self.com[1] == "-m":
                    if self.com[2] == "-p":
                        rune.lf_mp(path=self.com[3])
                    else:
                        if self.language == "en":
                            print("Command is not find")
                        elif self.language == "cn":
                            print("命令未找到")

                elif self.com[1] == "-f":
                    if self.com[2] == "-p":
                        rune.lf_fp(path=self.com[3])
                else:
                    if self.language == "en":
                        print("Command is not find")
                    elif self.language == "cn":
                        print("命令未找到")
            else:
                if self.language == "en":
                    print("Command is not find")
                elif self.language == "cn":
                    print("命令未找到")
        elif self.com_len == 5:
            if self.com[0] == "web":
                if self.com[1] == "-u":
                    if self.com[3] == "-b":

                        if self.language == "en":
                            rune.url_in_browser(browser=self.com[4], url=self.com[2])
                        elif self.language == "cn":
                            runc.url_in_browser(browser=self.com[4], url=self.com[2])
                    else:
                        if self.language == "en":
                            print("Command is not find")
                        elif self.language == "cn":
                            print("命令未找到")
                else:
                    if self.language == "en":
                        print("Command is not find")
                    elif self.language == "cn":
                        print("命令未找到")
            else:
                if self.language == "en":
                    print("Command is not find")
                elif self.language == "cn":
                    print("命令未找到")
        else:
            if self.language == "en":
                print("Command is not find")
            elif self.language == "cn":
                print("命令未找到")






if __name__ == "__main__":
    show_command = Show_Command()
    while True:
        try:
            while True:
                show_command.command()
        except Exception as e:
            print("\n"+str(e))