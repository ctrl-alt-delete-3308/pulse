#to install, you will need pip3:
# pip3 install twint
# to output search results to textfile:
# python3 twint_test.py > testText.txt

import twint
import numpy as np

# Configure
c = twint.Config()
# c.Username = "noneprivacy"
c.Search = "boulder"
c.Format = "Tweet: {tweet}"
c.Limit = 100
c.Pandas = True

twint.run.Search(c)
# np.savetxt('data.csv', data, delimiter=',')
# to output search results to textfile:
# python3 twint_test.py > SomeFile.txt
