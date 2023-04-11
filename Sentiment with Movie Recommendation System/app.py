import base64
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import pandas as pd
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
import streamlit_authenticator as stauth
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from streamlit_lottie import st_lottie
import json



hide='''

<style>
#MainMenu {visibility : hidden;}
footer {visibility : hidden;}
</style>
'''
st.markdown(hide,unsafe_allow_html=True)


names = ['Pasupathi', 'user']
usernames = ['Pasupathi', 'user']
passwords = ['456', '123']
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('LOGIN', 'main')

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('Images/login.jpg')
if authentication_status:

    selected = option_menu(menu_title='Main Menu', options=['HomePage', 'Recommend', 'Sentiment', 'Visualization', 'Dataset','Logout'],
                           orientation='horizontal',icons=['house','camera-reels','emoji-smile-fill','graph-up-arrow','download','door-closed-fill'],menu_icon='list')
    if selected =='Logout':
        def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
                f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
                unsafe_allow_html=True
            )
        add_bg_from_local('Images/login.jpg')
        st.write('')
        st.subheader('Click to Logout ')
        authenticator.logout('Logout', 'main')

    if selected == 'HomePage':
        def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
                f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
                unsafe_allow_html=True
            )


        add_bg_from_local('Images/bga.jpg')

        tren = pickle.load(open('pickle/trend.pkl', 'rb'))
        trend = pd.DataFrame(tren)
        rat = pickle.load(open('pickle/rate.pkl', 'rb'))
        rate = pd.DataFrame(rat)
        pop = pickle.load(open('pickle/popular.pkl', 'rb'))
        popular = pd.DataFrame(pop)
        bud = pickle.load(open('pickle/budget.pkl', 'rb'))
        budget = pd.DataFrame(bud)


        def fetchtitle(movie):
            title = movie['title']
            return list(title.values)


        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
                    movie_id))
            data = response.json()
            return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


        def fetch_id(movie):
            movieid = trend[trend['title'] == movie].index[0]
            id = trend[trend['title'] == movie].movie_id.values
            return id[0]


        def fetch_idrate(movie):
            idd = rate[rate['title'] == movie].movie_id.values
            return idd[0]


        def fetch_idpop(movie):
            idd = popular[popular['title'] == movie].movie_id.values
            return idd[0]


        def fetch_idbud(movie):
            idd = budget[budget['title'] == movie].movie_id.values
            return idd[0]


        # top 10 trending
        st.title('Top 10 Trending Movies 📈')
        st.write(' ')
        title = fetchtitle(trend)
        col1, col2, col3, col4, col5 = st.columns(5)
        col6, col7, col8, col9, col10 = st.columns(5)

        with col1:
            movid = fetch_id(title[0])
            poster = fetch_poster(movid)
            st.text(title[0])
            st.image(poster)
        with col2:
            movid = fetch_id(title[1])
            poster = fetch_poster(movid)
            st.text(title[1])
            st.image(poster)

        with col3:
            movid = fetch_id(title[2])
            poster = fetch_poster(movid)
            st.text(title[2])
            st.image(poster)

        with col4:
            movid = fetch_id(title[3])
            poster = fetch_poster(movid)
            st.text(title[3])
            st.image(poster)

        with col5:
            movid = fetch_id(title[4])
            poster = fetch_poster(movid)
            st.text(title[4])
            st.image(poster)

        st.write('')
        with col6:
            movid = fetch_id(title[5])
            poster = fetch_poster(movid)
            st.text(title[5])
            st.image(poster)

        with col7:
            movid = fetch_id(title[6])
            poster = fetch_poster(movid)
            st.text(title[6])
            st.image(poster)

        with col8:
            movid = fetch_id(title[7])
            poster = fetch_poster(movid)
            st.text(title[7])
            st.image(poster)

        with col9:
            movid = fetch_id(title[9])
            poster = fetch_poster(movid)
            st.text(title[9])
            st.image(poster)
        with col10:
            movid = fetch_id(title[8])
            poster = fetch_poster(movid)
            st.text(title[8])
            st.image(poster)

        st.write('')

        # top rated movies
        st.title('Top Rated Movies 🚀')
        st.write(' ')
        ratetit = fetchtitle(rate)
        col11, col12, col13, col14, col15 = st.columns(5)
        col16, col17, col18, col19, col20 = st.columns(5)
        with col11:
            movid = fetch_idrate(ratetit[0])
            poster = fetch_poster(movid)
            st.text(ratetit[0])
            st.image(poster)

        with col12:
            movid = fetch_idrate(ratetit[1])
            poster = fetch_poster(movid)
            st.text(ratetit[1])
            st.image(poster)

        with col13:
            movid = fetch_idrate(ratetit[2])
            poster = fetch_poster(movid)
            st.text(ratetit[2])
            st.image(poster)

        with col14:
            movid = fetch_idrate(ratetit[3])
            poster = fetch_poster(movid)
            st.text(ratetit[3])
            st.image(poster)

        with col15:
            movid = fetch_idrate(ratetit[4])
            poster = fetch_poster(movid)
            st.text(ratetit[4])
            st.image(poster)

        st.write('')
        st.write('')
        with col16:
            movid = fetch_idrate(ratetit[5])
            poster = fetch_poster(movid)
            st.text(ratetit[5])
            st.image(poster)

        with col17:
            movid = fetch_idrate(ratetit[6])
            poster = fetch_poster(movid)
            st.text(ratetit[6])
            st.image(poster)

        with col18:
            movid = fetch_idrate(ratetit[7])
            poster = fetch_poster(movid)
            st.text(ratetit[7])
            st.image(poster)

        with col19:
            movid = fetch_idrate(ratetit[8])
            poster = fetch_poster(movid)
            st.text(ratetit[8])
            st.image(poster)

        with col20:
            movid = fetch_idrate(ratetit[9])
            poster = fetch_poster(movid)
            st.text(ratetit[9])
            st.image(poster)

        st.write('')
        st.write('')
        st.title('High Budget Movies 💵💲')
        st.write(' ')
        budtit = fetchtitle(budget)
        col31, col32, col33, col34, col35 = st.columns(5)
        col36, col37, col38, col39, col40 = st.columns(5)
        with col31:
            movid = fetch_idbud(budtit[0])
            poster = fetch_poster(movid)
            st.text(budtit[0])
            st.image(poster)
        with col32:
            movid = fetch_idbud(budtit[1])
            poster = fetch_poster(movid)
            st.text(budtit[1])
            st.image(poster)
        with col33:
            movid = fetch_idbud(budtit[2])
            poster = fetch_poster(movid)
            st.text(budtit[2])
            st.image(poster)
        with col34:
            movid = fetch_idbud(budtit[3])
            poster = fetch_poster(movid)
            st.text(budtit[3])
            st.image(poster)
        with col35:
            movid = fetch_idbud(budtit[4])
            poster = fetch_poster(movid)
            st.text(budtit[4])
            st.image(poster)
        st.write('')
        st.write('')
        with col36:
            movid = fetch_idbud(budtit[5])
            poster = fetch_poster(movid)
            st.text(budtit[5])
            st.image(poster)
        with col37:
            movid = fetch_idbud(budtit[6])
            poster = fetch_poster(movid)
            st.text(budtit[6])
            st.image(poster)
        with col38:
            movid = fetch_idbud(budtit[7])
            poster = fetch_poster(movid)
            st.text(budtit[7])
            st.image(poster)
        with col39:
            movid = fetch_idbud(budtit[8])
            poster = fetch_poster(movid)
            st.text(budtit[8])
            st.image(poster)
        with col40:
            movid = fetch_idbud(budtit[9])
            poster = fetch_poster(movid)
            st.text(budtit[9])
            st.image(poster)

        # popular
        st.title('Most Popular Movies 📉')
        st.write(' ')
        poptit = fetchtitle(popular)
        col21, col22, col23, col24, col25 = st.columns(5)
        col26, col27, col28, col29, col30 = st.columns(5)
        with col21:
            movid = fetch_idpop(poptit[0])
            poster = fetch_poster(movid)
            st.text(poptit[0])
            st.image(poster)

        with col22:
            movid = fetch_idpop(poptit[1])
            poster = fetch_poster(movid)
            st.text(poptit[1])
            st.image(poster)

        with col23:
            movid = fetch_idpop(poptit[2])
            poster = fetch_poster(movid)
            st.text(poptit[2])
            st.image(poster)

        with col24:
            movid = fetch_idpop(poptit[3])
            poster = fetch_poster(movid)
            st.text(poptit[3])
            st.image(poster)

        with col25:
            movid = fetch_idpop(poptit[4])
            poster = fetch_poster(movid)
            st.text(poptit[4])
            st.image(poster)

        st.write('')
        st.write('')
        with col26:
            movid = fetch_idpop(poptit[5])
            poster = fetch_poster(movid)
            st.text(poptit[5])
            st.image(poster)

        with col27:
            movid = fetch_idpop(poptit[6])
            poster = fetch_poster(movid)
            st.text(poptit[6])
            st.image(poster)

        with col28:
            movid = fetch_idpop(poptit[7])
            poster = fetch_poster(movid)
            st.text(poptit[7])
            st.image(poster)

        with col29:
            movid = fetch_idpop(poptit[8])
            poster = fetch_poster(movid)
            st.text(poptit[8])
            st.image(poster)

        with col30:
            movid = fetch_idpop(poptit[9])
            poster = fetch_poster(movid)
            st.text(poptit[9])
            st.image(poster)


    if selected == 'Recommend':
        # browser title
        # st.set_page_config(page_title='Recommendation System')
        # page setting
        # st.sidebar.success('Select the aboves page :')

        # 🏠
        # st.set_page_config(layout="wide")
        # Background - Image
        def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
                f"""
               <style>
               .stApp {{
                   background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                   background-size: cover
               }}
               </style>
               """,
                unsafe_allow_html=True
            )


        add_bg_from_local('Images/wb.jpg')


        # Fetch Poster

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
                    movie_id))
            data = response.json()
            return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

            recommended_movies = []
            recommended_movies_posters = []
            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)

                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        movies_dict = pickle.load(open('pickle/movie_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)
        stor = pickle.load(open('pickle/story.pkl', 'rb'))
        story = pd.DataFrame(stor)
        dir = pickle.load(open('pickle/directorlst.pkl', 'rb'))
        director = pd.DataFrame(dir)
        similarity = pickle.load(open('pickle/similarity.pkl', 'rb'))
        movstory = pickle.load(open('pickle/moviestory.pkl', 'rb'))
        newstory = pd.DataFrame(movstory)

        # st.title('Movie Recommender System')
        new_title = '<p style="font-family:Georgia ;text-align:center; color:#ff5252; font-size: 36px;"><b>MOVIE RECOMMENDATION <b></p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.write('')
        st.write('')
        selected_movie_name = st.selectbox(
            'CHOOSE YOUR FAVOURITE MOVIE',
            movies['title'].values)
        st.write('')

        def header(name):
            return name

        def conimg(movie):
            movieid = movies[movies['title'] == movie].index[0]
            id = movies.iloc[movieid].movie_id
            return id
        def movstory(movie):
            movid = movies[movies['title'] == movie].index[0]
            content = newstory.iloc[movid]
            content = content.values[0]
            return content

        def fetch_directorname(movie):
            drid = movies[movies['title'] == movie].index[0]
            director_name = director.iloc[drid]
            director_name = director_name.values
            director_name = tuple(*director_name)[0]
            return director_name

        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            st.write('')
            movietitle = header(selected_movie_name)
            con = conimg(selected_movie_name)
            fetch = fetch_poster(con)
            moviestory = movstory(selected_movie_name)
            container = st.container()
            dirname = fetch_directorname(selected_movie_name)
            st.write('')
            conmovhed = f'<p style="font-size: 30px"><b>Overview of  {selected_movie_name}</b></p>'
            st.markdown(conmovhed, unsafe_allow_html=True)
            conmov = f'<p style="font-size: 15px;text-align:justify">{moviestory}.</p>'
            st.markdown(conmov, unsafe_allow_html=True)
            st.write('')
            condir = f'<p style="font-size: 30px"><b>Director of  {selected_movie_name}</b></p>'
            st.markdown(condir, unsafe_allow_html=True)
            condirname = f'<p style="font-size: 15px"> {dirname}</p>'
            st.markdown(condirname, unsafe_allow_html=True)
            #st.subheader("Director of " + selected_movie_name)
            #st.write(dirname)

            st.header(movietitle)
            st.write('')
            left, center, right = st.columns(3)
            with left:
                st.write("")
            with center:
                st.image(fetch, width=250)
            with right:
                st.write('')
            # st.text_area(moviestory)
            st.write('')

            st.header("The Suggest Movie Names")
            st.write('')
            st.write('')

            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)
            col5, col6 = st.columns(2)
            col7, col8 = st.columns(2)
            newcol = st.columns(1)


            def fetch_details(movie):
                #new_title = '<p style="font-family:Georgia ;text-align:center; color:#ff5252; font-size: 36px;"><b>MOVIE RECOMMENDATION <b></p>'
                conname=f'<p style="font-size: 20px"><b> Overview of {movie}</b></p>'
                st.markdown(conname, unsafe_allow_html=True)
                moviestory1 = movstory(movie)
                constry = f'<p style="font-size: 15px;text-align:justify">{moviestory1}.</p>'
                st.markdown(constry, unsafe_allow_html=True)
                condir = f'<p style="font-size: 20px"><b> Director </b></p>'
                st.markdown(condir, unsafe_allow_html=True)
                dirname1 = fetch_directorname(movie)
                condirname = f'<p style="font-size: 15px">  {dirname1}</p>'
                st.markdown(condirname, unsafe_allow_html=True)
                st.write(" ")
                st.write(" ")


            with col1:
                st.text(names[0])
                st.image(posters[0], width=230)
                movie1 = names[0]
                fetch_details(movie1)

            with col2:
                st.text(names[1])
                st.image(posters[1], width=230)
                movie2 = names[1]
                fetch_details(movie2)

            with col3:
                st.text(names[2])
                st.image(posters[2], width=230)
                movie3 = names[2]
                fetch_details(movie3)

            with col4:
                st.text(names[3])
                st.image(posters[3], width=230)
                movie4 = names[3]
                fetch_details(movie4)

            with col5:
                st.text(names[4])
                st.image(posters[4], width=230)
                movie5 = names[4]
                fetch_details(movie5)

            with col6:
                st.text(names[5])
                st.image(posters[5], width=230)
                movie6 = names[5]
                fetch_details(movie6)
            with col7:
                st.text(names[6])
                st.image(posters[6], width=230)
                movie7 = names[6]
                fetch_details(movie7)
            with col8:
                st.text(names[7])
                st.image(posters[7], width=230)
                movie8 = names[7]
                fetch_details(movie8)

    if selected == 'Sentiment':

        def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
                f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
                unsafe_allow_html=True
            )


        add_bg_from_local('Images/black.jpg')


        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()




        movies_dict = pickle.load(open('pickle/movie_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)
        stor = pickle.load(open('pickle/story.pkl', 'rb'))
        story = pd.DataFrame(stor)
        dir = pickle.load(open('pickle/directorlst.pkl', 'rb'))
        director = pd.DataFrame(dir)
        similarity = pickle.load(open('pickle/similarity.pkl', 'rb'))
        movstory = pickle.load(open('pickle/moviestory.pkl', 'rb'))
        newstory = pd.DataFrame(movstory)

        # title
        new_title = '<p style="font-family:Georgia ;text-align:center; color:#ff5252; font-size: 36px;"><b>SENTIMENT WITH MOVIE<b></p>'
        st.markdown(new_title, unsafe_allow_html=True)

        st.write('')
        st.write('')
        left, center, right = st.columns(3)
        with left:
            with open('./lottie/col1.json', "r") as file:
                url = json.load(file)
            st_lottie(url, height=210, width=230)

        with center:
            with open('./lottie/col2.json', "r") as file:
                url = json.load(file)
            st_lottie(url, height=200, width=200)
        with right:
            with open('./lottie/col3.json', "r") as file:
                url = json.load(file)
            st_lottie(url, height=200, width=200)
        # select movie title
        selected_movie_name = st.selectbox(
            'CHOOSE YOUR FAVOURITE MOVIE',
            movies['title'].values)


        def header(name):
            return name


        def conimg(movie):
            movieid = movies[movies['title'] == movie].index[0]
            id = movies.iloc[movieid].movie_id
            return id


        def movstory(movie):
            movid = movies[movies['title'] == movie].index[0]
            content = newstory.iloc[movid]
            content = content.values
            return content


        def fetch_directorname(movie):
            drid = movies[movies['title'] == movie].index[0]
            director_name = director.iloc[drid]
            director_name = director_name.values
            director_name = tuple(*director_name)
            return director_name


        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
                    movie_id))
            data = response.json()
            return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

            recommended_movies = []
            recommended_movies_posters = []
            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)

                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        st.write('')
        if st.button('Search'):

            names, posters = recommend(selected_movie_name)
            st.write('')
            movietitle = header(selected_movie_name)
            con = conimg(selected_movie_name)
            fetch = fetch_poster(con)
            moviestory = movstory(selected_movie_name)
            container = st.container()
            dirname = fetch_directorname(selected_movie_name)
            st.header(movietitle)
            left, center, right = st.columns(3)
            with left:
                st.write("")
            with center:
                st.image(fetch, width=250)
            with right:
                st.write('')
            st.write('')
            st.subheader("Overview of " + selected_movie_name)
            st.markdown(*moviestory)
        st.write('')
        title = st.text_input('Enter The Movie Story')
        st.write('')
        if st.button('Analyse Story'):
            lower_case = title.lower()
            cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
            tokenized_words = word_tokenize(cleaned_text, 'english')
            final_words = []
            for word in tokenized_words:
                if word not in stopwords.words('english'):
                    final_words.append(word)


            def sentiment(words):
                score = SentimentIntensityAnalyzer().polarity_scores(words)
                return score

            word = ' '.join(final_words)

            v = sentiment(word)
            per = {key: round(val * 100) for key, val in v.items()}
            del per['compound']
            i = per['neg']
            k = 'neg'
            for key, val in per.items():
                if i < val:
                    i = val
                    k = key
            kvalue=i

            st.write('')
            st.write('')
            subtitle = '<p style="font-family:Georgia ; color:#ff5252; font-size: 36px;"><b>Sentiment Analyse of Movie Story<b></p>'
            st.markdown(subtitle, unsafe_allow_html=True)
            if k == 'pos':
                st.write('')
                st.subheader(f'The Story of {selected_movie_name} is Positive 😊'.format(selected_movie_name))
                st.subheader('Positive Score is '+str(kvalue) + ' %')
                lottie_url = "https://assets6.lottiefiles.com/packages/lf20_NBpLbW.json"
                lottie_json = load_lottieurl(lottie_url)
                st_lottie(lottie_json, height=400, width=600)

            elif k == 'neg':
                st.write('')
                st.header(f'The Story of {selected_movie_name} is Negative 😡'.format(selected_movie_name))
                st.subheader('Negative Score is ' + str(kvalue) + ' %')
                with open('./lottie/neg.json', "r") as file:
                    url = json.load(file)
                st_lottie(url, height=400, width=600)

            elif k == 'neu':
                st.write('')
                st.header(f'The Story of {selected_movie_name} is Neutral 😐'.format(selected_movie_name))
                st.subheader(r'Neutral Score is ' + str(kvalue) + ' %')
                with open('./lottie/neu.json', "r") as file:
                    url = json.load(file)
                st_lottie(url, height=400, width=600)


    if selected == 'Visualization':
        def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
                f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
                unsafe_allow_html=True
            )


        add_bg_from_local('Images/bga.jpg')

        bud = pickle.load(open('pickle/budget.pkl', 'rb'))
        budget = pd.DataFrame(bud)
        tren = pickle.load(open('pickle/trend.pkl', 'rb'))
        trend = pd.DataFrame(tren)
        rat = pickle.load(open('pickle/rate.pkl', 'rb'))
        rate = pd.DataFrame(rat)
        pop = pickle.load(open('pickle/popular.pkl', 'rb'))
        popular = pd.DataFrame(pop)


        new_title = '<p style="font-family:Georgia ;text-align:center; color:#ff5252; font-size: 36px;"><b>CHARTS<b></p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.write('')
        st.write('')

        trending = '<p style="color:#ff5252; font-size: 36px;"><b>TRENDING MOVIES 📈<b></p>'
        st.markdown(trending, unsafe_allow_html=True)
        trend_plot = px.histogram(trend, x='title', y='revenue', color='title')
        st.plotly_chart(trend_plot)
        st.write('')
        st.write('')
        highbud = '<p style=" color:#ff5252; font-size: 36px;"><b>HIGH BUDGET MOVIES 💵💲<b></p>'
        st.markdown(highbud, unsafe_allow_html=True)
        budget_plot = px.bar(budget, x=budget['budget'], y=budget['title'], color='title')
        st.plotly_chart(budget_plot)
        st.write('')
        st.write('')
        popmov = '<p style="color:#ff5252; font-size: 36px;"><b>POPULAR MOVIES 📉<b></p>'
        st.markdown(popmov, unsafe_allow_html=True)
        budget_plot = px.area(popular, x='title', y='popularity', color='title')
        st.plotly_chart(budget_plot)
        st.write('')
        st.write('')
        toprat = '<p style="color:#ff5252; font-size: 36px;"><b>TOP RATED MOVIES 🚀<b></p>'
        st.markdown(toprat, unsafe_allow_html=True)
        trend_plot = px.funnel(rate, x='title', y='vote_count', color='title')
        st.plotly_chart(trend_plot)

    if selected == 'Dataset':
        def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
                f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
                unsafe_allow_html=True
            )


        add_bg_from_local('Images/bga.jpg')

        df = pd.read_csv('datasets/Final.csv')


        @st.cache_data
        def convert(df):
            return df.to_csv(index=False).encode('utf-8')


        st.title('DATASETS 📊')

        tmdb_credits = pd.read_csv('datasets/tmdb_5000_credits.csv')
        tmdb_movies = pd.read_csv('datasets/tmdb_5000_movies.csv')
        final = pd.read_csv('datasets/Final.csv')

        st.write('')
        st.write('')
        st.header('Dataset for Credits 📽️🎬')
        st.write(tmdb_credits)
        st.write('')
        st.write('')
        st.header('Dataset for Movies 🍿🎟️')
        st.write(tmdb_movies)
        st.write('')
        st.write('')
        st.header('Final Dataset 🏁')
        st.write(final)
        st.write('')
        st.write('')
        csv = convert(df)
        st.download_button('📥 Download Dataset', csv, 'Final.csv', 'text/csv', key='download-csv')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.write('')



if st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] == None:

    st.warning('Please enter your username and password !')







