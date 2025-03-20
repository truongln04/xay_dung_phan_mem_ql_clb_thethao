CREATE DATABASE QL_CLB_THE_THAO_CHUAN;
USE QL_CLB_THE_THAO_CHUAN;
SELECT * FROM TaiKhoan;
-- Bảng Câu Lạc Bộ
CREATE TABLE CauLacBo (
    ma_clb VARCHAR(100) PRIMARY KEY,
    ten_clb VARCHAR(100) NOT NULL,
    dia_chi TEXT NOT NULL,
    mo_ta TEXT NULL
);

-- Bảng Tài Khoản (Admin & Nhân Viên)
CREATE TABLE TaiKhoan (
    ma_tk VARCHAR(100) PRIMARY KEY,
    ten_dang_nhap VARCHAR(50) UNIQUE NOT NULL,
    mat_khau VARCHAR(255) NOT NULL,
    ho_ten VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    vai_tro ENUM('admin', 'nhanvien') NOT NULL,
    ma_clb VARCHAR(100) NULL,
    FOREIGN KEY (ma_clb) REFERENCES CauLacBo(ma_clb) ON DELETE SET NULL
);

-- Bảng Thành Viên
CREATE TABLE ThanhVien (
    ma_tv VARCHAR(100) PRIMARY KEY,
    ho_ten VARCHAR(100) NOT NULL,
    ngay_sinh DATE NOT NULL,
    gioi_tinh ENUM('Nam', 'Nữ', 'Khác') NOT NULL,
    sdt VARCHAR(15) NOT NULL,
    dia_chi TEXT NOT NULL,
    ma_clb VARCHAR(100) NOT NULL,
    FOREIGN KEY (ma_clb) REFERENCES CauLacBo(ma_clb) ON DELETE CASCADE
);

-- Bảng Huấn Luyện Viên (HLV)
CREATE TABLE HuanLuyenVien (
    ma_hlv VARCHAR(100) PRIMARY KEY,
    ho_ten VARCHAR(100) NOT NULL,
    chuyen_mon VARCHAR(100) NOT NULL,
    ngay_sinh DATE NOT NULL,
    gioi_tinh ENUM('Nam', 'Nữ', 'Khác') NOT NULL,
    sdt VARCHAR(15) NOT NULL,
    ma_clb VARCHAR(100) NOT NULL,
    FOREIGN KEY (ma_clb) REFERENCES CauLacBo(ma_clb) ON DELETE CASCADE
);

-- Bảng Lớp Tập
CREATE TABLE LopTap (
    ma_lop VARCHAR(100) PRIMARY KEY,
    ten_lop VARCHAR(100) NOT NULL,
    ma_clb VARCHAR(100) NOT NULL,
    ma_hlv VARCHAR(100) NOT NULL,
    hoc_phi DECIMAL(10,2) NOT NULL DEFAULT 0,
    ngay_bat_dau DATE NOT NULL,
    ngay_ket_thuc DATE NULL,
    FOREIGN KEY (ma_clb) REFERENCES CauLacBo(ma_clb) ON DELETE CASCADE,
    FOREIGN KEY (ma_hlv) REFERENCES HuanLuyenVien(ma_hlv) ON DELETE CASCADE
);

-- Bảng Đăng Ký Lớp
CREATE TABLE DangKyLop (
    ma_dk VARCHAR(100) PRIMARY KEY,
    ma_tv VARCHAR(100) NOT NULL,
    ma_lop VARCHAR(100) NOT NULL,
    ngay_dang_ky TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ma_tv) REFERENCES ThanhVien(ma_tv) ON DELETE CASCADE,
    FOREIGN KEY (ma_lop) REFERENCES LopTap(ma_lop) ON DELETE CASCADE
);

-- Bảng Hóa Đơn (Thanh Toán)
CREATE TABLE HoaDon (
    ma_hd VARCHAR(100) PRIMARY KEY,
    ma_tv VARCHAR(100) NOT NULL,
    ma_lop VARCHAR(100) NOT NULL,
    so_tien DECIMAL(10,2) NOT NULL,
    trang_thai ENUM('Chưa thanh toán', 'Đã thanh toán') DEFAULT 'Chưa thanh toán',
    ngay_thanh_toan DATE NULL,
    FOREIGN KEY (ma_tv) REFERENCES ThanhVien(ma_tv) ON DELETE CASCADE,
    FOREIGN KEY (ma_lop) REFERENCES LopTap(ma_lop) ON DELETE CASCADE
);
