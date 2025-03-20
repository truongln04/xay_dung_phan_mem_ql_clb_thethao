from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QFileDialog, QDateEdit
from openpyxl.workbook import Workbook
from Database.data import get_db_connection  # Import hàm kết nối MySQL


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow  # Lưu tham chiếu MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 580)
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
                   QComboBox, QDateEdit {
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
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 821, 561))
        self.lineEdit.setStyleSheet(
            "QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC); }")

        # Tiêu đề chính "QUẢN LÝ HÓA ĐƠN" giữ size 12
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 201, 41))
        font_title = QtGui.QFont()
        font_title.setPointSize(12)  # Giữ size 12
        font_title.setBold(True)
        font_title.setWeight(75)
        self.label.setFont(font_title)
        self.label.setStyleSheet(
            "color: #4A90E2; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC);")

        # Font cho QGroupBox (size nhỏ hơn, ví dụ 10)
        font_group = QtGui.QFont()
        font_group.setPointSize(10)  # Giảm xuống 10
        font_group.setBold(True)
        font_group.setWeight(75)

        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 601, 201))
        self.groupBox.setFont(font_group)  # Áp dụng font size 10

        # Mã Đăng Ký (di chuyển lên trên cùng)
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_16.setText("Mã Đăng Ký:")
        self.txtmadk = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtmadk.setGeometry(QtCore.QRect(100, 40, 161, 22))

        # Mã Hóa Đơn
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.txtmahoadon = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtmahoadon.setGeometry(QtCore.QRect(100, 80, 161, 22))

        # Mã Lớp
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 55, 16))
        self.txtmalop = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtmalop.setGeometry(QtCore.QRect(100, 120, 161, 22))

        # Mã Thành Viên
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.txtmatv = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtmatv.setGeometry(QtCore.QRect(100, 160, 161, 22))

        # Các trường bên phải
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(280, 40, 55, 16))
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(280, 80, 91, 16))
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(280, 120, 101, 16))
        self.txtsotien = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtsotien.setGeometry(QtCore.QRect(390, 40, 171, 22))
        self.txttrangthai = QtWidgets.QComboBox(parent=self.groupBox)
        self.txttrangthai.setGeometry(QtCore.QRect(390, 80, 171, 22))
        self.txttrangthai.addItems(["Chưa thanh toán", "Đã thanh toán"])
        self.txtngaythanhtoan = QDateEdit(parent=self.groupBox)
        self.txtngaythanhtoan.setGeometry(QtCore.QRect(390, 120, 171, 22))
        self.txtngaythanhtoan.setCalendarPopup(True)
        self.txtngaythanhtoan.setDate(QtCore.QDate.currentDate())
        self.txtngaythanhtoan.setDisplayFormat("yyyy-MM-dd")

        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 60, 181, 201))
        self.groupBox_3.setFont(font_group)  # Áp dụng font size 10
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(20, 30, 120, 16))
        self.txtmahoadon_2 = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.txtmahoadon_2.setGeometry(QtCore.QRect(20, 50, 131, 21))
        self.label_25 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(10, 90, 31, 31))
        self.label_25.setPixmap(QtGui.QPixmap("anh/timkiem.png"))
        self.label_25.setScaledContents(True)
        self.btnxuat = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnxuat.setGeometry(QtCore.QRect(40, 150, 93, 28))
        self.btntimkiem = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btntimkiem.setGeometry(QtCore.QRect(40, 100, 91, 31))
        self.btntimkiem.setFont(font_group)  # Áp dụng font size 10 cho nút tìm kiếm

        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 601, 271))
        self.groupBox_2.setFont(font_group)  # Áp dụng font size 10

        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(620, 280, 181, 271))
        self.groupBox_6.setFont(font_group)  # Áp dụng font size 10
        self.btnthem = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnthem.setGeometry(QtCore.QRect(50, 20, 93, 28))
        self.btnlammoi = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnlammoi.setGeometry(QtCore.QRect(50, 170, 93, 28))
        self.btnluu = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnluu.setGeometry(QtCore.QRect(50, 70, 93, 28))
        self.btnxoa = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnxoa.setGeometry(QtCore.QRect(50, 120, 93, 28))
        self.btnthoat = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnthoat.setGeometry(QtCore.QRect(50, 220, 93, 28))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        layout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.tblds = QtWidgets.QTableWidget(self.groupBox_2)
        self.tblds.setRowCount(0)
        self.tblds.setColumnCount(6)
        self.tblds.setHorizontalHeaderLabels([
            "Mã Hóa Đơn", "Mã Thành Viên", "Mã Lớp", "Số Tiền", "Trạng Thái", "Ngày Thanh Toán"
        ])
        self.tblds.setGeometry(QtCore.QRect(10, 20, 581, 241))
        layout.addWidget(self.tblds)

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
        self.tblds.itemSelectionChanged.connect(self.on_table_selection_changed)
        self.txtmadk.currentTextChanged.connect(self.on_madk_changed)

        # Load dữ liệu ban đầu
        self.load_data()
        self.load_account_ids()
        self.load_cbbmalop()
        self.load_cbbmatv()
        self.load_cbbmadk()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "QUẢN LÝ HÓA ĐƠN"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin hóa đơn:"))
        self.label_5.setText(_translate("MainWindow", "Mã hóa đơn"))
        self.label_11.setText(_translate("MainWindow", "Mã lớp:"))
        self.label_15.setText(_translate("MainWindow", "Mã thành viên"))
        self.label_17.setText(_translate("MainWindow", "Số tiền:"))
        self.label_18.setText(_translate("MainWindow", "Ngày thanh toán:"))
        self.label_19.setText(_translate("MainWindow", "Trạng thái:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tìm kiếm"))
        self.label_20.setText(_translate("MainWindow", "Trạng thái hóa đơn:"))
        self.btnxuat.setText(_translate("MainWindow", "Xuất Excel"))
        self.btntimkiem.setText(_translate("MainWindow", "Tìm kiếm"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Danh sách hóa đơn:"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Xử lý"))
        self.btnthem.setText(_translate("MainWindow", "Thêm"))
        self.btnlammoi.setText(_translate("MainWindow", "Làm mới"))
        self.btnluu.setText(_translate("MainWindow", "Lưu"))
        self.btnxoa.setText(_translate("MainWindow", "Xóa"))
        self.btnthoat.setText(_translate("MainWindow", "Thoát"))

    def load_data(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM hoadon")
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
        self.txtmahoadon_2.clear()
        self.txtmahoadon_2.addItems(["Chưa thanh toán", "Đã thanh toán"])

    def load_cbbmatv(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT ma_tv, ho_ten FROM ThanhVien")
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
            cursor.execute("SELECT ma_lop, ten_lop FROM LopTap")
            rows = cursor.fetchall()
            self.txtmalop.clear()
            self.malop_mapping = {}
            for row in rows:
                ma_lop, ten_lop = row
                display_text = f"{ma_lop} - {ten_lop}"
                self.malop_mapping[display_text] = ma_lop
                self.txtmalop.addItem(display_text)
            cursor.close()
            connection.close()

    def load_cbbmadk(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT ma_dk FROM dangkylop")
            rows = cursor.fetchall()
            self.txtmadk.clear()
            self.txtmadk.addItem("")  # Thêm tùy chọn rỗng
            for row in rows:
                self.txtmadk.addItem(row[0])
            cursor.close()
            connection.close()

    def on_madk_changed(self, madk):
        if not madk:
            # Nếu không chọn mã đăng ký, xóa các trường
            self.txtmahoadon.clear()
            self.txtmatv.setCurrentIndex(-1)
            self.txtmalop.setCurrentIndex(-1)
            self.txtsotien.clear()
            self.txttrangthai.setCurrentIndex(-1)
            self.txtngaythanhtoan.setDate(QtCore.QDate.currentDate())
            return

        connection = get_db_connection()
        if not connection:
            QMessageBox.critical(self.MainWindow, "Lỗi", "Không thể kết nối tới database!")
            return

        cursor = connection.cursor()
        try:
            # Lấy thông tin từ bảng dangkylop
            cursor.execute("SELECT ma_tv, ma_lop FROM dangkylop WHERE ma_dk = %s", (madk,))
            dk_result = cursor.fetchone()
            if dk_result:
                matv, malop = dk_result
                # Gán mã thành viên
                for display_text, ma in self.matv_mapping.items():
                    if ma == matv:
                        self.txtmatv.setCurrentText(display_text)
                        break
                # Gán mã lớp
                for display_text, ma in self.malop_mapping.items():
                    if ma == malop:
                        self.txtmalop.setCurrentText(display_text)
                        break

            # Lấy thông tin hóa đơn liên quan nếu có
            cursor.execute("""
                SELECT ma_hd, ma_tv, ma_lop, so_tien, trang_thai, ngay_thanh_toan 
                FROM HoaDon 
                WHERE ma_lop = %s AND ma_tv = %s
            """, (malop, matv))
            hd_result = cursor.fetchone()

            if hd_result:
                mahd, matv, malop, sotien, trangthai, ngaytt = hd_result
                self.txtmahoadon.setText(mahd)
                self.txtsotien.setText(str(sotien))
                self.txttrangthai.setCurrentText(trangthai)
                date = QtCore.QDate.fromString(ngaytt, "yyyy-MM-dd")
                self.txtngaythanhtoan.setDate(date)
            else:
                # Nếu không có hóa đơn, để trống các trường còn lại
                self.txtmahoadon.clear()
                self.txtsotien.clear()
                self.txttrangthai.setCurrentIndex(-1)
                self.txtngaythanhtoan.setDate(QtCore.QDate.currentDate())

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi lấy thông tin: {str(e)}")
        finally:
            cursor.close()
            connection.close()

    def on_table_selection_changed(self):
        row = self.tblds.currentRow()
        if row != -1:
            mahd = self.tblds.item(row, 0).text()
            matv = self.tblds.item(row, 1).text()
            malop = self.tblds.item(row, 2).text()
            sotien = self.tblds.item(row, 3).text()
            trangthai = self.tblds.item(row, 4).text()
            ngaytt = self.tblds.item(row, 5).text()

            self.txtmahoadon.setText(mahd)
            self.txtsotien.setText(sotien)
            self.txttrangthai.setCurrentText(trangthai)
            date = QtCore.QDate.fromString(ngaytt, "yyyy-MM-dd")
            self.txtngaythanhtoan.setDate(date)

            for display_text, ma in self.matv_mapping.items():
                if ma == matv:
                    self.txtmatv.setCurrentText(display_text)
                    break

            for display_text, ma in self.malop_mapping.items():
                if ma == malop:
                    self.txtmalop.setCurrentText(display_text)
                    break

    def add_account(self):
        try:
            mahd = self.txtmahoadon.text().strip()
            matv_display = self.txtmatv.currentText().strip()
            malop_display = self.txtmalop.currentText().strip()
            tien = self.txtsotien.text().strip()
            trangthai = self.txttrangthai.currentText().strip()
            ngaytt = self.txtngaythanhtoan.date().toString("yyyy-MM-dd")

            matv = self.matv_mapping.get(matv_display)
            malop = self.malop_mapping.get(malop_display)

            if not mahd or not matv or not malop:
                QMessageBox.warning(None, "Lỗi", "Mã hóa đơn, mã thành viên và mã lớp không được để trống!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM HoaDon WHERE ma_hd = %s", (mahd,))
            count = cursor.fetchone()[0]

            if count > 0:
                QMessageBox.warning(None, "Lỗi", "Mã hóa đơn đã tồn tại!")
                cursor.close()
                connection.close()
                return

            cursor.execute("""
                INSERT INTO HoaDon (ma_hd, ma_tv, ma_lop, so_tien, trang_thai, ngay_thanh_toan)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (mahd, matv, malop, tien, trangthai, ngaytt))
            connection.commit()
            QMessageBox.information(None, "Thành công", "Thêm hóa đơn thành công!")
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

    def delete_account(self):
        try:
            row = self.tblds.currentRow()
            if row == -1:
                QMessageBox.warning(None, "Lỗi", "Vui lòng chọn một dòng để xóa!")
                return

            mahd = self.tblds.item(row, 0).text()
            reply = QMessageBox.question(None, "Xác nhận", "Bạn có chắc muốn xóa hóa đơn này?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                connection = get_db_connection()
                if not connection:
                    QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                    return

                cursor = connection.cursor()
                cursor.execute("DELETE FROM HoaDon WHERE ma_hd = %s", (mahd,))
                connection.commit()
                QMessageBox.information(None, "Thành công", "Xóa hóa đơn thành công!")
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

            mahd = self.txtmahoadon.text().strip()
            matv_display = self.txtmatv.currentText().strip()
            malop_display = self.txtmalop.currentText().strip()
            tien = self.txtsotien.text().strip()
            trangthai = self.txttrangthai.currentText().strip()
            ngaytt = self.txtngaythanhtoan.date().toString("yyyy-MM-dd")

            matv = self.matv_mapping.get(matv_display)
            malop = self.malop_mapping.get(malop_display)

            if not mahd or not matv or not malop:
                QMessageBox.warning(None, "Lỗi", "Mã hóa đơn, mã thành viên và mã lớp không được để trống!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()
            cursor.execute("""
                UPDATE HoaDon SET ma_tv = %s, ma_lop = %s, so_tien = %s, trang_thai = %s, ngay_thanh_toan = %s
                WHERE ma_hd = %s
            """, (matv, malop, tien, trangthai, ngaytt, mahd))
            connection.commit()
            QMessageBox.information(None, "Thành công", "Cập nhật hóa đơn thành công!")
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

    def search_account(self):
        try:
            trangthai = self.txtmahoadon_2.currentText()
            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM HoaDon WHERE trang_thai = %s", (trangthai,))
            rows = cursor.fetchall()
            self.tblds.setRowCount(0)
            for row in rows:
                rowPosition = self.tblds.rowCount()
                self.tblds.insertRow(rowPosition)
                for col, value in enumerate(row):
                    self.tblds.setItem(rowPosition, col, QtWidgets.QTableWidgetItem(str(value)))
            cursor.close()
            connection.close()

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi tìm kiếm: {str(e)}")

    def export_data(self):
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "HoaDon Data"
            headers = ["Mã Hóa Đơn", "Mã Thành Viên", "Mã Lớp", "Số Tiền", "Trạng Thái", "Ngày Thanh Toán"]
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

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi xuất Excel: {str(e)}")

    def lam_moi_du_lieu(self):
        try:
            self.txtmahoadon.clear()
            self.txtsotien.clear()
            self.txttrangthai.setCurrentIndex(-1)
            self.txtngaythanhtoan.setDate(QtCore.QDate.currentDate())
            self.txtmatv.setCurrentIndex(-1)
            self.txtmalop.setCurrentIndex(-1)
            self.txtmadk.setCurrentIndex(0)
            self.txtmahoadon_2.setCurrentIndex(-1)
            self.load_data()
            self.load_account_ids()
            self.load_cbbmatv()
            self.load_cbbmalop()
            self.load_cbbmadk()
            QMessageBox.information(None, "Thành công", "Dữ liệu đã được làm mới!")
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi làm mới: {str(e)}")

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