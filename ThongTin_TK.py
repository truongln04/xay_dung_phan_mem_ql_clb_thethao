from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Database.data import get_db_connection  # Giả định đây là module kết nối MySQL

class Ui_AccountWindow(object):
    def __init__(self, user_id=None):  # Thêm tham số user_id
        self.user_id = user_id

    def setupUi(self, AccountWindow):
        self.AccountWindow = AccountWindow
        AccountWindow.setObjectName("AccountWindow")
        AccountWindow.resize(400, 350)
        AccountWindow.setStyleSheet("""
            QPushButton {
                background-color: #4A90E2;
                color: #FFFFFF;
                font-weight: bold;
                border: 1px solid #357ABD;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #357ABD;
                color: #FFFFFF;
                border: 2px solid #4A90E2;
            }
            QLabel#titleLabel {
                font-size: 20px;
                font-weight: bold;
                color: #357ABD;
            }
            QWidget {
                color: #333333;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 1px solid #B0B0B0;
                border-radius: 3px;
                padding: 2px;
            }
            QLineEdit:disabled {
                background-color: #E0E0E0;
                color: #666666;
            }
            QComboBox {
                background-color: #FFFFFF;
                color: #333333;
                border: 1px solid #B0B0B0;
                border-radius: 3px;
                padding: 2px;
            }
            QGroupBox {
                font-weight: bold;
                color: #357ABD;
            }
            QTableWidget {
                background-color: #FFFFFF;
                color: #333333;
                border: 1px solid #B0B0B0;
            }
            QTableWidget::item:selected {
                background-color: #4A90E2;
                color: #FFFFFF;
            }
        """)
        self.listView = QtWidgets.QListView(parent=AccountWindow)
        self.listView.setGeometry(QtCore.QRect(0, 0, 401, 351))
        self.listView.setStyleSheet(
            "QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC); }")
        self.listView.setObjectName("listView")

        self.txtRole = QtWidgets.QLineEdit(parent=AccountWindow)
        self.txtRole.setGeometry(QtCore.QRect(170, 190, 200, 30))
        self.txtRole.setReadOnly(True)
        self.txtRole.setObjectName("txtRole")

        self.btnSave = QtWidgets.QPushButton(parent=AccountWindow)
        self.btnSave.setGeometry(QtCore.QRect(90, 299, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")

        self.lblUsername = QtWidgets.QLabel(parent=AccountWindow)
        self.lblUsername.setGeometry(QtCore.QRect(40, 70, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblUsername.setFont(font)
        self.lblUsername.setObjectName("lblUsername")

        self.txtPhone = QtWidgets.QLineEdit(parent=AccountWindow)
        self.txtPhone.setGeometry(QtCore.QRect(170, 150, 200, 30))
        self.txtPhone.setObjectName("txtPhone")

        self.lblFullName = QtWidgets.QLabel(parent=AccountWindow)
        self.lblFullName.setGeometry(QtCore.QRect(40, 110, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblFullName.setFont(font)
        self.lblFullName.setObjectName("lblFullName")

        self.txtMaCLB = QtWidgets.QLineEdit(parent=AccountWindow)
        self.txtMaCLB.setGeometry(QtCore.QRect(170, 230, 200, 30))
        self.txtMaCLB.setReadOnly(True)
        self.txtMaCLB.setObjectName("txtMaCLB")

        self.lblMaCLB = QtWidgets.QLabel(parent=AccountWindow)
        self.lblMaCLB.setGeometry(QtCore.QRect(40, 230, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblMaCLB.setFont(font)
        self.lblMaCLB.setObjectName("lblMaCLB")

        self.txtUsername = QtWidgets.QLineEdit(parent=AccountWindow)
        self.txtUsername.setGeometry(QtCore.QRect(170, 70, 200, 30))
        self.txtUsername.setReadOnly(True)
        self.txtUsername.setObjectName("txtUsername")

        self.titleLabel = QtWidgets.QLabel(parent=AccountWindow)
        self.titleLabel.setGeometry(QtCore.QRect(70, 10, 250, 50))
        font = QtGui.QFont()
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(
            "QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC); }")
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.txtFullName = QtWidgets.QLineEdit(parent=AccountWindow)
        self.txtFullName.setGeometry(QtCore.QRect(170, 110, 200, 30))
        self.txtFullName.setObjectName("txtFullName")

        self.lblRole = QtWidgets.QLabel(parent=AccountWindow)
        self.lblRole.setGeometry(QtCore.QRect(40, 190, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblRole.setFont(font)
        self.lblRole.setObjectName("lblRole")

        self.lblPhone = QtWidgets.QLabel(parent=AccountWindow)
        self.lblPhone.setGeometry(QtCore.QRect(40, 150, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblPhone.setFont(font)
        self.lblPhone.setObjectName("lblPhone")

        self.btnClose = QtWidgets.QPushButton(parent=AccountWindow)
        self.btnClose.setGeometry(QtCore.QRect(230, 299, 100, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(AccountWindow)
        self.load_user_info()

        self.btnSave.clicked.connect(self.save_changes)
        self.btnClose.clicked.connect(AccountWindow.close)

        QtCore.QMetaObject.connectSlotsByName(AccountWindow)

    def retranslateUi(self, AccountWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountWindow.setWindowTitle(_translate("AccountWindow", "Thông Tin Tài Khoản"))
        self.btnSave.setText(_translate("AccountWindow", "Lưu"))
        self.lblUsername.setText(_translate("AccountWindow", "Tên đăng nhập:"))
        self.lblFullName.setText(_translate("AccountWindow", "Họ và tên:"))
        self.lblMaCLB.setText(_translate("AccountWindow", "Mã CLB:"))
        self.titleLabel.setText(_translate("AccountWindow", "Thông tin tài khoản"))
        self.lblRole.setText(_translate("AccountWindow", "Vai trò:"))
        self.lblPhone.setText(_translate("AccountWindow", "Số điện thoại:"))
        self.btnClose.setText(_translate("AccountWindow", "Đóng"))

    def load_user_info(self):
        if not self.user_id:
            QMessageBox.critical(self.AccountWindow, "Lỗi", "Không xác định được mã người dùng!")
            return

        try:
            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(self.AccountWindow, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
                return
            cursor = connection.cursor()
            query = "SELECT ten_dang_nhap, ho_ten, email, vai_tro, ma_clb FROM taikhoan WHERE ma_tk = %s"
            cursor.execute(query, (self.user_id,))
            user_info = cursor.fetchone()

            if user_info:
                self.txtUsername.setText(user_info[0])
                self.txtFullName.setText(user_info[1] if user_info[1] else "")
                self.txtPhone.setText(user_info[2] if user_info[2] else "")
                self.txtRole.setText(user_info[3])
                self.txtMaCLB.setText(user_info[4] if user_info[4] else "")
            else:
                QMessageBox.warning(self.AccountWindow, "Lỗi", "Không tìm thấy thông tin tài khoản!")

            cursor.close()
            connection.close()
        except Exception as e:
            QMessageBox.critical(self.AccountWindow, "Lỗi", f"Không thể tải thông tin tài khoản: {str(e)}")

    def save_changes(self):
        try:
            full_name = self.txtFullName.text().strip()
            phone = self.txtPhone.text().strip()

            if not full_name or not phone:
                QMessageBox.warning(self.AccountWindow, "Lỗi", "Họ tên và số điện thoại không được để trống!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(self.AccountWindow, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
                return
            cursor = connection.cursor()

            cursor.execute("SELECT ma_tk FROM taikhoan WHERE email = %s AND ma_tk != %s", (phone, self.user_id))
            duplicate_phone = cursor.fetchone()
            if duplicate_phone:
                QMessageBox.warning(self.AccountWindow, "Lỗi", "Số điện thoại đã được sử dụng bởi tài khoản khác!")
                return

            query = "UPDATE taikhoan SET ho_ten = %s, email = %s WHERE ma_tk = %s"
            cursor.execute(query, (full_name, phone, self.user_id))
            connection.commit()

            QMessageBox.information(self.AccountWindow, "Thành công", "Cập nhật thông tin tài khoản thành công!")
            self.load_user_info()

            cursor.close()
            connection.close()
        except Exception as e:
            QMessageBox.critical(self.AccountWindow, "Lỗi", f"Không thể lưu thông tin: {str(e)}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountWindow = QtWidgets.QMainWindow()
    ui = Ui_AccountWindow("1")  # Truyền user_id mẫu khi chạy độc lập
    ui.setupUi(AccountWindow)
    AccountWindow.show()
    sys.exit(app.exec())