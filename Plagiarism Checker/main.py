from difflib import SequenceMatcher

def calculate_similarity(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

def check_plagiarism(text1, text2, threshold=0.8):
    similarity_score = calculate_similarity(text1, text2)
    if similarity_score >= threshold:
        return f"Plagiarism detected! Similarity score: {similarity_score}"
    else:
        return f"No plagiarism detected. Similarity score: {similarity_score}"

# Example usage
text1 = "This is an example sentence."
text2 = "This is a sample sentence."

result = check_plagiarism(text1, text2)
print(result)


