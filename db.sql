-- ========================================
-- Base de datos del proyecto IDWEB
-- ========================================

DROP DATABASE IF EXISTS idweb_proyecto;
CREATE DATABASE idweb_proyecto
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE idweb_proyecto;

-- ========================================
-- Tabla de mensajes del formulario
-- ========================================

CREATE TABLE mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    mensaje TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
