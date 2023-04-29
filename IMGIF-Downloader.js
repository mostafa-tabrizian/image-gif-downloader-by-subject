const http = require('http')
const https = require('https')
const fs = require('fs')

listUrls = []

console.log('Downloading...')
console.log('*Use OpenVPN*')

for (let i = 0; i < listUrls.length; i++) {
    ImgNumberCounter = (i).toString()
    formatOfImg = listUrls[i].split('.').slice(-1)[0].split('?')[0].split('%')[0].split('/')[0].split('&')[0]
    const file = fs.createWriteStream(`./output/imgif${ImgNumberCounter}.${formatOfImg}`);

    if (listUrls[i].includes('https')) {
        const request = https.get(listUrls[i], function(response) {
            response.pipe(file);
        });

    } else if (listUrls[i].includes('http')) {
        const request = http.get(listUrls[i], function(response) {
            response.pipe(file);
        });

    } else {
        console.log('Not Valid', listUrls[i]) 
    }
}

console.log('Downloading...\n*It may take some time.*')
