# Revisemos un dato estadístico: https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/

import matplotlib.pyplot as plt

# Grafico de Redes Sociales: hasta 7/2020
labels = 'Facebook', 'Youtube', 'WhatsApp', 'Facebook Messenger', 'Weixin / WeChat', 'Instagram', 'TikTok', 'QQ', 'Sina Weibo', 'QZone', 'Reddit', 'Kuaishou', 'Snapchat', 'Pinterest', 'Twitter'
sizes = [2603, 2000, 2000, 1300, 1203, 1082, 800, 694, 550, 517, 430, 400, 397, 367, 326]
# efexto:
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 


# grafico de barras
fig1, ax1 = plt.subplots()
ax1.invert_yaxis()
ax1.barh(labels, sizes)
plt.show()

# grafico de tora:

fig2, ax1 = plt.subplots()
ax1.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct='%1.2f%%',
    shadow=True,
    startangle=90,
    radius=2
    )
plt.show()
