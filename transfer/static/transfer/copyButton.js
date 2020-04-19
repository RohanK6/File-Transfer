const btnCopy = document.getElementById('copy-btn');
const txt = btnCopy.innerHTML;

btnCopy.addEventListener('click', function() {
    sendToClipboard(txt);
});

function sendToClipboard(message) {
    var temporaryInput = document.createElement('input');
    temporaryInput.value = message;
    document.body.appendChild(temporaryInput);
    temporaryInput.select();
    document.execCommand('copy');
    document.body.removeChild(temporaryInput);
}