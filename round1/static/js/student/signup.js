const passwordEl = document.querySelector("#pass1");
const form = document.querySelector("#signup");

form.addEventListener("submit", function (e) {
  // prevent the form from submitting
  e.preventDefault();
  let isConfirmPasswordValid = checkPassword();

  let isFormValid = isConfirmPasswordValid;

  // submit to the server if the form is valid
  if (isFormValid) {
    form.submit();
  }
});
const checkPassword = () => {
  let valid = false;

  const password = passwordEl.value.trim();

  if (!isPasswordSecure(password)) {
    showError(
      passwordEl,
      "Password must has at least 8 characters that include at least 1 lowercase character, 1 uppercase characters, 1 number, and 1 special character in (!@#$%^&*)"
    );
  } else {
    valid = true;
  }

  return valid;
};

const showError = (input, message) => {
  // get the form-field element
  const formField = input.parentElement;
  // add the error class
  input.style.border = "1px solid red";
  formField.classList.remove("success");
  formField.classList.add("error");

  // show the error message
  const error = formField.querySelector("small");
  error.textContent = message;
};

const isPasswordSecure = (password) => {
  const re = new RegExp(
    "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})"
  );
  return re.test(password);
};

function error_fun() {
  const err_msg = document.getElementById("err").innerHTML;
  var a = err_msg.replaceAll(`'`, `"`);
  const b = JSON.parse(a);
  for (i in b) {
    const res_err = document.getElementById(i);
    const err_field = res_err.parentElement;
    res_err.style.border = "1px solid red";
    const error = err_field.querySelector("small");
    error.textContent = b[i];
  }
}
