canvas = d3.select("#hashbins");

function getHash(data) {
    return data.Year;
}

bins_per_row = 15;
imres = 50;
binwidth = 60;
binheight_fac = 3.0;
var people = [];
var bins;
var hashFnCode = document.getElementById("hashFnCode");
let maxBinsText = document.getElementById("maxBins");
maxBinsText.value = "-1";
var cname = document.getElementById("cname");
var bday = document.getElementById("bday");
var pimg = document.getElementById("pimg");

d3.csv("../data/HarryPotter/HarryPotter.csv",
        function(data){
            data.Month = parseInt(data.Month);
            data.Year = parseInt(data.Year);
            data.Day = parseInt(data.Day);
            people.push(data);
        });

function unwrap(idx, bins_per_row) {
    col = idx%bins_per_row;
    row = (idx-col)/bins_per_row;
    return {'col':col, 'row':row};
}

function loadPeople() {
    for (var i = 0; i < people.length; i++) {
        var data = people[i];
        data.path = "../data/HarryPotter/" + (i+1) + ".png";
        data.hashValue = 0;
        rowcol = unwrap(i, bins_per_row);
        people[i].elem = canvas.append("svg:image")
        .attr("width", imres)
        .attr("height", imres)
        .attr("xlink:href", data.path)
        .attr('x', binwidth*rowcol.col)
        .attr('y', 50*rowcol.row)
        .attr("idx", i)
        .on("mouseover", function(a, b, c, d) {
            var idx = d3.select(this).attr("idx");
            cname.innerHTML = people[idx].Name;
            bday.innerHTML = people[idx].Month + "/" + people[idx].Day + "/" + people[idx].Year;
            pimg.innerHTML = "<img src = " + people[idx].path + " width = 200 height = 200>";
        });
    }
}

function computeHashes() {
    eval(hashFnCode.value);
    // Step 1: Compute all hashes and figure out range
    var minHash, maxHash;
    hashValues = {};
    let maxBins = parseInt(maxBinsText.value);
    for (var i = 0; i < people.length; i++) {
        var h = getHash(people[i]);
        if (maxBins > -1) {
            h = h%maxBins;
        }
        people[i].hashValue = h;
        if (i == 0) {
            minHash = h;
            maxHash = h;
        }
        else {
            if (h > maxHash) {
                maxHash = h;
            }
            if (h < minHash) {
                minHash = h;
            }
        }
        if (!(h in hashValues)) {
            hashValues[h] = 0;
        }
        people[i].num = hashValues[h]; //Position in linked list
        hashValues[h] += 1;
    }

    // Step 2: Do animation moving to new bins
    var NBins = maxHash - minHash + 1;
    for (var i = 0; i < people.length; i++) {
        var h = people[i].hashValue;
        var rowcol = unwrap(h-minHash, bins_per_row);
        x  = binwidth*rowcol.col;
        y  = binheight_fac*binwidth*rowcol.row+10;
        y += binwidth*binheight_fac*people[i].num*1.0/(hashValues[h]+2);
        y += binwidth*binheight_fac/10;
        people[i].elem.transition()
            .attr("x", x)
            .attr("y", y);
    }
    // Step 3: Setup bins to display
    canvas.selectAll("rect").remove();
    canvas.selectAll("text").remove();
    for (var h = minHash; h <= maxHash; h++) {
        var rowcol = unwrap(h-minHash, bins_per_row);
        var x = binwidth*rowcol.col;
        var y = binwidth*rowcol.row*binheight_fac;
        canvas.append("rect")
            .attr("x", x)
            .attr("y", y)
            .attr("width", binwidth)
            .attr("height", binwidth*binheight_fac)
            .attr("fill", "none")
            .attr("stroke", "black");
        var s = ""+h;
        if (h in hashValues) {
            s += " (" + hashValues[h] + ")";
        }
        canvas.append("text")
            .attr("x", x)
            .attr("y", y+binwidth*binheight_fac/10)
            .style("font-size", "14px")
            .text(s);
    }

}
