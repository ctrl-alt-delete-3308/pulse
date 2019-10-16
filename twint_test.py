import twint
import numpy as np

# Configure
c = twint.Config()
# c.Username = "noneprivacy"
c.Search = "boulder"
c.Format = "Tweet: {tweet}"
c.Limit = 20
c.Pandas = True

twint.run.Search(c)
# np.savetxt('data.csv', data, delimiter=',')
# to output search results to textfile:
# python3 twint_test.py > SomeFile.txt
