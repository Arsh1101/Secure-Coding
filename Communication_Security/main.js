//JavaScript: Front-End
function wrongCode() {
    //'password' is not encrypted.
    const password = "mySecretPassword";
    fetch("https://example.com/login.php?password=" + password).then(response => {
    console.log(response);
  })
  .catch(error => {
    console.error(error);
  });
}
//JavaScript: Front-End
function correctCode() {
    //We have to encrypt code before send it to server like using 'encodeURIComponent' functions.
    const password = "mySecretPassword";
    fetch("https://example.com/login.php?password=" + encodeURIComponent(password), { method: "POST",
    headers: {"Content-Type": "application/x-www-form-urlencoded"},
    body: "password=" + encodeURIComponent(password)}).then(response => {
    console.log(response);
  }).catch(error => {
    console.error(error);
  });
}