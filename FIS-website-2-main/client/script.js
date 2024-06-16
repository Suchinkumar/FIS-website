async function registerSubmit() {
    let form = document.getElementById('register');
    let formData = new FormData(form);
    let userName = formData.get('user_id'); 
    let password = formData.get('password');
    let email = formData.get('email');
    let data = { userName, password, email }; 
    await fetch("http://localhost:5000/register", {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(data)
    }).then(response => response.json()) 
      .then(data => {
          document.getElementById("alert-box").style.visibility = "visible";
          document.getElementById("alert-box-text").innerHTML = JSON.stringify(data.message);
      });
}

async function loginSubmit() {
    let form = document.getElementById('login');
    let formData = new FormData(form);
    let userName = formData.get('user_id');
    let password = formData.get('password');
    let data = { userName, password };
    await fetch("http://localhost:5000/login", {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
      .then(data => {
          document.getElementById("alert-box").style.visibility = "visible";
          document.getElementById("alert-box-text").innerHTML = JSON.stringify(data.message);
      });
}


document.querySelectorAll("#login-btn, #register-btn, #login-submit-btn, #register-submit-btn, #close-button").forEach(button => {
    button.addEventListener("click", function() {
        switch (this.id) {
            case "login-btn":
                login();
                break;
            case "register-btn":
                register();
                break;
            case "login-submit-btn":
                loginSubmit();
                break;
            case "register-submit-btn":
                registerSubmit();
                break;
            case "close-button":
                closeButton();
                break;
        }
    });
});

function closeButton() {
    console.log("Closing alert box");
    document.getElementById("alert-box").style.visibility = "hidden";
}

function register() {
    let x = document.getElementById("login");
    let y = document.getElementById("register");
    let z = document.getElementById("btn");
    x.style.left = "-400px";
    y.style.left = "50px";
    z.style.left = "110px";
}

function login() {
    let x = document.getElementById("login");
    let y = document.getElementById("register");
    let z = document.getElementById("btn");
    x.style.left = "50px";
    y.style.left = "450px"; 
    z.style.left = "0px";
}