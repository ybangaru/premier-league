import pandas as pd
import glob, os.path

comments_data = {}
for filename in glob.glob('*.csv'):
    comments_data[filename[:-4]] = pd.read_csv(filename, error_bad_lines=False )

print(comments_data.keys())
combined_output = pd.DataFrame(data=None)

for key in comments_data:
    combined_output = pd.concat([combined_output, comments_data[key]])

combined_output.to_csv('reddit-comments.csv')
print(combined_output.shape)

    
# print(base_data[season2015-16].head())
# print(base_data[season2016-17].head())