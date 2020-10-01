import {deleteCookie, setCookie} from "./cookies";

export function loggedSuccessfully(t) {
    console.log(t);
    setCookie('token', t);
    window.location.replace('/')
}

export function loginFailed() {
    console.log("to delete");
    deleteCookie('token');
}