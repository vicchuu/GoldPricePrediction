

import pandas as ps


movie_dataset_0 = ps.read_csv("movie.csv")
"""info,describe"""
index=[int(a) for a in range(movie_dataset_0.shape[0])]
movie_dataset_0["id"] = index
#print(movie_dataset_0.info())
#print(movie_dataset_0.describe())

"""Checking null values """
#print(movie_dataset_0.isnull().sum())

"""Filling  NA with mode and mean model"""
#print("*************")

neededColumns = ["title","year","certificate","genre","description","IMDb_rating","directors","id"]

movie_dataset_1 = movie_dataset_0[neededColumns]


for a in neededColumns:
    if movie_dataset_1[a].isnull().sum() > 0:
        if movie_dataset_1[a].dtype =="object":
            #print(a)
            movie_dataset_1[a] = movie_dataset_1[a].fillna('')
        else:
            movie_dataset_1[a] = movie_dataset_1[a].fillna(movie_dataset_1[a].mean())

#print("*************")
#print(movie_dataset_0.isnull().sum())

"""All NA value replaced"""

"""Lets do some scatter plot"""
import matplotlib.pyplot as pt


#dataset.hist()
# from pandas.plotting  import scatter_matrix
#
# scatter_matrix(movie_dataset_0)
# pt.show()

"""Lets decide needed column ...."""
"""[title ,year , certificate , genre ,description,rating,directors"""
#print(movie_dataset_0.columns)

#print(movie_dataset_1.info())

"""printing unique values"""

# for a in movie_dataset_1.columns:
#     print("********")
#     print("Data Column :",a)
#     print(movie_dataset_1[a].nunique())

"""Printing movies name , if movies rate more than 8.7"""

rating =8

# ad = (movie_dataset_1.sort_values(by=movie_dataset_1["IMDb_rating"],ascending=True))
#
# print(ad[:,:10].to_string())

#print(movie_dataset_1[movie_dataset_1["IMDb_rating"]>rating].directors.unique()) #666 movies rating is higher than 5.7 rating



"""splitting genre bt "," """

#movie_dataset_1["newgenre"] = movie_dataset_1['genre'].str.split(',')

# """another way is to groupby"""
#
# print(movie_dataset_1.head(5).to_string())
# a = (movie_dataset_1["newgenre"])
# #
# #print(a)
"""dropping old genre"""
#movie_dataset_2 = movie_dataset_1.drop(["genre"],axis=1)

#print(movie_dataset_1.shape)

movie_dataset_2 = movie_dataset_1.applymap(str)
"""We need to combine all columns into single column feature vector"""
#["title","year","certificate","genre","description","IMDb_rating","directors"]
combined_fearures = movie_dataset_2["title"]+" "+movie_dataset_2["year"]+" "+movie_dataset_2["certificate"]+" "+movie_dataset_2["genre"]+" "\
            +movie_dataset_2["description"]+" " +movie_dataset_2["IMDb_rating"]+" "+movie_dataset_2["directors"]

#print(combined_fearures[0:10].to_string())
"""We need to convert text to numerical data...."""

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

movie_dataset_3 = vectorizer.fit_transform(combined_fearures)

#print(movie_dataset_3)

"""Now all the text is vectorized and converted to numerical value"""

"""now cosine similarity needed to update"""

from sklearn.metrics.pairwise import  cosine_similarity

cosine_similar =  cosine_similarity(movie_dataset_3)

#print(cosine_similar.shape)

movie_list = movie_dataset_1["title"].to_list()
director_list = movie_dataset_1["directors"].to_list()

import difflib


#print(close_match)
#def finding

def find_director_of_movie(dir_name):
    """args: dir name
    function fetch details of director and return the movie related to the director

    :returns str of movie name """
    ans=""
    close_match = difflib.get_close_matches(dir_name,director_list )
    print(close_match)
    close = close_match[0]
    #for l in list_ofMOvie:
    ans = movie_dataset_0[movie_dataset_0.directors == close]['id'].values[0]
    #    ans.append(imdb_index)
    ans=int(ans)
    print("ans :",ans," Close :",close)
    #getting similar types of movies
    #print("Simi :",sim)
    similarity_score = list(enumerate(cosine_similar[ans]))
    print(similarity_score)
    return ans

def find_title_of_movie(tit_name):
    """args: movie title name
    function fetch details of director and return the movie related to the director

    :returns str of movie name """
    ans=""
    close_match = difflib.get_close_matches(tit_name,movie_list )
    print(close_match)
    close = close_match[0]
    #for l in list_ofMOvie:
    ans = movie_dataset_0[movie_dataset_0.title == close]['id'].values[0]
    #    ans.append(imdb_index)
    ans=int(ans)
    print("ans :",ans," Close :",close)
    #getting similar types of movies
    similarity_score = list(enumerate(cosine_similar[ans]))

    #print(similarity_score)

    """need to sort similar movie title"""
    sorted_Similar_movies = sorted(similarity_score,key= lambda x:x[1],reverse=True)
    print("sorted : ",sorted_Similar_movies[:10])

    for a in range (10):
        ind = (sorted_Similar_movies[a])
        print(type(ind) ,ind)

        movie_name = movie_dataset_0[movie_dataset_0.id ==int(ind)]['title'].values[0]
        print(movie_name)
    return ans


l = find_title_of_movie("spider man ")
print(l)