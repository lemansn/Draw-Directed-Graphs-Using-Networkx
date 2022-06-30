# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt

#directed graph olusturuluyor
G = nx.DiGraph()

#düğümleri ekleme
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

#agirliklari ekliyor
G.add_edge(0,1,weight = 5)
G.add_edge(0,2,weight = 3)
G.add_edge(0,4, weight= 2)
G.add_edge(1,3,weight = 6)
G.add_edge(1,2,weight = 2)
G.add_edge(2, 3, weight = 2)
G.add_edge(2,1,weight = 1)
G.add_edge(4,1,weight =6)
G.add_edge(4,3,weight =4)
G.add_edge(4, 2, weight = 10)

G.nodes()

#position ayarlaniyor
G.nodes[0]['pos'] =(3,2)
G.nodes[1]['pos'] = (5,0)
G.nodes[2]['pos'] = (4,-2)
G.nodes[3]['pos'] = (2,-2)
G.nodes[4]['pos'] = (1,0)

#graph'i ekrana cizdirmek icin draw fonksiyonu
def _draw():

    #kose ve kenarlar icin uygun pozisyonlar, olculer, renkler ve yonler ayarlaniyor
    edge_labels=dict([((u,v,),d['weight'])
                  for u,v,d in G.edges(data=True)])
    node_pos=nx.get_node_attributes(G,'pos')
    nx.draw_networkx_edge_labels(G, node_pos, edge_labels=edge_labels, label_pos=0.4, font_size=9)
    node_col = ['red' for node in G.nodes()]
    edge_col = ['black' for edge in G.edges()]
    nx.draw_networkx(G, node_pos,node_color =node_col, node_size=450)
    nx.draw_networkx_edges(G, node_pos,edge_color= edge_col)
    plt.show()

#dijkstra ile en kisa yol uzunluklari bulunuyor
print('{0}. düğümünden {1}. düğüme en kısa yol:'.format(4, 2), nx.dijkstra_path_length(G,4,2))
print('{0}. düğümünden {1}. düğüme en kısa yol:'.format(4, 1), nx.dijkstra_path_length(G, 4, 1))
print('{0}. düğümünden {1}. düğüme en kısa yol:'.format(4, 0), nx.dijkstra_path_length(G, 4, 3))

#olusturulan graph cizdiriliyor
_draw()

# 1 node'u siliniyor ve yeni graph cizdiriliyor
G.remove_node(1)
_draw()
















