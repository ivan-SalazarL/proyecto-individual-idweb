document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');

  if (form) {
    form.addEventListener('submit', function (evento) {
      const nombre = document.getElementById('nombre').value.trim();
      const email = document.getElementById('email').value.trim();
      const mensaje = document.getElementById('mensaje').value.trim();

      const errores = [];

      if (nombre.length > 0 && nombre.length < 3) {
        errores.push('El nombre debe tener al menos 3 caracteres.');
      }

      const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!regexEmail.test(email)) {
        errores.push('Correo electrónico inválido.');
      }

      if (mensaje.length < 10) {
        errores.push('El mensaje debe tener al menos 10 caracteres.');
      }

      if (errores.length > 0) {
        evento.preventDefault();
        alert('Revisa lo siguiente:\n\n' + errores.join('\n'));
      }

    });
  }

  const btnArriba = document.getElementById('btnArriba');

  if (btnArriba) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 200) {
        btnArriba.classList.add('visible');
      } else {
        btnArriba.classList.remove('visible');
      }
    });

    btnArriba.addEventListener('click', function () {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});
