import os
from magic_pdf.data.data_reader_writer import FileBasedDataWriter, FileBasedDataReader
from magic_pdf.data.dataset import PymuDocDataset
from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze
from magic_pdf.config.enums import SupportedPdfParseMethod

#minerU 的orc模型貌似只支持PaddleOCR和

# PDF 文件路径
pdf_file_path = r"D:\工作\电网公平开放监管办法.pdf"
pdf_file_path_without_suff = pdf_file_path.split(".")[0]
pdf_file_path_parent_dir = os.path.dirname(pdf_file_path)
image_dir = os.path.join(pdf_file_path_parent_dir, "images")

# 创建 Markdown 写入实例
writer_markdown = FileBasedDataWriter()
writer_image = FileBasedDataWriter(image_dir)

# 读取 PDF 文件
reader_pdf = FileBasedDataReader("")
bytes_pdf = reader_pdf.read(pdf_file_path)

# 处理 PDF 数据
dataset_pdf = PymuDocDataset(bytes_pdf)

# 判断是否支持 OCR
if dataset_pdf.classify() == SupportedPdfParseMethod.OCR:
    infer_result = dataset_pdf.apply(doc_analyze, ocr=True)
    pipe_result = infer_result.pipe_ocr_mode(writer_image)
else:
    infer_result = dataset_pdf.apply(doc_analyze, ocr=False)
    pipe_result = infer_result.pipe_txt_mode(writer_image)

# 绘制布局和文本行
# pipe_result.draw_layout(f"{pdf_file_path_without_suff}_layout.pdf")
# pipe_result.draw_span(f"{pdf_file_path_without_suff}_spans.pdf")

# 获取 Markdown 内容并保存
markdown_content = pipe_result.get_markdown(image_dir)
pipe_result.dump_md(writer_markdown, f"{pdf_file_path_without_suff}.md", image_dir)

# 获取 JSON 格式的内容并保存
# content_list_content = pipe_result.get_content_list(image_dir)
# pipe_result.dump_content_list(writer_markdown, f"{pdf_file_path_without_suff}_content_list.json", image_dir)