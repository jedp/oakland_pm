/*
 * Oakland PM js init
 * Also, bingo bango.
 * @author cyap
 */
 

// create an oaklandPM namespace for all our js assets
var opm = {
    'constants': {},
    'common': {}
};

// define content container
opm.constants.CONTENT_CONTAINER = $('div.content');

// define api environment
opm.constants.API_BASE_URL = '/xhr/';

// define common functions
opm.common.getMarkup = function (path, params, callback) {
    $.ajax({
        url: [opm.constants.API_BASE_URL, path, '/'].join(''),
        type: 'POST',
        dataType: 'html',
        data: params,
        complete: function(res, textStatus) {
           callback(res.responseText);
        }
    });
}

opm.common.initLinks = function(){
	$('a').live('click', function(e){
		e.preventDefault();
		var url = $(this).attr('href').replace(/\//g, '');
		opm.pages.select(url);
	});
}

// fix csrf token thing
$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", csrf_token);
         }
     } 
});