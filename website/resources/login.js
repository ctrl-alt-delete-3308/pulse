var lowerCaseLetters = /[a-z]/g;
var upperCaseLetters = /[A-Z]/g;
var numbers = /[0-9]/g;
var symbols = /[!@#$%^&*(),.?":{}|<>]/g;


function validateEmail(email){
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function validatePassword(u_password){
  var pass = true;
  if(!lowerCaseLetters.test(u_password)) {pass = false;}
  if(!upperCaseLetters.test(u_password)) {pass = false;}
  if(!numbers.test(u_password)) {pass = false;}
  if(!symbols.test(u_password)) {pass = false;}
  if(!(u_password.length > 0)) {pass = false;}
  if(!(u_password.length < 16)) {pass = false;}

  if(!pass){ alert("password"); return false; }
  return true;
}

function userLogin(){
  u_username = document.getElementById("emailLogin").value;
  u_password = document.getElementById("passwordLogin").value;

  if(!validateEmail(u_username)){ alert("Invalid username!"); return; }
  if(!validatePassword(u_password)){ alert("Invalid username/password!"); return; }

  document.getElementById("emailLogin").value = "";
  document.getElementById("passwordLogin").value = "";

  //**HERE WE CAN CHECK AGAINST DATABASE**//
}
