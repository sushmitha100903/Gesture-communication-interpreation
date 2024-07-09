document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('video');
    const startButton = document.getElementById('start-button');
    const resultDiv = document.getElementById('result');

    // Access the webcam
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => {
            console.error("Error accessing webcam: ", err);
        });

    // Placeholder function for sign language recognition
    function recognizeSignLanguage() {
        // Placeholder: In a real application, you would use a model to recognize gestures
        resultDiv.innerText = "Recognizing sign language...";
        setTimeout(() => {
            resultDiv.innerText = "Sign recognized: Hello";
        }, 2000);
    }

    // Start recognition on button click
    startButton.addEventListener('click', () => {
        recognizeSignLanguage();
    });
});
