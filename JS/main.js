// openAI API
let url = `https://estsoft-openai-api.jejucodingcamp.workers.dev/`;

let $form = document.querySelector('.chat-form');


// 사용자의 질문
let question;

// 사용자의 질문을 객체를 만들어서 push
const makePrompt = function () {
    // 출발지 값 읽어오기
    let startInput = document.getElementById("start-point");
    let start = startInput.options[startInput.selectedIndex].value;
  
    // 여행지 값 읽어오기
    let destinationInput = document.getElementById("destination");
    let destination = destinationInput.options[destinationInput.selectedIndex].value;
  
    // 출발일 값 읽어오기
    let departInput = document.getElementById("depart-schedule");
    let depart = departInput.value;

    // 도착일 값 읽어오기
    let arriveInput = document.getElementById("arrive-schedule");
    let arrive = arriveInput.value;

    // 선호하는 여행테마 값 읽어오기
    let favoriteInputs = document.getElementsByName('tema');
    let favorite;
    for (let i =0; i < favoriteInputs.length; i++){
        if (favoriteInputs[i].checked) {
            favorite = favoriteInputs[i].value;
            break;
        }
    }

    // 차량 렌트 값 읽어오기
    let carRentInputs = document.getElementsByName("car-rent");
    let carRent;
    for (let i = 0; i < carRentInputs.length; i++) {
      if (carRentInputs[i].checked) {
        carRent = carRentInputs[i].value;
        break;
      }
    }
    
    // 메세지 전달 형식 : From user to API
    data.push({
      role: "user",
      content: `여행계획을 만들어줘. 출발일:${depart}, 도착일:${arrive}, 출발지:${start}, 여행지:${destination}, 선호하는여행테마:${favorite},자동차유무:${carRent} \n 이 내용을 기반으로 여행계획을 만들어줘`,
    });
    console.log(data);
}


// api 요청보내는 함수
const apiPost = async () => {
    const result = await 
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
      redirect: "follow",
    })
      .then((res) => res.json())
      .then((res) => {
        printAnswer(res.choices[0].message.content);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  
  // submit
  $form.addEventListener("submit", (e) => {
    e.preventDefault();
    makePrompt();
    apiPost();
  });

  
  // 화면에 답변 그려주는 함수
  const printAnswer = (answer) => {
    let chat_content = document.getElementById("chat-content");
    // 로딩을 시작하는 함수
    btnshow();
    chat_content.value = answer;
    // 로딩을 종료해주는 함수
    btnhide();
  };