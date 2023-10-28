import os
from flask import Flask, render_template, request, redirect, url_for
from pdfminer.high_level import extract_text
import openai

api_key = "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"
openai.api_key = api_key

prompt = """너는 지금부터 면접관이고, 사용자를 면접보는 역할이야
면접자에게 질문을 해야해
첫 질문은 사용자의 이력서를 보고 질문할 내용을 선택한다
다음에 질문할 내용을 선택하고 사용자에게 딱 한가지 질문하세요
안녕하세요로 시작
"""

app = Flask(__name__)

# 파일 업로드를 위한 디렉토리 설정
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 업로드 디렉토리가 없다면 생성
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return '파일이 없습니다.'
    
    file = request.files['file']
    
    if file.filename == '':
        return '파일을 선택하세요.'
    
    # 파일을 업로드 디렉토리에 저장
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], "test.pdf")) #file.filename))
    
    return redirect(url_for('gpt'))

@app.route('/gpt', methods=['get'])
def gpt():
    text = extract_text("uploads/test.pdf")
    
    messages = []
    messages.append({"role": "user", "content": text})
    # GPT 모델에 프롬프트를 전달하여 질문 생성
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            # {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=300  # 생성된 응답의 최대 길이를 조절할 수 있습니다.
    )
    
    user_question = response.choices[0].message["content"].strip()
    text = user_question.split("?")[0]
    
        

    print("GPT가 생성한 질문:", text)
    text.replace('\n', '')
    return render_template('gpt.html', user_question=text)

if __name__ == '__main__':
    app.run(debug=True)