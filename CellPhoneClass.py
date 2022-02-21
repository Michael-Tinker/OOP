class CellPhone:

    def __init__(self,manufacturer,model_num,retail_price):
        self.__manufacturer = manufacturer
        self.__model_num = model_num
        self.__retail_price = retail_price


#Set - Changing
    def set_manufact(self, manufacturer):
        #accepts an argument for the manufacturer
        #can update if necessary
        self.__manufacturer = manufacturer
 
    def set_model(self, model_num):
        #accepts an argument for the model
        #can update if necessary
        self.__model_num = model_num

    def set_retail_price(self, retail_price):
        #accepts an argument for the retail_price
        #can update if necessary
        self.__retail_price = retail_price

#Get - Printing
    def get_manufact(self):
        #returns the phone's manufacturer
        return self.__manufacturer
    def get_model(self):
        #returns the phone's model
        return self.__model_num
    def get_retail_price(self):
        #returns the phone's price
        return self.__retail_price
