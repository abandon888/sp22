import os
from typing import List

def insert_text_in_files(directory: str, text: str, file_extensions: List[str] = None) -> None:
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        # 获取文件的完整路径
        filepath = os.path.join(directory, filename)
        
        # 检查是否是文件，以及是否匹配给定的扩展名（如果提供了扩展名过滤）
        if os.path.isfile(filepath) and (file_extensions is None or any(filename.endswith(ext) for ext in file_extensions)):
            with open(filepath, 'r+', encoding='utf-8') as f:
                # 读取文件的内容
                content = f.read()
                # 将指定的文本插入文件的首行，并写回文件
                f.seek(0)
                f.write(text + '\n' + content)

    print(f"Inserted text into all files in the directory: {directory}")

insert_text_in_files('./tests', 'OK_FORMAT = True')