import os
from flask import Flask, render_template, request, redirect, url_for
from pdfminer.high_level import extract_text
import openai
import pyaudio
import wave

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
    
        
    text = text.replace('\n', '')
    print("GPT가 생성한 질문:", text)
    
    return render_template('gpt.html', user_question=text)

@app.route('/record', methods=['post'])
def record():
    print("녹음")
    FORMAT = pyaudio.paInt16  # 오디오 포맷 (16-bit int)
    CHANNELS = 1  # 모노 오디오
    RATE = 44100  # 샘플링 속도 (Hz)
    RECORD_SECONDS = 5  # 녹음 시간 (초)
    OUTPUT_FILENAME = "recorded_audio.wav"  # 녹음된 오디오 파일 이름

    # PyAudio 오브젝트 생성
    audio = pyaudio.PyAudio()

    # 녹음 스트림 열기
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=1024)

    print("녹음 시작...")

    frames = []

    # 오디오 녹음
    for i in range(0, int(RATE / 1024 * RECORD_SECONDS)):
        data = stream.read(1024)
        frames.append(data)

    print("녹음 종료.")

    # 스트림 정리
    stream.stop_stream()
    stream.close()

    # PyAudio 오브젝트 종료
    audio.terminate()

    # 녹음된 오디오를 WAV 파일로 저장
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"녹음된 오디오는 '{OUTPUT_FILENAME}'에 저장되었습니다.")
    return "HI"

if __name__ == '__main__':
    app.run(debug=True)