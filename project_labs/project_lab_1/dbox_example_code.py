from databox import Client
user_token = "<Enter your user token here>"

# Intialize the databox client
dbox = Client(user_token)

# Push your data metrics to the databox
# dbox.push("metric_name", metric_value)
dbox.push("Elon Musk", 20)
dbox.push("Disney", 2)
dbox.push("Apple", 200)
