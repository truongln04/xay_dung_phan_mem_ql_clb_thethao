from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from openpyxl.workbook import Workbook
from Database.data import get_db_connection  # Import hàm kết nối MySQL


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 593)
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
                font-size: 10px;
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
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 821, 571))
        self.listView.setStyleSheet(
            "QWidget { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC); }")

        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 290, 601, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)

        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 70, 181, 201))
        self.groupBox_3.setFont(font)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 55, 16))
        font_label = QtGui.QFont()
        font_label.setPointSize(10)
        font_label.setBold(True)
        self.label_9.setFont(font_label)
        self.txtmalop_2 = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.txtmalop_2.setGeometry(QtCore.QRect(10, 50, 151, 22))
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(10, 90, 31, 31))
        self.label_16.setPixmap(QtGui.QPixmap("anh/timkiem.png"))
        self.label_16.setScaledContents(True)
        self.btnxuat = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnxuat.setGeometry(QtCore.QRect(40, 149, 91, 31))
        self.btnxuat.setFont(font)
        self.btntimkiem = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btntimkiem.setGeometry(QtCore.QRect(40, 100, 91, 31))
        self.btntimkiem.setFont(font)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 201, 41))
        font_title = QtGui.QFont()
        font_title.setPointSize(12)
        font_title.setBold(True)
        font_title.setWeight(75)
        self.label.setFont(font_title)
        self.label.setStyleSheet(
            "color: #4A90E2;"
            " background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC);")

        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(620, 290, 181, 271))
        self.groupBox_5.setFont(font)
        self.btnthem = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnthem.setGeometry(QtCore.QRect(40, 20, 100, 31))
        self.btnthem.setFont(font)
        self.btnluu = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnluu.setGeometry(QtCore.QRect(40, 70, 100, 31))
        self.btnluu.setFont(font)
        self.btnxoa = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnxoa.setGeometry(QtCore.QRect(40, 120, 100, 31))
        self.btnxoa.setFont(font)
        self.btnthoat = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnthoat.setGeometry(QtCore.QRect(40, 220, 100, 31))
        self.btnthoat.setFont(font)
        self.btnlammoi = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnlammoi.setGeometry(QtCore.QRect(40, 170, 100, 31))
        self.btnlammoi.setFont(font)

        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 601, 201))
        self.groupBox.setFont(font)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.label_2.setFont(font_label)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 55, 16))
        self.label_3.setFont(font_label)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 55, 16))
        self.label_4.setFont(font_label)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 55, 16))
        self.label_5.setFont(font_label)
        self.txtmalop = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtmalop.setGeometry(QtCore.QRect(70, 40, 191, 22))
        self.txttenlop = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txttenlop.setGeometry(QtCore.QRect(70, 80, 191, 22))
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(290, 40, 55, 16))
        self.label_6.setFont(font_label)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(290, 120, 91, 16))
        self.label_7.setFont(font_label)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(290, 80, 91, 16))
        self.label_8.setFont(font_label)
        self.txthocphi = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txthocphi.setGeometry(QtCore.QRect(380, 40, 191, 22))
        self.txtngaybatdau = QtWidgets.QDateEdit(parent=self.groupBox)
        self.txtngaybatdau.setGeometry(QtCore.QRect(380, 80, 191, 22))
        self.txtngaybatdau.setCalendarPopup(True)
        self.txtngaybatdau.setDate(QtCore.QDate.currentDate())
        self.txtngaybatdau.setDisplayFormat("dd/MM/yyyy")
        self.txtngayketthuc = QtWidgets.QDateEdit(parent=self.groupBox)
        self.txtngayketthuc.setGeometry(QtCore.QRect(380, 120, 191, 22))
        self.txtngayketthuc.setCalendarPopup(True)
        self.txtngayketthuc.setDate(QtCore.QDate.currentDate())
        self.txtngayketthuc.setDisplayFormat("dd/MM/yyyy")
        self.txtmaclb = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtmaclb.setGeometry(QtCore.QRect(70, 120, 191, 22))
        self.txtmahlv = QtWidgets.QComboBox(parent=self.groupBox)
        self.txtmahlv.setGeometry(QtCore.QRect(70, 160, 191, 22))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        layout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.tblds = QtWidgets.QTableWidget(self.groupBox_2)
        self.tblds.setRowCount(0)
        self.tblds.setColumnCount(7)
        self.tblds.setHorizontalHeaderLabels([
            "Mã Lớp", "Tên Lớp", "Mã CLB", "Mã HLV", "Học Phí", "Ngày Bắt Đầu", "Ngày Kết Thúc"
        ])
        self.tblds.setGeometry(QtCore.QRect(10, 20, 581, 241))
        layout.addWidget(self.tblds)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Kết nối sự kiện
        self.txtmaclb.currentIndexChanged.connect(self.update_hlv_based_on_clb)
        self.btnthem.clicked.connect(self.add_account)
        self.btnxoa.clicked.connect(self.delete_account)
        self.btnluu.clicked.connect(self.update_account)
        self.btntimkiem.clicked.connect(self.search_account)
        self.btnxuat.clicked.connect(self.export_data)
        self.btnlammoi.clicked.connect(self.lam_moi_du_lieu)
        self.btnthoat.clicked.connect(self.thoat)
        self.tblds.itemSelectionChanged.connect(self.table_item_selected)

        # Load dữ liệu ban đầu
        self.load_data()
        self.load_cbbclb()
        self.load_cbbmalop2()
        self.load_cbbmahlv()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Danh sách lớp tập:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tìm kiếm"))
        self.label_9.setText(_translate("MainWindow", "Tên lớp:"))
        self.btnxuat.setText(_translate("MainWindow", "Xuất Excel"))
        self.btntimkiem.setText(_translate("MainWindow", "Tìm kiếm"))
        self.label.setText(_translate("MainWindow", "QUẢN LÝ LỚP TẬP"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Xử lí"))
        self.btnthem.setText(_translate("MainWindow", "Thêm"))
        self.btnluu.setText(_translate("MainWindow", "Lưu"))
        self.btnxoa.setText(_translate("MainWindow", "Xóa"))
        self.btnthoat.setText(_translate("MainWindow", "Thoát"))
        self.btnlammoi.setText(_translate("MainWindow", "Làm mới"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin lớp tập"))
        self.label_2.setText(_translate("MainWindow", "Mã lớp:"))
        self.label_3.setText(_translate("MainWindow", "Tên lớp:"))
        self.label_4.setText(_translate("MainWindow", "Mã CLB:"))
        self.label_5.setText(_translate("MainWindow", "Mã HLV:"))
        self.label_6.setText(_translate("MainWindow", "Học phí:"))
        self.label_7.setText(_translate("MainWindow", "Ngày kết thúc:"))
        self.label_8.setText(_translate("MainWindow", "Ngày bắt đầu:"))

    def load_data(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM loptap")
            rows = cursor.fetchall()
            self.tblds.setRowCount(0)
            for row in rows:
                rowPosition = self.tblds.rowCount()
                self.tblds.insertRow(rowPosition)
                for col, value in enumerate(row):
                    self.tblds.setItem(rowPosition, col, QtWidgets.QTableWidgetItem(str(value)))
            cursor.close()
            connection.close()

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

    def load_cbbmahlv(self):
        # Ban đầu để trống, sẽ được cập nhật khi chọn CLB
        self.txtmahlv.clear()
        self.hlv_mapping = {}

    def load_cbbmalop2(self):
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT ten_lop FROM LopTap")
            rows = cursor.fetchall()
            self.txtmalop_2.clear()
            for row in rows:
                self.txtmalop_2.addItem(row[0])
            cursor.close()
            connection.close()

    def update_hlv_based_on_clb(self):
        try:
            selected_clb = self.txtmaclb.currentText().strip()
            maclb = self.club_mapping.get(selected_clb, "")
            if not maclb:
                self.txtmahlv.clear()
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Không thể kết nối đến cơ sở dữ liệu!")
                return

            cursor = connection.cursor()
            cursor.execute("""
                SELECT ma_hlv, ho_ten 
                FROM HuanLuyenVien 
                WHERE ma_clb = %s
            """, (maclb,))
            rows = cursor.fetchall()

            self.txtmahlv.clear()
            self.hlv_mapping = {}
            for row in rows:
                ma_hlv, ho_ten = row
                display_text = f"{ma_hlv} - {ho_ten}"
                self.hlv_mapping[display_text] = ma_hlv
                self.txtmahlv.addItem(display_text)

            cursor.close()
            connection.close()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi cập nhật danh sách HLV: {str(e)}")

    def add_account(self):
        try:
            malop = self.txtmalop.text().strip()
            tenlop = self.txttenlop.text().strip()
            selected_clb = self.txtmaclb.currentText().strip()
            maclb = self.club_mapping.get(selected_clb, "")
            selected_hlv = self.txtmahlv.currentText().strip()
            mahlv = self.hlv_mapping.get(selected_hlv, "") if selected_hlv else ""
            hocphi = self.txthocphi.text().strip()
            ngaybd = self.txtngaybatdau.date().toString("yyyy-MM-dd")
            ngaykt = self.txtngayketthuc.date().toString("yyyy-MM-dd")

            if not malop or not tenlop:
                QMessageBox.warning(None, "Lỗi", "Mã lớp và Tên lớp không được để trống!")
                return

            if ngaykt <= ngaybd:
                QMessageBox.warning(None, "Lỗi", "Ngày kết thúc phải lớn hơn ngày bắt đầu!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM LopTap WHERE ma_lop = %s", (malop,))
            count = cursor.fetchone()[0]

            if count > 0:
                QMessageBox.warning(None, "Lỗi", "Mã lớp đã tồn tại!")
                cursor.close()
                connection.close()
                return

            cursor.execute("""
                INSERT INTO LopTap (ma_lop, ten_lop, ma_clb, ma_hlv, hoc_phi, ngay_bat_dau, ngay_ket_thuc)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (malop, tenlop, maclb, mahlv, hocphi, ngaybd, ngaykt))
            connection.commit()
            QMessageBox.information(None, "Thành công", "Thêm lớp tập thành công!")
            self.load_data()
            self.load_cbbmalop2()
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

            malop = self.tblds.item(row, 0).text()
            reply = QMessageBox.question(None, "Xác nhận", "Bạn có chắc muốn xóa lớp tập này?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                connection = get_db_connection()
                if not connection:
                    QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                    return

                cursor = connection.cursor()
                cursor.execute("DELETE FROM LopTap WHERE ma_lop = %s", (malop,))
                connection.commit()
                QMessageBox.information(None, "Thành công", "Xóa lớp tập thành công!")
                self.load_data()
                self.load_cbbmalop2()
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

            malop = self.txtmalop.text().strip()
            tenlop = self.txttenlop.text().strip()
            selected_clb = self.txtmaclb.currentText().strip()
            maclb = self.club_mapping.get(selected_clb, "")
            selected_hlv = self.txtmahlv.currentText().strip()
            mahlv = self.hlv_mapping.get(selected_hlv, "") if selected_hlv else ""
            hocphi = self.txthocphi.text().strip()
            ngaybd = self.txtngaybatdau.date().toString("yyyy-MM-dd")
            ngaykt = self.txtngayketthuc.date().toString("yyyy-MM-dd")

            if not malop or not tenlop:
                QMessageBox.warning(None, "Lỗi", "Mã lớp và Tên lớp không được để trống!")
                return

            if ngaykt <= ngaybd:
                QMessageBox.warning(None, "Lỗi", "Ngày kết thúc phải lớn hơn ngày bắt đầu!")
                return

            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()
            cursor.execute("""
                UPDATE LopTap SET ten_lop = %s, ma_clb = %s, ma_hlv = %s, hoc_phi = %s, ngay_bat_dau = %s, ngay_ket_thuc = %s
                WHERE ma_lop = %s
            """, (tenlop, maclb, mahlv, hocphi, ngaybd, ngaykt, malop))
            connection.commit()
            QMessageBox.information(None, "Thành công", "Cập nhật lớp tập thành công!")
            self.load_data()
            self.load_cbbmalop2()
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
            tenlop = self.txtmalop_2.currentText()
            connection = get_db_connection()
            if not connection:
                QMessageBox.critical(None, "Lỗi", "Không thể kết nối tới database!")
                return

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM LopTap WHERE ten_lop = %s", (tenlop,))
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
            ws.title = "LopTap Data"
            headers = ["Mã Lớp", "Tên Lớp", "Mã CLB", "Mã HLV", "Học Phí", "Ngày Bắt Đầu", "Ngày Kết Thúc"]
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
            self.txtmalop.clear()
            self.txttenlop.clear()
            self.txthocphi.clear()
            self.txtngayketthuc.setDate(QtCore.QDate.currentDate())
            self.txtngaybatdau.setDate(QtCore.QDate.currentDate())
            self.txtmaclb.setCurrentIndex(-1)
            self.txtmahlv.setCurrentIndex(-1)
            self.txtmalop_2.setCurrentIndex(-1)
            self.load_data()
            QMessageBox.information(None, "Thành công", "Dữ liệu đã được làm mới!")
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Lỗi khi làm mới: {str(e)}")

    def thoat(self):
        reply = QMessageBox.question(None, "Xác nhận", "Bạn có muốn thoát không?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()

    def table_item_selected(self):
        selected_row = self.tblds.currentRow()
        if selected_row != -1:
            self.txtmalop.setText(self.tblds.item(selected_row, 0).text())
            self.txttenlop.setText(self.tblds.item(selected_row, 1).text())

            ma_clb = self.tblds.item(selected_row, 2).text()
            for i in range(self.txtmaclb.count()):
                item_text = self.txtmaclb.itemText(i)
                if item_text.startswith(ma_clb):
                    self.txtmaclb.setCurrentIndex(i)
                    break

            ma_hlv = self.tblds.item(selected_row, 3).text()
            for i in range(self.txtmahlv.count()):
                item_text = self.txtmahlv.itemText(i)
                if item_text.startswith(ma_hlv):
                    self.txtmahlv.setCurrentIndex(i)
                    break

            self.txthocphi.setText(self.tblds.item(selected_row, 4).text())
            start_date = QtCore.QDate.fromString(self.tblds.item(selected_row, 5).text(), "yyyy-MM-dd")
            self.txtngaybatdau.setDate(start_date)
            end_date = QtCore.QDate.fromString(self.tblds.item(selected_row, 6).text(), "yyyy-MM-dd")
            self.txtngayketthuc.setDate(end_date)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())