import pandas as pd
from deep_translator import GoogleTranslator


df = pd.read_csv('matchs_file.csv', encoding='utf-8')

def translate_text(text):
    try:
        return GoogleTranslator(source='ar', target='en').translate(text)
    except:
        return text 

df_translated = pd.DataFrame()
# Translate all columns
df_translated['Championship Title'] = df['Championship Title'].astype(str).apply(translate_text)
df_translated['Team 1'] = df['Team 1'].astype(str).apply(translate_text)
df_translated['Team 2'] = df['Team 2'].astype(str).apply(translate_text)
df_translated['Score'] = df['Score'].astype(str).apply(translate_text)  # Translate scores
df_translated['Timing'] = df['Timing'].astype(str).apply(translate_text)  # Translate timing if needed

# Save only the translated data
df_translated.to_csv('translated_data.csv', index=False, encoding='utf-8')

print("Translation complete! Check 'translated_data.csv'.")
