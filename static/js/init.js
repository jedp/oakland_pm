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
    $.postJSON([line2.constants.API_BASE_URL, path].join(''), params, callback);
}