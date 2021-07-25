# Filename: trader.py

"""This app help you trade faster than telgram."""

import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
import requests
from PyQt5.QtCore import QRect, QMetaObject, Qt, QCoreApplication, QTimer
from PyQt5.QtWidgets import QApplication, QGroupBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal

__version__ = '0.1'
__author__ = 'Leodanis Pozo Ramos'

class NewPrice(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    def run(self):
        """Long-running task."""
        while True:
            raw_prices = requests.get("https://fapi.binance.com/fapi/v1/ticker/price?symbol=BTCUSDT").json()
            btc_price = "{} : {}".format("BTCUSDTPERP", raw_prices['price'])
            live_price_label = btc_price
            self.btclabel.setText(live_price_label)
            self.progress.emit(1)


# Create a subclass of QMainWindow to setup the calculator's GUI
class PyTraderUi(QMainWindow):
    """PyCalc's View (GUI)."""

    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Trader')
        self.setFixedSize(800, 600)
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.setupUi()
        # timer = QTimer(self)
        # timer.timeout.connect(self.update_live_prices)
        # timer.start(5000)

    def update_live_prices(self):
        self.thread = QThread()
        self.worker = NewPrice()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()



    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")

        self.resize(1000, 800)
        self.setLayoutDirection(Qt.RightToLeft)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")


        self.strategies = QGroupBox(self.centralwidget)
        self.strategies.setObjectName(u"strategies")
        self.strategies.setGeometry(QRect(20, 10, 391, 134))
        self.strategy_symbol = QLineEdit(self.strategies)
        self.strategy_symbol.setObjectName(u"strategy_symbol")
        self.strategy_symbol.setGeometry(QRect(12, 28, 301, 24))
        self.strategy_symbol_l = QLabel(self.strategies)
        self.strategy_symbol_l.setObjectName(u"strategy_symbol_l")
        self.strategy_symbol_l.setGeometry(QRect(320, 30, 43, 16))
        self.widget = QWidget(self.strategies)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(12, 66, 361, 65))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.strategy_200 = QPushButton(self.widget)
        self.strategy_200.setObjectName(u"strategy_200")

        self.gridLayout_3.addWidget(self.strategy_200, 0, 0, 1, 1)

        self.strategy_100 = QPushButton(self.widget)
        self.strategy_100.setObjectName(u"strategy_100")

        self.gridLayout_3.addWidget(self.strategy_100, 0, 1, 1, 1)

        self.strategy_400 = QPushButton(self.widget)
        self.strategy_400.setObjectName(u"strategy_400")

        self.gridLayout_3.addWidget(self.strategy_400, 1, 0, 1, 1)

        self.strategy_300 = QPushButton(self.widget)
        self.strategy_300.setObjectName(u"strategy_300")

        self.gridLayout_3.addWidget(self.strategy_300, 1, 1, 1, 1)

        self.live = QGroupBox(self.centralwidget)
        self.live.setObjectName(u"live")
        self.live.setGeometry(QRect(419, 20, 351, 79))
        self.gridLayout_2 = QGridLayout(self.live)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btclabel = QLabel(self.live)
        self.btclabel.setObjectName(u"btclabel")

        self.gridLayout_2.addWidget(self.btclabel, 0, 0, 1, 1)

        self.ltclabel = QLabel(self.live)
        self.ltclabel.setObjectName(u"ltclabel")

        self.gridLayout_2.addWidget(self.ltclabel, 1, 0, 1, 1)

        self.marketbuygroup = QGroupBox(self.centralwidget)
        self.marketbuygroup.setObjectName(u"marketbuygroup")
        self.marketbuygroup.setGeometry(QRect(420, 120, 168, 284))
        self.formLayout_2 = QFormLayout(self.marketbuygroup)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.msymbol_l = QLabel(self.marketbuygroup)
        self.msymbol_l.setObjectName(u"msymbol_l")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.msymbol_l)

        self.msymbol = QLineEdit(self.marketbuygroup)
        self.msymbol.setObjectName(u"msymbol")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.msymbol)

        self.mamount_l = QLabel(self.marketbuygroup)
        self.mamount_l.setObjectName(u"mamount_l")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.mamount_l)

        self.mamount = QLineEdit(self.marketbuygroup)
        self.mamount.setObjectName(u"mamount")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.mamount)

        self.mtakeprofit_l = QLabel(self.marketbuygroup)
        self.mtakeprofit_l.setObjectName(u"mtakeprofit_l")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.mtakeprofit_l)

        self.mtakeprofit = QLineEdit(self.marketbuygroup)
        self.mtakeprofit.setObjectName(u"mtakeprofit")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.mtakeprofit)

        self.mstoploss_l = QLabel(self.marketbuygroup)
        self.mstoploss_l.setObjectName(u"mstoploss_l")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.mstoploss_l)

        self.mstoploss = QLineEdit(self.marketbuygroup)
        self.mstoploss.setObjectName(u"mstoploss")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.mstoploss)

        self.mbuy_b = QPushButton(self.marketbuygroup)
        self.mbuy_b.setObjectName(u"mbuy_b")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.mbuy_b)

        self.limitbuygroup = QGroupBox(self.centralwidget)
        self.limitbuygroup.setObjectName(u"limitbuygroup")
        self.limitbuygroup.setGeometry(QRect(600, 110, 168, 391))
        self.formLayout_3 = QFormLayout(self.limitbuygroup)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lsymbol_l = QLabel(self.limitbuygroup)
        self.lsymbol_l.setObjectName(u"lsymbol_l")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lsymbol_l)

        self.lsymbol = QLineEdit(self.limitbuygroup)
        self.lsymbol.setObjectName(u"lsymbol")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lsymbol)

        self.lsymbol_l_2 = QLabel(self.limitbuygroup)
        self.lsymbol_l_2.setObjectName(u"lsymbol_l_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lsymbol_l_2)

        self.lsymbol_2 = QLineEdit(self.limitbuygroup)
        self.lsymbol_2.setObjectName(u"lsymbol_2")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lsymbol_2)

        self.lamount_l = QLabel(self.limitbuygroup)
        self.lamount_l.setObjectName(u"lamount_l")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.lamount_l)

        self.lamount = QLineEdit(self.limitbuygroup)
        self.lamount.setObjectName(u"lamount")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.lamount)

        self.ltakeprofit_l = QLabel(self.limitbuygroup)
        self.ltakeprofit_l.setObjectName(u"ltakeprofit_l")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.ltakeprofit_l)

        self.ltakeprofit = QLineEdit(self.limitbuygroup)
        self.ltakeprofit.setObjectName(u"ltakeprofit")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.ltakeprofit)

        self.lstoploss_l = QLabel(self.limitbuygroup)
        self.lstoploss_l.setObjectName(u"lstoploss_l")

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.lstoploss_l)

        self.lstoploss = QLineEdit(self.limitbuygroup)
        self.lstoploss.setObjectName(u"lstoploss")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.lstoploss)

        self.lbuy_b = QPushButton(self.limitbuygroup)
        self.lbuy_b.setObjectName(u"lbuy_b")

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.lbuy_b)

        self.edit_orders_group = QGroupBox(self.centralwidget)
        self.edit_orders_group.setObjectName(u"edit_orders_group")
        self.edit_orders_group.setGeometry(QRect(20, 150, 391, 208))
        self.gridLayout = QGridLayout(self.edit_orders_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list_orders = QPushButton(self.edit_orders_group)
        self.list_orders.setObjectName(u"list_orders")

        self.gridLayout.addWidget(self.list_orders, 0, 0, 1, 1)

        self.close_all_orders = QPushButton(self.edit_orders_group)
        self.close_all_orders.setObjectName(u"close_all_orders")

        self.gridLayout.addWidget(self.close_all_orders, 1, 0, 1, 1)

        self.close_order = QPushButton(self.edit_orders_group)
        self.close_order.setObjectName(u"close_order")

        self.gridLayout.addWidget(self.close_order, 2, 0, 1, 1)

        self.tpandexit = QPushButton(self.edit_orders_group)
        self.tpandexit.setObjectName(u"tpandexit")

        self.gridLayout.addWidget(self.tpandexit, 3, 0, 1, 1)

        self.tp_all = QPushButton(self.edit_orders_group)
        self.tp_all.setObjectName(u"tp_all")

        self.gridLayout.addWidget(self.tp_all, 4, 0, 1, 1)

        self.panicsell = QPushButton(self.centralwidget)
        self.panicsell.setObjectName(u"panicsell")
        self.panicsell.setGeometry(QRect(420, 420, 171, 28))
        self.toolbox_group = QGroupBox(self.centralwidget)
        self.toolbox_group.setObjectName(u"toolbox_group")
        self.toolbox_group.setGeometry(QRect(20, 370, 391, 139))
        self.toolbox_group.setLayoutDirection(Qt.RightToLeft)
        self.tperiod = QLineEdit(self.toolbox_group)
        self.tperiod.setObjectName(u"tperiod")
        self.tperiod.setGeometry(QRect(200, 30, 137, 24))
        self.ttimeframe = QComboBox(self.toolbox_group)
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.addItem("")
        self.ttimeframe.setObjectName(u"ttimeframe")
        self.ttimeframe.setGeometry(QRect(50, 30, 55, 22))
        self.timeframe_l = QLabel(self.toolbox_group)
        self.timeframe_l.setObjectName(u"timeframe_l")
        self.timeframe_l.setGeometry(QRect(110, 30, 61, 16))
        self.tperiod_l = QLabel(self.toolbox_group)
        self.tperiod_l.setObjectName(u"tperiod_l")
        self.tperiod_l.setGeometry(QRect(340, 30, 34, 16))
        self.splitter = QSplitter(self.toolbox_group)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 100, 351, 28))
        self.splitter.setOrientation(Qt.Horizontal)
        self.temadistance = QPushButton(self.splitter)
        self.temadistance.setObjectName(u"temadistance")
        self.splitter.addWidget(self.temadistance)
        self.ATRpercent = QPushButton(self.splitter)
        self.ATRpercent.setObjectName(u"ATRpercent")
        self.splitter.addWidget(self.ATRpercent)
        self.EMASupport = QPushButton(self.splitter)
        self.EMASupport.setObjectName(u"EMASupport")
        self.splitter.addWidget(self.EMASupport)
        self.orders_status = QPushButton(self.centralwidget)
        self.orders_status.setObjectName(u"orders_status")
        self.orders_status.setGeometry(QRect(420, 460, 171, 28))

        self.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(self)
        self.mbuy_b.clicked.connect(self.update_live_prices)
        QMetaObject.connectSlotsByName(self)

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u06a9\u0645\u06a9 \u062a\u0631\u06cc\u062f\u0631", None))
        self.strategies.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0627\u0633\u062a\u0631\u0627\u062a\u0698\u06cc \u0647\u0627",
                                       None))
        self.strategy_symbol_l.setText(
            QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632 \u0627\u0631\u0632 :", None))
        self.strategy_200.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u062e\u0631\u06cc\u062f 1 \u062f\u0631\u0635\u062f 200 \u062f\u0644\u0627\u0631\u06cc",
                                                             None))
        self.strategy_100.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u062e\u0631\u06cc\u062f 1 \u062f\u0631\u0635\u062f 100 \u062f\u0644\u0627\u0631\u06cc",
                                                             None))
        self.strategy_400.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u062e\u0631\u06cc\u062f 1 \u062f\u0631\u0635\u062f 400 \u062f\u0644\u0627\u0631\u06cc",
                                                             None))
        self.strategy_300.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u062e\u0631\u06cc\u062f 1 \u062f\u0631\u0635\u062f 300 \u062f\u0644\u0627\u0631\u06cc",
                                                             None))
        self.live.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a  \u0644\u062d\u0638\u0647 \u0627\u06cc",
                                       None))
        self.btclabel.setText(
            QCoreApplication.translate("MainWindow", u"\u0628\u06cc\u062a\u06a9\u0648\u06cc\u0646:", None))
        self.ltclabel.setText(
            QCoreApplication.translate("MainWindow", u"\u0644\u0627\u06cc\u062a \u06a9\u0648\u06cc\u0646:", None))
        self.marketbuygroup.setTitle(
            QCoreApplication.translate("MainWindow", u"\u062e\u0631\u06cc\u062f \u0645\u0627\u0631\u06a9\u062a", None))
        self.msymbol_l.setText(
            QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632 \u0627\u0631\u0632 :", None))
        self.msymbol.setText(QCoreApplication.translate("MainWindow", u"LTC", None))
        self.mamount_l.setText(
            QCoreApplication.translate("MainWindow", u"\u0645\u0642\u062f\u0627\u0631 \u062a\u062a\u0631 :", None))
        self.mamount.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.mtakeprofit_l.setText(QCoreApplication.translate("MainWindow", u"\u062d\u062f \u0633\u0648\u062f:", None))
        self.mtakeprofit.setText(QCoreApplication.translate("MainWindow", u"1%", None))
        self.mstoploss_l.setText(QCoreApplication.translate("MainWindow", u"\u062d\u062f \u0636\u0631\u0631 :", None))
        self.mstoploss.setText(QCoreApplication.translate("MainWindow", u"1%", None))
        self.mbuy_b.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u06cc\u062f", None))
        self.limitbuygroup.setTitle(
            QCoreApplication.translate("MainWindow", u"\u062e\u0631\u06cc\u062f \u0644\u06cc\u0645\u06cc\u062a", None))
        self.lsymbol_l.setText(
            QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632 \u0627\u0631\u0632 :", None))
        self.lsymbol.setText(QCoreApplication.translate("MainWindow", u"LTC", None))
        self.lsymbol_l_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0642\u06cc\u0645\u062a \u062e\u0631\u06cc\u062f:", None))
        self.lsymbol_2.setText(QCoreApplication.translate("MainWindow", u"174", None))
        self.lamount_l.setText(
            QCoreApplication.translate("MainWindow", u"\u0645\u0642\u062f\u0627\u0631 \u062a\u062a\u0631:", None))
        self.lamount.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.ltakeprofit_l.setText(QCoreApplication.translate("MainWindow", u"\u062d\u062f \u0633\u0648\u062f:", None))
        self.ltakeprofit.setText(QCoreApplication.translate("MainWindow", u"1%", None))
        self.lstoploss_l.setText(QCoreApplication.translate("MainWindow", u"\u062d\u062f \u0636\u0631\u0631 :", None))
        self.lstoploss.setText(QCoreApplication.translate("MainWindow", u"1%", None))
        self.lbuy_b.setText(QCoreApplication.translate("MainWindow", u"\u062e\u0631\u06cc\u062f", None))
        self.edit_orders_group.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0633\u0641\u0627\u0631\u0634\u0627\u062a", None))
        self.list_orders.setText(QCoreApplication.translate("MainWindow",
                                                            u"\u0644\u06cc\u0633\u062a \u0633\u0641\u0627\u0631\u0634\u0627\u062a",
                                                            None))
        self.close_all_orders.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0628\u0633\u062a\u0646 \u0647\u0645\u0647 \u0633\u0641\u0627\u0631\u0634 \u0647\u0627",
                                                                 None))
        self.close_order.setText(
            QCoreApplication.translate("MainWindow", u"\u0628\u0633\u062a\u0646 \u0633\u0641\u0627\u0631\u0634", None))
        self.tpandexit.setText(QCoreApplication.translate("MainWindow",
                                                          u"\u06af\u0631\u0641\u062a\u0646 \u0633\u0648\u062f \u0648 \u062e\u0631\u0648\u062c",
                                                          None))
        self.tp_all.setText(QCoreApplication.translate("MainWindow",
                                                       u"\u0641\u0631\u0648\u0634 \u0647\u0645\u0647 \u0633\u0641\u0627\u0631\u0634\u0627\u062a",
                                                       None))
        self.panicsell.setText(QCoreApplication.translate("MainWindow",
                                                          u"\u062a\u0628\u062f\u06cc\u0644 \u0647\u0645\u0647 \u0628\u0647 \u062a\u062a\u0631",
                                                          None))
        self.toolbox_group.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0627\u0628\u0632\u0627\u0631\u0647\u0627", None))
        self.tperiod.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.ttimeframe.setItemText(0, QCoreApplication.translate("MainWindow", u"1m", None))
        self.ttimeframe.setItemText(1, QCoreApplication.translate("MainWindow", u"5m", None))
        self.ttimeframe.setItemText(2, QCoreApplication.translate("MainWindow", u"15m", None))
        self.ttimeframe.setItemText(3, QCoreApplication.translate("MainWindow", u"30m", None))
        self.ttimeframe.setItemText(4, QCoreApplication.translate("MainWindow", u"1h", None))
        self.ttimeframe.setItemText(5, QCoreApplication.translate("MainWindow", u"2h", None))
        self.ttimeframe.setItemText(6, QCoreApplication.translate("MainWindow", u"4h", None))
        self.ttimeframe.setItemText(7, QCoreApplication.translate("MainWindow", u"6h", None))
        self.ttimeframe.setItemText(8, QCoreApplication.translate("MainWindow", u"12h", None))
        self.ttimeframe.setItemText(9, QCoreApplication.translate("MainWindow", u"1d", None))
        self.ttimeframe.setItemText(10, QCoreApplication.translate("MainWindow", u"3d", None))
        self.ttimeframe.setItemText(11, QCoreApplication.translate("MainWindow", u"1w", None))
        self.ttimeframe.setItemText(12, QCoreApplication.translate("MainWindow", u"1M", None))

        self.timeframe_l.setText(
            QCoreApplication.translate("MainWindow", u"\u062a\u0627\u06cc\u0645 \u0641\u0631\u06cc\u0645 : ", None))
        self.tperiod_l.setText(QCoreApplication.translate("MainWindow", u"\u067e\u0631\u06cc\u0648\u062f :", None))
        self.temadistance.setText(QCoreApplication.translate("MainWindow", u"EMA Distance", None))
        self.ATRpercent.setText(QCoreApplication.translate("MainWindow", u"ATR %", None))
        self.EMASupport.setText(QCoreApplication.translate("MainWindow", u"EMA Support", None))
        self.orders_status.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0648\u0636\u0639\u06cc\u062a \u0633\u0641\u0627\u0631\u0634\u0627\u062a",
                                                              None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow",
                                                      u"\u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u067e\u06cc\u0634\u0641\u0631\u0636",
                                                      None))
    # retranslateUi


# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pytrader = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyTraderUi()
    view.show()
    # Execute the calculator's main loop
    sys.exit(pytrader.exec_())


if __name__ == '__main__':
    main()
