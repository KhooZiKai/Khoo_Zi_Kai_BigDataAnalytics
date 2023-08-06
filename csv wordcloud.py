
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Read the contents of the file
file_path = r"C:\Users\khooz\Downloads\pythoncount_output_c\part-00000"  # Only Works On My Computer, Change to you Input Path
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(data)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
