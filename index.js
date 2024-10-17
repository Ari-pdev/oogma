window.addEventListener("pywebview", function () {
  console.log("The event is ready, now running the function.");
  window.pywebview.api.dummy_func().then(function (result) {
    console.log(result);
  });
});
