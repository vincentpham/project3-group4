d3.json(url).then((data) =>{

    let changingprice = data.changing_price;
    let city = data.changing_price;

    let trace = {
        x: changingprice,
        y: yticks,
        text: city,
        type: "bar",
        orientation: "v"
    };

    let layout = {
        title: "Real Estae Evolution Prices in USA Over 24 Years"
    };

    Plotly.newPlot("bar", [trace], layout)


});