def insert_patient_data (name : str,age : int):
    if type(name)== str and type(age)== int:
       print(name)
       print(age)
       print('inserted into database successfully')
    else:
        raise TypeError('Incorrect Data Type')

insert_patient_data ('afrin',25)