import matplotlib.pyplot as plt

print("DIGITE SEUS GANHOS\n")
salario = float(input("SALÁRIO: R$ "))
aluguel = float(input("ALUGUEL: R$ "))
outros  = float(input("OUTROS:  R$ "))

ganhos = salario + aluguel + outros

print("\nDIGITE SUAS DESPESAS\n")
despesas = []
nomes = ["Água","Luz","Cartão de Crédito","Combustível","Gás","Internet","Compras","TV por assinatura"]

comprimentoMaximo = 0
for i in range(len(nomes)):
    if(len(nomes[i]) > comprimentoMaximo):
        comprimentoMaximo = len(nomes[i])


for i in range(len(nomes)):
    print(nomes[i] + ":" + (" "*(comprimentoMaximo-len(nomes[i])+1)) + "R$ ", end='')
    x = float(input())
    despesas.append(x)

despesa = 0
for i in range(len(despesas)):
    despesa += despesas[i]

'''GRÁFICO DE BARRAS'''
# x-coordinates of left sides of bars
left = [1, 2, 3]
 
# heights of bars
height = [ganhos, despesa, ganhos-despesa]
 
# labels for bars
tick_label = ['Ganhos', 'Despesas', 'Resto']
 
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['green', 'red','yellow'])
 
# naming the x-axis
plt.xlabel('')
# naming the y-axis
plt.ylabel('Reais')
# plot title
plt.title('Gastos e ganhos da casa.')
 

'''GRAFICO DE PIZZA'''
# function to show the plot
plt.show()

activities = ['Ganhos', 'Gastos']

# portion covered by each label
slices = [ganhos, despesa]
 
# color for each label
colors = ['green', 'red']
 
# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
        startangle=90, shadow = True,
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()