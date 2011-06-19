/**
 * Cache class
 * This class is a simple named cache manager intended to cleanly
 * enable various objects to communicate with each other.
 *
 * @author Chris Yap
 */
opm.Cache = function() {
	this.cache = {
		
	};
};

opm.Cache.prototype = {
    
    createCache: function(cacheId) {
        this.cache[cacheId] = [];
    },
    
	addToCache: function(cacheId, itemToCache) {
		this.cache[cacheId].push(itemToCache);
	},
	
	removeFromCache: function(cacheId, itemToRemove) {
	    var index = $.inArray(itemToRemove, this.cache[cacheId]);
	    if (index > -1) {
	        this.cache[cacheId].remove(index);
	    }
	},
	
	findInCache: function(cacheId, item) {
	    var found = $.inArray(item, this.cache[cacheId]);
	    if (found > -1) {
	        return true;
	    }
	    else {
	        return false;
	    }
	},
	
	clearCache: function(cacheId) {
		this.cache[cacheId] = [];
	},
	
	checkEmpty: function(cacheId) {
		if (this.cache[cacheId].length < 1) {
			return true;
		}
		else {
			return false;
		}
	},
	
	getCache: function(cacheId) {
		return this.cache[cacheId];
	}
};