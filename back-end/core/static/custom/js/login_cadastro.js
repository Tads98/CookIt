function loginOpen() {
    document.getElementById("login-form").style.display = "block";
    document.getElementById("cadastro-form").style.display = "none";
    document.getElementById("login-button").style.backgroundColor = "gray";
    document.getElementById("cadastro-button").style.backgroundColor = "lightgray";
}

function cadastroOpen() {
    document.getElementById("login-form").style.display = "none";
    document.getElementById("cadastro-form").style.display = "block";
    document.getElementById("login-button").style.backgroundColor = "lightgray";
    document.getElementById("cadastro-button").style.backgroundColor = "gray";
}