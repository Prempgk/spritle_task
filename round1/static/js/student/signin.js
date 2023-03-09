function error_fun() {
    const err_msg = document.getElementById("err").innerHTML;
    var a = err_msg.replaceAll(`'`, `"`);
    const err_data = JSON.parse(a);
    for (i in err_data) {
      const res_err = document.getElementById(i);
      const err_field = res_err.parentElement;
      res_err.style.border = "1px solid red";
      const error = err_field.querySelector("small");
      error.textContent = err_data[i];
    }
  }
