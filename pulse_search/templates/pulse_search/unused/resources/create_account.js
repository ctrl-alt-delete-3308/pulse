var lowerCaseLetters = /[a-z]/g;
var upperCaseLetters = /[A-Z]/g;
var numbers = /[0-9]/g;
var symbols = /[!@#$%^&*(),.?":{}|<>]/g;

function validateEmail(email){
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function validatePassword(user_pass1, user_pass2){
  var pass = true;
  if(!lowerCaseLetters.test(user_pass1)) {pass = false;}
  if(!upperCaseLetters.test(user_pass1)) {pass = false;}
  if(!numbers.test(user_pass1)) {pass = false;}
  if(!symbols.test(user_pass1)) {pass = false;}
  if(!(user_pass1.length > 0)) {pass = false;}
  if(!(user_pass1.length < 16)) {pass = false;}

  if(!pass){
    alert("Password minimum length is 8 characters and must contain a number, symbol, uppercase and lowercase letter. It cannot exceed 15 characters");
    return false;
  }
  pass = (user_pass1==user_pass2)? pass : false;
  if(!pass){
    alert("Passwords did not match!");
    return false;
  }
  return true;
}

function register(){
  first_name = document.getElementById("userFirstName").value;
  last_name = document.getElementById("userLastName").value;
  user_email = document.getElementById("userEmail").value;
  user_pass1 = document.getElementById("userPassword").value;
  user_pass2 = document.getElementById("userConfirmPassword").value;

  if(first_name.length==0 || first_name.length > 20){
    alert("Name should be between 0 and 20 characters");
    return;
  }
  if(last_name.length==0 || last_name.length > 20){
    alert("Name should be between 0 and 20 characters");
    return;
  }
  if(!validateEmail(user_email)){
    alert("Invalid email address!");
    return;
  }
  if(!validatePassword(user_pass1, user_pass2)){
    return;
  }

  //**HERE WE CAN ADD TO DATABASE**
}
