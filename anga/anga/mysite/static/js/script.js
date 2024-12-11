document.addEventListener("DOMContentLoaded", () => {
    const cityForm = document.getElementById("city-form");
    const geolocationBtn = document.getElementById("geolocation-btn");
    const weatherResults = document.getElementById("weather-results");
    const forecastContainer = document.getElementById("forecast-container");
    const favoriteCities = document.getElementById("favorite-cities");
    const loadingSpinner = document.getElementById("loading-spinner");

    const apiKey = "API_KEY"; 

    const showLoading = () => {
        loadingSpinner.classList.remove("hidden");
    };

    const hideLoading = () => {
        loadingSpinner.classList.add("hidden");
    };

    const fetchWeather = async (city) => {
        showLoading();
        try {
            const response = await fetch(
                `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`
            );
            const data = await response.json();
            if (response.ok) {
                displayWeather(data);
                fetchForecast(city);
            } else {
                alert(data.message);
            }
        } catch (error) {
            alert("Error fetching weather data.");
        } finally {
            hideLoading();
        }
    };

    const fetchForecast = async (city) => {
        try {
            const response = await fetch(
                `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}&units=metric`
            );
            const data = await response.json();
            if (response.ok) {
                displayForecast(data);
            }
        } catch (error) {
            console.error("Error fetching forecast:", error);
        }
    };

    const displayWeather = (data) => {
        document.getElementById("city-name").textContent = data.name;
        document.getElementById("weather-icon").src = 
            `https://openweathermap.org/img/wn/${data.weather[0].icon}.png`;
        document.getElementById("temperature").textContent = 
            `Temperature: ${data.main.temp} \u00b0C`;
        document.getElementById("description").textContent = data.weather[0].description;
        document.getElementById("details").textContent = 
            `Humidity: ${data.main.humidity}% | Wind Speed: ${data.wind.speed} m/s`;
        weatherResults.classList.remove("hidden");
    };

    const displayForecast = (data) => {
        forecastContainer.innerHTML = "";
        const forecasts = data.list.filter((_, index) => index % 8 === 0); // Every 8th entry is a daily forecast
        forecasts.forEach((forecast) => {
            const forecastCard = document.createElement("div");
            forecastCard.className = "card";
            forecastCard.innerHTML = `
                <p>${new Date(forecast.dt_txt).toDateString()}</p>
                <img src="https://openweathermap.org/img/wn/${forecast.weather[0].icon}.png" alt="Weather Icon">
                <p>${forecast.weather[0].description}</p>
                <p>Temp: ${forecast.main.temp} \u00b0C</p>
            `;
            forecastContainer.appendChild(forecastCard);
        });
        document.getElementById("forecast").classList.remove("hidden");
    };

    const saveToFavorites = (city) => {
        const listItem = document.createElement("li");
        listItem.textContent = city;
        favoriteCities.appendChild(listItem);
    };

    cityForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const city = document.getElementById("city-input").value;
        if (city) {
            fetchWeather(city);
            saveToFavorites(city);
        }
    });

    geolocationBtn.addEventListener("click", () => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(async (position) => {
                const { latitude, longitude } = position.coords;
                showLoading();
                try {
                    const response = await fetch(
                        `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${apiKey}&units=metric`
                    );
                    const data = await response.json();
                    if (response.ok) {
                        displayWeather(data);
                        fetchForecast(data.name);
                    }
                } catch (error) {
                    alert("Error fetching location-based weather.");
                } finally {
                    hideLoading();
                }
            });
        } else {
            alert("Geolocation is not supported by your browser.");
        }
    });
});
