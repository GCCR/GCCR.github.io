// GitHub doesn't allow using any of their hosted content in an iframe/object
// But there's a workaround
var url = "https://raw.githubusercontent.com/GCCR/members-map/master/members-map.html";
var members_map;
// Fetch the HTML map as text
fetch(url)
  .then(function(response) {
    response.text().then(function(text) {
        members_map = text;
        done();
    });
  });
// Generate a data URI from the map's text and 
// use it as the source of the iframe
function done() {
  var blob = new Blob([members_map], {type: 'text/html'});
  var node = document.getElementById("members_map");
  node.src = URL.createObjectURL(blob);
}
