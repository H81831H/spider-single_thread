import os

class Filework:
    filepath = ""
    content = ""
#初始化
    def __init__(self,filename=None,content=None):
        self.filename = filename
        self.content = content

#1输出当前工作目录
    def print_current_directory(self):
        current_directory = os.getcwd()
        print("当前工作目录:", current_directory)

#2输出目录内容
    def print_file_list(self):
        files_and_dirs = os.listdir(self.filename)
        print("目录内容:", files_and_dirs)

#3创建新目录及文件
    def create_write_file(self):
        i = 0
        try:
            os.mkdir(f"{self.filename}")
            print("目录与文件创建成功")
        except FileExistsError:
            print("目录已经存在")

#4读取文件
    def read_file(self):
        with open(f"{self.filename}", "r") as f:
            txt = f.read()
            print(f"文件内容:{txt}")

#5删除空目录
    def delete_file(self):
        try:
            os.rmdir(self.filename)
        except OSError:
            print("目录不为空，无法删除")

#6写入已创建文件
    def write_old_file(self):
        try:
            with open(str(f"{self.filename}"), "w") as f:
                f.write(self.content)
                print("文件写入成功")
        except FileNotFoundError:
            print("文件不存在")

#打印操作目录
def lst_menu():
    lst = ["1.输出当前工作目录", "2.创建新目录及文件", "3.读取文件", "4.删除空目录", "5.写入已创建文件", "q.退出"]
    for i in lst:
        print(i)

def menu_choice():
    while True:
        choice = str(input("请输入选项:"))
        if choice == "q":
            print("感谢使用，再见！")
            break      
           
        try:
            match choice:
                case "1":
                    file_work = Filework()
                    file_work.print_current_directory()
                case "2":
                    path = input("请输入要创建的目录路径：")
                    content = input("请输入要写入的内容：")
                    file_work = Filework(path, content)
                    file_work.create_write_file()
                case "3":
                    path = input("请输入要读取的文件路径：")
                    file_work = Filework(path)
                    file_work.read_file()
                case "4":
                    path = input("请输入要删除的目录路径：")
                    file_work = Filework(path)
                    file_work.delete_file()
                case "5":
                    path = input("请输入文件路径：")
                    content = input("请输入要写入的内容：")
                    file_work = Filework(path, content)
                    file_work.write_old_file()
                case _:
                    print("无效的选项，请重新选择！")

            print("\n-------------------")
            lst_menu()
            print("-------------------")
            
        except Exception as e:
            print(f"操作出错：{str(e)}")
            print("\n-------------------")
            lst_menu()
            print("-------------------")

if __name__ == "__main__":
    print("欢迎使用文件操作系统")
    print("-------------------")
    lst_menu()
    print("-------------------")
    menu_choice()




























































































































