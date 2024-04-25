# Task 1: Keyword Highlighter

reviews = [ "This product is really good. I'm impressed with its quality.",
                  "The performance of this product is excellent. Highly recommended!",
                  "I had a bad experience with this product. It didn't meet my expectations.",
                  "Poor quality product. Wouldn't recommend it to anyone.",
                  "The product was average. Nothing extraordinary about it.",
                  "Short review."]
keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews: # outer for loop goes through each review
    for keyword in keywords: # inner for loop goes through each keyword
        if review.count(keyword) > 0: # reviews are printed when a keyword is detected
            print(review.replace(keyword, keyword.upper())) # capitalize the keyword to highlight it

# Task 2: Sentiment Tally

print()
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for i,review in enumerate(reviews): # iterate through each review
    poscount = 0
    negcount = 0
    for posword in positive_words: # loop to determine number of positive words in review
        poscount += review.lower().count(posword)
    for negword in negative_words: # loop to determine number of negative words in review
        negcount += review.lower().count(negword)
    print ("Review {}: {} positive words, {} negative words.".format(i + 1, poscount, negcount)) # Values are printed once num of words is found

# Task 3: Review Summary

def shortenReview(review): # Function to shorten reviews
    if (len(review) < 30): # If the review is less than 30 characters, it doesn't need to be shortened.
        return review
    else:
        output = []
        char_count = 0
        words = review.split() # use split function to break up review into a list of words
        for word in words: # loop through the words in the review
            if char_count > 30: # exit loop if total characters of words is greater than 30
                break
            char_count += 1 + len(word) # keeps track of character length of shortened review
            output.append(word) # add words part of shortened review to a new list
        return " ".join(output) + "..." # return the first 30 characters of the review with '...' at the end, without cutting of words

print()
for review in reviews: # loop to show how each review looks when shortened
    print(shortenReview(review)) # print each review after it has been shortened