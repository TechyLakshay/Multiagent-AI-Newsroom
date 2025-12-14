# filepath: c:\Users\laksh\Desktop\AI\AGENTS\agents\editor.py
def editor_decision(headline, summary, fact_result):
    try:
        if "Disputed" in fact_result:
            return f"❌ Rejected: {headline}"
        else:
            article = f"📰 {headline}\n\n{summary}\n\n{fact_result}"
            
            # Add timestamp and better formatting
            from datetime import datetime
            article = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n{article}"
            
            with open("published_news.txt", "a", encoding="utf-8") as f:
                f.write(article + "\n" + "-"*50 + "\n\n")
            
            return f"✅ Published: {headline}"
    except Exception as e:
        return f"⚠️ Error publishing: {headline}"
