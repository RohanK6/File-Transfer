const realBtn = document.getElementById('real-btn');
const customBtn = document.getElementById('custom-btn');

customBtn.addEventListener("click", function() {
    realBtn.click();
});

realBtn.addEventListener("change", function() {
    if (realBtn.value) {
        customBtn.innerHTML = realBtn.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
        document.getElementById('custom-btn').id = 'custom-btn-uploaded';
    } 
    else {
        customBtn.innerHTML = "Select...";
    }
});