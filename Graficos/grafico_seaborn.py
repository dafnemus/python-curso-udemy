import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


redes = 'Facebook', 'Youtube', 'WhatsApp', 'Facebook Messenger', 'Weixin / WeChat', 'Instagram', 'TikTok', 'QQ', 'Sina Weibo', 'QZone', 'Reddit', 'Kuaishou', 'Snapchat', 'Pinterest', 'Twitter'
user = [2603, 2000, 2000, 1300, 1203, 1082, 800, 694, 550, 517, 430, 400, 397, 367, 326]
# efexto:
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 

# integro los datos con pandas
pd_redes = pd.DataFrame({'name':redes, 'number in millions':user})
print(pd_redes)

# seaborn:
# estilos
# orientacion

sns.set_style("white")
sns.barplot(y="name", x="number in millions", data=pd_redes, orient="h")
plt.show()

sns.set_style("dark")
sns.barplot(y="name", x="number in millions", data=pd_redes, orient="h")
plt.show()

sns.set_theme(style="whitegrid")
sns.barplot(y="name", x="number in millions", data=pd_redes, orient="h")
plt.show()

g = sns.barplot(x="name", y="number in millions", linewidth=2.5, facecolor=(1, 1, 1, 0), edgecolor=".2", data=pd_redes)
g.set_xticklabels(g.get_xticklabels(), rotation=45)
plt.show()

