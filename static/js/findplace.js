var options = {
	//fruits
	data: [
    "The Burrow",
    "Windyridge",
    "Garden Cottage",
    "Four Winds",
    "Wild Bank",
    "Mile End",
    "Dreamwood",
    "Stillness",
    "Bridgelands",
    "Dengarden",
    "Kuredu",
    "Cumfrubrum",
    "Chestnuts",
    "The Warren",
    "The Cuckoo's Nest",
    "Crystal Cottage",
    "Kites Farm",
    "Robins Hedge",
    "Heatherbell",
    "Chimney Cottage",
    "Rosemary House",
    "Mulberry",
    "Stonehurst",
    "Seacrest",
		],
	list: {
		maxNumberOfElements: 10,
		match: {
			enabled: true
		}
	}
};



//$("#maxsize").easyAutocomplete(options);

$(document).ready(function(){
  $(function(){
		$("#maxsize").easyAutocomplete(options);
		$(".search-box-button").click( function(event) {
		alert("You clicked me! ouch!");
		});
	})});
