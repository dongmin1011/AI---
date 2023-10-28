from pdfminer.high_level import extract_text

# PDF 파일을 열어서 텍스트를 추출합니다
text = extract_text("uploads/test.pdf")


# 추출된 텍스트를 출력합니다
print(text)
