import random
import re
from collections import defaultdict

def train_qa_llm(filename, context_size=2):
    """Reads your massive science text file and builds an organized phrase dictionary."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"⚠️ Error: Please create a '{filename}' file first.")
        return None, None

    # Split text into a list of clean paragraphs
    paragraphs = [p.strip() for p in text.split('\n') if len(p.strip()) > 20]
    words = text.split()
    
    brain = defaultdict(list)
    for i in range(len(words) - context_size):
        context_phrase = tuple(words[i:i+context_size])
        next_word = words[i+context_size]
        brain[context_phrase].append(next_word)
        
    return brain, paragraphs

def answer_question(user_prompt, brain, paragraphs):
    """Scans the learned text data to answer the user's random question."""
    clean_prompt = user_prompt.strip().lower()
    
    # Clean the question into separate search keywords
    keywords = re.findall(r'\b\w{4,}\b', clean_prompt) # Extract words longer than 3 letters
    
    best_paragraph = None
    max_matches = 0
    
    # Find the paragraph in your science file that has the most matching keywords
    for p in paragraphs:
        matches = sum(1 for word in keywords if word in p.lower())
        if matches > max_matches:
            max_matches = matches
            best_paragraph = p
            
    # If we found a matching science paragraph, give it as the answer
    if best_paragraph and max_matches > 0:
        return best_paragraph
        
    return "I cannot find information about that specific topic in my local science databases. Try asking about gravity, biology, dna, or cardiology."

if __name__ == "__main__":
    corpus_file = "science_corpus.txt"
    brain, science_paragraphs = train_qa_llm(corpus_file)
    
    print("🧠 Custom Science Question-Answering Model Online!")
    print("=" * 60)
    print("Ask me any science question based on your downloaded files, or type 'exit' to quit.")
    print("=" * 60)
    
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ['exit', 'bye']:
            print("System offline. Goodbye!")
            break
            
        if not user_input.strip():
            continue
            
        print("🤖 Chatbot: [Analyzing prompt against text repositories...]")
        reply = answer_question(user_input, brain, science_paragraphs)
        print(f"🤖 Chatbot: {reply}")
        print("-" * 60)
