$(document).ready(function(){
  /* $('#carouselProductos').carousel({
    interval: 1000
  }); */
  
  /* $('#carouselProductos .carousel-item').each(function(){
      var minPerSlide = 4;
      var next = $(this).next();
      if (!next.length) {
      next = $(this).siblings(':first');
      }
      next.children(':first-child').clone().appendTo($(this));
  
      for (var i=0;i<minPerSlide;i++) {
          next=next.next();
          if (!next.length) {
            next = $(this).siblings(':first');
          }
      
          next.children(':first-child').clone().appendTo($(this));
        }
  }); */


  $('#carouselProductos').on('slide.bs.carousel', function (e) {
    /*
        CC 2.0 License Iatek LLC 2018 - Attribution required
    */
    var $e = $(e.relatedTarget);
    var idx = $e.index();
    var itemsPerSlide = 5;
    var totalItems = $('#carouselProductos .carousel-item').length;
 
    if (idx >= totalItems-(itemsPerSlide-1)) {
        var it = itemsPerSlide - (totalItems - idx);
        for (var i=0; i<it; i++) {
            // append slides to end
            if (e.direction=="left") {
                $('#carouselProductos .carousel-item').eq(i).appendTo('#carouselProductos .carousel-inner');
            }
            else {
                $('#carouselProductos .carousel-item').eq(0).appendTo('#carouselProductos .carousel-inner');
            }
        }
    }
});

})