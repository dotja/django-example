function showMeaning() {
  var x = document.getElementById("meaning");
  var y = document.getElementById("meaning_hidden");
  var z = document.getElementById("show_hide");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
    z.innerHTML = "H I D E";
  } else {
    x.style.display = "none";
    y.style.display = "block";
    z.innerHTML = "S H O W";
  }
}