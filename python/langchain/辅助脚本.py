import nltk
import shutil

# 清除 NLTK 缓存目录
nltk_cache_dir = nltk.data.path[0]
shutil.rmtree(nltk_cache_dir, ignore_errors=True)
print(f"已清理缓存目录: {nltk_cache_dir}")