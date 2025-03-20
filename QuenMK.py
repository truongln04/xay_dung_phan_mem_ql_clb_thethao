from PyQt6 import QtCore, QtWidgets
import subprocess
from Database.data import get_db_connection
from PyQt6.QtWidgets import QMessageBox
import smtplib
import random
import string
from email.mime.text import MIMEText
import re
from datetime import datetime, timedelta

class Ui_ForgotPasswordWindow(object):
    def setupUi(self, ForgotPasswordWindow):
        ForgotPasswordWindow.setObjectName("ForgotPasswordWindow")
        ForgotPasswordWindow.resize(444, 420)  # Tăng chiều cao để chứa thêm trường OTP
        ForgotPasswordWindow.setStyleSheet("""
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
        self.listView = QtWidgets.QListView(parent=ForgotPasswordWindow)
        self.listView.setGeometry(QtCore.QRect(0, 0, 451, 421))  # Sửa từ QtCore.Rect thành QtCore.QRect
        self.listView.setStyleSheet("QWidget {background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC);}")
        self.listView.setObjectName("listView")

        self.titleLabel = QtWidgets.QLabel(parent=ForgotPasswordWindow)
        self.titleLabel.setGeometry(QtCore.QRect(90, 30, 250, 50))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.usernameLabel = QtWidgets.QLabel(parent=ForgotPasswordWindow)
        self.usernameLabel.setGeometry(QtCore.QRect(40, 100, 120, 30))
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameInput = QtWidgets.QLineEdit(parent=ForgotPasswordWindow)
        self.usernameInput.setGeometry(QtCore.QRect(170, 100, 220, 30))
        self.usernameInput.setObjectName("usernameInput")

        self.emailLabel = QtWidgets.QLabel(parent=ForgotPasswordWindow)
        self.emailLabel.setGeometry(QtCore.QRect(40, 150, 120, 30))
        self.emailLabel.setObjectName("emailLabel")
        self.emailInput = QtWidgets.QLineEdit(parent=ForgotPasswordWindow)
        self.emailInput.setGeometry(QtCore.QRect(170, 150, 220, 30))
        self.emailInput.setObjectName("emailInput")

        self.sendOtpButton = QtWidgets.QPushButton(parent=ForgotPasswordWindow)
        self.sendOtpButton.setGeometry(QtCore.QRect(290, 190, 100, 30))
        self.sendOtpButton.setObjectName("sendOtpButton")

        self.otpLabel = QtWidgets.QLabel(parent=ForgotPasswordWindow)
        self.otpLabel.setGeometry(QtCore.QRect(40, 230, 120, 30))
        self.otpLabel.setObjectName("otpLabel")
        self.otpInput = QtWidgets.QLineEdit(parent=ForgotPasswordWindow)
        self.otpInput.setGeometry(QtCore.QRect(170, 230, 220, 30))
        self.otpInput.setObjectName("otpInput")

        self.newPasswordLabel = QtWidgets.QLabel(parent=ForgotPasswordWindow)
        self.newPasswordLabel.setGeometry(QtCore.QRect(40, 280, 120, 30))
        self.newPasswordLabel.setObjectName("newPasswordLabel")
        self.newPasswordInput = QtWidgets.QLineEdit(parent=ForgotPasswordWindow)
        self.newPasswordInput.setGeometry(QtCore.QRect(170, 280, 220, 30))
        self.newPasswordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.newPasswordInput.setObjectName("newPasswordInput")

        self.showPasswordCheckbox = QtWidgets.QCheckBox(parent=ForgotPasswordWindow)
        self.showPasswordCheckbox.setGeometry(QtCore.QRect(170, 320, 150, 20))
        self.showPasswordCheckbox.setObjectName("showPasswordCheckbox")

        self.resetPasswordButton = QtWidgets.QPushButton(parent=ForgotPasswordWindow)
        self.resetPasswordButton.setGeometry(QtCore.QRect(100, 350, 120, 41))
        self.resetPasswordButton.setObjectName("resetPasswordButton")
        self.loginButton = QtWidgets.QPushButton(parent=ForgotPasswordWindow)
        self.loginButton.setGeometry(QtCore.QRect(250, 350, 121, 41))
        self.loginButton.setObjectName("loginButton")

        self.retranslateUi(ForgotPasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(ForgotPasswordWindow)

        # Kết nối sự kiện
        self.loginButton.clicked.connect(lambda: self.openLoginWindow(ForgotPasswordWindow))
        self.showPasswordCheckbox.stateChanged.connect(self.toggle_password_visibility)
        self.sendOtpButton.clicked.connect(self.send_otp)
        self.resetPasswordButton.clicked.connect(self.resetPassword)

        # Biến lưu OTP và thời gian
        self.generated_otp = None
        self.otp_timestamp = None

    def retranslateUi(self, ForgotPasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        ForgotPasswordWindow.setWindowTitle(_translate("ForgotPasswordWindow", "Quên mật khẩu"))
        self.loginButton.setText(_translate("ForgotPasswordWindow", "Đăng nhập"))
        self.titleLabel.setText(_translate("ForgotPasswordWindow", "Quên mật khẩu"))
        self.resetPasswordButton.setText(_translate("ForgotPasswordWindow", "Đặt lại mật khẩu"))
        self.usernameLabel.setText(_translate("ForgotPasswordWindow", "Tên đăng nhập:"))
        self.emailLabel.setText(_translate("ForgotPasswordWindow", "Email:"))
        self.sendOtpButton.setText(_translate("ForgotPasswordWindow", "Gửi OTP"))
        self.otpLabel.setText(_translate("ForgotPasswordWindow", "Mã OTP:"))
        self.newPasswordLabel.setText(_translate("ForgotPasswordWindow", "Mật khẩu mới:"))
        self.showPasswordCheckbox.setText(_translate("ForgotPasswordWindow", "Hiển thị mật khẩu"))

    def openLoginWindow(self, ForgotPasswordWindow):
        subprocess.Popen(["python", "DangNhap.py"])
        ForgotPasswordWindow.close()

    def toggle_password_visibility(self):
        if self.showPasswordCheckbox.isChecked():
            self.newPasswordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.newPasswordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def generate_otp(self):
        """Tạo mã OTP ngẫu nhiên gồm 6 chữ số"""
        return ''.join(random.choices(string.digits, k=6))

    def is_valid_email(self, email):
        """Kiểm tra định dạng email"""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def send_otp(self):
        username = self.usernameInput.text().strip()
        email = self.emailInput.text().strip()

        if not username or not email:
            QMessageBox.warning(None, "Lỗi", "Vui lòng nhập tên đăng nhập và email!")
            return

        if not self.is_valid_email(email):
            QMessageBox.warning(None, "Lỗi", "Email không hợp lệ! Vui lòng nhập đúng định dạng (example@domain.com)")
            return

        conn = get_db_connection()
        if not conn:
            QMessageBox.critical(None, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM TaiKhoan WHERE ten_dang_nhap=%s AND email=%s", (username, email))
            account = cursor.fetchone()

            if not account:
                QMessageBox.warning(None, "Lỗi", "Tên đăng nhập hoặc email không đúng!")
                return

            # Tạo và lưu OTP cùng với thời gian
            self.generated_otp = self.generate_otp()
            self.otp_timestamp = datetime.now()  # Lưu thời gian tạo OTP

            # Gửi email chứa OTP
            sender_email = "truongclashth2@gmail.com"  # Thay bằng email của bạn
            sender_password = "fuqq yshu haak uhgk"  # Thay bằng mật khẩu ứng dụng 16 ký tự (không có khoảng trắng)
            subject = "Mã OTP để đặt lại mật khẩu"
            body = f"Mã OTP của bạn là: {self.generated_otp}. Vui lòng sử dụng mã này để đặt lại mật khẩu trong vòng 2 phút."

            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = sender_email
            msg["To"] = email

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())

            QMessageBox.information(None, "Thành công", f"Mã OTP đã được gửi đến {email}!")
            conn.close()

        except smtplib.SMTPAuthenticationError as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi xác thực SMTP: Kiểm tra lại email và mật khẩu ứng dụng. Chi tiết: {str(e)}")
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi gửi OTP: {str(e)}")
            if 'conn' in locals():
                conn.close()

    def resetPassword(self):
        username = self.usernameInput.text().strip()
        email = self.emailInput.text().strip()
        otp = self.otpInput.text().strip()
        new_password = self.newPasswordInput.text().strip()

        if not username or not email or not otp or not new_password:
            QMessageBox.warning(None, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        if self.generated_otp is None:
            QMessageBox.warning(None, "Lỗi", "Vui lòng gửi mã OTP trước!")
            return

        if datetime.now() > self.otp_timestamp + timedelta(minutes=2):
            QMessageBox.warning(None, "Lỗi", "Mã OTP đã hết hạn! Vui lòng gửi lại mã mới.")
            self.generated_otp = None
            self.otp_timestamp = None
            return

        if otp != self.generated_otp:
            QMessageBox.warning(None, "Lỗi", "Mã OTP không đúng!")
            return

        conn = get_db_connection()
        if not conn:
            QMessageBox.critical(None, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM TaiKhoan WHERE ten_dang_nhap=%s AND email=%s", (username, email))
            account = cursor.fetchone()

            if not account:
                QMessageBox.warning(None, "Lỗi", "Tên đăng nhập hoặc email không đúng!")
                return

            cursor.execute("UPDATE TaiKhoan SET mat_khau=%s WHERE ten_dang_nhap=%s", (new_password, username))
            conn.commit()
            QMessageBox.information(None, "Thành công", "Mật khẩu đã được cập nhật!")
            self.usernameInput.clear()
            self.emailInput.clear()
            self.otpInput.clear()
            self.newPasswordInput.clear()
            self.generated_otp = None
            self.otp_timestamp = None  # Reset thời gian OTP

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi cập nhật mật khẩu: {str(e)}")
        finally:
            conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPasswordWindow = QtWidgets.QWidget()
    ui = Ui_ForgotPasswordWindow()
    ui.setupUi(ForgotPasswordWindow)
    ForgotPasswordWindow.show()
    sys.exit(app.exec())