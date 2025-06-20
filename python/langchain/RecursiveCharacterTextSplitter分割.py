# #先将md文档整体读出来
# loader = UnstructuredMarkdownLoader("D:\\工作\\ocr\\TextIn\\md2\\加快建设农业强国规划（2024-2035）.md"
#                                     , mode="single")
# docs = loader.load()

#保留markdown语法
from langchain_community.document_loaders import TextLoader
loader = TextLoader("D:\\工作\\ocr\\TextIn\\md2\\加快建设农业强国规划（2024-2035）.md",encoding="utf-8")
docs = loader.load()

#用RecursiveCharacterTextSplitter分割成多个块。最大块包含6000*0.9个中文字符
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=6000*1.5*0.9/3,
    chunk_overlap=100,
    length_function=len,
    # separators=["第*章","\n\n","\n"],  #不带markdown语法的分割符
    separators=["第*章", "#","##","\\*\\*","\n\n"],  # 带markdown语法的分割符
    is_separator_regex=True
)

#分割成多个块
splits = text_splitter.split_documents(docs)
#打印分割后的块
for i, doc in enumerate(splits):
    print(i, "分段:\n", doc.page_content)
    #打印分段的长度
    print("分段长度:", len(doc.page_content))