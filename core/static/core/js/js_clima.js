const apiKey = '64b350eb51f633527ce356a277a2329a';

const locations = [
  { name: 'Buenos Aires', lat: -34.581337, lon: -58.426246 },
];

function mostrarInformacionClima(locationName, weatherData) {
    const weatherDataElement = document.getElementById('weather-data');
    const temperature = (weatherData.main.temp - 273.15).toFixed(2);
  
    const weatherInfoElement = document.createElement('div');
    weatherInfoElement.innerHTML = `<p><b>${locationName}</b></p>
      <p><b>Temperatura: ${temperature}°C</b></p>
      <p><b>Descripción: ${weatherData.weather[0].description}</b></p>`;
  
    weatherDataElement.appendChild(weatherInfoElement);
}

function obtenerClima(location) {
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${location.lat}&lon=${location.lon}&appid=${apiKey}&lang=es`;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      mostrarInformacionClima(location.name, data);
    })
    .catch(error => {
      console.error(`Error al obtener datos del clima para ${location.name}:`, error);
    });
}

locations.forEach(location => {
  obtenerClima(location);
});