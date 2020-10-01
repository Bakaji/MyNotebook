export function setCookie(cookie_name, cookie_value, expires_days) {
    const d = new Date();
    d.setTime(d.getTime() + (expires_days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + d.toUTCString();
    document.cookie = cookie_name + "=" + cookie_value + ";" + expires + ";path=/";
}

export function deleteCookie(cookie_name) {
    const d = new Date();
    d.setTime(d.getTime() - (24 * 60 * 60 * 1000));
    const expires = "expires=" + d.toUTCString();
    document.cookie = cookie_name + "=" + ";" + expires + ";path=/";
}
