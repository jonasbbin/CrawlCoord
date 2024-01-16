import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout, QFileDialog, QTextEdit, QSizePolicy, QCheckBox, QMessageBox
from identification import Identifier
from PyQt5.QtGui import QPalette, QColor
import pandas as pd
import numpy as np
"""
Main window of the application
"""
class Coord2Community(QWidget):
    def __init__(self,):
        #Initilizes fields for the window
        super().__init__()
        self.X = ""
        self.Y = ""

        self.identifier = Identifier()

        self.gemeinde , self.canton, self.country = self.identifier.get_gemeinde_region_canton(self.X, self.Y)
        self.region = ""
        self.corr = False
        self.old_cords = False
        self.init_ui()

    def update_gemeinde(self):
        """
        Updates Gemeinde, Kanton and Land
        """
        self.gemeinde, self.canton, self.country = self.identifier.get_gemeinde_region_canton(int(self.x_coord_entry.text()), int(self.y_coord_entry.text()))
        self.gemeinde_entry.setText(self.gemeinde)
        self.canton_entry.setText(self.canton)
        self.land_entry.setText(self.country)

    
    def init_ui(self):
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        # Get the system background color
        sys_palette = QApplication.palette()
        sys_background_color = sys_palette.color(QPalette.Window)
        custom_color_2 = QColor(8, 90, 111) 
        custom_color = QColor(30, 8, 90) 
        custom_color = QColor(8, 8, 51)
        custom_color_2 = QColor(4, 4, 30) 

        manualdesc = QLineEdit(self)
        manualdesc.setText("Manuelle Eingabe")
        manualdesc.setReadOnly(True) 
        manualdesc.setStyleSheet(f"background-color: {custom_color.name()}")#palette(window)")  # Set text color to grey
        manualdesc.setToolTip("Fahre über andere Titel/Buttons um mehr Information zu erfahren")
        grid_layout.addWidget(manualdesc , 13, 0, 1, 2)

        self.x_coord_entry = QLineEdit(self)
        self.x_coord_entry.setText(str("X-Koordinate"))
        self.x_coord_entry.setStyleSheet("color: white")  # Set initial text color to grey
        self.x_coord_entry.selectAll()  # Select all text when entry is focused

        self.y_coord_entry = QLineEdit(self)
        self.y_coord_entry.setText(str("Y-Koordinate"))
        self.y_coord_entry.setStyleSheet("color: white")  # Set initial text color to grey
        self.y_coord_entry.selectAll()  # Select all text when entry is focused

        self.gemeinde_entry = QLineEdit(self)
        self.gemeinde_entry.setText("Gemeinde")
        self.gemeinde_entry.setStyleSheet("color: white")  # Set initial text color to grey
        self.gemeinde_entry.selectAll()  # Select all text when entry is focused

        self.canton_entry = QLineEdit(self)
        self.canton_entry.setText("Kanton")
        self.canton_entry.setStyleSheet("color: white")  # Set initial text color to grey
        self.canton_entry.selectAll()  # Select all text when entry is focused

        self.land_entry = QLineEdit(self)
        self.land_entry.setText("Land")
        self.land_entry.setStyleSheet("color: white")  # Set initial text color to grey
        self.land_entry.selectAll()  # Select all text when entry is focused

        start_button = QPushButton("Starten", self)
        start_button.setToolTip("Startet das Programm. Das neue File wird im gleichen Ordner mit dem Zusatz '_adapted' generiert.")
        start_button.clicked.connect(self.adaptation)

        region_update = QPushButton("Berechnen", self)
        region_update.setToolTip('Berechnet die Gemeinde, den Kanton und das Land der gegebenen Koordinaten.')
        region_update.clicked.connect(self.update_gemeinde)

        title_1 = QLineEdit(self)
        title_1.setText("Automatische Eingabe")
        title_1.setStyleSheet(f"background-color: {custom_color.name()}")  # Set text color to grey
        title_1.setToolTip("Fahre über andere Titel/Buttons um mehr Information zu erfahren")
        title_1.setReadOnly(True)
        grid_layout.addWidget(title_1, 1,0, 1, 2) 
        
        path_title_2 = QTextEdit(self)
        path_title_2.setPlainText("""Dieses Tool erschafft Gemeinde-, Kantons- und Landeseinträge zu gegebenen Koordinaten.""")

        path_title_2.setReadOnly(True)
        path_title_2.setStyleSheet(f"background-color: {sys_background_color.name()};")
        path_title_2.setGeometry(0, 0, 50, 50)  
        grid_layout.addWidget(path_title_2 , 0, 0, 1, 2)

        select_button_2 = QPushButton('File auswählen', self)
        select_button_2.clicked.connect(self.get_file)
        select_button_2.setToolTip('Wähle die Excel-Datei welche gelesen werden sollte und für die Berechnung benützt wird.')
        grid_layout.addWidget(select_button_2, 2 , 0)

        self.file_path_entry = QLineEdit(self)
        self.file_path_entry.setText("Filepfad")
        self.file_path_entry.setStyleSheet("color: white")  
        grid_layout.addWidget(self.file_path_entry, 2, 1)


        koordtitle = QLineEdit(self)
        koordtitle.setText("Input-Spaltennamen")
        #koordtitle.setStyleSheet("background-color: palette(window)")  # Set text color to grey
        koordtitle.setToolTip('Spaltennamen der Koordinaten in der Exceltabelle.')
        koordtitle.setReadOnly(True)
        koordtitle.setStyleSheet(f"background-color: {custom_color_2.name()}") 
        grid_layout.addWidget(koordtitle , 3, 0, 1, 1)

        self.x_coord_name = QLineEdit(self)
        self.x_coord_name.setText("X")
        self.x_coord_name.setStyleSheet("color: white")  # Set initial text color to grey
        grid_layout.addWidget(self.x_coord_name, 4, 0)

        self.y_coord_name = QLineEdit(self)
        self.y_coord_name.setText("Y")
        self.y_coord_name.setStyleSheet("color: white")  # Set initial text color to grey
        grid_layout.addWidget(self.y_coord_name, 4, 1)
        
        koordtitle_2 = QLineEdit(self)
        koordtitle_2.setText("Output-Spaltennamen")
        koordtitle_2.setReadOnly(True)
        koordtitle_2.setStyleSheet(f"background-color: {custom_color_2.name()}")
        koordtitle_2.setToolTip('Spaltennamen der respektiven Kolonnen in der neuen Exceltabelle. Falls die Namen bereits existieren werden alte Kolonnen überschrieben.')
        grid_layout.addWidget(koordtitle_2 , 5, 0, 1, 1)

        self.gemeinde_name = QLineEdit(self)
        self.gemeinde_name.setText("Gemeinde")
        self.gemeinde_name.setStyleSheet("color: white")  # Set initial text color to grey
        grid_layout.addWidget(self.gemeinde_name, 6, 0)

        self.canton_name = QLineEdit(self)
        self.canton_name.setText("Kanton")
        self.canton_name.setStyleSheet("color: white")  # Set initial text color to grey
        grid_layout.addWidget(self.canton_name, 6, 1)

        self.country_name = QLineEdit(self)
        self.country_name.setText("Land")
        self.country_name.setStyleSheet("color: white")  # Set initial text color to grey



        spacer = QWidget(self)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid_layout.addWidget(spacer, 12 , 0 , 1 , 2)

        checkbox = QCheckBox('Alte Koordinaten', self)
        checkbox.stateChanged.connect(self.checkboxStateChanged_coords)
        checkbox.setToolTip('Wandelt Koordinaten im alten Koordinatensystem in neue um. Ansonsten werden sie ignoriert.')
        
        grid_layout.addWidget(checkbox, 9, 0)

        checkbox_2 = QCheckBox('Automatische Fehlerkorrektur', self)
        checkbox_2.stateChanged.connect(self.checkboxStateChanged_correction)
        checkbox_2.setToolTip('Korrigiert automatisch Koordinateneinträge welche zu kurz oder lang sind, bis sie im neuen Koordinatensystem sind.')
        grid_layout.addWidget(checkbox_2, 9, 1)

        grid_layout.addWidget(self.country_name, 7, 0)  

        grid_layout.addWidget(start_button, 10,0,1,2)


        grid_layout.addWidget(self.x_coord_entry, 14, 0)
        
        grid_layout.addWidget(self.y_coord_entry, 14, 1)

        grid_layout.addWidget(self.gemeinde_entry, 19, 0)
        grid_layout.addWidget(region_update, 16,0)

        grid_layout.addWidget(self.canton_entry, 19, 1)

        grid_layout.addWidget(self.land_entry, 20, 0)

        main_layout = QVBoxLayout()
        
        main_layout.addLayout(layout)
        main_layout.addLayout(grid_layout)
        self.setTabOrder(path_title_2,self.x_coord_name)
        self.setTabOrder(manualdesc,self.x_coord_name)
        self.setTabOrder(self.file_path_entry,self.x_coord_name)
        self.setTabOrder(self.x_coord_name, self.y_coord_name)
        self.setTabOrder(self.y_coord_name, self.gemeinde_name)
        self.setTabOrder(self.gemeinde_name, self.canton_name)
        self.setTabOrder(self.canton_name, self.country_name)
        self.setTabOrder(self.country_name, self.x_coord_entry)
        self.setTabOrder(self.x_coord_entry, self.y_coord_entry)
        self.setTabOrder(self.y_coord_entry, self.gemeinde_entry)
        self.setTabOrder(self.gemeinde_entry, self.canton_entry)
        self.setTabOrder(self.canton_entry, self.canton_entry)
        self.setTabOrder(self.canton_entry, self.land_entry)
        
        self.setLayout(main_layout)
        self.setWindowTitle("Koordinaten zu Gemeinde/Kanton/Land")
        self.setFixedSize(450, 550)  # Set window size to 1000, 700
        self.show()
        self.raise_()

    def checkboxStateChanged_coords(self):
        self.old_cords = not self.old_cords
        #print("Old coords:", self.old_cords)

    def checkboxStateChanged_correction(self):
        self.corr = not self.corr
        #print("Corr:", self.corr)

    def get_file(self):
        """
        Let's the user select a file
        """
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Select a file')
        self.file_path_entry.setText(file_path)

    def adaptation(self):
        def modify_coords(row, x='Korrdinaten X', y='Korrdinaten Y', old_coordinates=True, corrections=True):
            try:

                x_coord = int(row[x])
                y_coord = int(row[y])
                if corrections:
                    while x_coord < 100000:
                        x_coord = x_coord*10
                    while x_coord >= 10000000:
                        x_coord = int(x_coord / 10)


                    while y_coord < 100000:
                        y_coord = y_coord*10
                    while y_coord>= 10000000:
                        y_coord = int(y_coord/10)


                if old_coordinates:
                    if x_coord< 1000000 and x_coord >= 100000 :
                        x_coord += 2000000
                    if y_coord< 1000000 and y_coord >= 100000 :
                        y_coord += 1000000

                row[x] = int(x_coord)
                row[y] = int(y_coord)

                return row
            except Exception as e:
                #print(e)
                return row



        filename = self.file_path_entry.text() 
        x_name = self.x_coord_name.text()
        y_name = self.y_coord_name.text()
        commun_out = self.gemeinde_name.text()
        canton_out = self.canton_name.text()
        country_out = self.country_name.text()

        try: 
            spider_data = pd.read_excel(filename)
            
        except Exception:
            QMessageBox.critical(self, 'Error', f'Datei konnte nicht gelesen werden. Überprüfe den Dateipfad und die Datei.')
            return

        try: 
            identifier = Identifier()
            spider_data = spider_data.apply(lambda row:  modify_coords(row, x_name, y_name, self.old_cords, self.corr), axis=1)
            gemeinden = spider_data.apply(lambda row: identifier.get_gemeinde_region_canton(row[x_name], row[y_name]), axis=1)

            gemeinden = [list(t) for t in gemeinden]
            gemeinden = np.array(gemeinden)
            spider_data[commun_out] = gemeinden[:,0]
            spider_data[canton_out] = gemeinden[:,1]
            spider_data[country_out] = gemeinden[:,2]
        
            spider_data.to_excel(f"{filename[0:-5]}_adapted.xlsx", index=False)

            # Create a QMessageBox
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Notification")
            msg_box.setText(f"Neue Excel Datei erfolgreich erstellt.")

            # Add an "Okay" button
            okay_button = QPushButton("Okay")
            msg_box.addButton(okay_button, QMessageBox.AcceptRole)

            # Connect the button to close the message box
            okay_button.clicked.connect(msg_box.accept)

            # Show the message box
            result = msg_box.exec_()
        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', f'Fehler beim vearbeiten der Koordinaten. Überprüfe Spaltennamen oder Koordinaten.')
    def on_submit(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    ex = Coord2Community()
    app.exec_()
    #sys.exit(app.exec_())


if __name__ == '__main__':
    main()
