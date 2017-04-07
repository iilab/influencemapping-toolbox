$(function() {
  var $formFilters = $('.form-filters'),
      $search = $formFilters.find('#search'),
      $facets = $('.form-control.facet'),
      $items = $('.item'),
      searchState = {},
      facets = {},
      facetValues = {};

  var updateItems = function() {
    var searchText = $search.val() || '';
    searchText = searchText.toLowerCase().trim();
    var searchRex = new RegExp('.*' + searchText + '.*');
    $items.each(function(i, item) {
      var $item = $(item), 
          visible = true;
      if (searchText.length) {
        var text = $item.find('.item-title').html();
        text = text + ' ' + $item.find('.item-description').html();
        visible = searchRex.test(text.toLowerCase());
      }
      for (var f in facets) {
        if (!!searchState[f]) {
          var val = $item.data(f);
          if (val != searchState[f]) {
            visible = false;
          } 
        }
      }
      $item.toggle(visible);
    });
  };

  $facets.each(function(i, el) {
    var $el = $(el);
    facets[$el.attr('id')] = $el;
  });

  $items.each(function(i, item) {
    var $item = $(item);
    for (var f in facets) {
      var val = $item.data(f);
      if (val.trim().length) {
        if (!facetValues[f]) {
          facetValues[f] = {};  
        }
        if (!facetValues[f][val]) {
          facetValues[f][val] = 0;  
        }
        facetValues[f][val] += 1;  
      }
    }
  });

  $.each(facetValues, function(facet, values) {
    var $facet = $facets.filter('#' + facet);
    $.each(values, function(value, count) {
      $facet.append('<option value="'+value+'">'+value+' ('+count+')</option>');
    });
  });

  $facets.on('change', function(event) {
    var $facet = $(event.target),
        val = $facet.val();
    searchState[$facet.attr('id')] = val;
    updateItems();
  });

  $search.on('change', updateItems());
  $search.on('keypress', updateItems());

  $formFilters.on('submit', function(e) {
    console.log(e);
    e.preventDefault();
    updateItems()
  });
});
