CREATE DATABASE proyectopy;

USE proyectopy;

CREATE TABLE usuario1(
    id int PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30),
    apellido VARCHAR(30),
    saldo int(100),
    numerocuenta VARCHAR(15),
    clave VARCHAR(10)
);

USE proyectopy;
INSERT INTO usuario1(nombre,apellido,saldo,numerocuenta,clave) VALUES
('Alexander','Gonzales',70000,12345678910,'123456'),
('Daniel','Fernandez',50000,23456789101,'234567'),
('Angela','Maldonado',60500,34567891012,'345678'),
('Bryan','Mamani',70000,45678910123,'456789')

USE proyectopy;
SELECT * FROM usuario1;