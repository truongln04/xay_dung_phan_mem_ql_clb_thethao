from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import subprocess
import sys
from Database.data import get_db_connection  # Import hàm kết nối MySQL

# Tạo QLabel có thể click
class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()  # Tạo signal khi nhấn vào QLabel

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()  # Phát tín hiệu khi QLabel được nhấn

class Ui_LoginWindow(object):
    current_user = None  # Biến lưu mã người dùng sau khi đăng nhập
    current_role = None  # Biến lưu vai trò người dùng

    def setupUi(self, LoginWindow):
        self.LoginWindow = LoginWindow  # Lưu tham chiếu đến LoginWindow
        self.LoginWindow.setObjectName("LoginWindow")
        self.LoginWindow.resize(435, 372)
        self.LoginWindow.setStyleSheet("""
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
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC);
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
        self.listView = QtWidgets.QListView(parent=self.LoginWindow)
        self.listView.setGeometry(QtCore.QRect(0, 0, 441, 371))
        self.listView.setStyleSheet("QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC); }")
        self.listView.setObjectName("listView")
        self.usernameLabel = QtWidgets.QLabel(parent=self.LoginWindow)
        self.usernameLabel.setGeometry(QtCore.QRect(30, 110, 101, 30))
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameInput = QtWidgets.QLineEdit(parent=self.LoginWindow)
        self.usernameInput.setGeometry(QtCore.QRect(139, 110, 241, 30))
        self.usernameInput.setObjectName("usernameInput")
        self.loginButton = QtWidgets.QPushButton(parent=self.LoginWindow)
        self.loginButton.setGeometry(QtCore.QRect(140, 270, 101, 41))
        self.loginButton.setObjectName("loginButton")
        self.titleLabel = QtWidgets.QLabel(parent=self.LoginWindow)
        self.titleLabel.setGeometry(QtCore.QRect(90, 30, 250, 50))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.passwordLabel = QtWidgets.QLabel(parent=self.LoginWindow)
        self.passwordLabel.setGeometry(QtCore.QRect(30, 160, 101, 30))
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordInput = QtWidgets.QLineEdit(parent=self.LoginWindow)
        self.passwordInput.setGeometry(QtCore.QRect(139, 160, 241, 30))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.showPasswordCheckbox = QtWidgets.QCheckBox(parent=self.LoginWindow)
        self.showPasswordCheckbox.setGeometry(QtCore.QRect(140, 200, 131, 20))
        self.showPasswordCheckbox.setObjectName("showPasswordCheckbox")
        self.exitButton = QtWidgets.QPushButton(parent=self.LoginWindow)
        self.exitButton.setGeometry(QtCore.QRect(270, 270, 101, 41))
        self.exitButton.setObjectName("exitButton")
        self.forgotPasswordLabel = ClickableLabel(parent=self.LoginWindow)
        self.forgotPasswordLabel.setGeometry(QtCore.QRect(280, 200, 101, 20))
        self.forgotPasswordLabel.setObjectName("forgotPasswordLabel")

        self.retranslateUi(self.LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(self.LoginWindow)
        self.showPasswordCheckbox.stateChanged.connect(self.toggle_password_visibility)
        self.forgotPasswordLabel.clicked.connect(self.openForgotPassword)
        self.loginButton.clicked.connect(self.handle_login)
        self.exitButton.clicked.connect(self.exit_application)  # Gọi phương thức thoát

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Trang đăng nhập"))
        self.usernameLabel.setText(_translate("LoginWindow", "Tên đăng nhập:"))
        self.loginButton.setText(_translate("LoginWindow", "Đăng nhập"))
        self.titleLabel.setText(_translate("LoginWindow", "Đăng nhập"))
        self.passwordLabel.setText(_translate("LoginWindow", "Mật khẩu:"))
        self.showPasswordCheckbox.setText(_translate("LoginWindow", "Hiển thị mật khẩu"))
        self.exitButton.setText(_translate("LoginWindow", "Thoát"))
        self.forgotPasswordLabel.setText(_translate("LoginWindow", "Quên mật khẩu?"))

    def toggle_password_visibility(self):
        if self.showPasswordCheckbox.isChecked():
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def openForgotPassword(self):
        try:
            self.LoginWindow.hide()  # Ẩn form đăng nhập
            subprocess.Popen(["python", "QuenMK.py"])
        except FileNotFoundError:
            QMessageBox.warning(None, "Lỗi", "Không tìm thấy file QuenMK.py!")
            self.LoginWindow.show()  # Hiển thị lại nếu lỗi

    def handle_login(self):
        username = self.usernameInput.text().strip()
        password = self.passwordInput.text().strip()

        if not username or not password:
            QMessageBox.warning(self.LoginWindow, "Lỗi", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu!")
            return

        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT ma_tk, vai_tro FROM taikhoan WHERE ten_dang_nhap = %s AND mat_khau = %s"
                cursor.execute(query, (username, password))
                user = cursor.fetchone()

                if user:
                    self.current_user = user[0]  # Lưu mã tài khoản
                    self.current_role = user[1]  # Lưu vai trò
                    QMessageBox.information(self.LoginWindow, "Thành công", f"Đăng nhập thành công!\nVai trò: {self.current_role}")
                    self.LoginWindow.hide()  # Ẩn form đăng nhập
                    subprocess.Popen(["python", "Main.py", str(self.current_user), str(self.current_role)])
                else:
                    QMessageBox.warning(self.LoginWindow, "Lỗi", "Sai tài khoản hoặc mật khẩu!")
            except Exception as e:
                QMessageBox.critical(self.LoginWindow, "Lỗi", f"Lỗi khi đăng nhập: {str(e)}")
            finally:
                cursor.close()
                conn.close()
        else:
            QMessageBox.critical(self.LoginWindow, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")

    def exit_application(self):
        # Thoát hoàn toàn ứng dụng khi nhấn "Thoát"
        QtWidgets.QApplication.instance().quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QWidget()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())