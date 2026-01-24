var listObj = new List('literature-list', {
    valueNames: ['authors', 'title', 'journal', 'year', 'dateAdded', 'doi', 
      'tag-covid19', 'tag-taste', 'tag-smell', 'tag-viral', 'tag-case-report',
      'tag-preprint', 'tag-genes'],
    page: 10,
    pagination: {
      name: "pagination",
      paginationClass: "pagination",
      innerWindow: 2,
      outerWindow: 1,
    }
  });

  // add filters
  var label_to_tag = {
    "COVID-19": "covid19",
    "Smell": "smell",
    "Taste": "taste",
    "Viral": "viral",
    "Case report": "case-report",
    "Preprint": "preprint",
    "Genes": "genes",
  };
  $('.filter').on('click', function() {
    label = $(this).text();
    if (label == "Reset") {
      listObj.filter()
    } else {
      tag = "tag-" + label_to_tag[label];
      listObj.filter(function(item) {
        if (item.values()[tag] == label_to_tag[label]) {
          return true;
        } else {
          return false;
        }
      })
    }
  })

  // apply bootstrap theme to page numbers
  function apply_bootstrap_theme() {
    $('.pagination li').toggleClass("page-item");
    $('.pagination li a').toggleClass("page-link");
  }
  apply_bootstrap_theme();
  listObj.on('searchComplete', function() {
    apply_bootstrap_theme();
  })
  listObj.on('filterComplete', function() {
    apply_bootstrap_theme();
  })
  listObj.on('sortComplete', function() {
    apply_bootstrap_theme();
  })
  $(document).on('click', '.page', function() {
    apply_bootstrap_theme();
  })