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
        this.container = E('div');
    },
    
    setup: function() {
        
    },
    
    enter: function() {
        
    }
});


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