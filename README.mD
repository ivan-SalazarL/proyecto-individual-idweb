# APLICACIÓN WEB PERSONAL – IDWEB

## 1. Descripción general

Este proyecto corresponde a una **aplicación web personal** desarrollada como parte del curso **Introducción al Desarrollo Web (IDWEB)**.  
El objetivo principal es demostrar la integración entre **frontend, backend y base de datos**, utilizando tecnologías básicas vistas en clase y sin el uso de frameworks.

La aplicación consiste en un sitio web personal con distintas secciones temáticas y un formulario que permite a los usuarios enviar recomendaciones. Los datos enviados son procesados por un servidor web en Python, almacenados en una base de datos MySQL y consultados desde un área protegida con contraseña.

---

## 2. Tecnologías utilizadas

- **HTML5**: estructura de las páginas web  
- **CSS3**: estilos personalizados y uso de layouts  
- **JavaScript**: validación del formulario y efectos interactivos  
- **Python**: servidor web implementado con `http.server`  
- **MySQL**: almacenamiento de los mensajes enviados  

---

## 3. Estructura del proyecto

proyecto-individual-idweb-main  
│  
├── server.py  
├── index.html  
├── gustos.html  
├── juegos.html  
├── mascotas.html  
├── vida.html  
│  
├── css/  
│   └── estilos.css  
│  
├── js/  
│   └── script.js  
│  
├── img/  
│   └── imágenes del sitio  
│  
└── db.sql  

---

## 4. Funcionalidades principales

- Navegación entre **cinco páginas web** interconectadas  
- Aplicación de estilos personalizados en todo el sitio  
- Uso de layouts mediante grids y secciones  
- Validación del formulario de contacto con JavaScript  
- Botón interactivo para volver al inicio de la página  
- Servidor web desarrollado en Python puro  
- Procesamiento manual de peticiones GET y POST  
- Almacenamiento de datos del formulario en MySQL  
- Área privada protegida con contraseña para visualizar los mensajes recibidos  

---

## 5. Requisitos para ejecutar el proyecto

- **Python 3**  
- **MySQL** (WAMP, XAMPP o MySQL Server)  
- Navegador web moderno  

---

## 6. Configuración de la base de datos

1. Abrir **phpMyAdmin**  
2. Ejecutar el archivo `db.sql` incluido en el proyecto  
3. Se creará la base de datos `idweb_proyecto` y la tabla `mensajes`  

---

## 7. Ejecución del servidor

Desde la carpeta raíz del proyecto, ejecutar el siguiente comando:

python server.py  

El servidor se iniciará en la dirección:

http://localhost:8000  

---

## 8. Uso de la aplicación

1. Acceder a la página principal desde el navegador  
2. Navegar por las distintas secciones del sitio web  
3. En la sección **Historias que duelen**, enviar una recomendación mediante el formulario  
4. Los datos enviados se almacenan en la base de datos  
5. Acceder al área privada desde el botón disponible en la interfaz  
6. Ingresar la contraseña para visualizar los mensajes guardados  

---

## 9. Área protegida

La aplicación cuenta con un área privada protegida mediante una contraseña simple configurada en el servidor.  
Esta sección permite consultar los mensajes almacenados en la base de datos en formato de tabla.

---

## 10. Trabajo futuro

- Implementar mecanismos de autenticación más seguros  
- Permitir la edición o eliminación de mensajes  
- Mejorar el diseño del área administrativa  
- Separar frontend y backend en módulos independientes  

---

## 11. Conclusiones

Este proyecto permitió aplicar de manera práctica los conceptos fundamentales del desarrollo web, integrando frontend, backend y base de datos sin el uso de frameworks. El desarrollo manual del servidor facilitó la comprensión del flujo de datos y del funcionamiento interno de una aplicación web básica.

---

## 12. Autor

Iván Salazar  
Curso: Introducción al Desarrollo Web  
Universidad Nacional de San Agustín
