/* google maps javascript*/

function initMap() {
  var uluru = {lat: 55.873543, lng: -4.289058};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: uluru
  });
  var marker = new google.maps.Marker({
    position: uluru,
    map: map
  });
}
