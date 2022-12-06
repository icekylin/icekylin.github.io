import os

def alter(file,old_str,new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                print(f'{file} 文件修改成功')
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

def dir(path):
    files = os.listdir(path)
    return files


if __name__ == '__main__':
    old_str = "../../../../000%20-%20Inbox/010%20-%20Assets/images/"
    new_str = "../assets/img/"
    files = dir("/Users/kylin/Mind/Blog/source/_posts/")

    for f in files:
        alter(f"../_posts/{f}", old_str, new_str)