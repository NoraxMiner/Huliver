input_data = open('input.txt', 'r') 

data= input_data.read() 

#--------------------------------------------------------------------


data = data.split() 
K = int(data[0]) 
M = int(data[1])
aut = K*K*M

#--------------------------------------------------------------------
output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
output_data.write(str(aut))

# ВАЖНО!!! 
# не забываем закрывать открытые ранее файлы!
input_data.close() 
output_data.close()