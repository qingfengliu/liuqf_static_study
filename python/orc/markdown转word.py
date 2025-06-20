#使用pandoc将markdown转换为word
#pandoc路径为D:\program\pandoc-3.6.4\pandoc.exe
import subprocess

# Markdown文件的路径
md_file_path = [r'D:\工作\ocr\TextIn\md\电网公平开放监管办法.md'
    ,r'D:\工作\ocr\TextIn\md\林业草原保护发展规划纲要.md'
    ,r'D:\工作\ocr\TextIn\md\石油天然气开采行业绿色工厂评价要求.md'
    ,r'D:\工作\ocr\TextIn\md\无损检测员国家职业技能标准.md'
]
# 输出Word文件的路径
docx_file_path = [r'D:\工作\ocr\TextIn\md\电网公平开放监管办法.docx'
                  ,r'D:\工作\ocr\TextIn\md\林业草原保护发展规划纲要.docx'
    ,r'D:\工作\ocr\TextIn\md\石油天然气开采行业绿色工厂评价要求.docx'
    ,r'D:\工作\ocr\TextIn\md\无损检测员国家职业技能标准.docx']

# 使用pandoc命令行工具进行转换
# 遍历每个文件进行转换
for i in range(len(md_file_path)):
    try:

        # 使用subprocess.run()执行命令
        subprocess.run([r'D:\program\pandoc-3.6.4\pandoc.exe', md_file_path[i], '-o', docx_file_path[i]], check=True)
        print(f"转换成功：{md_file_path[i]} -> {docx_file_path[i]}")
    except subprocess.CalledProcessError as e:
        print(f"转换失败：{md_file_path[i]} -> {docx_file_path[i]}")
        print(f"错误信息：{e}")