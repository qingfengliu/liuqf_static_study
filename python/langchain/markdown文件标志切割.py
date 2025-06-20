from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter
###方案1.markdown，通过标题分割。
###可用，不完美。将小块要合并一下。知识库文档不宜过小。

# 1. 定义标题提取规则
headers_to_split_on = [
    ("#", "Header 1"),
    # ("##", "Header 2"),
    # ("###", "Header 3"),
]

# 2. 创建 Markdown 专用分割器
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False,    # 保留标题文本
    return_each_line=False
)


# 打开文件D:\工作\ocr\TextIn\md\电网公平开放监管办法.md,并转换为字符串
with open(r"D:\工作\ocr\TextIn\md\电网公平开放监管办法.md", "r", encoding="utf-8") as f:
    text = f.read()


# 4. 执行结构化分割
splits = []
#markdown_splitter.split_text把markdown语法内容去掉
chunks = markdown_splitter.split_text(text)
splits.extend(chunks)


with open(r"D:\工作\ocr\TextIn\md\电网公平开放监管办法分割_分段.md", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(splits):
        f.write(chunk.page_content)
        f.write("\n分段分段分段分段分段分段分段分段分段分段分段分段分段分段分段分段分段分段分段分段\n")

loader = UnstructuredMarkdownLoader("D:\\工作\\ocr\\TextIn\\md\\电网公平开放监管办法分割_分段.md"
                                    , mode="single")
docs = loader.load()

###############################以下是用UnstructuredMarkdownLoader类，分割的更细，原理差不多实际#####################################################
# #去除markdown语法
# with open(r"D:\工作\ocr\TextIn\md\无损检测员国家职业技能标准分割.txt", "w", encoding="utf-8") as f:
#     f.write(docs[0].page_content)
#
# from langchain_community.document_loaders import UnstructuredMarkdownLoader
#
# #UnstructuredMarkdownLoader可以将markdown文件用markdown语法分割成多个块
# #分割后的文档非常散，还是需要进行合并。
# loader = UnstructuredMarkdownLoader("D:\\工作\\ocr\\TextIn\\md\\无损检测员国家职业技能标准.md"
#                                     , mode="elements")
# docs = loader.load()
#
# for i,doc in enumerate(docs):
#     print(i,"分段:\n",doc.page_content)