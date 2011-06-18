
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
    
    this.elms = {
        'container': $('.content'),
        'nav': $('.nav')
    };
    
    this.vars = {
        'current_page': $('#feed')
    };
    
    this.initNav();
    this.setupPage('feed');
    $(this.vars.current_page).show();
}

opm.OaklandPm.prototype = {
    initNav: function() {
        $(this.elms.nav).find('li').each(function(i, item) {
            $(item).click(function() {
                this.handlePageTransition($(item).attr('rel'), {});
            }.bindScope(this));
        }.bindScope(this));
    },
    
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
    
    handlePageTransition: function(next_page_id, params) {
        $.ajax({
            url: next_page_id,
            type: 'POST',
            dataType: 'html',
            data: params,
            complete: function(res, textStatus) {
                $(this.elms.container).append(res);
                $(this.vars.current_page).fadeOut('fast', function() {
                    var next_page = $(this.vars.current_page).next('.page');
                    $(next_page).fadeIn('slow');
                    $(this.vars.current_page).remove();
                    this.setupPage($(next_page).attr('id'));
                }.bindScope(this));
            }.bindScope(this)
        });
    },
    
    handleFeed: function() {
        
    },
    
    handleEventDetail: function() {
        
    },
    
    handleCategories: function() {
        
    }
}