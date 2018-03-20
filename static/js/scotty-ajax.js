$(document).ready(function(){

//    $('#suggestion').keyup(function(){
    $('#suggestion').on('input',function(){
      $('#suggestion').css("background-color", "pink");
      var query;
      query = $(this).val();
      $.get('/dog/suggest_cottage/', {suggestion: query}, function(data){
          $('#cottages').html(data);
        });
      });

//    $('#suggestion').on('input',function(e){
//      alert('Changed!');
//    });
});
