// Creating the map object
let myMap = L.map("map", {
  center: [40.7, -73.95],
  zoom: 11
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

function markerSize(population) {
  return Math.sqrt(population) * 50;
}

function markeradius(size){
  return Math.sqrt(size) * 50;

}


function color(price){
  let color_1="";
  
  if ( price > 100000.000) {
    color_1 = "yellow";
  }
  else if (price > 300000.00) {
    color_1 = "blue";
  }
  else if (price > 500000.00) {
    color_1 = "green";
  }
  else if (price > 750000.00){
    color_1="red";
  }
  else {
    color_1 = "purple";
  }
  return color_1;

}



// Assemble the API query URL.
let url = "http://127.0.0.1:5000/uscities"

// Get the data with d3.
d3.json(url).then(function(data){

  d3.select("#selDataset").on("change", function optionChanged(){
    let dropdownMenu=d3.select("#selDataset");
    var dataset=dropdownMenu.property("value");

    
    for (let i=0;i<data.length;i++){
      let year=data[i][`${dataset}`];
      let x= Math.round(year);
      console.log(x);

      

      let color_depth="";

      if(x<500000){

        color_depth='#A1E8A1';
           

      }
      
      else {
        color_depth='#175E17';

            
      }
 
      console.log(x)
      console.log(color_depth)
      L.circle([data[i].latitude,data[i].longitude], {
        fillOpacity: 0.75,
        color: color_depth ,
        fillColor: "white",
        // Setting our circle's radius to equal the output of our markerSize() function:
        // This will make our marker's size proportionate to its population.
        radius: Math.sqrt(year)*100
      }).bindPopup(`<h1>${data[i].city}</h1> <hr> <h3>average_price: ${year.toLocaleString()}</h3>`).addTo(myMap)

  
      }
    })

  
});




var select = document.getElementById("selDataset"); 
var options = ["Ave_Price_2000",
"Ave_Price_2001",
"Ave_Price_2002",
"Ave_Price_2003",
"Ave_Price_2004",
"Ave_Price_2005",
"Ave_Price_2006",
"Ave_Price_2007",
"Ave_Price_2008",
"Ave_Price_2009",
"Ave_Price_2010",
"Ave_Price_2011",
"Ave_Price_2012",
"Ave_Price_2013",
"Ave_Price_2014",
"Ave_Price_2015",
"Ave_Price_2016",
"Ave_Price_2017",
"Ave_Price_2018",
"Ave_Price_2019",
"Ave_Price_2020",
"Ave_Price_2021",
"Ave_Price_2022",
"Ave_Price_2023"] 


select.innerHTML = "";

for(var i = 0; i < options.length; i++) {
    var opt = options[i];
    select.innerHTML += "<option value=\"" + opt + "\">" + opt + "</option>";
};
 