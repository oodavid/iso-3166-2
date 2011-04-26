iso = {};
iso.xml;
iso.map;
iso.json = {};
iso.errors_n;
iso.errors = {};
iso.codes = [];
iso.code_n;
iso.init = function(e) {
	// Render a simple map
	var myLatlng = new google.maps.LatLng(55,-1);
	var myOptions = {
		zoom: 4,
		center: myLatlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}
	iso.map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
	// Create a geocoder object
	iso.geocoder = new google.maps.Geocoder();
};
iso.load = function () {
	// Loading the XML
	$.ajax({
		type: "GET",
		url: "iso-codes/iso_3166_2/iso_3166_2.xml",
		dataType: "xml",
		success: iso.parse
	});
};
iso.parse = function (xml) {
	// Save the xml object
	iso.xml = xml;
	// Parse the object
	var countryName;
	$(iso.xml).find('iso_3166_2_entries').contents().each(function(){
		switch (this.nodeType) {
			case 3:
				// Ignore text nodes
				return true;
			case 8:
				// Comments store the country name
				countryName = $.trim(this.nodeValue);
				return true;
			case 1:
				// Add this country to the JSON
				var parentCode = $(this).attr('code');
				iso.json[parentCode] = { code: parentCode, name: countryName, division: 'country' };
				// Parse the children
				$(this).find('iso_3166_subset').each(function(){
					var division = $(this).attr('type').toLowerCase();
					// Parse the grandchildren
					$(this).find('iso_3166_2_entry').each(function(){
						var myParent = parentCode;
						// If it references a different parent, find it (might use a space or hyphen)
						if ($(this).attr('parent')) {
							var tmp1 = parentCode + ' ' + $(this).attr('parent');
							var tmp2 = parentCode + '-' + $(this).attr('parent');
							if (iso.json[tmp1]) { myParent = tmp1; }
							if (iso.json[tmp2]) { myParent = tmp2; }
						}
						iso.json[$(this).attr('code')] = { code: $(this).attr('code'), name: $(this).attr('name'), division: division, parent: myParent };
					});
				});
				return true;
		}
	});
	// Reset some vars
	iso.errors = {};
	iso.errors_n = 0;
	iso.codes = [];
	iso.code_n = 0;
	// Set the list of codes for iterating
	$.each(iso.json, function(k, v){
		// If it's a higher priority country, put it to the top for fast-track processing :-)
		if ($.inArray(v.code.substring(0,2), ['GB', 'US', 'IE']) > -1) {
			iso.codes.unshift(v.code);
		} else {
			iso.codes.push(v.code);
		}
	});
	// Now iterate and geocode them badboys!
	iso.iterate();
	// Log the activity
	setInterval('console.log(iso.codes.length + " objects, " + iso.code_n + " lookups (" + iso.errors_n + " skipped)");', 60000);
};
iso.iterate = function() {
	// We done already?
	if (!iso.codes[iso.code_n]) {
		alert('$.toJSON(iso.json);\n\nfor all your JSON data needs\n\niso.errors;\n\nfor all your errors');
		return;
	}
	// Grab the object
	ob = iso.json[iso.codes[iso.code_n]];
	// Geocode it
	iso.geocoder.geocode( { 'address': ob.name + ', ' + ob.code }, function(results, status) {
		// Grab the object again (scope)
		ob = iso.json[iso.codes[iso.code_n]];
		// Hows it?
		if (status == google.maps.GeocoderStatus.OK) {
			// Update the object
			ob.lat = results[0].geometry.location.lat();
			ob.lng = results[0].geometry.location.lng();
			// Turn this off to save on processing :-)
			/* 
			// Set location
			iso.map.setCenter(results[0].geometry.location);
			// Add a marker
			var marker = new google.maps.Marker({
				map: iso.map,
				position: results[0].geometry.location,
				title: ob.name + ', ' + ob.code
			});
			*/
			// Increment and get the next one
			iso.code_n ++;
			iso.iterate();
		} else {
			// Hit the limit?
			if(status == 'OVER_QUERY_LIMIT') {
				// Wait a moment and try again
				setTimeout('iso.iterate()', 20000);
			} else {
				// Make a note and carry on
				iso.errors_n ++;
				iso.errors[ob.code] = status;
				iso.code_n ++;
				iso.iterate();
			}
		}
	});
};
$(document).ready(iso.init);
