Team work:

import pandas as pd #analysis 
import matplotlib.pyplot as plt #visualization 
import seaborn as sns #different approach how to create nice visualisation 
pokemon_df = pd.read_csv('/content/Pokemon.csv')

# How many Pokémons are with 'Type 1' == Water as a % of total? 
amount_water_type = pokemon_df[pokemon_df['Type 1'] == 'Water'].shape[0]
total_pokemon_count = pokemon_df.shape[0]
perc_of_total = (amount_water_type/total_pokemon_count)*100
print(f'There are {amount_water_type} Water type pokemons. Which makes {perc_of_total:.2f} % out of total Pokemon amount') # '.2f' is to round up to 2 decimals 

# What is the maximum 'Speed' value? 
max_speed = pokemon_df['Speed'].max()

# What is the minimum 'Speed' value? 
min_speed = pokemon_df['Speed'].min()

# What is the difference between max and min 'Speed'? 
difference = max_speed - min_speed
print(f'The difference between max and min is {difference}.')

# Filter the DataFrame to include only the Pokémon with 'Speed' >= 80. How many Pokémon meet this criterion? Display this DataFrame using your preferred visualization method.
speed_gt_80 = pokemon_df[pokemon_df['Speed'] > 80]
speed_gt_80
print(f'{len(speed_gt_80)} pokemons have Speed above 80')

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
ax = sns.countplot(data=speed_gt_80, x='Type 1', hue='Type 1', palette='viridis', order=speed_gt_80['Type 1'].value_counts().index, legend=False)
plt.title('Count of Pokemon with Speed >= 80 by Type', fontsize=16)
plt.xlabel('Type 1', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45)

# Add the count on top of each bar
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), 
                textcoords='offset points', fontsize=12, color='black')
    
plt.show()


# Find Pokémon with the longest name (excluding spaces)? What is this pokemons name?
pokemon_df['Name Length'] = pokemon_df['Name'].str.replace(' ', '').str.len()
longest_name_pokemon = pokemon_df.loc[pokemon_df['Name Length'].idxmax()]
longest_name = longest_name_pokemon['Name']
print(f'The Pokemon with the longest name (excluding spaces) is {longest_name}.')




