-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 13 Jan 2024 pada 10.22
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411259`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `astronot`
--

CREATE TABLE `astronot` (
  `nama` varchar(50) NOT NULL,
  `umur` int(20) NOT NULL,
  `warna_baju_luar` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `astronot`
--

INSERT INTO `astronot` (`nama`, `umur`, `warna_baju_luar`) VALUES
('Franco', 35, 'Merah'),
('Nana', 22, 'Pink'),
('Diggie', 25, 'Hijau'),
('Cici', 28, 'Biru');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengawas`
--

CREATE TABLE `pengawas` (
  `nama` varchar(50) NOT NULL,
  `umur` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pengawas`
--

INSERT INTO `pengawas` (`nama`, `umur`) VALUES
('Lord', 50),
('Gord', 45),
('Pharsha', 42),
('Nova', 38);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
