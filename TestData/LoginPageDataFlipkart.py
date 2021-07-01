import openpyxl
class LoginPageDataFlipkart:

    test_ValidloginCredentials =[{'EnterEmailOrMobNumber': 8130253170, 'EnterPassword': "Bilaspur@123"}]
    test_InvalidloginCredentials = [{"EnterEmailOrMobNumber":8130253170, "EnterPassword":"abc@123"},{"EnterEmailOrMobNumber":8130253170, "EnterPassword":"Bipur@123"},{"EnterEmailOrMobNumber":8130253170, "EnterPassword":"abc@3"}]
    test_NumberForgetPassword = [{"EnterEmailOrMobNumber":8130253170}]

    @staticmethod
    def getTestValidCredentials(test_case_name):
        Dict = {}
        book = openpyxl.load_workbook("C:\\Users\\deepa\\OneDrive\\Desktop\\ValidLoginCredentials.xlsx")
        sheet = book.active
        for i in range(1, sheet.max_row + 1):
            if sheet.cell(row=i, column=1).value == test_case_name:
                for j in range(2, sheet.max_column + 1):
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value

        return[Dict]