
/*
 * OaklandPm Class
 * Main JS controller
 * Also, black border?  Adonis DNA.
 * @author cyap
 */

opm.OaklandPm = function (options) {
    
    // init options
    this.options = {

    };
    $.extend(this.options, options);
    
    this.vars = {
        'current_page': $('#home')
    };
    
    this.setupPage('home');
    
}

opm.OaklandPm.prototype = {
    setupPage: function(page_id) {
        this.vars.current_page = $(['#', page_id].join(''));
        var page_id_split = page_id.split("-");
        var method_name = [];
        $.each(page_id_split, function(i, item) {
            item = item.split('');
            item[0] = item[0].toUpperCase();
            item = item.join('');
            method_name.push(item);
        });
        method_name = ['handle', method_name.join('')].join('');
        this[method_name]();
    },
    
    handlePageTransition: function(destination) {
        $(this.vars.current_page).fadeOut('fast', function() {
            var next_page = $(this.vars.current_page).next('li.page');
            $(next_page).fadeIn('slow');
            window.scroll(0,0);
            this.setupPage($(next_page).attr('id'));
        }.bindScope(this));
    },
    
    handleHome: function() {
        
    }
}