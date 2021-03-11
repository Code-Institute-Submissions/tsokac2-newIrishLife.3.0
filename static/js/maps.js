function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom : 11,
        center: {
            lat: 53.350140,
            lng: -6.266155
        }
    });
/*addDomListener EVENTS  - CODE SOURCE: https://developers.google.com/maps/documentation/javascript/overview*/
google.maps.event.addDomListener(window, "resize", function() {
    var center = map.getCenter();
    google.maps.event.trigger(map, "resize");
    map.setCenter(center);
  });

  

}