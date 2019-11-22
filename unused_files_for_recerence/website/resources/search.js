// window.location.href = "display_results.html?term="+value;

function searching(){
  window.location.href = "display_results.html?term="+document.getElementById("searchTerm").value;;
}

//FUNCTION TO GET THE ARGUMENTS IN THE URL, pass the argument you want. For seach, param = term
function ParseURLParameter(param){
  var fullURL = window.location.search.substring(1);
  var paramArray = fullURL.split('&');
  for(var i = 0; i < paramArray.length; i++){
    var currentParam = paramArray[i].split('=');
    if(currentParam[0] == param){
      // alert(currentParam[1]);
      document.getElementById("p_search").innerHTML = "<font color=\"505356\">showing results for '"+currentParam[1]+"'</font>";
      return currentParam[1];
    }
  }
}
