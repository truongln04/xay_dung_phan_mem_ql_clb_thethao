from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from openpyxl.workbook import Workbook
from Database.data import get_db_connection  # Import hàm kết nối MySQL
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 585)
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
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 851, 561))
        self.lineEdit.setStyleSheet(
            "QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC); }")
        self.lineEdit.setObjectName("lineEdit")

        # GroupBox Thông tin huấn luyện viên
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 601, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 55, 16))
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_15.setObjectName("label_15")
        self.txtmahlv = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtmahlv.setGeometry(QtCore.QRect(100, 40, 161, 22))
        self.txtmahlv.setObjectName("txtmahlv")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(300, 40, 55, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(300, 120, 71, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(300, 80, 91, 16))
        self.label_19.setObjectName("label_19")
        self.txtgioitinh = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtgioitinh.setGeometry(QtCore.QRect(390, 40, 171, 22))
        self.txtgioitinh.addItems(["Nam", "Nữ"])
        self.txtgioitinh.setObjectName("txtgioitinh")
        self.txtsdt = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtsdt.setGeometry(QtCore.QRect(390, 80, 171, 22))
        self.txtsdt.setObjectName("txtsdt")
        self.txtchuyenmon = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtchuyenmon.setGeometry(QtCore.QRect(100, 120, 161, 22))
        self.txtchuyenmon.setObjectName("txtchuyenmon")
        self.txtmaclb = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtmaclb.setGeometry(QtCore.QRect(390, 120, 171, 22))
        self.txtmaclb.setObjectName("txtmaclb")
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_16.setObjectName("label_16")
        self.txtngaysinh = QtWidgets.QDateEdit(parent=self.groupBox)
        self.txtngaysinh.setGeometry(QtCore.QRect(100, 160, 161, 22))
        self.txtngaysinh.setCalendarPopup(True)
        self.txtngaysinh.setDate(QtCore.QDate.currentDate())
        self.txtngaysinh.setDisplayFormat("dd/MM/yyyy")
        self.txtngaysinh.setObjectName("txtngaysinh")
        self.txthoten = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txthoten.setGeometry(QtCore.QRect(100, 80, 161, 22))
        self.txthoten.setObjectName("txthoten")

        # Tiêu đề
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "color: #357ABD; background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC);")
        self.label.setObjectName("label")

        # GroupBox Xử lý
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(620, 280, 181, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.btnthem = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnthem.setGeometry(QtCore.QRect(50, 30, 93, 28))
        self.btnthem.setObjectName("btnthem")
        self.btnlammoi = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnlammoi.setGeometry(QtCore.QRect(50, 180, 93, 28))
        self.btnlammoi.setObjectName("btnlammoi")
        self.btnluu = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnluu.setGeometry(QtCore.QRect(50, 80, 93, 28))
        self.btnluu.setObjectName("btnluu")
        self.btnxoa = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnxoa.setGeometry(QtCore.QRect(50, 130, 93, 28))
        self.btnxoa.setObjectName("btnxoa")
        self.btnthoat = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnthoat.setGeometry(QtCore.QRect(50, 230, 93, 28))
        self.btnthoat.setObjectName("btnthoat")

        # GroupBox Tìm kiếm
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 60, 181, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(20, 30, 98, 16))
        self.label_20.setObjectName("label_20")
        self.txtmahlv_2 = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.txtmahlv_2.setGeometry(QtCore.QRect(20, 50, 131, 22))
        self.txtmahlv_2.setObjectName("txtmahlv_2")
        self.btnxuat = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnxuat.setGeometry(QtCore.QRect(40, 150, 93, 28))
        self.btnxuat.setObjectName("btnxuat")
        self.btntimkiem = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btntimkiem.setGeometry(QtCore.QRect(40, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btntimkiem.setFont(font)
        self.btntimkiem.setObjectName("btntimkiem")

        # GroupBox Danh sách huấn luyện viên
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 601, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tblds = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tblds.setGeometry(QtCore.QRect(10, 30, 581, 221))
        self.tblds.setColumnCount(7)
        self.tblds.setHorizontalHeaderLabels(
            ["Mã HLV", "Họ Tên", "Chuyên Môn", "Ngày Sinh", "Giới Tính", "SĐT", "Mã CLB"])
        self.tblds.setRowCount(0)
        self.tblds.setObjectName("tblds")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.setup_events()
        self.load_data()
        self.load_cbbclb()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quản lý Huấn luyện viên"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin huấn luyện viên:"))
        self.label_5.setText(_translate("MainWindow", "Mã HLV:"))
        self.label_11.setText(_translate("MainWindow", "Họ tên:"))
        self.label_15.setText(_translate("MainWindow", "Chuyên môn:"))
        self.label_17.setText(_translate("MainWindow", "Giới tính:"))
        self.label_18.setText(_translate("MainWindow", "Mã CLB:"))
        self.label_19.setText(_translate("MainWindow", "Số điện thoại:"))
        self.label_16.setText(_translate("MainWindow", "Ngày sinh:"))
        self.label.setText(_translate("MainWindow", "QUẢN LÝ HUẤN LUYỆN VIÊN"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Xử lý"))
        self.btnthem.setText(_translate("MainWindow", "Thêm"))
        self.btnlammoi.setText(_translate("MainWindow", "Làm mới"))
        self.btnluu.setText(_translate("MainWindow", "Lưu"))
        self.btnxoa.setText(_translate("MainWindow", "Xóa"))
        self.btnthoat.setText(_translate("MainWindow", "Thoát"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tìm kiếm"))
        self.label_20.setText(_translate("MainWindow", "Từ khóa tìm kiếm:"))
        self.btnxuat.setText(_translate("MainWindow", "Xuất Excel"))
        self.btntimkiem.setText(_translate("MainWindow", "Tìm kiếm"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Danh sách huấn luyện viên:"))

    def setup_events(self):
        self.btnthem.clicked.connect(self.add_account)
        self.btnxoa.clicked.connect(self.delete_account)
        self.btnluu.clicked.connect(self.update_account)
        self.btntimkiem.clicked.connect(self.search_account)
        self.btnxuat.clicked.connect(self.export_data)
        self.btnlammoi.clicked.connect(self.lam_moi_du_lieu)
        self.btnthoat.clicked.connect(self.MainWindow.close)
        self.tblds.itemSelectionChanged.connect(self.table_item_selected)

    def load_data(self):
        try:
            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
                return
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM HuanLuyenVien")
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
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tải dữ liệu: {str(e)}")

    def load_cbbclb(self):
        try:
            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
                return
            cursor = connection.cursor()
            cursor.execute("SELECT ma_clb, ten_clb FROM CauLacBo")
            rows = cursor.fetchall()
            self.txtmaclb.clear()
            self.club_mapping = {}
            for row in rows:
                ma_clb, ten_clb = row
                display_text = f"{ma_clb} - {ten_clb}"
                self.club_mapping[display_text] = ma_clb
                self.txtmaclb.addItem(display_text)
            cursor.close()
            connection.close()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tải danh sách CLB: {str(e)}")

    def add_account(self):
        try:
            mahlv = self.txtmahlv.text().strip()
            tenhlv = self.txthoten.text().strip()
            chuyenmon = self.txtchuyenmon.text().strip()
            ngaysinh = self.txtngaysinh.date().toString("yyyy-MM-dd")
            gioitinh = self.txtgioitinh.currentText().strip()
            sdt = self.txtsdt.text().strip()
            selected_text = self.txtmaclb.currentText().strip()
            maclb = self.club_mapping.get(selected_text, "")

            if not all([mahlv, tenhlv, chuyenmon, ngaysinh, gioitinh, sdt, maclb]):
                QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
                return
            cursor = connection.cursor()

            cursor.execute("SELECT COUNT(*) FROM HuanLuyenVien WHERE ma_hlv = %s OR sdt = %s", (mahlv, sdt))
            count = cursor.fetchone()[0]
            if count > 0:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Mã HLV hoặc số điện thoại đã tồn tại!")
                return

            cursor.execute("""
                INSERT INTO HuanLuyenVien (ma_hlv, ho_ten, chuyen_mon, ngay_sinh, gioi_tinh, sdt, ma_clb)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (mahlv, tenhlv, chuyenmon, ngaysinh, gioitinh, sdt, maclb))

            connection.commit()
            QMessageBox.information(None, "Thành công", "Thêm huấn luyện viên thành công!")
            self.load_data()
            cursor.close()
            connection.close()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi thêm: {str(e)}")

    def delete_account(self):
        try:
            row = self.tblds.currentRow()
            if row == -1:
                QMessageBox.warning(None, "Lỗi", "Vui lòng chọn mã để xóa!")
                return

            mahlv = self.tblds.item(row, 0).text()
            reply = QMessageBox.question(None, "Xác nhận", "Bạn có chắc muốn xóa huấn luyện viên này?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                connection = get_db_connection()
                if not connection:
                    QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                    return

                cursor = connection.cursor()
                cursor.execute("DELETE FROM HuanLuyenVien WHERE ma_hlv = %s", (mahlv,))
                connection.commit()
                QMessageBox.information(None, "Thành công", "Xóa huấn luyện viên thành công!")
                self.load_data()
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
                QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một huấn luyện viên để sửa!")
                return

            mahlv = self.txtmahlv.text().strip()
            tenhlv = self.txthoten.text().strip()
            chuyenmon = self.txtchuyenmon.text().strip()
            ngaysinh = self.txtngaysinh.date().toString("yyyy-MM-dd")
            gioitinh = self.txtgioitinh.currentText().strip()
            sdt = self.txtsdt.text().strip()
            selected_text = self.txtmaclb.currentText().strip()
            maclb = self.club_mapping.get(selected_text, "")

            if not all([mahlv, tenhlv, chuyenmon, ngaysinh, gioitinh, sdt, maclb]):
                QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
                return
            cursor = connection.cursor()

            cursor.execute("SELECT COUNT(*) FROM HuanLuyenVien WHERE sdt = %s AND ma_hlv != %s", (sdt, mahlv))
            count = cursor.fetchone()[0]
            if count > 0:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Số điện thoại đã tồn tại!")
                return

            cursor.execute("""
                UPDATE HuanLuyenVien 
                SET ho_ten = %s, chuyen_mon = %s, ngay_sinh = %s, gioi_tinh = %s, sdt = %s, ma_clb = %s
                WHERE ma_hlv = %s
            """, (tenhlv, chuyenmon, ngaysinh, gioitinh, sdt, maclb, mahlv))

            connection.commit()
            QMessageBox.information(self.MainWindow, "Thành công", "Cập nhật huấn luyện viên thành công!")
            self.load_data()
            cursor.close()
            connection.close()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi sửa: {str(e)}")

    def search_account(self):
        try:
            keyword = self.txtmahlv_2.text().strip()
            if not keyword:
                self.load_data()
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
                return
            cursor = connection.cursor()

            query = """
                SELECT * FROM HuanLuyenVien 
                WHERE ma_hlv LIKE %s 
                OR ho_ten LIKE %s 
                OR chuyen_mon LIKE %s 
                OR ngay_sinh LIKE %s 
                OR gioi_tinh LIKE %s 
                OR sdt LIKE %s 
                OR ma_clb LIKE %s
            """
            search_term = f"%{keyword}%"
            cursor.execute(query, (search_term, search_term, search_term, search_term, search_term, search_term, search_term))

            rows = cursor.fetchall()
            self.tblds.setRowCount(0)
            for row in rows:
                rowPosition = self.tblds.rowCount()
                self.tblds.insertRow(rowPosition)
                for col, value in enumerate(row):
                    self.tblds.setItem(rowPosition, col, QtWidgets.QTableWidgetItem(str(value)))

            cursor.close()
            connection.close()

            if self.tblds.rowCount() == 0:
                QMessageBox.information(self.MainWindow, "Thông báo", "Không tìm thấy kết quả nào!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tìm kiếm: {str(e)}")

    def export_data(self):
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "HuanLuyenVien Data"
            headers = [self.tblds.horizontalHeaderItem(col).text() for col in range(self.tblds.columnCount())]
            ws.append(headers)
            for row in range(self.tblds.rowCount()):
                row_data = [self.tblds.item(row, col).text() if self.tblds.item(row, col) else ""
                            for col in range(self.tblds.columnCount())]
                ws.append(row_data)
            file_path, _ = QFileDialog.getSaveFileName(self.MainWindow, "Lưu file Excel", "", "Excel Files (*.xlsx)")
            if file_path:
                wb.save(file_path)
                QMessageBox.information(self.MainWindow, "Thành công", "Dữ liệu đã được xuất thành công!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể xuất Excel: {str(e)}")

    def lam_moi_du_lieu(self):
        try:
            self.txtmahlv.clear()
            self.txthoten.clear()
            self.txtgioitinh.setCurrentIndex(0)
            self.txtngaysinh.setDate(QtCore.QDate.currentDate())
            self.txtsdt.clear()
            self.txtchuyenmon.clear()
            self.txtmaclb.setCurrentIndex(-1)
            self.txtmahlv_2.clear()
            self.load_data()
            QMessageBox.information(self.MainWindow, "Thành công", "Dữ liệu đã được làm mới!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể làm mới: {str(e)}")

    def table_item_selected(self):
        selected_row = self.tblds.currentRow()
        if selected_row != -1:
            self.txtmahlv.setText(self.tblds.item(selected_row, 0).text())
            self.txthoten.setText(self.tblds.item(selected_row, 1).text())
            self.txtchuyenmon.setText(self.tblds.item(selected_row, 2).text())
            date_str = self.tblds.item(selected_row, 3).text()
            date = QtCore.QDate.fromString(date_str, "yyyy-MM-dd")
            self.txtngaysinh.setDate(date)
            gender = self.tblds.item(selected_row, 4).text()
            self.txtgioitinh.setCurrentText(gender)
            self.txtsdt.setText(self.tblds.item(selected_row, 5).text())
            ma_clb = self.tblds.item(selected_row, 6).text()
            for i in range(self.txtmaclb.count()):
                item_text = self.txtmaclb.itemText(i)
                if item_text.startswith(ma_clb):
                    self.txtmaclb.setCurrentIndex(i)
                    break


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())