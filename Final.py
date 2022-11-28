import streamlit as st
import pandas as pd
import snscrape.modules.twitter as snt

st.title('Twitter scraper')

st.subheader("""
Let's scrape some Tweets...:smile:
""")
tweets = []
with st.form(key='Twitter_form'):
    search_term = st.text_input('What do you want to search for?')
    limit = st.slider('How many tweets do you want to get?', 0, 1000, step=10)
    output_csv = st.radio('Save a CSV file?', ['Yes', 'No'])
    file_name = st.text_input('Name the CSV file:')
    submit_button = st.form_submit_button(label='Search')

    if submit_button:
        Search = search_term
        Limit = limit

        Store_csv = True

        if Store_csv:
            Output = f'{file_name}.csv'

        for tweet in snt.TwitterHashtagScraper(search_term).get_items():

            if len(tweets) == limit:
                break
            else:
                tweets.append(
                    [tweet.date,tweet.id, tweet.url, tweet.user.username, tweet.sourceLabel, tweet.user.location, tweet.content,
                     tweet.likeCount, tweet.retweetCount, tweet.quoteCount, tweet.replyCount])

        df = pd.DataFrame(tweets, columns=['Date','ID', 'TweetURL', 'User', 'Source', 'Location', 'Tweet', 'Likes_Count',
                                           'Retweet_Count', 'Quote_Count', 'Reply_Count'])
        st.table(df)


try:
    st.download_button(label='Download results', data=convert_df(data), file_name=f'{file_name}.csv', mime='text/csv')
except:
    pass

