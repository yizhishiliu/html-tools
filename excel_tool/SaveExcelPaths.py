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

# 保存文件路径到历史记录
def save_history(history):
    with open(history_file, 'wb') as f:
        pickle.dump(history, f)

# 获取用户打开的Excel文件路径
def get_open_excel_files():
    excel = win32com.client.Dispatch("Excel.Application")
    open_workbooks = excel.Workbooks
    file_paths = [wb.FullName for wb in open_workbooks]
    return file_paths

# 记录用户打开的Excel文件路径
def record_open_excel_files():
    open_files = get_open_excel_files()
    if open_files:
        print("正在记录以下文件：")
        for file in open_files:
            print(file)
        history = load_history()
        history.extend(open_files)
        history = list(set(history))  # 去重
        save_history(history)
    else:
        print("没有打开的Excel文件。")

if __name__ == "__main__":
    record_open_excel_files()  # 记录文件
