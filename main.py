import feed_stream as f1
fs = f1.FeedStream('e2e94047de9a19a1522d6662e5e3e710fbf350c6e68c37f2588db933377f84207abd7ea3a7b979ffb1714')
data = fs.get_news()

for string in data:
    print(string)


