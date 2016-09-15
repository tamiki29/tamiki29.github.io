// Tries to dectect the current language and switches the text of the site accordingly.
// source: http://buildingwebapps.blogspot.de/2012/05/localizing-html5-application-using.html
(function() {
    // Try to get language info from the browser.
    var lang = window.navigator.userLanguage || window.navigator.language;
    if (lang) {
        if (lang.length > 2) {
            // Convert e.g. 'en-GB' to 'en'. We do not support
            // resources for specific cultures at the moment.
            lang = lang.substring(0, 2);
        }
        // Include the languages that we want to support
        // in the following condition.
        // If we do not support the current navigator language,
        // default to english.
        if (lang != 'en' && lang != 'fr' && lang != 'de') {
            lang = 'en';
        }
    } else {
        // Default to english if we did not succeed in getting
        // a language from the browser.
        lang = 'en';
    }

    // English is already part of the HTML file, so we 
    // only replace strings if the language is different from English    
    if (lang != 'en') {
        // Construct a language-specific resource path.
        var resourcePath = 'strings.' + lang + '.js';
        // Get a reference to the HEAD element of the HTML page.
        var head = document.head || document.getElementsByTagName('head')[0];
        // Dynamically add the resourcePath to the HEAD element
        // to start loading the resources.
        var scriptEl = document.createElement('script');
        scriptEl.type = 'text/javascript';
        scriptEl.src = resourcePath;
        head.appendChild(scriptEl);
        // Get all HTML elements that have a resource key.
        var resElms = document.querySelectorAll('[data-res]');
        for (var n = 0; n < resElms.length; n++) {
            var resEl = resElms[n];
            // Get the resource key from the element.
            var resKey = resEl.getAttribute('data-res');
            if (resKey) {
                // Get all the resources that start with the key.
                for (var key in resources) {
                    if (key.indexOf(resKey) == 0) {
                        var resValue = resources[key];
                        if (key.indexOf('.') == -1) {
                            // No dot notation in resource key,
                            // assign the resource value to the element's
                            // innerHTML.
                            resEl.innerHTML = resValue;
                        } else {
                            // Dot notation in resource key, assign the
                            // resource value to the element's property
                            // whose name corresponds to the substring
                            // after the dot.
                            var attrKey = key.substring(key.indexOf('.') + 1);
                            resEl[attrKey] = resValue;
                        }
                    }
                }
            }
        }
    }
}
).call(this);
