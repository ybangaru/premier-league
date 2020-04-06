import pandas as pd
import glob, os.path

odds_data = {}
for filename in glob.glob('*.csv'):
    odds_data[filename[:-4]] = pd.read_csv(filename, error_bad_lines=False )

print(odds_data.keys())
combined_output = pd.DataFrame(data=None)

for key in odds_data:
    combined_output = pd.concat([combined_output, odds_data[key]])

combined_output.to_csv('odds_data.csv', index=False)
print(combined_output.shape)

    
# print(base_data[season2015-16].head())
# print(base_data[season2016-17].head())