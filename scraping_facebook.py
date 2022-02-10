import requests
from facebook_scraper import get_posts

import pandas as pd
from datetime import date

cuenta = str(input('Escriba nombre único de cuenta a analizar:\n'))
paginas = int(input('Escriba cantidad de pag a a extraer información:\n'))

def extraer():
    posts = []
    for post in get_posts(cuenta, pages=paginas, options={"comments": True}):
        posts.append(post)
    return posts

posts = extraer()

print('\n\n\nVerifique si la cantidad de post corresponde a la que requiere \nEsta es la cantidad de post extraidos:', len(posts))
# cantidad de post extraidos 
aux = input('Si quiere ajustar la cantidad de paginas a revisar escriba "s" , sino cualquier cosa\n')
while aux == 's' or aux=='S':
    paginas = int(input('Escriba cantidad de pag a a extraer información:\n'))
    posts = extraer()
    aux = input('Si quiere ajustar la cantidad de paginas a revisar escriba "s"\n')

df1 = pd.DataFrame(posts)

tabla_general = df1[['username','post_id','time','post_text','likes','comments','shares','video','image']]

tabla_general.to_excel('tabla_general.xlsx')
print("Creada tabla general de informacion de todos los posts extraidos\n")
select = int(input('Escriba nro de post del que desea extraer comentarios \nRecuerde que se empiezan a contar desde el nro 0\n'))

print('Verificar información del post:\n')
print('fecha de publicación',posts[select]["time"])
print('post id', posts[select]['post_id'])

aux = input('Si se ha equivocado de post escriba "s"\n')
while aux == 's' or aux=='S':
    select = int(input('Escriba nro de post del que desea extraer comentarios \nRecuerde que se empiezan a contar desde el nro 0\n'))
    print('Verificar información del post:\n')
    print('fecha de publicación',posts[select]["time"])
    print('post id', posts[select]['post_id'])
    aux = input('Si se ha equivocado de post escriba "s" sino cualquier cosa\n')

comentarios_pub_x = pd.DataFrame(df1['comments_full'][select])

tabla_comentarios_x = comentarios_pub_x[['comment_id','commenter_name','comment_time','comment_reaction_count',
                                         'comment_text']]
tabla_comentarios_x.to_excel('comentarios_pub_select.xlsx')
print('\n Creada tabla de comentarios en post seleccionado')

f = open('pub_select.jpg','wb')
response = requests.get(df1['image'][select])
f.write(response.content) #guarda imagen
f.close()

print('Imagen correspondiente al post ha sido descargada\n')
print('Todos los archivos se encuentran almacenados en este directorio como:\n')
print('Imagen: pub_select.jpg\nTabla de posts: tabla_general.xlsx\nTabla comentarios: comentarios_pub_select.xlsx')