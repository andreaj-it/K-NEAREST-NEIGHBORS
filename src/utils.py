def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L 

def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L   

def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0] ##fetching the movie index
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate( distances)),reverse =True , key = lambda x:x[1])[1:6]
    
    for i in movie_list:
        print(new_df.iloc[i[0]].title)