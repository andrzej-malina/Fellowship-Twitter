import pandas as pd
from tweepy import API
import twitter_auth


def tweets_to_df(screen_name):
    # autoryzacja danych z Twittera
    auth = twitter_auth.twitter_auth()

    # inicjalizacja tweepy
    api = API(auth)

    # pusta lista do zbierania tweetów
    all_tweets = []

    # ostatnie tweety, wykorzystując user_timeline możemy ściągnąć ostatnie 200 tweetów
    last_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # zapisujemy ostatnie tweety
    all_tweets.extend(last_tweets)

    # zapisujemy id najstarszego tweeta - 1
    oldest = all_tweets[-1].id - 1

    # pętla zapisujące tweety aż do wyczerpania tweetów
    while len(last_tweets) > 0:
        # print(f'Zapisuje tweet {oldest}')

        # używamy parametru max_id, aby zapobiec duplikatom
        last_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # zapisujemy nowe tweety
        all_tweets.extend(last_tweets)

        # aktualizujemy id najstarszego tweeta - 1
        oldest = all_tweets[-1].id - 1

        # print(f'Zapisano dotychczas {len(all_tweets)} tweetów')

    # zapisujemy listę tweetów do 2 wymiarowej matrycy
    output_tweets = [[tweet.user.screen_name, tweet.user.name, tweet.created_at, tweet.id,
                      tweet.text, tweet.retweet_count, tweet.favorite_count, tweet.lang,
                      tweet.source, tweet.user.location, tweet.user.url, tweet.user.followers_count,
                      tweet.user.friends_count] for tweet in all_tweets]

    return pd.DataFrame(output_tweets)
