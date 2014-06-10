google.maps.event.addDomListener(window, 'load', initializeMap);
$(function() {
	$('button#locate').bind('click', function() {
		$.getJSON($SCRIPT_ROOT + '/_locate_nearest', {
			address: $('input[name="address"]').val(),
		}, function(data) {
			addLocation({
				lat: data.loc.geometry.location.lat, 
				lng: data.loc.geometry.location.lng,
				name: data.loc.name,
				curr: true});
			for (var i=0; i < data.results.length; i++) {
				addLocation({
					lat: data.results[i].geometry.location.lat,
					lng: data.results[i].geometry.location.lng,
					name: data.results[i].name
				});					
			}
			panMap();
		});
		return false;
	});
});
