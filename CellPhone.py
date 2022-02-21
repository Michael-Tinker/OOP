import CellPhoneClass as cp

def main():
    # Get the starting inputs
   manufacturer = input('Enter the phone manufacturer: ')
   model_num = input("Enter the phone model number: ")
   retail_price = float(input("Enter the phone retail price: "))

   # Create a Phone object.
   cellphone = cp.CellPhone(manufacturer, model_num, retail_price)

   # Display the phone's details according to the class
   print("manufacturer: ", cellphone.get_manufact())
   print("Model: ", cellphone.get_model())
   print("Retail Price: ", cellphone.get_retail_price())
   
   # Updating the phone details
   new_man = input("What is the phone manufactuere: ")
   new_num = input("What is the phone model number: ")
   new_price = float(input("What is the phone price: "))
   cellphone.set_manufact(new_man)
   cellphone.set_model(new_num)
   cellphone.set_retail_price(new_price)

   # Display the balance.
   print("manufacturer: ", cellphone.get_manufact())
   print("Model: ", cellphone.get_model())
   print("Retail Price: ", cellphone.get_retail_price())
   

main()