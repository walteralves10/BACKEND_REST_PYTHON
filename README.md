  
Objetivo
Foi feito uma API simples de trocas de mensagens com diferentes canais. Parecido com o slack

instalação 

Utilização S.O: Windows 10
Banco de dados: MongoDB

Linguagem de programação: Python com framework FastAPI
python 3
pip install fastapi
pip install uvicorn
só é precisoo instalar uma unica vez

compilar API
uvicorn index:app --reload
index -> nome da classe inicial, padrão.
app -> nome da variavel que recebe a biblioteca/framework FastAPI

caso der erro na compilação, tente instalar essas bibliotecas (não me lembro se instalei):
pydantic ou BaseModel
ObjectId

O intuito foi desenvolver uma API com código limpo. 
locais de estudo:
https://fastapi.tiangolo.com/pt/ -> Documentação
https://www.youtube.com/watch?v=yZifRUvxdAk&list=PLQCmSnNFVYnQ28Gd7SmWiM-dChqaWiy8i -> o exemplo usado para API neste video esta 
em JavaScript mas da pra pegar uma noção de Estruturação do codigo
https://www.youtube.com/watch?v=G7hZlOLhhMY -> Video explicativo com FastAPI Python. Busquei esse video pra entender um pouco mais 
como a API funcionaria com todos os recursos. Evitar perca de tempo com alguns erros iniciantes. Depois de analisar o codigo fui colocar
em pratica a Estruturação de acordo com o primeiro video, pois, a forma estrutural estava mais harmonica.
