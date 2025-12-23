/**
 * ARCHIVO: script.js
 * DESCRIPCIÓN: Gestiona la interactividad del frontend, validaciones y efectos de navegación.
 * ESTUDIANTE: Iván Salazar
 */

document.addEventListener('DOMContentLoaded', function () {

    /* ==========================================================
       1. VALIDACIÓN DEL FORMULARIO DE CONTACTO
       ========================================================== */
    const form = document.querySelector('form');

    if (form) {
        form.addEventListener('submit', function (e) {
            // Captura de valores eliminando espacios en blanco innecesarios
            const nombre = document.getElementById('nombre').value.trim();
            const email = document.getElementById('email').value.trim();
            const mensaje = document.getElementById('mensaje').value.trim();
            let errores = [];

            // Validación de longitud del nombre
            if (nombre.length > 0 && nombre.length < 3) {
                errores.push("El nombre debe tener al menos 3 caracteres.");
            }

            // Validación de formato de correo mediante Expresión Regular (RegEx)
            const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!regexEmail.test(email)) {
                errores.push("Por favor, ingresa un correo electrónico válido.");
            }

            // Validación de longitud del mensaje (mínimo 10 caracteres)
            if (mensaje.length < 10) {
                errores.push("El mensaje es demasiado corto (mínimo 10 caracteres).");
            }

            // Si existen errores, se detiene el envío y se notifican al usuario
            if (errores.length > 0) {
                e.preventDefault(); // Evita que el formulario se envíe al servidor
                alert(errores.join("\n"));
            }
        });
    }

    /* ==========================================================
       2. FUNCIONALIDAD DEL BOTÓN "IR ARRIBA" (SCROLL TOP)
       ========================================================== */
    const btnArriba = document.getElementById('btnArriba');

    if (btnArriba) {
        // Detecta el movimiento del scroll en la ventana
        window.addEventListener('scroll', () => {
            // El botón aparece si el usuario baja más de 200 píxeles
            if (window.scrollY > 200) {
                btnArriba.classList.add('visible');
            } else {
                btnArriba.classList.remove('visible');
            }
        });

        // Evento click para subir suavemente al inicio
        btnArriba.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth' // Desplazamiento animado
            });
        });
    }

    /* ==========================================================
       3. TRANSICIÓN DE SALIDA (EFECTO FADE-OUT)
       ========================================================== */
    // Seleccionamos todos los enlaces que lleven a páginas HTML
    document.querySelectorAll('a').forEach(link => {
        const href = link.getAttribute('href');
        
        if (href && href.endsWith('.html')) {
            link.addEventListener('click', e => {
                const destino = link.href;

                // Si el enlace no es a la misma página, aplicamos animación
                if (!destino.includes('#')) {
                    e.preventDefault(); // Pausamos la navegación instantánea
                    document.body.style.opacity = 0; // Efecto visual de desvanecimiento
                    
                    // Esperamos 300ms (lo que dura la transición CSS) antes de cambiar de página
                    setTimeout(() => {
                        window.location.href = destino;
                    }, 300);
                }
            });
        }
    });

}); // Fin del evento DOMContentLoaded