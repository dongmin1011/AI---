const recordButton = document.getElementById('recordButton');
const audioElement = document.getElementById('audioElement');
let recorder;

recordButton.addEventListener('click', () => {
    if (recordButton.textContent === '녹음 시작') {
        startRecording();
    } else {
        stopRecording();
    }
});

async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(stream);
    const chunks = [];

    recorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
            chunks.push(event.data);
        }
    };

    recorder.onstop = () => {
        const blob = new Blob(chunks, { 'type': 'audio/wav' });
        audioElement.src = URL.createObjectURL(blob);
    };

    recorder.start();
    recordButton.textContent = '녹음 중지';
}

function stopRecording() {
    if (recorder && recorder.state === 'recording') {
        recorder.stop();
        recordButton.textContent = '녹음 시작';
    }
}
