function viewhide() {
    var d = document.getElementById("dep");
    var s = document.getElementById("stu")
    if (d.style.display === "none") {
      d.style.display = "block";
      s.style.display ="none";
    } else {
        s.style.display = "block";
        d.style.display ="none";
    }
  }