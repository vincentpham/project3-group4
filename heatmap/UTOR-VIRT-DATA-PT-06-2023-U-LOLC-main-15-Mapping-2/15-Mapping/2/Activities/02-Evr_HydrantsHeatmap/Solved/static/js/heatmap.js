let myMap = L.map("map", {
  center: [40.7127837, -74.0059413],
  zoom: 7
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

let url = "http://127.0.0.1:5000/uslocation";

d3.json(url).then(function(response) {

  let heatArray=[];
  for(let i=0;i<response.length;i++){
    heatArray.push([response[i].latitude,response[i].longitude,response[i].change])
  }
  let heat = L.heatLayer(heatArray, {
    radius: 20,
    minOpacity:0.4,
    gradient:{0.4: 'blue', 0.65: 'lime', 1: 'red'}
  }).addTo(myMap);



  

  
  





});
