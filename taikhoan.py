from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from openpyxl import Workbook
from Database.data import get_db_connection  # Giả sử đây là module kết nối database của bạn


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 605)
        MainWindow.setStyleSheet("""
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
                background-color: #E0E0E0;
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
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 831, 591))
        self.lineEdit.setStyleSheet(
            "QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC); }")
        self.lineEdit.setObjectName("lineEdit")

        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 601, 211))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.label_13 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_13.setObjectName("label_13")

        self.label_43 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_43.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_43.setObjectName("label_43")

        self.label_44 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_44.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_44.setObjectName("label_44")

        self.txtmatk = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtmatk.setGeometry(QtCore.QRect(110, 40, 161, 22))
        self.txtmatk.setObjectName("txtmatk")

        self.txttendn = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txttendn.setGeometry(QtCore.QRect(110, 80, 161, 22))
        self.txttendn.setObjectName("txttendn")

        self.txtmk = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtmk.setGeometry(QtCore.QRect(110, 120, 161, 22))
        self.txtmk.setObjectName("txtmk")

        self.label_45 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_45.setGeometry(QtCore.QRect(290, 40, 91, 16))
        self.label_45.setObjectName("label_45")

        self.label_46 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_46.setGeometry(QtCore.QRect(290, 120, 101, 16))
        self.label_46.setObjectName("label_46")

        self.label_47 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_47.setGeometry(QtCore.QRect(290, 80, 91, 16))
        self.label_47.setObjectName("label_47")

        self.txtemail = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtemail.setGeometry(QtCore.QRect(400, 40, 181, 22))
        self.txtemail.setObjectName("txtemail")

        self.txtvaitro = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtvaitro.setGeometry(QtCore.QRect(400, 80, 181, 22))
        self.txtvaitro.setObjectName("txtvaitro")
        self.txtvaitro.addItems(["admin", "nhanvien"])

        self.txtmaclb = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtmaclb.setGeometry(QtCore.QRect(400, 120, 181, 22))
        self.txtmaclb.setObjectName("txtmaclb")

        self.label_48 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_48.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_48.setObjectName("label_48")

        self.txthoten = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txthoten.setGeometry(QtCore.QRect(110, 160, 161, 22))
        self.txthoten.setObjectName("txthoten")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "color: #357ABD; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC);")
        self.label.setObjectName("label")

        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 80, 181, 211))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")

        self.label_37 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_37.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_37.setObjectName("label_37")

        self.txtmatk_2 = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.txtmatk_2.setGeometry(QtCore.QRect(10, 50, 151, 22))
        self.txtmatk_2.setObjectName("txtmatk_2")

        self.btnxuat = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnxuat.setGeometry(QtCore.QRect(40, 150, 93, 28))
        self.btnxuat.setObjectName("btnxuat")

        self.btntimkiem = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btntimkiem.setGeometry(QtCore.QRect(40, 100, 91, 31))
        self.btntimkiem.setObjectName("btntimkiem")

        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(620, 300, 181, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")

        self.btnthem = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnthem.setGeometry(QtCore.QRect(40, 30, 93, 28))
        self.btnthem.setObjectName("btnthem")

        self.btnlammoi = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnlammoi.setGeometry(QtCore.QRect(40, 180, 93, 28))
        self.btnlammoi.setObjectName("btnlammoi")

        self.btnluu = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnluu.setGeometry(QtCore.QRect(40, 80, 93, 28))
        self.btnluu.setObjectName("btnluu")

        self.btnxoa = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnxoa.setGeometry(QtCore.QRect(40, 130, 93, 28))
        self.btnxoa.setObjectName("btnxoa")

        self.btnthoat = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnthoat.setGeometry(QtCore.QRect(40, 230, 93, 28))
        self.btnthoat.setObjectName("btnthoat")

        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 300, 601, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.tblds = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tblds.setGeometry(QtCore.QRect(10, 30, 581, 231))
        self.tblds.setColumnCount(7)
        self.tblds.setHorizontalHeaderLabels(
            ["Mã Tài Khoản", "Tên Đăng Nhập", "Mật Khẩu", "Họ Tên", "Email", "Vai Trò", "Mã CLB"])
        self.tblds.setColumnWidth(0, 80)
        self.tblds.setColumnWidth(1, 100)
        self.tblds.setColumnWidth(2, 100)
        self.tblds.setColumnWidth(3, 100)
        self.tblds.setColumnWidth(4, 80)
        self.tblds.setColumnWidth(5, 80)
        self.tblds.setColumnWidth(6, 80)
        self.tblds.setObjectName("tblds")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Kết nối sự kiện
        self.btnthem.clicked.connect(self.add_account)
        self.btnxoa.clicked.connect(self.delete_account)
        self.btnluu.clicked.connect(self.update_account)
        self.btntimkiem.clicked.connect(self.search_account)
        self.btnxuat.clicked.connect(self.export_data)
        self.btnlammoi.clicked.connect(self.lam_moi_du_lieu)
        self.btnthoat.clicked.connect(self.thoat)
        self.tblds.itemClicked.connect(self.table_item_clicked)

        # Load dữ liệu ban đầu
        self.load_data()
        self.load_cbbclb()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin tài khoản:"))
        self.label_13.setText(_translate("MainWindow", "Mã tài khoản:"))
        self.label_43.setText(_translate("MainWindow", "Tên đăng nhập:"))
        self.label_44.setText(_translate("MainWindow", "Mật khẩu:"))
        self.label_45.setText(_translate("MainWindow", "Email:"))
        self.label_46.setText(_translate("MainWindow", "Mã CLB:"))
        self.label_47.setText(_translate("MainWindow", "Vai trò:"))
        self.label_48.setText(_translate("MainWindow", "Họ tên:"))
        self.label.setText(_translate("MainWindow", "QUẢN LÝ NHÂN VIÊN"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tìm kiếm:"))
        self.label_37.setText(_translate("MainWindow", "Tìm kiếm:"))
        self.btnxuat.setText(_translate("MainWindow", "Xuất Excel"))
        self.btntimkiem.setText(_translate("MainWindow", "Tìm kiếm"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Xử lý:"))
        self.btnthem.setText(_translate("MainWindow", "Thêm"))
        self.btnlammoi.setText(_translate("MainWindow", "Làm mới"))
        self.btnluu.setText(_translate("MainWindow", "Lưu"))
        self.btnxoa.setText(_translate("MainWindow", "Xóa"))
        self.btnthoat.setText(_translate("MainWindow", "Thoát"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Danh sách tài khoản:"))

    def load_data(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM taikhoan")
            rows = cursor.fetchall()
            self.tblds.setRowCount(0)
            for row in rows:
                rowPosition = self.tblds.rowCount()
                self.tblds.insertRow(rowPosition)
                for col, value in enumerate(row):
                    self.tblds.setItem(rowPosition, col,
                                       QtWidgets.QTableWidgetItem(str(value) if value is not None else ""))
            cursor.close()
            connection.close()

    def load_cbbclb(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT ma_clb, ten_clb FROM caulacbo")
            rows = cursor.fetchall()
            self.txtmaclb.clear()
            self.club_mapping = {}
            self.club_mapping[""] = None
            self.txtmaclb.addItem("")
            for row in rows:
                ma_clb, ten_clb = row
                display_text = f"{ma_clb} - {ten_clb}"
                self.club_mapping[display_text] = ma_clb
                self.txtmaclb.addItem(display_text)
            cursor.close()
            connection.close()

    def table_item_clicked(self, item):
        row = item.row()
        self.txtmatk.setText(self.tblds.item(row, 0).text())
        self.txttendn.setText(self.tblds.item(row, 1).text())
        self.txtmk.setText(self.tblds.item(row, 2).text())
        self.txthoten.setText(self.tblds.item(row, 3).text())
        self.txtemail.setText(self.tblds.item(row, 4).text())
        self.txtvaitro.setCurrentText(self.tblds.item(row, 5).text())

        ma_clb = self.tblds.item(row, 6).text()
        if ma_clb:
            for display_text, club_id in self.club_mapping.items():
                if club_id == ma_clb:
                    self.txtmaclb.setCurrentText(display_text)
                    break
        else:
            self.txtmaclb.setCurrentIndex(0)

    def add_account(self):
        try:
            matk = self.txtmatk.text().strip()
            tendn = self.txttendn.text().strip()
            matkhau = self.txtmk.text().strip()
            hoten = self.txthoten.text().strip()
            email = self.txtemail.text().strip()
            vaitro = self.txtvaitro.currentText()
            selected_text = self.txtmaclb.currentText().strip()
            maclb = self.club_mapping.get(selected_text)

            if not matk or not tendn or not matkhau or not hoten or not email or not vaitro:
                QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ các trường bắt buộc!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()

            # Kiểm tra trùng mã tài khoản
            cursor.execute("SELECT COUNT(*) FROM taikhoan WHERE ma_tk = %s", (matk,))
            matk_count = cursor.fetchone()[0]
            if matk_count > 0:
                QMessageBox.warning(None, "Lỗi", "Mã tài khoản đã tồn tại!")
                cursor.close()
                connection.close()
                return

            # Kiểm tra trùng tên đăng nhập
            cursor.execute("SELECT COUNT(*) FROM taikhoan WHERE ten_dang_nhap = %s", (tendn,))
            tendn_count = cursor.fetchone()[0]
            if tendn_count > 0:
                QMessageBox.warning(None, "Lỗi", "Tên đăng nhập đã tồn tại!")
                cursor.close()
                connection.close()
                return

            # Kiểm tra trùng email
            cursor.execute("SELECT COUNT(*) FROM taikhoan WHERE email = %s", (email,))
            email_count = cursor.fetchone()[0]
            if email_count > 0:
                QMessageBox.warning(None, "Lỗi", "Email đã tồn tại!")
                cursor.close()
                connection.close()
                return

            cursor.execute("""
                INSERT INTO taikhoan (ma_tk, ten_dang_nhap, mat_khau, ho_ten, email, vai_tro, ma_clb)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (matk, tendn, matkhau, hoten, email, vaitro, maclb))
            connection.commit()
            self.load_data()
            QMessageBox.information(None, "Thành công", "Thêm tài khoản thành công!")
            cursor.close()
            connection.close()

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi thêm tài khoản: {str(e)}")
            if 'connection' in locals():
                connection.rollback()
                cursor.close()
                connection.close()

    def delete_account(self):
        try:
            row = self.tblds.currentRow()
            if row == -1:
                QMessageBox.warning(None, "Lỗi", "Vui lòng chọn một dòng để xóa!")
                return

            matk = self.tblds.item(row, 0).text()
            reply = QMessageBox.question(None, "Xác nhận", "Bạn có chắc muốn xóa tài khoản này?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                connection = get_db_connection()
                if not connection:
                    QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                    return

                cursor = connection.cursor()
                cursor.execute("DELETE FROM taikhoan WHERE ma_tk = %s", (matk,))
                connection.commit()
                self.load_data()
                QMessageBox.information(None, "Thành công", "Xóa tài khoản thành công!")
                cursor.close()
                connection.close()

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi xóa: {str(e)}")
            if 'connection' in locals():
                connection.rollback()
                cursor.close()
                connection.close()

    def update_account(self):
        try:
            row = self.tblds.currentRow()
            if row == -1:
                QMessageBox.warning(None, "Lỗi", "Vui lòng chọn một dòng để sửa!")
                return

            matk = self.txtmatk.text().strip()
            tendn = self.txttendn.text().strip()
            matkhau = self.txtmk.text().strip()
            hoten = self.txthoten.text().strip()
            email = self.txtemail.text().strip()
            vaitro = self.txtvaitro.currentText()
            selected_text = self.txtmaclb.currentText().strip()
            maclb = self.club_mapping.get(selected_text)

            if not matk or not tendn or not matkhau or not hoten or not email or not vaitro:
                QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ các trường bắt buộc!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()

            # Kiểm tra trùng tên đăng nhập với tài khoản khác (trừ tài khoản hiện tại)
            cursor.execute("SELECT COUNT(*) FROM taikhoan WHERE ten_dang_nhap = %s AND ma_tk != %s",
                           (tendn, matk))
            tendn_count = cursor.fetchone()[0]
            if tendn_count > 0:
                QMessageBox.warning(None, "Lỗi", "Tên đăng nhập đã tồn tại cho tài khoản khác!")
                cursor.close()
                connection.close()
                return

            # Kiểm tra trùng email với tài khoản khác (trừ tài khoản hiện tại)
            cursor.execute("SELECT COUNT(*) FROM taikhoan WHERE email = %s AND ma_tk != %s",
                           (email, matk))
            email_count = cursor.fetchone()[0]
            if email_count > 0:
                QMessageBox.warning(None, "Lỗi", "Email đã tồn tại cho tài khoản khác!")
                cursor.close()
                connection.close()
                return

            cursor.execute("""
                UPDATE taikhoan SET ten_dang_nhap = %s, mat_khau = %s, ho_ten = %s, email = %s, vai_tro = %s, ma_clb = %s
                WHERE ma_tk = %s
            """, (tendn, matkhau, hoten, email, vaitro, maclb, matk))
            connection.commit()
            self.load_data()
            QMessageBox.information(None, "Thành công", "Cập nhật tài khoản thành công!")
            cursor.close()
            connection.close()

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi sửa: {str(e)}")
            if 'connection' in locals():
                connection.rollback()
                cursor.close()
                connection.close()

    def search_account(self):
        try:
            search_text = self.txtmatk_2.text().strip()
            if not search_text:
                QMessageBox.warning(None, "Lỗi", "Vui lòng nhập thông tin để tìm kiếm!")
                self.load_data()
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()
            query = """
                SELECT * FROM taikhoan 
                WHERE ma_tk LIKE %s 
                OR ten_dang_nhap LIKE %s 
                OR mat_khau LIKE %s 
                OR ho_ten LIKE %s 
                OR email LIKE %s 
                OR vai_tro LIKE %s 
                OR ma_clb LIKE %s
            """
            search_pattern = f"%{search_text}%"
            cursor.execute(query, (search_pattern, search_pattern, search_pattern,
                                 search_pattern, search_pattern, search_pattern, search_pattern))
            rows = cursor.fetchall()

            self.tblds.setRowCount(0)
            if rows:
                for row in rows:
                    rowPosition = self.tblds.rowCount()
                    self.tblds.insertRow(rowPosition)
                    for col, value in enumerate(row):
                        self.tblds.setItem(rowPosition, col,
                                         QtWidgets.QTableWidgetItem(str(value) if value is not None else ""))
                QMessageBox.information(None, "Thành công", f"Tìm thấy {len(rows)} kết quả!")
            else:
                QMessageBox.information(None, "Thông báo", "Không tìm thấy tài khoản nào phù hợp!")

            cursor.close()
            connection.close()

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi tìm kiếm: {str(e)}")
            if 'connection' in locals():
                cursor.close()
                connection.close()

    def export_data(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "TaiKhoan Data"
        headers = ["Mã Tài Khoản", "Tên Đăng Nhập", "Mật Khẩu", "Họ Tên", "Email", "Vai Trò", "Mã CLB"]
        ws.append(headers)

        for row in range(self.tblds.rowCount()):
            row_data = []
            for col in range(self.tblds.columnCount()):
                item = self.tblds.item(row, col)
                row_data.append(item.text() if item else "")
            ws.append(row_data)

        file_path, _ = QFileDialog.getSaveFileName(None, "Lưu file Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            wb.save(file_path)
            QMessageBox.information(None, "Thành công", "Dữ liệu đã được xuất thành công!")

    def lam_moi_du_lieu(self):
        self.txtmatk.clear()
        self.txttendn.clear()
        self.txtmk.clear()
        self.txthoten.clear()
        self.txtemail.clear()
        self.txtvaitro.setCurrentIndex(-1)
        self.txtmatk_2.clear()
        self.txtmaclb.setCurrentIndex(-1)
        self.load_data()
        self.load_cbbclb()
        QMessageBox.information(None, "Thành công", "Dữ liệu đã được làm mới!")

    def thoat(self):
        reply = QMessageBox.question(None, "Xác nhận", "Bạn có muốn thoát không?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())