-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-08-2025 a las 00:03:27
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyectosena`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inspeccion`
--

CREATE TABLE `inspeccion` (
  `id` int(11) NOT NULL,
  `observaciones` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lote`
--

CREATE TABLE `lote` (
  `id` int(11) NOT NULL,
  `tipodegrano` varchar(50) NOT NULL,
  `procedencia` varchar(50) NOT NULL,
  `fecha` date DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parametro`
--

CREATE TABLE `parametro` (
  `id` int(11) NOT NULL,
  `rnombre` varchar(100) NOT NULL,
  `unidad_medida` int(11) NOT NULL,
  `valor_min` int(40) NOT NULL,
  `valor_max` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reporte`
--

CREATE TABLE `reporte` (
  `id` int(11) NOT NULL,
  `rutaarchivo` varchar(100) NOT NULL,
  `id_inspeccion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultado`
--

CREATE TABLE `resultado` (
  `id` int(11) NOT NULL,
  `valormedido` varchar(100) NOT NULL,
  `id_inspeccion` int(11) NOT NULL,
  `id_parametro` int(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id`, `nombre`) VALUES
(1, 'Administrador de base de datos'),
(2, 'Operario de maquina separadora'),
(3, 'Analista de inventario'),
(4, 'Inspector de calidad'),
(5, 'Supervisor de produccion'),
(6, 'Tecnico de mantenimiento'),
(7, 'Jefe de seguridad industrial'),
(8, 'Auxiliar de bodega'),
(9, 'Encargado de empaque'),
(10, 'Gerente de planta'),
(11, 'Encargado de logistica'),
(12, 'Analista de inventario'),
(13, 'Coordinador de calidad'),
(14, 'Gerente de operaciones'),
(15, 'Especialista en trazabilidad'),
(16, 'Desarrollador de Software'),
(17, 'Ingeniero de automatizacion'),
(18, 'Soporte tecnico de software'),
(19, 'Especialista en ciberseguridad'),
(20, 'Ingeniero de IoT');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `contra` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `rol` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `contra`, `email`, `rol`) VALUES
(1, 'Juan', 'Mozuca', 'mcsoddisds', 'juanito@gmail.com', 1),
(2, 'Sebastian', 'Murcia', 'wipereori', 'sebastian@gmail.com', 2),
(3, 'Nicolas', 'Ruiz', 'eeyeyeye', 'nicolas34@gmail.com', 3),
(4, 'Mateo', 'Ruiz', 'tjfggsddzhffn', 'mateit@gmsil.com', 4),
(5, 'Felipe', 'Hernandez', 'bdfbdbnd', 'felip@gmail.com', 5),
(6, 'Andres', 'Gomez', 'vuhnuhi', 'andrs@gmail.com', 6),
(7, 'Jonathan', 'Anzola', 'jhnm?', 'jhonat@gmail.com', 7),
(8, 'Jhon', 'Suarez', 'bkjkjhh', 'jhon@gmail.com', 8),
(9, 'Sara', 'Sanchez', 'ssxxfd', 'Shar@gmail.com', 10),
(11, 'Sara', 'Sanchez', 'ssxxfd', 'Shara@gmail.com', 11),
(12, 'Sofia', 'Acevedo', 'ytugygyg', 'Sfia@gmail.com', 12),
(13, 'Kevin', 'Murcia', 'tftyfyfyt', 'Kevinj@gmail.com', 13),
(14, 'Santiago', 'Rojas', 'utyuyuu', 'Santi@gmail.com', 14),
(15, 'Pablo', 'daza', 'futftwef', 'Pablo@gmail.com', 15),
(16, 'Ivan', 'Palacios', 'yggyh', 'Ivan@gmail.com', 16),
(17, 'Alfredo', 'Castillo', 'afryafsa', 'Alfredo@gmail.com', 17),
(18, 'Johan', 'Castro', 'gydggydy', 'Johan@gmail.com', 18),
(19, 'Michael', 'Leon', 'teatfwayfts', 'Michael@gmail.com', 19),
(20, 'Duban', 'Pozada', 'drdsacrw', 'Duban@gmail.com', 20);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `inspeccion`
--
ALTER TABLE `inspeccion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `lote`
--
ALTER TABLE `lote`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indices de la tabla `parametro`
--
ALTER TABLE `parametro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `reporte`
--
ALTER TABLE `reporte`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `resultado`
--
ALTER TABLE `resultado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `rol` (`rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `inspeccion`
--
ALTER TABLE `inspeccion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `lote`
--
ALTER TABLE `lote`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `parametro`
--
ALTER TABLE `parametro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reporte`
--
ALTER TABLE `reporte`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `resultado`
--
ALTER TABLE `resultado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `rol` FOREIGN KEY (`rol`) REFERENCES `rol` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
