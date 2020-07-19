import os  
import shutil
# 获取指定文件夹下的所有文件的文件名（绝对路径）
def listdir(path):
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path)
        else:
            list_name.append(file_path)
    return list_name

# 将列表中的文件存储到指定位置
def mv_files(path_dst,list_files):
    for file_name in list_files:
        shutil.move(file_name,path_dst)
        print(file_name)

# 按一定间隔取出列表中的元素
def get_list_mv_file(list_name,interv):
    list_mv_file = []
    for i in range(0,len(list_name),interv):
        list_mv_file.append(list_name[i])
    return list_mv_file


if __name__ == "__main__":
    path_file_dir = "/home/hanchen/data/pics_10s/"
    interval = 5
    path_dst_dir = "/home/hanchen/data/pics_10s_labled"
    #os.makedirs(path_dst_dir)
    # 获取所有文件名
    list_file_name = listdir(path_file_dir)
    print("list_file_name len:",len(list_file_name))
    # 按间隔取出文件名
    list_mv_file = get_list_mv_file(list_file_name,interval)
    print("list_file_name len:",len(list_mv_file))
    # 将取出的文件另存为到指定文件夹
    mv_files(path_dst_dir,list_mv_file)
    print("Files has been saved in "+path_dst_dir)
	
	
	

	
