// A function to determine the marker size based on the population


function markerSize(population) {
  return Math.sqrt(population) * 50;
}
url="http://127.0.0.1:5000/uscities";
d3.json(url).then((response)=>{
  let stateMarkers = [];
  for (let i = 0; i < response.length; i++) {
    let lat=response[i].latitude;
    let long=response[i].longitude;
  
    stateMarkers.push(
      L.circle([lat,long], {
      stroke: false,
      fillOpacity: 0.75,
      color: "white",
      fillColor: "purple",
      radius: markerSize(response[i].population)
    })
  )
  }
  
  




  


  let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
	  attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  let states = L.layerGroup(stateMarkers);
  let cities = L.layerGroup(stateMarkers);


  let baseMaps = {
  "Street Map": street,
  "Topographic Map": topo
  };


  let overlayMaps = {
    "State Population": states,
    "City Population": cities
  };


  let myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5,
    layers: [street, states, cities]
  });


  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);

})

  

  







  