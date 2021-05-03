class Show_Command:

    def __init__(self):
        import os
        print(os.getcwd(), ">>", end="")
        self.cmd = input()
        self.com = self.cmd.split()
        self.com_len = len(self.com)
        self.com_len = len(self.com)



    def command(self):
        import os,run
        # 判断命令长度
        if self.com_len == 0:
            print("Command is not find")
        # 命令长度为1
        elif self.com_len == 1:
            # 命令为file
            if self.com[0] == "file":
                run.file_help()

            elif self.com[0] == "exit" or self.com[0] == "quit" or self.com[0] == "bye":
                print("bye")
                exit()
            elif self.com[0] == "cd":
                print("cd [PATH]:Change working directory")

            elif self.com[0] == "lf":
                print(os.listdir())

            elif self.com[0] == "img":
                run.img_help()

            else:
               print(run.url(text=self.com[0]))
        # 命令长度为2
        elif self.com_len == 2:
            # 命令第一节为file
            if self.com[0] == "file":
                # 命令第2节为?
                if self.com[1] == "?":
                    run.file_help()

                else:
                    print("Command is not find")
            elif self.com[0] == "cd":
                if self.com[1] == "?":
                    print("cd [PATH]:Change working directory")
                else:
                    try:
                        os.chdir(self.com[1])
                    except FileNotFoundError:
                        print("Please enter true path")
            elif self.com[0] == "lf":
                if self.com[1] == "?":
                    run.lf_help()

                elif self.com[1] == "-m":
                    run.lf_m()

                elif self.com[1] == "-f":
                    run.lf_f()

                else:
                    print("Command is not find")
            elif self.com[0] == "img":
                if self.com[1] == "-help":
                    run.file_help()
                else:
                    print("Command is not find")
            else:
                print("Command is not find")
        # 命令长度为3
        elif self.com_len == 3:
            # 命令第一节为file
            if self.com[0] == "file":

                if self.com[1] == "cat":
                    run.file_cat(self.com[2])
                elif self.com[1] == "rm":
                    run.file_rm(self.com[2])
                elif self.com[1] == "new":
                    run.file_new(self.com[2])
                elif self.com[1] == "append":
                    run.file_append(self.com[2])
                else:
                    print("Command is not find")
            elif self.com[0] == "lf":
                if self.com[1] == "-p":
                    try:
                        print(os.listdir(self.com[2]))
                    except FileNotFoundError:
                        print("Please enter true path")
            elif self.com[0] == "img":
                if self.com[1] == "-o":
                    run.img_open(name=self.com[2])
                elif self.com[1] == "-g":
                    run.img_gray(name=self.com[2])
                elif self.com[1] == "-l":
                    run.img_line(name=self.com[2])
            elif self.com[0] == "ch":
                run.chage_hosts(com=self.com[1],ip=self.com[2])
            elif self.com[0] == "web":
                if self.com[1] == "-u":
                    response = run.url(text=self.com[2])
                    if response == "Command is not find":
                        print("url is wrong")
            else:
                print("Command is not find")
        elif self.com_len == 4:
            if self.com[0] == "lf":
                if self.com[1] == "-m":
                    if self.com[2] == "-p":
                        run.lf_mp(path=self.com[3])
                    else:
                        print("Command is not find")

                elif self.com[1] == "-f":
                    if self.com[2] == "-p":
                        run.lf_fp(path=self.com[3])
                else:
                    print("Command is not find")
            else:
                print("Command is not find")
        elif self.com_len == 5:
            if self.com[0] == "web":
                if self.com[1] == "-u":
                    if self.com[3] == "-b":
                        run.url_in_browser(browser=self.com[4],url=self.com[2])
                    else:
                        print("Command is not find")
                else:
                    print("Command is not find")
            else:
                print("Command is not find")
        else:
            print("Command is not find")






if __name__ == "__main__":
    while True:
        try:
            while True:
                show_command = Show_Command()
                show_command.command()
        except Exception as e:
            print("\n"+e)