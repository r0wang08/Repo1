from collections import Counter

#function to make a list to store all keywords in column of 'review_content'
#loop over keywords
def find_most_mentioned_keywords(df, num_keywords):
    all_keywords = []
    for review in df['review_content']:
        keywords = review.split()
        all_keywords.extend(keywords)
    keyword_counts = Counter(all_keywords)
    return keyword_counts.most_common(num_keywords)

df = pd.read_csv('your_data.csv')
top_keywords = find_most_mentioned_keywords(df, 10)
print(top_keywords)