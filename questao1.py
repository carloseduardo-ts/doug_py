import matplotlib.pyplot as plt
import pandas as pd

i = input("Digite qual planilha você deseja plotar: ")

ws = pd.read_excel('q1.xlsx', sheet_name=i)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(ws.x, ws.y)
plt.show()
