'use strict';
const request = require('request');

// ضع مفتاح API الخاص بك من Alpha Vantage هنا
const apiKey = '26E4LN8EWHQHLJSG';
const url = `https://www.alphavantage.co/query?function=REALTIME_OPTIONS&symbol=IBM&apikey=${apiKey}`;

request.get({
    url: url,
    json: true,
    headers: {'User-Agent': 'request'}
}, (err, res, data) => {
    if (err) {
        console.error('Error:', err);
    } else if (res.statusCode !== 200) {
        console.error('Status:', res.statusCode);
    } else {
        // عرض البيانات المسترجعة من API
        console.log(data);
    }
});
