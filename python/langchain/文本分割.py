from langchain_core.embeddings import Embeddings
from sentence_transformers import SentenceTransformer
import re

class ACGEEmbeddings(Embeddings):
    def __init__(self, model_name="aspire/acge_text_embedding"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(texts).tolist()

    def embed_query(self, text: str) -> list[float]:
        return self.model.encode(text).tolist()

from langchain_experimental.text_splitter import SemanticChunker

# 初始化模型
embeddings = ACGEEmbeddings()

# 创建分块器 (默认使用 cosine 相似度)
#C:\Users\Admin\.cache\huggingface\hub\models--aspire--acge_text_embedding
text_splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="percentile",  # 阈值类型
    breakpoint_threshold_amount=95,         # 阈值数值
    add_start_index=True,                     # 保留原始位置信息
    buffer_size=5,  # 调整窗口大小
    sentence_split_regex = r'[。！？\n]+'
)


with open("D:\\工作\\ocr\\TextIn\\md2\\加快建设农业强国规划（2024-2035）.md", "r", encoding="utf-8") as f:
    text = f.read()


# sentences = re.split(r'[。！？\n]+', text)
# print(sentences)
# embeddings = embeddings.embed_documents(sentences)
# print(embeddings)
# 执行分块
chunks = text_splitter.create_documents([text])

# 查看结果
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk.page_content)
    print("-" * 50)