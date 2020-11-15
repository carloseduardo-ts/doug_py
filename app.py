import matplotlib.pyplot as plt
import pandas as pd

ws = pd.read_excel('q1.xlsx', sheet_name="p1")
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(ws.x, ws.y)
plt.show()