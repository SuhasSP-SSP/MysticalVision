import sys
import os
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from ui import *
import icons
from ImageClassifier import CreateDataAndModel, Run
_translate = QtCore.QCoreApplication.translate

class function(Ui_MainWindow):
    def gui_functions(self, MainWindow):
        self.submenus.setCurrentIndex(0)

####================ Connecting Push Buttons =================####

        #Home Screen Buttons
        self.create_new_Button.clicked.connect(lambda : self.submenus.setCurrentIndex(1)) 
        self.open_existing_Button.clicked.connect(lambda : self.submenus.setCurrentIndex(4))
        self.help_Button.clicked.connect(lambda : self.submenus.setCurrentIndex(8))
        self.exit_Button.clicked.connect(MainWindow.close)

        #Home Button
        self.homeButtonList = [self.homeButton, self.homeButton_2, self.homeButton_3, self.homeButton_4, self.homeButton_5, self.homeButton_6, self.homeButton_7, self.homeButton_8]
        for self.homeButton in self.homeButtonList:
            self.homeButton.clicked.connect(lambda : self.submenus.setCurrentIndex(0))
        
        #Continue Buttons
        self.continueButton_4.clicked.connect(lambda : self.submenus.setCurrentIndex(5))
        self.continueButton.clicked.connect(lambda : self.submenus.setCurrentIndex(2))

        #Create New Project - create_new_folder
        self.continueButton_2.clicked.connect(lambda : self.submenus.setCurrentIndex(3))
        self.selectfolderButton.clicked.connect(self.selectFolder)

        #Create New Project - create_new_gen
        self.continueButton_3.clicked.connect(lambda : self.submenus.setCurrentIndex(4))
        self.continueButton_3.clicked.connect(self.Generate_Model) #Trigger to generate the model

        #Open existing model - open_existing_select
        self.selectmodelButton.clicked.connect(self.selectModel)

        #Open existing model - open_existing_predict
        self.singleimageButton.clicked.connect(self.predictImage)
        self.multiplemagesButton.clicked.connect(self.predictmultipleImages)

        #Export Button - Result to TXT
        self.exportButton.setShortcut("Ctrl+S")
        self.exportButton.setStatusTip('Save File')
        self.exportButton.clicked.connect(self.file_save)
        #To define the in-def elements at 'def MultiplePredictionsResult()' in 'def predictmultipleImages(self)'
        self.prediction_result = ""
        self.prediction_result_dict = {}
        self.prediction_result_dict_arrange = ""
        self.prediction_result_export = []
        self.prediction_result_text = ""

####================ Main Functions =================####

    def selectFolder(self):
        self.browse = QFileDialog.directory #Pops out the window to select folder
        self.foldersPath = QFileDialog.getExistingDirectory() #Gives path in text as the response from the above selected folder

    def Generate_Model(self):
        self.project_name = self.input_projectname.text()
        self.project_name = self.project_name.replace(" ", "") #11C
        main = CreateDataAndModel(file_path=self.foldersPath+"/", model_file_name_to_save=(self.project_name+".hdf5"), init_lr=0.0001, epochs=2, batch_size=16)
        main.create()

    def selectModel(self):
        self.existingFile_select = QFileDialog.getOpenFileName(None, "Select a Data Model", "", "Data File (*.hdf5)")
        self.modelPath = self.existingFile_select[0] #11C #Tuple Extraction
        # print(self.modelPath)
        self.modelFolderPathDetails = os.path.split(self.modelPath) #Head 0 & Tail 1 - split
        self.modelFolderPath = (self.modelFolderPathDetails[0]) #modelFolderPath is IC Module's input

#------------Image Predictions------------>

#SINGLE IMAGE PREDICTION

    def predictImage(self):
        self.imageDetails = QFileDialog.getOpenFileName(None, "Select an image to predict", "", "Image only (*)")
        self.imagePath = self.imageDetails[0] #Image Path - #11C

        def runSinglePrediction(): #2
            self.result_single.repaint()
            r = Run(model_file_name = self.modelPath, modelFolderPath = self.modelFolderPath) #Model file path, Model folder path
            imagetoPredict = self.imagePath #Folder path for prediction

            pred = r.run(imagetoPredict)
            accuracy = r.results

            def singleImageResult():
                pixmap = QPixmap(self.imagePath)
                self.prediction_image.setPixmap(pixmap)
                self.prediction_image.setScaledContents(True)

                self.single_result_prediction.setText(_translate("MainWindow", pred))
                self.single_result_classes.setText(_translate("MainWindow", str(r.classes)))
                self.single_result_accuracy.setText(_translate("MainWindow", str(accuracy)))
                
                self.result_single.repaint()
                print(r.classes)
                print(accuracy)

            singleImageResult() #To execute

        def continueRunSinglePrediction(): #1
            self.submenus.setCurrentIndex(6)
            self.result_single.repaint()
            runSinglePrediction()
        self.continueButton_5.clicked.connect(continueRunSinglePrediction)

#MULTIPLE IMAGES/FOLDER PREDICTIONS 
          
    def predictmultipleImages(self):
        self.browsePredictionFolder = QFileDialog.directory #Pops out the window to select folder
        self.PredictionFolderPath = QFileDialog.getExistingDirectory() #Gives path in text as the response from the above selected folder

        def runMultiplePredictions():

            r = Run(self.modelPath, modelFolderPath = self.modelFolderPath) #Model file path, Model folder path
            folder_path = (self.PredictionFolderPath+"/")

            def MultiplePredictionsResult():

                prediction_result_tuple = ()
                for file in os.listdir(folder_path):

                    ##>> For Terminal
                    prediction = r.run(folder_path + file)
                    accuracy = r.results
                    # print(file, "-->", prediction, "\t", accuracy, "\n\n")

                    ##>> GUI Display
                    prediction_result_tuple += (file, "-->", prediction, "\n", str(accuracy), "\n\n") #11C
                    self.prediction_result = " ".join(prediction_result_tuple)
                    
                    self.multiple_result_prediction.setText(_translate("MainWindow", str(self.prediction_result)))
                    self.result_multiple.repaint()

                    ##>> For dictionary  -  11C
                    key = file
                    value = prediction
                    self.prediction_result_dict[key] = value
                    self.prediction_result_dict_arrange = json.dumps(self.prediction_result_dict, indent = 1)
                    self.prediction_result_export = ["Mystical Vision \n--------------------\n\n", 'Format ==> "File Name":"Prediction"\n\n', self.prediction_result_dict_arrange]
                    self.prediction_result_text = "".join(self.prediction_result_export)
                    
                    # print(prediction_result) ##-- Terminal Output
                self.multiple_result_classes.setText(_translate("MainWindow", str(r.classes)))

            MultiplePredictionsResult()

        def continueRunMultiplePredictions(): #1
            self.submenus.setCurrentIndex(7)
            self.result_multiple.repaint()
            runMultiplePredictions()
        self.continueButton_5.clicked.connect(continueRunMultiplePredictions)

#Save to Text File

    def file_save(self):
        name = QFileDialog.getSaveFileName(None, "Save the Result of Prediction", "", '*.txt')
        name = name[0]
        file = open(name,'w')
        text = self.prediction_result_text
        file.write(text)
        file.close()

# >>> Execute the program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = function()
    ui.setupUi(MainWindow)
    ui.gui_functions(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())