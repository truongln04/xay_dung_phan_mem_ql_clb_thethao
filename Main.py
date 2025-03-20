import subprocess
import sys
import os
from PyQt6 import QtCore, QtGui, QtWidgets
import ThongTin_TK
import thanhvien
import hoadon
import loptap
import huanluyenvien
import caulacbo
import taikhoan
import dangkilop
import gioithieu
import thongke

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)

        self.user_id = None
        self.user_role = None

        if len(sys.argv) > 2:
            self.user_id = sys.argv[1]
            self.user_role = sys.argv[2]
            print(f"Đã nhận: user_id={self.user_id}, role={self.user_role}")

        MainWindow.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC);
            }
            QPushButton {
                background-color: #4A90E2;
                color: #FFFFFF;
                font-weight: bold;
                border: 1px solid #357ABD;
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #357ABD;
                color: #FFFFFF;
                border: 2px solid #4A90E2;
            }
            QPushButton:disabled {
                background-color: #D3D3D3;
                color: #A9A9A9;
                border: 1px solid #A9A9A9;
            }
            QWidget#sidebar {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4A90E2, stop:1 #357ABD);
            }
            QLabel#titleLabel {
                font-size: 24px;
                font-weight: bold;
                color: #357ABD;
            }
        """)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.listView = QtWidgets.QListView(parent=MainWindow)
        self.listView.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.listView.setObjectName("listView")

        self.btnThanhVien = QtWidgets.QPushButton(parent=MainWindow)
        self.btnThanhVien.setGeometry(QtCore.QRect(730, 100, 130, 225))
        self.btnThanhVien.setFont(font)
        self.btnThanhVien.setObjectName("btnThanhVien")

        self.btnNhanVien = QtWidgets.QPushButton(parent=MainWindow)
        self.btnNhanVien.setGeometry(QtCore.QRect(240, 100, 130, 225))
        self.btnNhanVien.setFont(font)
        self.btnNhanVien.setObjectName("btnNhanVien")

        self.btnCLB = QtWidgets.QPushButton(parent=MainWindow)
        self.btnCLB.setGeometry(QtCore.QRect(410, 100, 130, 225))
        self.btnCLB.setFont(font)
        self.btnCLB.setObjectName("btnCLB")

        self.btnThongKe = QtWidgets.QPushButton(parent=MainWindow)
        self.btnThongKe.setGeometry(QtCore.QRect(730, 350, 130, 225))
        self.btnThongKe.setFont(font)
        self.btnThongKe.setObjectName("btnThongKe")

        self.btnDangKy = QtWidgets.QPushButton(parent=MainWindow)
        self.btnDangKy.setGeometry(QtCore.QRect(410, 350, 130, 225))
        self.btnDangKy.setFont(font)
        self.btnDangKy.setObjectName("btnDangKy")

        self.btnHoaDon = QtWidgets.QPushButton(parent=MainWindow)
        self.btnHoaDon.setGeometry(QtCore.QRect(570, 350, 130, 225))
        self.btnHoaDon.setFont(font)
        self.btnHoaDon.setObjectName("btnHoaDon")

        self.btnHLV = QtWidgets.QPushButton(parent=MainWindow)
        self.btnHLV.setGeometry(QtCore.QRect(570, 100, 130, 225))
        self.btnHLV.setFont(font)
        self.btnHLV.setObjectName("btnHLV")

        self.btnLopTap = QtWidgets.QPushButton(parent=MainWindow)
        self.btnLopTap.setGeometry(QtCore.QRect(240, 350, 130, 225))
        self.btnLopTap.setFont(font)
        self.btnLopTap.setObjectName("btnLopTap")

        self.sidebar = QtWidgets.QWidget(parent=MainWindow)
        self.sidebar.setGeometry(QtCore.QRect(0, 0, 200, 600))
        self.sidebar.setObjectName("sidebar")

        self.btnAccount = QtWidgets.QPushButton(parent=self.sidebar)
        self.btnAccount.setGeometry(QtCore.QRect(40, 150, 120, 40))
        self.btnAccount.setFont(font)
        self.btnAccount.setObjectName("btnAccount")

        self.btnAbout = QtWidgets.QPushButton(parent=self.sidebar)
        self.btnAbout.setGeometry(QtCore.QRect(40, 200, 120, 40))
        self.btnAbout.setFont(font)
        self.btnAbout.setObjectName("btnAbout")

        self.btnLogout = QtWidgets.QPushButton(parent=self.sidebar)
        self.btnLogout.setGeometry(QtCore.QRect(40, 250, 120, 40))
        self.btnLogout.setFont(font)
        self.btnLogout.setObjectName("btnLogout")

        self.titleLabel = QtWidgets.QLabel(parent=MainWindow)
        self.titleLabel.setGeometry(QtCore.QRect(360, 20, 400, 50))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.windows = []
        self.ui_instances = []

        self.btnAccount.clicked.connect(self.openThongTinTK)
        self.btnAbout.clicked.connect(self.openAbout)
        self.btnThanhVien.clicked.connect(self.openThanhVien)
        self.btnNhanVien.clicked.connect(self.openNhanVien)
        self.btnCLB.clicked.connect(self.openCLB)
        self.btnHoaDon.clicked.connect(self.openHoaDon)
        self.btnHLV.clicked.connect(self.openHuanLuyenVien)
        self.btnThongKe.clicked.connect(self.openThongKe)
        self.btnDangKy.clicked.connect(self.openDangKyLop)
        self.btnLopTap.clicked.connect(self.openLopTap)
        self.btnLogout.clicked.connect(self.logout)

        self.retranslateUi(MainWindow)
        self.apply_permissions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quản lý Câu lạc bộ Thể thao"))
        self.btnThanhVien.setText(_translate("MainWindow", "Thành viên"))
        self.btnNhanVien.setText(_translate("MainWindow", "Nhân viên"))
        self.btnCLB.setText(_translate("MainWindow", "Câu lạc bộ"))
        self.btnThongKe.setText(_translate("MainWindow", "Thống kê"))
        self.btnDangKy.setText(_translate("MainWindow", "Đăng ký lớp"))
        self.titleLabel.setText(_translate("MainWindow", "QUẢN LÝ CÂU LẠC BỘ THỂ THAO"))
        self.btnHoaDon.setText(_translate("MainWindow", "Hóa đơn"))
        self.btnHLV.setText(_translate("MainWindow", "Huấn luyện viên"))
        self.btnAccount.setText(_translate("MainWindow", "Tài khoản"))
        self.btnAbout.setText(_translate("MainWindow", "Giới thiệu"))
        self.btnLogout.setText(_translate("MainWindow", "Đăng xuất"))
        self.btnLopTap.setText(_translate("MainWindow", "Lớp tập"))

    def apply_permissions(self):
        if not self.user_role:
            QtWidgets.QMessageBox.critical(self.MainWindow, "Lỗi", "Không xác định được vai trò người dùng!")
            return
        if self.user_role.lower() == "admin":
            print("Đăng nhập với vai trò Admin")
        elif self.user_role.lower() == "nhanvien":
            self.btnThongKe.setEnabled(False)
            self.btnNhanVien.setEnabled(False)
            print("Đăng nhập với vai trò Nhân viên")
        else:
            QtWidgets.QMessageBox.critical(self.MainWindow, "Lỗi", "Vai trò không hợp lệ!")
            self.logout()

    def _open_new_window(self, ui_class, user_id=None):
        try:
            print(f"Đang cố gắng mở form: {ui_class.__name__}")
            new_window = QtWidgets.QMainWindow()
            print("Đã tạo cửa sổ mới")
            ui = ui_class(user_id) if user_id else ui_class()  # Truyền user_id nếu có
            print("Đã tạo instance UI")
            ui.setupUi(new_window)
            print("Đã gọi setupUi")
            new_window.show()
            print("Đã hiển thị cửa sổ")
            self.windows.append(new_window)
            self.ui_instances.append(ui)
            print(f"Đã mở thành công form: {ui_class.__name__}")
        except Exception as e:
            error_msg = f"Không thể mở form {ui_class.__name__}: {str(e)}"
            QtWidgets.QMessageBox.critical(self.MainWindow, "Lỗi", error_msg)
            print(f"Lỗi: {error_msg}")

    def openThongTinTK(self):
        self._open_new_window(ThongTin_TK.Ui_AccountWindow, self.user_id)

    def openThanhVien(self):
        self._open_new_window(thanhvien.Ui_MainWindow)

    def openNhanVien(self):
        self._open_new_window(taikhoan.Ui_MainWindow)

    def openCLB(self):
        self._open_new_window(caulacbo.Ui_MainWindow)

    def openHoaDon(self):
        self._open_new_window(hoadon.Ui_MainWindow)

    def openHuanLuyenVien(self):
        self._open_new_window(huanluyenvien.Ui_MainWindow)

    def openThongKe(self):
        self._open_new_window(thongke.Ui_MainWindow)

    def openDangKyLop(self):
        self._open_new_window(dangkilop.Ui_MainWindow)

    def openLopTap(self):
        self._open_new_window(loptap.Ui_MainWindow)

    def openAbout(self):
        self._open_new_window(gioithieu.Ui_AboutWindow)

    def logout(self):
        try:
            QtWidgets.QApplication.quit()
            subprocess.Popen(["python", "DangNhap.py"])
            print("Đã đăng xuất thành công")
        except Exception as e:
            error_msg = f"Lỗi khi đăng xuất: {str(e)}"
            QtWidgets.QMessageBox.critical(self.MainWindow, "Lỗi", error_msg)
            print(f"Lỗi khi đăng xuất: {error_msg}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())