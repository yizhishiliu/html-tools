import os
import pickle
import win32com.client

# 获取脚本所在的目录路径
current_directory = os.path.dirname(os.path.abspath(__file__))
history_file = os.path.join(current_directory, "excel_open_history.pkl")

# 读取已保存的历史路径
def load_history():
    if os.path.exists(history_file):
        with open(history_file, 'rb') as f:
            return pickle.load(f)
    return []

# 打开Excel文件
def open_excel_files(files):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True  # 启动Excel应用并让它可见
    for file in files:
        if os.path.exists(file):  # 确保文件路径存在
            excel.Workbooks.Open(file)
        else:
            print(f"文件不存在: {file}")

# 让用户直接打开已记录的文件
def open_saved_files():
    history = load_history()
    if history:
        print("正在打开历史记录中的文件：")
        open_excel_files(history)
    else:
        print("没有历史记录可供打开。")

if __name__ == "__main__":
    open_saved_files()  # 打开保存的文件
