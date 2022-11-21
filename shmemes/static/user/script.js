async function login() {
    const user_login = document.getElementById('username');
    const user_password = document.getElementById('password'); 

    const response = await requestPost('/user/api/login/', {'username': user_login.value, 'password': user_password.value});

    console.log(response.status);

    if (response.status === 'ok') {
        document.location.href = '/feed/';
    }
}


async function register() {
    const user_login = document.getElementById('username');
    const user_password = document.getElementById('password'); 
    
    const response = await requestPost('/user/api/register/', {'username': user_login.value, 'password': user_password.value});

    console.log(response.status);
    
    if (response.status === 'ok') {
        document.location.href = '/user/login/';
    }
}