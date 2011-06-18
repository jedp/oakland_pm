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
        'is_setup': false
    };
    
    this.initNav();
    this.handlePageTransition('feed', {});
    
    // detect platform
    if (navigator.platform.indexOf('iPhone') != -1 || navigator.platform.indexOf('iPod') != -1) {
        switch (screen.width) {
            case 480:
                this.vars.current_platform = 'iPhone4';
                break;
            
            default:
                this.vars.current_platform = 'iPhone'
                break;
        }
    }
    else if (navigator.platform.indexOf('iPad') != -1) {
        this.vars.current_platform = 'iPad';
    }
    else {
        this.vars.current_platform = 'default';
    }
    
    // hide address bar for mobile (not handling android yet)
    if (this.vars.current_platform != 'default') {
        setTimeout(function() { window.scrollTo(0, 1) }, 100);
    }
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
            url: [next_page_id, '/'].join(''),
            type: 'POST',
            dataType: 'html',
            data: params,
            complete: function(res, textStatus) {
                $(this.elms.container).append(res.responseText);
                if (this.vars.is_setup) {
                    $(this.vars.current_page).fadeOut('fast', function() {
                        var next_page = $(this.vars.current_page).next('.page');
                        $(next_page).fadeIn('slow');
                        $(this.vars.current_page).remove();
                        this.setupPage($(next_page).attr('id'));
                    }.bindScope(this));
                }
                else {
                    this.vars.is_setup = true;
                    this.vars.current_page = $('#feed');
                    $(this.vars.current_page).show();
                    this.setupPage('feed');
                }
            }.bindScope(this)
        });
    },
    
    handleFeed: function() {
      	$('li.attending').each(function(index){
    		new opm.Draw("check", this);
    	});  
    },
    
    handleEventDetail: function() {
        
    },
    
    handleCategories: function() {
        
    }

}

/*
opm.Page = function (proto) {
    
    var cls = function () {
        this.init.apply(this, arguments);
    }

    cls.prototype = {
        container: null,
        is_setup: false,
        init: function () {},
        setup: function () {},
        enter: function () {}
    }

    $.extend(cls.prototype, proto);

    return cls;
}

opm.Feed = opm.Page({
    init: function() {
        
    },
    
    setup: function() {
        
    },
    
    enter: function() {
        
    }
});
*/

opm.Draw = function(what, container){
	this.elms = {
        "container" : container
    };
    this.vars = {
        "what" : what
    };
    
    switch(what){
    	case "check":
    		this.drawCheck(this.elms.container);
    		break;
    	case "circle":
    		break;
    	default:
    		console.log("ERROR: NO DRAWING TYPE SPECIFIED!");
    		break;
    }
}
opm.Draw.prototype = {
	drawCheck : function(container){
		var parent = this;
		var paper = Raphael(container, 50, 50);
		
		var st = paper.set();
		st.push(
    		paper.rect(0, 25, 25, 25)
    		// paper.circle(30, 10, 5)
		);
		st.attr({fill: "red"});
	},
}












