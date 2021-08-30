import datetime
import pickle
import os

first_time = True
# 检查 pickle 文件是否存在
if os.path.isfile("last_run.pkl"):
    # 如果存在。就打开该文件进行读取
    pickle_file = open("last_run.pkl", 'rb')
    # 还原 datetime 对象
    last_time = pickle.load(pickle_file)
    pickle_file.close()
    print(f"The last time this program was run was {last_time}")
    first_time = False

# 打开（或创建）picke 文件来写入信息
pickle_file = open("last_run.pkl", 'wb')
pickle.dump(datetime.datetime.now(), pickle_file)
pickle_file.close()
if first_time:
    print("Created new pickle file.")
