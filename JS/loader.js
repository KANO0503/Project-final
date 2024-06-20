// submit 버튼, loading 이미지 선언
const submitBtn = document.getElementById('button');
const loadingGif = document.getElementById('loading-gif');

// 로딩이 보여지는 함수
function btnshow() {
    loadingGif.style.display = 'block';
}
// 로딩이 종료되는 함수
function btnhide() {
    loadingGif.style.display = 'none';
}