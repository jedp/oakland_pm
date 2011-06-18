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

// define api environment
opm.constants.API_BASE_URL = '/api/';

// define common functions
opm.common.apicall = function (path, params, callback) {
    $.postJSON([opm.constants.API_BASE_URL, path].join(''), params, callback);
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