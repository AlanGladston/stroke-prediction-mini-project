function gotoPredict()
{
    var button = document.getElementById("but");
    button.addEventListener("click", function() {
    console.log("working");
    window.location.href = "/predict";
});
}