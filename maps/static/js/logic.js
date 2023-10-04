//let url = "http://127.0.0.1:5000/usproperties";

let url = "http://127.0.0.1:5000/usproperties";

d3.json(url).then(function(data){
  
  fetch('http://127.0.0.1:5000/usproperties')
  .then(response => response.json())
    .then(data => {
      console.log("Properties data:", data);
    })
    .catch(error => {
        console.error('Error:', error);
    });

map(data);




  

});
 




function PriceColor(price) {
    if (price <=100000) return '#008000';
    else if (price > 100000 & price <= 250000) return '#A52A2A';
    else if (price > 250000 & price <= 500000) return '#FFFF00';
    else if (price > 500000 & price <= 1000000) return '#F0E68C';
    else if (price > 1000000 & price <= 5000000) return '#FF00FF';
    else if (price > 5000000 & price <= 10000000) return '#FFC0CB';
    else if (price > 10000000 & price <= 15000000) return '#EE82EE';
    else if (price > 15000000 & price <= 20000000) return '#0000FF';
    else if (price > 20000000 & price <= 25000000) return '#CD853F';
    else if (price > 25000000 & price <= 50000000) return '#000080';
    else if (price > 50000000 & price <= 100000000) return '#DDA0DD';
    else return '#FF0000';
};


function map(){

  var Thunderforest_Landscape = L.tileLayer('https://{s}.tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey={apikey}', {
    attribution: '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    apikey: '<your apikey>',
    maxZoom: 22})
  
      var Jawg_Streets = L.tileLayer('https://{s}.tile.jawg.io/jawg-streets/{z}/{x}/{y}{r}.png?access-token={accessToken}', {
          attribution: '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          minZoom: 0,
          maxZoom: 22,
          subdomains: 'abcd',
          accessToken: '<your accessToken>'
      })
      
      var Esri_WorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
       
       })

    let baseMaps = {

        "Landscape": Thunderforest_Landscape,
        "Streets": Jawg_Streets,
        "WorldImagery": Esri_WorldImagery
    };

    let condition1 = new L.LayerGroup();
    let condition2 = new L.LayerGroup();
    let condition3 = new L.LayerGroup();
    let condition4 = new L.LayerGroup();
    let condition5 = new L.LayerGroup();
    let condition6 = new L.LayerGroup();
    let condition7 = new L.LayerGroup();
    let condition8 = new L.LayerGroup();
    let condition9 = new L.LayerGroup();
    let condition10 = new L.LayerGroup();
    let condition11 = new L.LayerGroup();
    let condition12 = new L.LayerGroup();

    let overlayMaps = {
        "<span style='color: #008000'>100,000 or Less</span>": condition1,
        "<span style='color: #A52A2A'>>100,000 & <=250,000</span>": condition2,
        "<span style='color: #FFFF00'>>250,000 & >=500,000</span>": condition3,
        "<span style='color: #F0E68C'>>500,000 & >=1,000,000</span>": condition4,
        "<span style='color: #FF00FF'>>1,000,000 & >=5,000,000</span>": condition5,
        "<span style='color: #FFC0CB'>>5,000,000 & >=10,000,000</span>": condition6,
        "<span style='color: #EE82EE'>>10,000,000 & >=15,000,000</span>": condition7,
        "<span style='color: #0000FF'>>15,000,000 & >=20,000,000</span>": condition8,
        "<span style='color: #CD853F'>>20,000,000 & >=25,000,000</span>": condition9,
        "<span style='color: #000080'>>25,000,000 & >=50,000,000</span>": condition10,
        "<span style='color: #DDA0DD'>>50,000,000 & >=100,000,000</span>": condition11,
        "<span style='color: #FF0000'>100,000,000 or Higher</span>":condition12
    };

    let myMap = L.map("map", {
        center: [
          37.09, -95.71
        ],
        zoom: 5,
        layers: [Thunderforest_Landscape, null]
    });

    L.control.layers(baseMaps, overlayMaps,  
        {collapsed:true
          }).addTo(myMap);

    //function styleInfo(){
        //return{
           //color: PriceColor(),
            //fillcolor: 1
        //}   
    //};

    function propertyIcon(){

        L.icon({
            iconUrl: 'pngegg_blue.png',
            shadowUrl: null,
        
            iconSize:     [38, 95], 
            popupAnchor:  [-3, -76] 
        });


    };
 
    
    iffunction()

    d3.json(url).then(function(data) {

        L.geoJson(data, {
                pointToLayer: function (data, latlon) {  
                return L.marker(latlon,{icon: propertyIcon})
                .bindPopup(`
                <body>
                    <h2><strong>City:</strong>${(data.city)}</h2>
                    <p><strong>Property_ID:</strong> ${(data.property_id)}</p>
                    <p><strong>Address:</strong> ${(data.address)}</p>
                    <p><strong>Number of bedroom:</strong> ${(data.bedroom_number)}</p>
                    <p><strong>Number of bathroom:</strong> ${(data.bathroom_number)}</p>
                    <p><strong>Status:</strong> ${(data.property_status)}</p>
                    <p><strong>Price:</strong> ${(data.price)}</p>
                </body>`); 
                }
                
                
            })
    
    });



function iffunction(price){

  price = data.price;

    if(price <=100000) {
        dataform().addTo(condition1);
        condition1.addTo(myMap);
    }
    else if (price > 250000 & price <= 500000){
        dataform().addTo(condition2);
        condition2.addTo(myMap);
    }
    else if (price > 250000 & price <= 500000){
        dataform().addTo(condition3);
        condition3.addTo(myMap);
    }
    else if (price > 500000 & price <= 1000000){
        dataform().addTo(condition4);
        condition4.addTo(myMap);
    }
    else if (price > 1000000 & price <= 5000000){
        dataform().addTo(condition5);
        condition5.addTo(myMap);
    }
    else if (price > 5000000 & price <= 10000000){
        dataform().addTo(condition6);
        condition6.addTo(myMap);
    }
    else if (price > 10000000 & price <= 15000000){
        dataform().addTo(condition7);
        condition7.addTo(myMap);
    }
    else if (price > 15000000 & price <= 20000000){
        dataform().addTo(condition8);
        condition8.addTo(myMap);
    }
    else if (price > 20000000 & price <= 25000000){
        dataform().addTo(condition9);
        condition9.addTo(myMap);
    }
    else if (price > 25000000 & price <= 50000000){
        dataform().addTo(condition10);
        condition10.addTo(myMap);
    }
    else if (price > 50000000 & price <= 100000000){
        dataform().addTo(condition11);
        condition11.addTo(myMap);
    }
    else {
        dataform().addTo(condition12);
        condition12.addTo(myMap);
    }

};
     

};

