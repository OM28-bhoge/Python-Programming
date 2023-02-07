def similarity_score(sub1, sub2):
    sub1 = sub1.lower().split()
    sub2 = sub2.lower().split()
    common_words = 0
    unique_words = 0
    for word in sub1:
        if word in sub2:
            common_words += 1
            sub2.remove(word)
        unique_words += 1
    unique_words += len(sub2)
    return round(common_words / unique_words * 100, 2)

sub1 = input("Enter the first submission: ")
sub2 = input("Enter the second submission: ")
score = similarity_score(sub1, sub2)
print(f"The similarity score between the two is: {score}%.")