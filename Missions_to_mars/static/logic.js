d3.select("#button-scraping").on('click', function(){
    console.log("hola");
    d3.json("/api/consigue").then((d)=>{
        console.log(d);
        d3.select("#results-area").selectAll("hr").remove();
        d3.select("#results-area").selectAll("div").remove();
        d3.select("#results-area").append('hr');
        d3.select("#results-area").append("div").attr('class','row justify-content-center').attr('id','title-table');
        d3.select("#results-area").append("div").attr('class','row justify-content-center').attr('id','upper-table');
        d3.select("#results-area").append("div").attr('class','row').attr('id','middle-table');
        d3.select("#results-area").append("div").attr('class','row').attr('id','lower-table1');
        d3.select("#results-area").append("div").attr('class','row').attr('id','lower-table2');

        d3.select("#title-table").append("h5").attr('class','font-weight-bold').text('Latest Mars News');
        d3.select("#upper-table").append("h6").attr('class','font-weight-bold').text(d.news.title);
        d3.select("#upper-table").append("p").text(d.news.teaser);

        d3.select("#middle-table").append("div").attr('class', "col-9").attr('id','feat-img');
        d3.select("#feat-img").append("h5").attr('class','font-weight-bold').text('Featured Mars Image');
        d3.select("#feat-img").append("img").attr('src',d.feat_img).attr('class','img-fluid');

        d3.select("#middle-table").append("div").attr('class', "col-3").attr('id','other-tables');
        d3.select("#other-tables").append("div").attr('class','card').attr('id','card-weather');
        d3.select("#card-weather").append("div").attr('class','card-body').attr('id','body-weather');
        d3.select("#body-weather").append("h6").attr('class','card-title font-weight-bold').text('Current Weather on Mars');
        d3.select("#body-weather").append("p").attr('class','card-text').text(d.weather);
        d3.select("#other-tables").append('hr');
        d3.select("#other-tables").append("h6").attr('class','font-weight-bold').text('Mars Facts');
        d3.select("#other-tables").append().html(d.html_table);

        d3.select("#lower-table1").append('div').attr('class','col-6').attr('id','hem-1');
        d3.select("#lower-table1").append('div').attr('class','col-6').attr('id','hem-2');
        d3.select("#lower-table2").append('div').attr('class','col-6').attr('id','hem-3');
        d3.select("#lower-table2").append('div').attr('class','col-6').attr('id','hem-4');

        d3.select("#hem-1").append('div').attr('class','card').attr('id','card-hem-1');
        d3.select("#card-hem-1").append('img').attr('class','card-img-top img-fluid').attr('src',d.hemisphere[0].img_url);
        d3.select("#card-hem-1").append('div').attr('class','card-body').attr('id','body-hem-1');
        d3.select("#body-hem-1").append('h6').attr('class','card-text').text(d.hemisphere[0].title);

        d3.select("#hem-2").append('div').attr('class','card').attr('id','card-hem-2');
        d3.select("#card-hem-2").append('img').attr('class','card-img-top img-fluid').attr('src',d.hemisphere[1].img_url);
        d3.select("#card-hem-2").append('div').attr('class','card-body').attr('id','body-hem-2');
        d3.select("#body-hem-2").append('h6').attr('class','card-text').text(d.hemisphere[1].title);

        d3.select("#hem-3").append('div').attr('class','card').attr('id','card-hem-3');
        d3.select("#card-hem-3").append('img').attr('class','card-img-top img-fluid').attr('src',d.hemisphere[2].img_url);
        d3.select("#card-hem-3").append('div').attr('class','card-body').attr('id','body-hem-3');
        d3.select("#body-hem-3").append('h6').attr('class','card-text').text(d.hemisphere[2].title);

        d3.select("#hem-4").append('div').attr('class','card').attr('id','card-hem-4');
        d3.select("#card-hem-4").append('img').attr('class','card-img-top img-fluid').attr('src',d.hemisphere[3].img_url);
        d3.select("#card-hem-4").append('div').attr('class','card-body').attr('id','body-hem-4');
        d3.select("#body-hem-4").append('h6').attr('class','card-text').text(d.hemisphere[3].title);

    })
})


