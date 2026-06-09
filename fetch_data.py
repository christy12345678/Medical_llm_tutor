import json
import urllib.request
import urllib.parse

# The list of science and medical topics you want your model to learn
topics = ["Gravity", "Cardiology", "DNA", "Atom"]

print("📥 Initializing secure background download tool...")

for topic in topics:
    # Safely convert strings into web-safe URLs
    encoded_topic = urllib.parse.quote(topic)
    url = f"https://wikipedia.org{encoded_topic}&format=json"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'ScienceLLM_Project/1.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            pages = data['query']['pages']
            page_id = list(pages.keys())[0]
            
            if page_id != "-1":
                extract_text = pages[page_id]['extract']
                
                # Append the clean paragraphs directly to your database file
                with open("science_corpus.txt", "a", encoding="utf-8") as f:
                    f.write("\n\n" + extract_text)
                print(f"✨ Successfully downloaded and indexed: {topic}")
            else:
                print(f"⚠️ Could not find page for: {topic}")
    except Exception as e:
        print(f"❌ Network issue downloading {topic}: {e}")

print("🏁 All scientific articles appended to science_corpus.txt successfully!")
