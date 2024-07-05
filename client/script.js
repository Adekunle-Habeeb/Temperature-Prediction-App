// function onClickedEstimatePrice() {
//     console.log("Estimate price button clicked");
//     var citySelect = document.getElementById("city");
//     var selectedCity = citySelect.options[citySelect.selectedIndex].text;
//     var year = document.getElementById("year");
//     var month = document.getElementById("month");
//     var tolerance = document.getElementById("tolerance");
//     var predictionSentence = document.getElementById("uiPredictionSentence");

//     // var url = "/predict_temperature_range";
//     // var url = "http://127.0.0.1:8000/predict_temperature_range"
//     var url = 'https://temperature-prediction-app-23pw.onrender.com/get_city_names'
//     // var url = "/api/predict_temperature_range";


//     $.post(url, {
//         city: citySelect.value,
//         year: year.value,
//         month: month.value,
//         tolerance: tolerance.value
//     }, function (data, status) {
//         console.log(data);
        
//         var monthNames = ["January", "February", "March", "April", "May", "June",
//                           "July", "August", "September", "October", "November", "December"];
        
//         var monthName = monthNames[parseInt(month.value) - 1];
        
//         var currentYear = new Date().getFullYear();
        
//         if (parseInt(year.value) < currentYear) {
//             var predictionSentence = "The temperature for " + selectedCity + " in " + monthName + " " + year.value + " was " + data.lower_bound.toFixed(1) + "°C.";
//         } else {
//             var predictionSentence = "The temperature predicted for " + selectedCity + " in " + monthName + " " + year.value + " is " + data.lower_bound.toFixed(1) + "°C - " + data.upper_bound.toFixed(1) + "°C.";
//         }
        
//         document.getElementById("uiPredictionSentence").innerHTML = predictionSentence;
//         console.log(status);
//     });
// }

// function onPageLoad() {
//     console.log("Document loaded");
//     // var url = "/api/get_city_names";
//     // var url = "http://127.0.0.1:8000/get_city_names"
//     var url = 'https://temperature-prediction-app-23pw.onrender.com/get_city_names'
//     // s

//     $.get(url, function (data, status) {
//         console.log("Received response for get_location_names request");
//         if (data && data.cities) {
//             var cities = data.cities;
//             var uiCities = document.getElementById("city");
//             cities.forEach(function (city) {
//                 var opt = new Option(city, city);
//                 uiCities.add(opt);
//             });
//         } else {
//             console.error("Error fetching city names:", status);
//         }
//     });
// }

// window.onload = onPageLoad;




function getBaseUrl() {
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        return 'http://127.0.0.1:8001'; // Local backend URL
    } else {
        // return 'https://habeeb-temp-app.el.r.appspot.com'; // Production URL
        // return 'https://temperature-prediction-app-23pw.onrender.com'
    }
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var citySelect = document.getElementById("city");
    var selectedCity = citySelect.options[citySelect.selectedIndex].text;
    var year = document.getElementById("year");
    var month = document.getElementById("month");
    var tolerance = document.getElementById("tolerance");

    var baseUrl = getBaseUrl();
    var url = `${baseUrl}/predict_temperature_range`;

    $.post(url, {
        city: citySelect.value,
        year: year.value,
        month: month.value,
        tolerance: tolerance.value
    }, function (data, status) {
        console.log(data);

        var monthNames = ["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"];

        var monthName = monthNames[parseInt(month.value) - 1];
        var currentYear = new Date().getFullYear();

        var predictionSentence;
        if (parseInt(year.value) < currentYear) {
            predictionSentence = `The temperature for ${selectedCity} in ${monthName} ${year.value} was ${data.lower_bound.toFixed(1)}°C.`;
        } else {
            predictionSentence = `The temperature predicted for ${selectedCity} in ${monthName} ${year.value} is ${data.lower_bound.toFixed(1)}°C - ${data.upper_bound.toFixed(1)}°C.`;
        }

        document.getElementById("uiPredictionSentence").innerHTML = predictionSentence;
        console.log(status);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.error("Request failed:", textStatus, errorThrown);
    });
}

function onPageLoad() {
    console.log("Document loaded");

    var baseUrl = getBaseUrl();
    var url = `${baseUrl}/get_city_names`;

    $.get(url, function (data, status) {
        console.log("Received response for get_city_names request", data, status);
        if (status === 'success' && data && data.cities) {
            var cities = data.cities;
            var uiCities = document.getElementById("city");
            cities.forEach(function (city) {
                var opt = new Option(city, city);
                uiCities.add(opt);
            });
        } else {
            console.error("Error fetching city names:", status, data);
        }
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.error("Request failed:", textStatus, errorThrown);
    });
}

window.onload = onPageLoad;
