-- ==========================================================
-- ESTRUCTURA DE LA BASE DE DATOS - PROYECTO IDWEB
-- DESCRIPCIÓN: Creación de esquema y tablas para persistencia
-- AUTOR: Iván Salazar
-- ==========================================================

-- 1. Limpieza de entorno: Borra la base de datos si ya existe para evitar conflictos en la instalación
DROP DATABASE IF EXISTS idweb_proyecto;

-- 2. Creación de la base de datos con soporte para caracteres especiales (emojis, tildes, etc.)
CREATE DATABASE idweb_proyecto
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

-- 3. Selección de la base de datos para las operaciones siguientes
USE idweb_proyecto;


CREATE TABLE mensajes (
    -- Identificador único para cada mensaje, se incrementa automáticamente
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Nombre del remitente (máximo 100 caracteres)
    nombre VARCHAR(100) NOT NULL,
    
    -- Correo electrónico validado previamente en el frontend
    email VARCHAR(150) NOT NULL,
    
    -- El mensaje completo, usamos TEXT por si el contenido es extenso
    mensaje TEXT NOT NULL,
    
    -- Registro automático de la fecha y hora exacta del envío
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================================
-- NOTAS TÉCNICAS:
-- El motor de almacenamiento predeterminado será InnoDB, 
-- garantizando la integridad referencial y transacciones.
-- ==========================================================