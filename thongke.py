import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from PyQt6 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Database.data import get_db_connection  # Kết nối MySQL

# Hàm lấy dữ liệu từ MySQL
def get_db_data(query):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        cursor.close()
        connection.close()
        return pd.DataFrame(data, columns=columns)
    except mysql.connector.Error as err:
        print(f"Lỗi khi truy xuất dữ liệu: {err}")
        return pd.DataFrame()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 583)
        MainWindow.setStyleSheet("""
            /* Nút QPushButton */
            QPushButton {
                background-color: #00AEEF;
                color: white;
                font-weight: bold;
                border: 2px solid #0288D1;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0288D1, stop:1 #0277BD);
                color: #FFFFFF;
                border: 2px solid #4FC3F7;
            }
            QPushButton:pressed {
                background-color: #0277BD;
            }

            /* Tiêu đề QLabel#titleLabel */
            QLabel#titleLabel {
                font-size: 24px;
                font-weight: bold;
                color: #00AEEF;
                text-shadow: 2px 2px 4px #333333;
            }

            /* Nền chính QWidget */
            QWidget {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #E1F5FE, stop:1 #B3E5FC);
                color: #0288D1;
                font-weight: bold;
            }

            /* QLineEdit */
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                border: 1px solid #B0BEC5;
                border-radius: 3px;
                padding: 2px;
            }
            QLineEdit:focus {
                border: 2px solid #00AEEF;
            }

            /* QGroupBox */
            QGroupBox {
                font-weight: bold;
                color: #00AEEF;
                border: 1px solid #4FC3F7;
                border-radius: 5px;
                padding: 10px;
                background-color: rgba(0, 174, 239, 20);
            }

            /* QTableWidget */
            QTableWidget {
                background-color: #FFFFFF;
                color: #333333;
                border: 1px solid #B0BEC5;
                font-size: 10px;  /* Giảm kích thước chữ trong bảng */
            }
            QTableWidget::item:selected {
                background-color: #4FC3F7;
                color: #FFFFFF;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tiêu đề
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # GroupBox xử lý
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 60, 181, 501))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")

        self.cbbbd = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.cbbbd.setGeometry(QtCore.QRect(10, 50, 151, 22))
        self.cbbbd.setObjectName("cbbbd")
        self.cbbbd.addItems(["Số lượng thành viên", "Doanh thu CLB", "Tỷ lệ thanh toán"])

        self.btnxem = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnxem.setGeometry(QtCore.QRect(40, 100, 91, 31))
        self.btnxem.setFont(font)
        self.btnxem.setObjectName("btnxem")

        self.btnxuat = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnxuat.setGeometry(QtCore.QRect(40, 150, 93, 28))
        self.btnxuat.setObjectName("btnxuat")

        # GroupBox hiển thị biểu đồ và bảng
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 601, 511))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.chart_layout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.chart_layout.setObjectName("chart_layout")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Kết nối nút
        self.btnxem.clicked.connect(self.show_chart)
        self.btnxuat.clicked.connect(self.export_to_excel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thống kê CLB"))
        self.label.setText(_translate("MainWindow", "THỐNG KÊ"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Xử lý:"))
        self.btnxem.setText(_translate("MainWindow", "Xem"))
        self.btnxuat.setText(_translate("MainWindow", "Xuất Excel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Thống kê:"))

    def show_chart(self):
        # Xóa biểu đồ hoặc bảng cũ nếu có
        for i in reversed(range(self.chart_layout.count())):
            self.chart_layout.itemAt(i).widget().setParent(None)

        choice = self.cbbbd.currentText()
        figsize = (5.5, 4)  # Tăng chiều cao để biểu đồ to và dễ nhìn hơn
        plt.rcParams['font.family'] = 'Arial'

        if choice == "Số lượng thành viên":
            query_tv = """
            SELECT c.ten_clb AS "Câu lạc bộ", COUNT(t.ma_tv) AS "Số lượng thành viên"
            FROM CauLacBo c 
            LEFT JOIN ThanhVien t ON c.ma_clb = t.ma_clb
            GROUP BY c.ten_clb
            ORDER BY COUNT(t.ma_tv) DESC;
            """
            df_tv = get_db_data(query_tv)
            df_tv["Số lượng thành viên"] = df_tv["Số lượng thành viên"].astype(int)

            fig, ax = plt.subplots(figsize=figsize)
            bars = ax.bar(df_tv["Câu lạc bộ"], df_tv["Số lượng thành viên"], color='#4FC3F7', width=0.6)
            ax.set_xlabel("Câu lạc bộ", fontsize=12)
            ax.set_ylabel("Số lượng", fontsize=12)
            ax.set_title("Số lượng thành viên theo CLB", fontsize=14, pad=15)
            ax.tick_params(axis='x', labelsize=10, rotation=0)  # Tăng kích thước chữ, không xoay

            for bar in bars:
                yval = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, yval, int(yval),
                        ha='center', va='bottom', fontsize=10, color='black')

            total_members = df_tv["Số lượng thành viên"].sum()
            ax.text(0.98, 1.1, f'Tổng: {total_members}', transform=ax.transAxes,
                    fontsize=12, ha='right', va='top', bbox=dict(facecolor='white', alpha=0.7))

            # Nhúng biểu đồ vào layout trước
            canvas = FigureCanvas(fig)
            canvas.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
            self.chart_layout.addWidget(canvas)

            # Tạo bảng chi tiết và thêm sau biểu đồ
            query_detail = """
            SELECT c.ten_clb AS "Câu lạc bộ", t.ma_tv AS "Mã thành viên", t.ho_ten AS "Họ tên", 
                   t.ngay_sinh AS "Ngày sinh", t.gioi_tinh AS "Giới tính", t.sdt AS "Số điện thoại", 
                   t.dia_chi AS "Địa chỉ"
            FROM CauLacBo c
            LEFT JOIN ThanhVien t ON c.ma_clb = t.ma_clb
            ORDER BY c.ten_clb, t.ma_tv;
            """
            df_detail = get_db_data(query_detail)
            self.add_table_to_layout(df_detail)

        elif choice == "Doanh thu CLB":
            query_doanhthu = """
            SELECT c.ten_clb AS "Câu lạc bộ", COALESCE(SUM(hd.so_tien), 0) AS "Doanh thu"
            FROM CauLacBo c 
            LEFT JOIN LopTap l ON c.ma_clb = l.ma_clb
            LEFT JOIN HoaDon hd ON l.ma_lop = hd.ma_lop AND hd.trang_thai = 'Đã thanh toán'
            GROUP BY c.ten_clb
            HAVING COALESCE(SUM(hd.so_tien), 0) > 0
            ORDER BY SUM(hd.so_tien) DESC;
            """
            df_doanhthu = get_db_data(query_doanhthu)
            df_doanhthu["Doanh thu"] = df_doanhthu["Doanh thu"].astype(float)

            fig, ax = plt.subplots(figsize=figsize)
            wedges, texts, autotexts = ax.pie(df_doanhthu["Doanh thu"], labels=df_doanhthu["Câu lạc bộ"],
                                              autopct='%1.1f%%', startangle=90, shadow=False,
                                              colors=['#FFD54F', '#4FC3F7', '#FF8A65', '#81C784'],
                                              textprops={'fontsize': 10, 'color': 'black'})
            ax.set_title("Doanh thu theo CLB", fontsize=14, pad=15)

            for i, autotext in enumerate(autotexts):
                money = df_doanhthu["Doanh thu"].iloc[i]
                autotext.set_text(f'{autotext.get_text()}\n{money:,.3f} VNĐ')  # Không hiển thị thập phân
                autotext.set_fontsize(9)

            total_revenue = df_doanhthu["Doanh thu"].sum()
            ax.text(1.4, 0.85, f'Tổng: {total_revenue:,.3f} VNĐ', transform=ax.transAxes,
                    fontsize=12, ha='right', va='top', bbox=dict(facecolor='white', alpha=0.7))

            # Nhúng biểu đồ vào layout trước
            canvas = FigureCanvas(fig)
            canvas.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
            self.chart_layout.addWidget(canvas)

            # Tạo bảng chi tiết và thêm sau biểu đồ
            query_detail = """
            SELECT c.ten_clb AS "Câu lạc bộ", hd.ma_hd AS "Mã hóa đơn", l.ten_lop AS "Tên lớp", 
                   hd.ma_tv AS "Mã thành viên", hd.so_tien AS "Số tiền", 
                   hd.trang_thai AS "Trạng thái", hd.ngay_thanh_toan AS "Ngày thanh toán"
            FROM CauLacBo c
            LEFT JOIN LopTap l ON c.ma_clb = l.ma_clb
            LEFT JOIN HoaDon hd ON l.ma_lop = hd.ma_lop
            WHERE hd.so_tien > 0
            ORDER BY c.ten_clb, hd.ma_hd;
            """
            df_detail = get_db_data(query_detail)
            self.add_table_to_layout(df_detail)

        elif choice == "Tỷ lệ thanh toán":
            query_thanhtoan = """
            SELECT trang_thai, COUNT(ma_hd) AS "Số lượng hóa đơn"
            FROM HoaDon
            GROUP BY trang_thai;
            """
            df_thanhtoan = get_db_data(query_thanhtoan)
            df_thanhtoan["Số lượng hóa đơn"] = df_thanhtoan["Số lượng hóa đơn"].astype(int)

            fig, ax = plt.subplots(figsize=figsize)
            wedges, texts, autotexts = ax.pie(df_thanhtoan["Số lượng hóa đơn"], labels=df_thanhtoan["trang_thai"],
                                              autopct='%1.1f%%', startangle=90, shadow=False,
                                              colors=['#81C784', '#EF5350'],
                                              textprops={'fontsize': 10, 'color': 'black'})
            ax.set_title("Tỷ lệ thanh toán hóa đơn", fontsize=14, pad=15)

            for i, autotext in enumerate(autotexts):
                count = df_thanhtoan["Số lượng hóa đơn"].iloc[i]
                autotext.set_text(f'{autotext.get_text()}\n{count} hóa đơn')
                autotext.set_fontsize(9)

            total_invoices = df_thanhtoan["Số lượng hóa đơn"].sum()
            ax.text(1.4, 0.85, f'Tổng: {total_invoices} hóa đơn', transform=ax.transAxes,
                    fontsize=12, ha='right', va='top', bbox=dict(facecolor='white', alpha=0.7))

            # Nhúng biểu đồ vào layout trước
            canvas = FigureCanvas(fig)
            canvas.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
            self.chart_layout.addWidget(canvas)

            # Tạo bảng chi tiết và thêm sau biểu đồ
            query_detail = """
            SELECT hd.ma_hd AS "Mã hóa đơn", l.ten_lop AS "Tên lớp", c.ten_clb AS "Câu lạc bộ",
                   hd.ma_tv AS "Mã thành viên", hd.so_tien AS "Số tiền", 
                   hd.trang_thai AS "Trạng thái", hd.ngay_thanh_toan AS "Ngày thanh toán"
            FROM HoaDon hd
            LEFT JOIN LopTap l ON hd.ma_lop = l.ma_lop
            LEFT JOIN CauLacBo c ON l.ma_clb = c.ma_clb
            ORDER BY hd.ma_hd;
            """
            df_detail = get_db_data(query_detail)
            self.add_table_to_layout(df_detail)

        # Tự động điều chỉnh bố cục
        plt.tight_layout()

    def add_table_to_layout(self, df):
        # Tạo QTableWidget để hiển thị dữ liệu chi tiết
        table = QtWidgets.QTableWidget()
        table.setRowCount(len(df))
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(df.columns)

        # Điền dữ liệu vào bảng
        for row_idx, row in df.iterrows():
            for col_idx, value in enumerate(row):
                table.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(value)))

        # Tự động điều chỉnh kích thước cột và giới hạn chiều cao bảng
        table.resizeColumnsToContents()
        table.setMaximumHeight(150)  # Giới hạn chiều cao bảng để nhỏ hơn
        table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Thêm thanh cuộn dọc
        table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Thêm thanh cuộn ngang
        table.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)

        # Thêm bảng vào layout
        self.chart_layout.addWidget(table)

    def export_to_excel(self):
        choice = self.cbbbd.currentText()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Lưu file Excel", "", "Excel Files (*.xlsx)")
        if not file_path:
            return

        try:
            if choice == "Số lượng thành viên":
                query_detail = """
                SELECT c.ten_clb AS "Câu lạc bộ", t.ma_tv AS "Mã thành viên", t.ho_ten AS "Họ tên", 
                       t.ngay_sinh AS "Ngày sinh", t.gioi_tinh AS "Giới tính", t.sdt AS "Số điện thoại", 
                       t.dia_chi AS "Địa chỉ"
                FROM CauLacBo c
                LEFT JOIN ThanhVien t ON c.ma_clb = t.ma_clb
                ORDER BY c.ten_clb, t.ma_tv;
                """
                df = get_db_data(query_detail)
                df.to_excel(file_path, index=False)
                self.statusbar.showMessage(f"Đã xuất file: {file_path}", 5000)

            elif choice == "Doanh thu CLB":
                query_detail = """
                SELECT c.ten_clb AS "Câu lạc bộ", hd.ma_hd AS "Mã hóa đơn", l.ten_lop AS "Tên lớp", 
                       hd.ma_tv AS "Mã thành viên", hd.so_tien AS "Số tiền", 
                       hd.trang_thai AS "Trạng thái", hd.ngay_thanh_toan AS "Ngày thanh toán"
                FROM CauLacBo c
                LEFT JOIN LopTap l ON c.ma_clb = l.ma_clb
                LEFT JOIN HoaDon hd ON l.ma_lop = hd.ma_lop
                WHERE hd.so_tien > 0
                ORDER BY c.ten_clb, hd.ma_hd;
                """
                df = get_db_data(query_detail)
                df.to_excel(file_path, index=False)
                self.statusbar.showMessage(f"Đã xuất file: {file_path}", 5000)

            elif choice == "Tỷ lệ thanh toán":
                query_detail = """
                SELECT hd.ma_hd AS "Mã hóa đơn", l.ten_lop AS "Tên lớp", c.ten_clb AS "Câu lạc bộ",
                       hd.ma_tv AS "Mã thành viên", hd.so_tien AS "Số tiền", 
                       hd.trang_thai AS "Trạng thái", hd.ngay_thanh_toan AS "Ngày thanh toán"
                FROM HoaDon hd
                LEFT JOIN LopTap l ON hd.ma_lop = l.ma_lop
                LEFT JOIN CauLacBo c ON l.ma_clb = c.ma_clb
                ORDER BY hd.ma_hd;
                """
                df = get_db_data(query_detail)
                df.to_excel(file_path, index=False)
                self.statusbar.showMessage(f"Đã xuất file: {file_path}", 5000)

        except Exception as e:
            self.statusbar.showMessage(f"Lỗi khi xuất file: {str(e)}", 5000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())