// document.getElementById('youridhere').scrollIntoView();
function scrollToHeart() {
    console.log("scrolling to heart");
    document.getElementById('heartViewId').scrollIntoView();
}
function scrollToKidney()
{
    console.log("scrolling to kidney");
    document.getElementById('kidneyViewId').scrollIntoView();
}

function predictkidney()
{
    input1 = document.getElementById('kidney-input-1').value;
    input2 = document.getElementById('kidney-input-2').value;
    input3 = document.getElementById('kidney-input-3').value;
    input4 = document.getElementById('kidney-input-4').value;
    input5 = document.getElementById('kidney-input-5').value;
    data = {"input1":input1, "input2":input2, "input3":input3, "input4":input4, "input5":input5}
    console.log(data)
    $.get( "http://127.0.0.1:8080/predict_kidney", data, function( result ) {
        console.log(result)
        document.getElementById("kidneyPredictionResult").innerHTML = result["prediction"]
});
}
function predict() {
    console.log("Predicting");
    input1 = document.getElementById('heart-input-1').value;
    input2 = document.getElementById('heart-input-2').value;
    input3 = document.getElementById('heart-input-3').value;
    input4 = document.getElementById('heart-input-4').value;
    input5 = document.getElementById('heart-input-5').value;
    data = {"input1":input1, "input2":input2, "input3":input3, "input4":input4, "input5":input5}
    console.log(data)
    $.get( "http://127.0.0.1:8080/predict_heart", data, function( result ) {
        console.log(result)
        document.getElementById("heartPredictionResult").innerHTML = result["prediction"]
    });
}