async function request(url) {
    return await fetch(url).then(result => result.json());
}

async function requestPost(url,  body) {
    return await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
    }).then(result => result.json());
}

console.debug('requests module connected');
