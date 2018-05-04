import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Zodiac = ["Scopio", "Virgo", "Gemini", "Pisces", "Libra", "Cancer", "Taurus", "Capricorn", "Aires", "Sagittarius", "Leo", "Aquarius"]
x = [9.6, 9.4, 9.3, 9.1, 8.8, 8.5, 8.3, 8.2, 8.1, 7.3, 7.1, 6.3]
"""This is a very simple program that creates a barplot based on the data I entered
to determine which Zodiac sign makes up the most percentage of the United States population"""


plt.xlabel(" Zodiac Sign")
plt.ylabel(" Percentage")
plt.title("What Percentage of the US Population do Zodiac Signs Make Up ")
#plt.xticks(x ,("Scopio", "Virgo", "Gemini", "Pisces", "Libra", "Cancer", "Taurus", "Capricorn", "Aires", "Sagittarius", "Leo", "Aquarius"))
plt.bar(Zodiac, x)
plt.figure(1)
plt.show()

import new


