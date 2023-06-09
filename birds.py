import pandas as pd
from pyodide.http import open_url
url = (
    'https://githubusercontent.combdempe18/What-bird-am-I/blob/main/bird_details.csv '
)
df = pd.read_csv(open_url(url))

random_bird = pd.sample(1)

label = random_bird.species
image = random_bird.image

label
