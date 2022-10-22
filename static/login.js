function depshow() {
    var d = document.getElementById("dep");
    var s = document.getElementById("stu");
    var f = document.getElementById('fac');
    var st = document.getElementById('staf');
    var a = document.getElementById('adm');
    d.style.display = "block";
    s.style.display = "none";
    f.style.display = "none";
    st.style.display = "none";
    a.style.display = "none";
}

function stushow() {
  var d = document.getElementById("dep");
  var s = document.getElementById("stu");
  var f = document.getElementById('fac');
  var st = document.getElementById('staf');
  var a = document.getElementById('adm');
  d.style.display = "none";
  s.style.display = "block";
  f.style.display = "none";
  st.style.display = "none";
  a.style.display = "none";
}

function staffshow() {
  var d = document.getElementById("dep");
  var s = document.getElementById("stu");
  var f = document.getElementById('fac');
  var st = document.getElementById('staf');
  var a = document.getElementById('adm');
  
  d.style.display = "none";
  s.style.display = "none";
  f.style.display = "none";
  st.style.display = "block";
  a.style.display = "none";
}

function facshow() {
  var d = document.getElementById("dep");
  var s = document.getElementById("stu");
  var f = document.getElementById('fac');
  var st = document.getElementById('staf');
  var a = document.getElementById('adm');

  d.style.display = "none";
  s.style.display = "none";
  f.style.display = "block";
  st.style.display = "none";
  a.style.display = "none";
}

function admshow() {
  var d = document.getElementById("dep");
  var s = document.getElementById("stu");
  var f = document.getElementById('fac');
  var st = document.getElementById('staf');
  var a = document.getElementById('adm');
  
  d.style.display = "none";
  s.style.display = "none";
  f.style.display = "none";
  st.style.display = "none";
  a.style.display = "block";

}