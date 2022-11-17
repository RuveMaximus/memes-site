async function request(url) {
    return await fetch(url).then(result => result.json());
}

console.debug('requests module connected');
