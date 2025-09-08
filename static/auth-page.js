function showForm(formId) {
  const loginForm = document.getElementById("login-form");
  const registerForm = document.getElementById("register-form");
  const loginTab = document.getElementById("login-tab");
  const registerTab = document.getElementById("register-tab");

  if (formId === "login") {
    loginForm.classList.remove("hidden-form");
    registerForm.classList.add("hidden-form");
    loginTab.classList.add("tab-active");
    registerTab.classList.remove("tab-active");
  } else {
    loginForm.classList.add("hidden-form");
    registerForm.classList.remove("hidden-form");
    loginTab.classList.remove("tab-active");
    registerTab.classList.add("tab-active");
  }
}
