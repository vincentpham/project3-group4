const url="https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json"

const dataPromise =d3.json(url);


console.log("datPromise:", dataPromise);

dataPromise.then (function(data){

    console.log(data)
    let sample_data=data["metadata"][0];
    document.getElementById('sample-metadata').innerHTML +=  "id:" + sample_data["id"] + "<br />" +"ethnicity:"+ sample_data["ethnicity"] +"<br />"+"gender:" + sample_data["gender"] +"<br />" +"age"+ sample_data["age"] + "<br />"+"location:" + sample_data["location"] + "<br />" +"bbtype:"+ sample_data["bbtype"]+ "<br />" +"wfreq:"+ sample_data["wfreq"];
    let first_one_x=data["samples"][0]["sample_values"].slice(0,10);

   
    let first_one_y=data["samples"][0]["otu_ids"].slice(0,10);
    let y_data=[];
    let z=data["samples"][0]["otu_labels"].slice(0,10);
    let hover_1=z.reverse();
    for (i=0;i<first_one_y.length;i++){
        y_data.push("OTU"+first_one_y[i])

    }
    let final_y=y_data.reverse()
    let final_x=first_one_x.reverse()
    let final_x_bubble=data["samples"][0]["otu_ids"];
    let final_y_bubble=data["samples"][0]["sample_values"];
    let samle_values_for_bubble=data["samples"][0]["sample_values"];
    let bubble_text_1=data["samples"][0]["otu_labels"];
    console.log(samle_values_for_bubble);
    let Trace1={
        x:final_x,
        y:final_y,
        text:hover_1,
        type:'bar',
        orientation:'h'
    }
    let graph_data=[Trace1]
    Plotly.newPlot("bar", graph_data);
    var trace12 = {
        x: final_x_bubble,
        y: final_y_bubble,
        text:bubble_text_1,
        mode: 'markers',
        marker: {
        size: samle_values_for_bubble,

        color:final_x_bubble

        }
      };
      
      var data_2 = [trace12];
      
      
      Plotly.newPlot('bubble', data_2);
    d3.select("#selDataset").on("change", function optionChanged()
    {
        let dropdownMenu=d3.select("#selDataset");
        let dataset=dropdownMenu.property("value");
        let data1=data["samples"];
        let comp_val=data["names"];
        for (let i=0;i<comp_val.length;i++){
            if(dataset===comp_val[i]){
                
                var target_val=i;
                
            }
        }
        console.log(target_val);
        let m_data=data["metadata"][target_val];
        document.getElementById('sample-metadata').innerHTML =  "id:" + m_data["id"] + "<br />" +"ethnicity:"+ m_data["ethnicity"] +"<br />"+"gender:" + m_data["gender"] +"<br />" +"age"+ m_data["age"] + "<br />"+"location:" + m_data["location"] + "<br />" +"bbtype:"+ m_data["bbtype"]+ "<br />" +"wfreq:"+ m_data["wfreq"];

        let x_new=data1[target_val]["sample_values"];
        let text_1=data1[target_val]["otu_labels"].slice(0,10);
        let text_1_final=text_1.reverse();
        let bubble_color=data1[target_val]["otu_ids"];
        let bubble_size=data1[target_val]["sample_values"];
        let bubble_text=data1[target_val]["otu_labels"];
        
        if (x_new.length>10){
            x_new=x_new.slice(0,10);
        }
        let x_final_1=x_new.reverse();
        console.log(x_final_1);

        let y_new=data1[target_val]["otu_ids"];
        if (y_new.length>10){
            y_new=y_new.slice(0,10);
        }
        let y_new_1=[];
        for(i=0;i<y_new.length;i++){
            y_new_1.push("OTU"+y_new[i]);
        }
        let y_final_1=y_new_1.reverse();
        console.log(y_final_1);
        let x_new_bubble=data1[target_val]["otu_ids"];
        let y_new_bubble=data1[target_val]["sample_values"];

        Plotly.restyle("bar", "x", [x_final_1]);
        Plotly.restyle("bar", "y", [y_final_1]);
        Plotly.restyle("bubble", "x", [x_new_bubble]);
        Plotly.restyle("bubble", "y", [y_new_bubble]);
        Plotly.restyle("bubble","color",[bubble_color]);
        Plotly.restyle("bar","text",[bubble_text]);
        Plotly.restyle("bubble", "size", [bubble_size])


        
        




    })
        
}); 
    

    
        
    
    



var select = document.getElementById("selDataset"); 
    var options = ["940", "941", "943", "944", "945", "946", "947", "948", "949", "950", "952", "953", "954", "955", "956", "958", "959", "960", "961", "962", "963", "964", "966", "967", "968", "969", "970", "971", "972", "973", "974", "975", "978", "1233", "1234", "1235", "1236", "1237", "1238", "1242", "1243", "1246", "1253", "1254", "1258", "1259", "1260", "1264", "1265", "1273", "1275", "1276", "1277", "1278", "1279", "1280", "1281", "1282", "1283", "1284", "1285", "1286", "1287", "1288", "1289", "1290", "1291", "1292", "1293", "1294", "1295", "1296", "1297", "1298", "1308", "1309", "1310", "1374", "1415", "1439", "1441", "1443", "1486", "1487", "1489", "1490", "1491", "1494", "1495", "1497", "1499", "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1507", "1508", "1510", "1511", "1512", "1513", "1514", "1515", "1516", "1517", "1518", "1519", "1521", "1524", "1526", "1527", "1530", "1531", "1532", "1533", "1534", "1535", "1536", "1537", "1539", "1540", "1541", "1542", "1543", "1544", "1545", "1546", "1547", "1548", "1549", "1550", "1551", "1552", "1553", "1554", "1555", "1556", "1557", "1558", "1561", "1562", "1563", "1564", "1572", "1573", "1574", "1576", "1577", "1581", "1601"]; 


select.innerHTML = "";

for(var i = 0; i < options.length; i++) {
    var opt = options[i];
    select.innerHTML += "<option value=\"" + opt + "\">" + opt + "</option>";
};