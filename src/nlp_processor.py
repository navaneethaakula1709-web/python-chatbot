import re

import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# ==========================================================
# NLP COMPONENTS
# ==========================================================

STOP_WORDS = set(stopwords.words("english"))

LEMMATIZER = WordNetLemmatizer()


# ==========================================================
# CLEAN TEXT
# ==========================================================

def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# ==========================================================
# TOKENIZATION
# ==========================================================

def tokenize(text):

    cleaned_text = clean_text(text)

    tokens = cleaned_text.split()

    return tokens


# ==========================================================
# REMOVE STOP WORDS
# ==========================================================

def remove_stopwords(tokens):

    filtered_tokens = []

    for word in tokens:

        if word not in STOP_WORDS:

            filtered_tokens.append(word)

    return filtered_tokens


# ==========================================================
# LEMMATIZATION
# ==========================================================

def lemmatize_words(tokens):

    lemmatized_words = []

    for word in tokens:

        lemma = LEMMATIZER.lemmatize(word)

        lemmatized_words.append(lemma)

    return lemmatized_words


# ==========================================================
# COMPLETE NLP PIPELINE
# ==========================================================

def preprocess(text):

    cleaned_text = clean_text(text)

    tokens = tokenize(cleaned_text)

    filtered_tokens = remove_stopwords(tokens)

    lemmatized_tokens = lemmatize_words(
        filtered_tokens
    )

    processed_text = " ".join(
        lemmatized_tokens
    )

    return {
        "original": text,
        "cleaned": cleaned_text,
        "tokens": tokens,
        "without_stopwords": filtered_tokens,
        "lemmatized": lemmatized_tokens,
        "processed": processed_text
    }


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    question = (
        "What are the different types "
        "of Python functions?"
    )

    result = preprocess(question)

    print("=" * 60)
    print("             NLP PROCESSOR")
    print("=" * 60)

    print()
    print("Original:")
    print(result["original"])

    print()
    print("Cleaned:")
    print(result["cleaned"])

    print()
    print("Tokens:")
    print(result["tokens"])

    print()
    print("Without Stop Words:")
    print(result["without_stopwords"])

    print()
    print("Lemmatized:")
    print(result["lemmatized"])

    print()
    print("Final Processed Text:")
    print(result["processed"])

    print()
    print("=" * 60)