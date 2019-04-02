'use strict';

let https = require('https');

// **********************************************
// *** Update or verify the following values. ***
// **********************************************

// Replace this with a valid service name.
let service_name = 'ENTER SERVICE NAME HERE';

// Replace this with a valid subscription key.
let subscriptionKey = 'ENTER KEY HERE';

let index_name = 'test-index';

let document_key = '1';

let host = service_name + '.search.windows.net';
let operation = '/indexes/' + index_name + '/docs/' + document_key;
let api_version = '2017-11-11';
let params = {
    'api-version': api_version
};

/*
 * Helper functions.
 */

let pretty_print = function (s) {
    return JSON.stringify(JSON.parse(s), null, 4);
};

let get_path = function (operation, params) {
    var pairs = [];
    for (var key in params) {
        pairs.push(key + '=' + params[key]);
    }
    return operation + '?' + pairs.join('&');
};

// callback is the function to call once we have the entire response.
let response_handler = function (callback, response) {
    let body = '';
    response.on('data', function (d) {
        body += d;
    });
    response.on('end', function () {
        // Call the callback function with the response and body.
        callback({ response: response, body: body });
    });
    response.on('error', function (e) {
        console.log('Error: ' + e.message);
    });
};

// Get an HTTP response handler that calls the specified callback function once we have the entire response.
let get_response_handler = function (callback) {
    // Return a function that takes an HTTP response, and is closed over the specified callback.
    // This function signature is required by https.request, hence the need for the closure.
    return function (response) {
        response_handler(callback, response);
    }
};

// callback is the function to call once we have the entire response from the GET request.
let get = function (host, path, callback) {
    let request_params = {
        method: 'GET',
        hostname: host,
        path: path,
        headers: {
            'api-key': subscriptionKey,
        }
    };

    console.log('Calling GET ' + host + path + '.');
    // Pass the callback function to the response handler.
    let req = https.request(request_params, get_response_handler(callback));
    req.end();
};

/*
 * Send the request and provide a callback function that prints the response.
 */

get(host, get_path(operation, params), function (result) {
    console.log(pretty_print(result.body));
});
