from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(600, 500)  # Tăng kích thước form để chứa nội dung dài hơn
        AboutWindow.setWindowTitle("Giới thiệu")

        # Áp dụng stylesheet tương tự form đăng nhập
        AboutWindow.setStyleSheet("""
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
            QLabel {
                color: #333333;
            }
        """)

        # Background gradient
        self.background = QtWidgets.QListView(parent=AboutWindow)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.background.setStyleSheet(
            "QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC); }")
        self.background.setObjectName("background")

        # Tiêu đề
        self.titleLabel = QtWidgets.QLabel(parent=AboutWindow)
        self.titleLabel.setGeometry(QtCore.QRect(50, 20, 500, 50))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.titleLabel.setFont(font)

        # Nội dung giới thiệu
        self.introLabel = QtWidgets.QLabel(parent=AboutWindow)
        self.introLabel.setGeometry(QtCore.QRect(50, 80, 500, 250))  # Tăng chiều cao để chứa nội dung dài
        self.introLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.introLabel.setWordWrap(True)
        self.introLabel.setObjectName("introLabel")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.introLabel.setFont(font)

        # Thông tin liên hệ
        self.contactLabel = QtWidgets.QLabel(parent=AboutWindow)
        self.contactLabel.setGeometry(QtCore.QRect(50, 340, 500, 100))  # Điều chỉnh vị trí
        self.contactLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.contactLabel.setWordWrap(True)
        self.contactLabel.setObjectName("contactLabel")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contactLabel.setFont(font)

        # Nút đóng
        self.closeButton = QtWidgets.QPushButton(parent=AboutWindow)
        self.closeButton.setGeometry(QtCore.QRect(250, 450, 100, 40))  # Điều chỉnh vị trí nút
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

        # Kết nối sự kiện
        self.closeButton.clicked.connect(AboutWindow.close)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        self.titleLabel.setText(_translate("AboutWindow", "Giới thiệu"))
        self.introLabel.setText(_translate("AboutWindow",
                                           "\u2022 Đây là phần mềm quản lý câu lạc bộ thể thao được phát triển nhằm hỗ trợ các tổ chức thể thao trong việc quản lý hiệu quả.\n"
                                           "\u2022 Ứng dụng cho phép người dùng quản lý thông tin chi tiết của các thành viên, bao gồm thông tin cá nhân, lịch sử tham gia, và các hoạt động trong câu lạc bộ.\n"
                                           "\u2022 Hỗ trợ quản lý thông tin các câu lạc bộ như danh sách thành viên, lịch thi đấu, kết quả trận đấu, và các sự kiện quan trọng.\n"
                                           "\u2022 Cung cấp công cụ theo dõi và phân tích dữ liệu, giúp người quản lý dễ dàng đánh giá hiệu suất hoạt động của câu lạc bộ.\n"
                                           "\u2022 Tính năng xuất báo cáo dưới dạng Excel, hỗ trợ lưu trữ và chia sẻ thông tin một cách nhanh chóng và chuyên nghiệp.\n"
                                           "\u2022 Giao diện thân thiện, dễ sử dụng, phù hợp với cả người dùng không chuyên về công nghệ."
                                           ))
        self.contactLabel.setText(_translate("AboutWindow",
                                             "Liên hệ:\n"
                                             "\u2022 Email: support@sportsclub.com - Hỗ trợ kỹ thuật 24/7.\n"
                                             "\u2022 Điện thoại: 0123-456-789 - Liên hệ trong giờ hành chính.\n"
                                             "\u2022 Địa chỉ: 123 Đường Thể Dục, Quận Thể Thao, TP. Sức khỏe - Trụ sở chính của nhóm phát triển."
                                             ))
        self.closeButton.setText(_translate("AboutWindow", "Đóng"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AboutWindow = QtWidgets.QWidget()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec())