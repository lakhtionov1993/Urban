def all_variants(text):
    for i in range(len(text)):
        for m in range(len(text)-i):
            yield text[m:i+m+1]


a = all_variants("abc")
for i in a:
    print(i)
