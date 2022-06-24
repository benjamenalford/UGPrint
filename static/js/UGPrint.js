let url = d3.select("#url");
let submit = d3.select("#submit");
let tabview = d3.select("#tab");
let status = d3.select("#status");
status.style("opacity", 0);

submit.on("click", () => {
    status.style("opacity", 100);
    d3.text("/getTab", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: "url=" + JSON.stringify(url.node().value)
    }).then(data => {
        status.style("opacity", 0);
        tabview.text(data);
    });
});