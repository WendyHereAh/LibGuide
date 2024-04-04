// Make a GET request
const apiUrl = "https://b115bwp7pf.execute-api.ap-southeast-1.amazonaws.com/LibCal_Data";

fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        // Process the data here
        const events = document.getElementById('events');

        // Display the data on webpage (ui design, ongoing....)
        for (let i = 0; i < data.length; i++) {
            const event = data[i];
            const eventDiv = document.createElement('div');
            eventDiv.innerHTML = `
                <h3>${event.title}</h3>
                <p>${event.id}</p>
                <p>${event.date}</p>
                <p>${event.startTime}</p>
                <p>${event.endTime}</p>
                <p>${event.url}</p>
            `;
                
            events.appendChild(eventDiv);
            }
    })
    .catch(error => console.log("error"));