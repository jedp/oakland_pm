/*
 * OaklandPm Page Class
 * Main JS controller
 * Also, black border?  Adonis DNA.
 * @author cyap
 */

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

/* BEGIN PAGE DEFINITIONS */

opm.Feed = opm.Page({
    init: function() {
        console.log('feed init');
        this.container = E('div');
    },
    
    setup: function() {
        console.log('feed setup');
    },
    
    enter: function() {
        console.log('feed enter');
        opm.common.getMarkup('feed', {}, function(res){
            $(this.container).html(res);
        }.bindScope(this));
    }
});

opm.EventDetail = opm.Page({
    init: function() {
        console.log('event detail init');
        this.container = E('div');
    },
    
    setup: function() {
        console.log('event detail setup');
    },
    
    enter: function(event_id) {
        opm.common.getMarkup(['event', event_id].join('/'), {}, function(res){
            $(this.container).html(res);
        }.bindScope(this));
    }
});

opm.Categories = opm.Page({
    init: function() {
        console.log('categories init');
        this.container = E('div');
    },
    
    setup: function() {
        console.log('categories setup');
    },
    
    enter: function() {
        console.log('categories enter');
        opm.common.getMarkup('categories', {}, function(res){
            $(this.container).html(res);
        }.bindScope(this));
    }
});

opm.About = opm.Page({
    init: function() {
        console.log('about init');
        this.container = E('div');
    },
    
    setup: function() {
        console.log('about setup');
    },
    
    enter: function() {
        console.log('about enter');
        opm.common.getMarkup('about', {}, function(res){
            $(this.container).html(res);
        }.bindScope(this));
    }
});

/* END PAGE DEFINITIONS */

opm.pages = {
    _current: null,
    _hider: E('div'),
    
    setContainer: function(container) {
        if (opm.pages._current)
        {
            opm.pages._current.appendTo(opm.pages._hider);
        }
        opm.pages._current = container;
        $(opm.constants.CONTENT_CONTAINER).html(container);
    },
    
    select: function() {
		var args = Array.create(arguments);
        var page_name = args.shift();
        var page = opm.pages[page_name];

		if (page) {
            opm.pages.setContainer(page.container);
            
            if (!page.is_setup)
            {
                page.setup.apply(page, args);
                page.is_setup = true;
            }
            
            page.enter.apply(page, args);
        }
		
    }
	
};
/*
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
*/
