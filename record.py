import pyaudio
import wave

# 오디오 설정
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