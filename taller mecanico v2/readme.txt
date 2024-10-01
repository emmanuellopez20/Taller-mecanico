CREATE TABLE IF NOT EXISTS usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    perfil VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);


CREATE TABLE IF NOT EXISTS vehiculos (
    matricula VARCHAR(20) PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

CREATE TABLE piezas (
    pieza_id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE reparaciones (
    reparacion_id INT AUTO_INCREMENT PRIMARY KEY,
    hora_entrada TIME NOT NULL,
    hora_salida TIME,
    fecha_entrada DATE NOT NULL,
    fecha_salida DATE,
    matricula VARCHAR(20) NOT NULL,
    cliente_id INT NOT NULL,
    tipo_servicio VARCHAR(255) NOT NULL,
    pieza_id INT,
    cantidad_piezas INT,
    FOREIGN KEY (matricula) REFERENCES vehiculos(matricula),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    FOREIGN KEY (pieza_id) REFERENCES piezas(pieza_id)
);
