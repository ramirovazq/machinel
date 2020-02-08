#import matplotlib.pyplot as plt#; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Six',      # six flags
		   'Comida',   # vittorios, comida six flags, mcdonalds perif
		   'Gas',      # gasolina
		   'gmenores', # fsf, farmacia ahorro, pelicula youtube, netflix
		   'kidz')    # entradas youtube
y_pos = np.arange(len(objects))
gastos = [2796+1922, 
			   644+254+280,
			   539.15+300, 
			   189.58+205+110+25+4+169, 
			   199+213]

plt.bar(y_pos, gastos, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Dinero $MXN')
plt.title('Gastos TC diciembre 2020')

print("total de gastos....")
print(sum(gastos))

plt.show()