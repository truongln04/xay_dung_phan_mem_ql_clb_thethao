from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from openpyxl.workbook import Workbook
from Database.data import get_db_connection  # Import hàm kết nối MySQL


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 583)
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
            QLineEdit, QDateEdit {
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
        self.lineEdit.setGeometry(QtCore.QRect(0, -10, 661, 571))
        self.lineEdit.setStyleSheet("QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC); }")
        self.lineEdit.setObjectName("lineEdit")

        # GroupBox Xử lý
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 270, 601, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")

        self.btnthem = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnthem.setGeometry(QtCore.QRect(50, 20, 93, 28))
        self.btnthem.setObjectName("btnthem")

        self.btnlammoi = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnlammoi.setGeometry(QtCore.QRect(370, 20, 93, 28))
        self.btnlammoi.setObjectName("btnlammoi")

        self.btnluu = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnluu.setGeometry(QtCore.QRect(150, 20, 93, 28))
        self.btnluu.setObjectName("btnluu")

        self.btnxoa = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnxoa.setGeometry(QtCore.QRect(260, 20, 93, 28))
        self.btnxoa.setObjectName("btnxoa")

        self.btnthoat = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnthoat.setGeometry(QtCore.QRect(480, 20, 93, 28))
        self.btnthoat.setObjectName("btnthoat")

        # GroupBox Thông tin đăng ký
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 311, 201))
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_5.setObjectName("label_5")

        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 85, 16))
        self.label_11.setObjectName("label_11")

        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_15.setObjectName("label_15")

        self.txtmadk = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtmadk.setGeometry(QtCore.QRect(100, 40, 161, 22))
        self.txtmadk.setObjectName("txtmadk")

        self.label_16 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_16.setObjectName("label_16")

        self.txtngaydk = QtWidgets.QDateEdit(parent=self.groupBox)
        self.txtngaydk.setGeometry(QtCore.QRect(100, 160, 161, 22))
        self.txtngaydk.setCalendarPopup(True)
        self.txtngaydk.setDate(QtCore.QDate.currentDate())
        self.txtngaydk.setDisplayFormat("yyyy-MM-dd")
        self.txtngaydk.setObjectName("txtngaydk")

        self.txtmatv = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtmatv.setGeometry(QtCore.QRect(100, 80, 161, 22))
        self.txtmatv.setObjectName("txtmatv")

        self.txtmalop = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtmalop.setGeometry(QtCore.QRect(100, 120, 161, 22))
        self.txtmalop.setObjectName("txtmalop")

        # GroupBox Danh sách đăng ký
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 340, 601, 211))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.tblds = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tblds.setGeometry(QtCore.QRect(10, 20, 581, 181))
        self.tblds.setColumnCount(4)
        self.tblds.setHorizontalHeaderLabels(["Mã ĐK", "Mã Thành Viên", "Mã Lớp", "Ngày Đăng Ký"])
        self.tblds.setColumnWidth(0, 60)
        self.tblds.setColumnWidth(1, 150)
        self.tblds.setColumnWidth(2, 170)
        self.tblds.setColumnWidth(3, 250)
        self.tblds.setObjectName("tblds")

        # GroupBox Tìm kiếm
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(340, 60, 281, 201))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")

        self.label_20 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(50, 30, 101, 16))
        self.label_20.setObjectName("label_20")

        self.txtmadk_2 = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.txtmadk_2.setGeometry(QtCore.QRect(50, 50, 151, 21))
        self.txtmadk_2.setObjectName("txtmadk_2")

        self.btnxuat = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnxuat.setGeometry(QtCore.QRect(110, 150, 81, 28))
        self.btnxuat.setObjectName("btnxuat")

        self.btnTimKiem = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnTimKiem.setGeometry(QtCore.QRect(110, 100, 81, 31))
        self.btnTimKiem.setFont(font)
        self.btnTimKiem.setObjectName("btnTimKiem")

        # Tiêu đề chính
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #4A90E2; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC);")
        self.label.setObjectName("label")

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
        self.btnxuat.clicked.connect(self.export_data)
        self.btnlammoi.clicked.connect(self.lam_moi_du_lieu)
        self.btnTimKiem.clicked.connect(self.search_account)
        self.btnthoat.clicked.connect(self.thoat)
        self.tblds.itemSelectionChanged.connect(self.on_table_selection_changed)

        # Load dữ liệu ban đầu
        self.load_data()
        self.load_account_ids()
        self.load_cbbmatv()
        self.load_cbbmalop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Xử lý"))
        self.btnthem.setText(_translate("MainWindow", "Thêm"))
        self.btnlammoi.setText(_translate("MainWindow", "Làm mới"))
        self.btnluu.setText(_translate("MainWindow", "Lưu"))
        self.btnxoa.setText(_translate("MainWindow", "Xóa"))
        self.btnthoat.setText(_translate("MainWindow", "Thoát"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin đăng ký:"))
        self.label_5.setText(_translate("MainWindow", "Mã ĐK:"))
        self.label_11.setText(_translate("MainWindow", "Mã Thành Viên:"))
        self.label_15.setText(_translate("MainWindow", "Mã Lớp:"))
        self.label_16.setText(_translate("MainWindow", "Ngày Đăng Ký:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Danh sách đăng ký:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tìm kiếm"))
        self.label_20.setText(_translate("MainWindow", "Mã DK:"))
        self.btnxuat.setText(_translate("MainWindow", "Xuất Excel"))
        self.btnTimKiem.setText(_translate("MainWindow", "Tìm kiếm"))
        self.label.setText(_translate("MainWindow", "QUẢN LÝ ĐĂNG KÝ LỚP"))

    def load_data(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM dangkylop")
            rows = cursor.fetchall()
            self.tblds.setRowCount(0)
            for row in rows:
                rowPosition = self.tblds.rowCount()
                self.tblds.insertRow(rowPosition)
                for col, value in enumerate(row):
                    self.tblds.setItem(rowPosition, col, QtWidgets.QTableWidgetItem(str(value)))
            cursor.close()
            connection.close()

    def load_account_ids(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT ma_dk FROM dangkylop")
            rows = cursor.fetchall()
            self.txtmadk_2.clear()
            for row in rows:
                self.txtmadk_2.addItem(row[0])
            cursor.close()
            connection.close()

    def load_cbbmatv(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT ma_tv, ho_ten FROM thanhvien")
            rows = cursor.fetchall()
            self.txtmatv.clear()
            self.matv_mapping = {}
            for row in rows:
                ma_tv, ho_ten = row
                display_text = f"{ma_tv} - {ho_ten}"
                self.matv_mapping[display_text] = ma_tv
                self.txtmatv.addItem(display_text)
            cursor.close()
            connection.close()

    def load_cbbmalop(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT ma_lop, ten_lop, ngay_bat_dau, ngay_ket_thuc FROM loptap")
            rows = cursor.fetchall()
            self.txtmalop.clear()
            self.malop_mapping = {}
            self.lop_dates = {}  # Lưu thông tin ngày bắt đầu và kết thúc của lớp
            for row in rows:
                ma_lop, ten_lop, ngay_bd, ngay_kt = row
                display_text = f"{ma_lop} - {ten_lop}"
                self.malop_mapping[display_text] = ma_lop
                self.lop_dates[ma_lop] = (ngay_bd, ngay_kt)
                self.txtmalop.addItem(display_text)
            cursor.close()
            connection.close()

    def on_table_selection_changed(self):
        row = self.tblds.currentRow()
        if row != -1:
            madk = self.tblds.item(row, 0).text()
            matv = self.tblds.item(row, 1).text()
            malop = self.tblds.item(row, 2).text()
            ngaydk = self.tblds.item(row, 3).text()

            self.txtmadk.setText(madk)
            self.txtngaydk.setDate(QtCore.QDate.fromString(ngaydk, "yyyy-MM-dd"))

            for display_text, ma in self.matv_mapping.items():
                if ma == matv:
                    self.txtmatv.setCurrentText(display_text)
                    break

            for display_text, ma in self.malop_mapping.items():
                if ma == malop:
                    self.txtmalop.setCurrentText(display_text)
                    break

    def search_account(self):
        madk = self.txtmadk_2.currentText()
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM dangkylop WHERE ma_dk = %s", (madk,))
            rows = cursor.fetchall()
            self.tblds.setRowCount(0)
            for row in rows:
                rowPosition = self.tblds.rowCount()
                self.tblds.insertRow(rowPosition)
                for col, value in enumerate(row):
                    self.tblds.setItem(rowPosition, col, QtWidgets.QTableWidgetItem(str(value)))
            cursor.close()
            connection.close()

    def add_account(self):
        try:
            madk = self.txtmadk.text().strip()
            matv_display = self.txtmatv.currentText().strip()
            malop_display = self.txtmalop.currentText().strip()
            ngaydk = self.txtngaydk.date().toString("yyyy-MM-dd")

            matv = self.matv_mapping.get(matv_display)
            malop = self.malop_mapping.get(malop_display)

            if not madk or not matv or not malop:
                QMessageBox.warning(None, "Lỗi", "Mã ĐK, Mã Thành Viên và Mã Lớp không được để trống!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()

            # Kiểm tra xem toàn bộ thông tin đăng ký đã tồn tại chưa
            cursor.execute("""
                SELECT COUNT(*) FROM dangkylop 
                WHERE ma_dk = %s AND ma_tv = %s AND ma_lop = %s AND ngay_dang_ky = %s
            """, (madk, matv, malop, ngaydk))
            if cursor.fetchone()[0] > 0:
                QMessageBox.warning(None, "Lỗi", "Thông tin đăng ký này đã tồn tại!")
                cursor.close()
                connection.close()
                return

            # Kiểm tra mã ĐK đã tồn tại chưa
            cursor.execute("SELECT COUNT(*) FROM dangkylop WHERE ma_dk = %s", (madk,))
            if cursor.fetchone()[0] > 0:
                QMessageBox.warning(None, "Lỗi", "Mã ĐK đã tồn tại!")
                cursor.close()
                connection.close()
                return

            # Kiểm tra số lần đăng ký của thành viên cho lớp này
            cursor.execute("SELECT COUNT(*) FROM dangkylop WHERE ma_tv = %s AND ma_lop = %s", (matv, malop))
            count = cursor.fetchone()[0]
            if count >= 2:
                QMessageBox.warning(None, "Lỗi", "Thành viên này đã đăng ký lớp này 2 lần!")
                cursor.close()
                connection.close()
                return

            # Kiểm tra ngày đăng ký có hợp lý với khoảng thời gian của lớp không
            ngay_bd, ngay_kt = self.lop_dates.get(malop, (None, None))
            if ngay_bd and ngay_kt:
                ngaydk_date = QtCore.QDate.fromString(ngaydk, "yyyy-MM-dd")
                ngay_bd_date = QtCore.QDate.fromString(str(ngay_bd), "yyyy-MM-dd")
                ngay_kt_date = QtCore.QDate.fromString(str(ngay_kt), "yyyy-MM-dd")
                if ngaydk_date < ngay_bd_date or ngaydk_date > ngay_kt_date:
                    QMessageBox.warning(None, "Lỗi", "Ngày đăng ký không nằm trong khoảng thời gian hoạt động của lớp!")
                    cursor.close()
                    connection.close()
                    return

            # Thêm đăng ký vào bảng dangkylop
            cursor.execute("""
                INSERT INTO dangkylop (ma_dk, ma_tv, ma_lop, ngay_dang_ky)
                VALUES (%s, %s, %s, %s)
            """, (madk, matv, malop, ngaydk))

            # Tự động thêm hóa đơn vào bảng hoadon với ngay_thanh_toan = NULL
            ma_hd = f"HD{madk}"  # Tạo mã hóa đơn dựa trên mã đăng ký
            so_tien = self.get_class_fee(malop)  # Lấy số tiền từ bảng loptap
            trang_thai = "Chưa thanh toán"
            ngay_thanh_toan = None  # Đặt NULL vì chưa thanh toán

            cursor.execute("""
                INSERT INTO hoadon (ma_hd, ma_tv, ma_lop, so_tien, trang_thai, ngay_thanh_toan)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (ma_hd, matv, malop, so_tien, trang_thai, ngay_thanh_toan))

            connection.commit()
            QMessageBox.information(None, "Thành công", "Thêm đăng ký và hóa đơn thành công!")
            self.load_data()
            self.load_account_ids()
            cursor.close()
            connection.close()

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi thêm: {str(e)}")
            if 'connection' in locals():
                connection.rollback()
                cursor.close()
                connection.close()

    def get_class_fee(self, malop):
        """Hàm lấy số tiền học phí từ bảng loptap dựa trên mã lớp"""
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT hoc_phi FROM loptap WHERE ma_lop = %s", (malop,))
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            if result:
                return result[0]  # Trả về học phí
        return 0  # Mặc định trả về 0 nếu không tìm thấy

    def delete_account(self):
        try:
            row = self.tblds.currentRow()
            if row == -1:
                QMessageBox.warning(None, "Lỗi", "Vui lòng chọn một dòng để xóa!")
                return

            madk = self.tblds.item(row, 0).text()
            reply = QMessageBox.question(None, "Xác nhận", "Bạn có chắc muốn xóa đăng ký này?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                connection = get_db_connection()
                if not connection:
                    QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                    return

                cursor = connection.cursor()
                cursor.execute("DELETE FROM dangkylop WHERE ma_dk = %s", (madk,))
                connection.commit()
                QMessageBox.information(None, "Thành công", "Xóa đăng ký thành công!")
                self.load_data()
                self.load_account_ids()
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

            madk = self.txtmadk.text().strip()
            matv_display = self.txtmatv.currentText().strip()
            malop_display = self.txtmalop.currentText().strip()
            ngaydk = self.txtngaydk.date().toString("yyyy-MM-dd")

            matv = self.matv_mapping.get(matv_display)
            malop = self.malop_mapping.get(malop_display)

            if not madk or not matv or not malop:
                QMessageBox.warning(None, "Lỗi", "Mã ĐK, Mã Thành Viên và Mã Lớp không được để trống!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()

            # Kiểm tra ngày đăng ký có hợp lý với khoảng thời gian của lớp không
            ngay_bd, ngay_kt = self.lop_dates.get(malop, (None, None))
            if ngay_bd and ngay_kt:
                ngaydk_date = QtCore.QDate.fromString(ngaydk, "yyyy-MM-dd")
                ngay_bd_date = QtCore.QDate.fromString(str(ngay_bd), "yyyy-MM-dd")
                ngay_kt_date = QtCore.QDate.fromString(str(ngay_kt), "yyyy-MM-dd")
                if ngaydk_date < ngay_bd_date or ngaydk_date > ngay_kt_date:
                    QMessageBox.warning(None, "Lỗi", "Ngày đăng ký không nằm trong khoảng thời gian hoạt động của lớp!")
                    cursor.close()
                    connection.close()
                    return

            cursor.execute("""
                UPDATE dangkylop SET ma_tv = %s, ma_lop = %s, ngay_dang_ky = %s
                WHERE ma_dk = %s
            """, (matv, malop, ngaydk, madk))
            connection.commit()
            QMessageBox.information(None, "Thành công", "Cập nhật đăng ký thành công!")
            self.load_data()
            self.load_account_ids()
            cursor.close()
            connection.close()

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi sửa: {str(e)}")
            if 'connection' in locals():
                connection.rollback()
                cursor.close()
                connection.close()

    def lam_moi_du_lieu(self):
        self.txtmadk.clear()
        self.txtngaydk.setDate(QtCore.QDate.currentDate())
        self.txtmatv.setCurrentIndex(-1)
        self.txtmalop.setCurrentIndex(-1)
        self.txtmadk_2.setCurrentIndex(-1)
        self.load_data()
        self.load_account_ids()
        self.load_cbbmatv()
        self.load_cbbmalop()
        QMessageBox.information(None, "Thành công", "Dữ liệu đã được làm mới!")

    def thoat(self):
        reply = QMessageBox.question(None, "Xác nhận", "Bạn có muốn thoát không?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()

    def export_data(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "DangKyLop Data"
        headers = ["Mã ĐK", "Mã Thành Viên", "Mã Lớp", "Ngày Đăng Ký"]
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())