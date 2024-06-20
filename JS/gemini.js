// ./JS/gemini.js
async function createTravelPlan(event) {
    event.preventDefault(); // 폼 제출 기본 동작 막기

    const startPoint = document.getElementById('start-point').value;
    const destination = document.getElementById('destination').value;
    const departDate = document.getElementById('depart-schedule').value;
    const arriveDate = document.getElementById('arrive-schedule').value;
    const temas = Array.from(document.querySelectorAll('input[name="tema"]:checked')).map(tema => tema.value);
    const carRent = document.querySelector('input[name="car-rent"]:checked').value;

    const requestData = {
        startPoint,
        destination,
        departDate,
        arriveDate,
        temas,
        carRent
    };

    document.getElementById('loading-gif').style.display = 'block';

    try {
        const response = await fetch('https://api.gemini.com/travel_plan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer YOUR_API_KEY' // Replace with your actual API key
            },
            body: JSON.stringify(requestData)
        });

        const result = await response.json();
        document.getElementById('loading-gif').style.display = 'none';
        document.getElementById('chat-content').value = JSON.stringify(result, null, 2);
    } catch (error) {
        document.getElementById('loading-gif').style.display = 'none';
        document.getElementById('chat-content').value = `Error: ${error.message}`;
    }
}
