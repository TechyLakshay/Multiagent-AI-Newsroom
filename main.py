# # from agents.story_hunter import get_headlines
# # from agents.reporter import generate_summary
# # from agents.fact_checker import fact_check
# # from agents.editor import editor_decision

# # def run_pipeline():
# #     headlines = get_headlines()
# #     for h in headlines:
# #         print("\n📰 Headline:", h)
# #         summary = generate_summary(h)
# #         print("✍️ Summary:", summary)
# #         fact = fact_check(summary)
# #         print("✅ Fact Check:", fact)
# #         decision = editor_decision(fact)
# #         print("📢 Editor:", decision)
# ------------------------------------------------------------------
# # if __name__ == "__main__":
# #     run_pipeline()
# # main_autonomous.py - Make your agents fully autonomous
# import time
# import threading
# from datetime import datetime
# from agents.story_hunter import get_headlines
# from agents.reporter import generate_summary
# from agents.fact_checker import fact_check
# from agents.editor import editor_decision

# class AutonomousNewsroom:
#     def __init__(self):
#         self.is_running = False
#         self.processed_headlines = set()  # Avoid duplicates
#         self.published_count = 0
        
#     def autonomous_pipeline(self):
#         """Fully autonomous news processing pipeline"""
#         print("🚀 AUTONOMOUS NEWSROOM STARTED")
#         print("=" * 50)
        
#         self.is_running = True
        
#         while self.is_running:
#             try:
#                 print(f"\n⏰ [{datetime.now().strftime('%H:%M:%S')}] Starting autonomous cycle...")
                
#                 # 1. Story Hunter Agent - Discovers news
#                 print("🔍 Story Hunter: Discovering news...")
#                 headlines = get_headlines(country="in", limit=10)
                
#                 new_stories = 0
#                 for story in headlines:
#                     headline = story["headline"]
#                     source = story["source"]
                    
#                     # Skip if already processed
#                     if headline in self.processed_headlines:
#                         continue
                    
#                     self.processed_headlines.add(headline)
#                     new_stories += 1
                    
#                     print(f"\n📰 NEW STORY DETECTED: {headline[:60]}...")
#                     print(f"📡 Source: {source}")
                    
#                     # 2. Reporter Agent - Autonomous investigation
#                     print("✍️  Reporter Agent: Investigating story...")
#                     summary = generate_summary(headline)
#                     print(f"📝 Generated Summary: {summary[:100]}...")
                    
#                     # 3. Fact Checker Agent - Autonomous verification  
#                     print("🔍 Fact Checker: Verifying claims...")
#                     fact_result = fact_check(headline)
#                     print(f"✅ Fact Check Result: {fact_result}")
                    
#                     # 4. Editor Agent - Autonomous publishing decision
#                     print("📝 Editor: Making publishing decision...")
#                     decision = editor_decision(headline, summary, fact_result)
#                     print(f"📰 Editorial Decision: {decision}")
                    
#                     if "Published" in decision:
#                         self.published_count += 1
                    
#                     print("-" * 50)
                
#                 print(f"🎯 Cycle Complete: {new_stories} new stories processed")
#                 print(f"📊 Total Published Today: {self.published_count}")
                
#                 # Wait before next autonomous cycle
#                 print("⏳ Waiting 60 seconds before next scan...")
#                 time.sleep(60)
                
#             except KeyboardInterrupt:
#                 print("\n🛑 Stopping autonomous newsroom...")
#                 self.is_running = False
#                 break
#             except Exception as e:
#                 print(f"⚠️  Error in autonomous cycle: {e}")
#                 time.sleep(30)  # Wait before retry
    
#     def start_autonomous_mode(self):
#         """Start the autonomous newsroom in a separate thread"""
#         if not self.is_running:
#             thread = threading.Thread(target=self.autonomous_pipeline, daemon=True)
#             thread.start()
#             return thread
#         else:
#             print("Newsroom already running!")
#             return None
    
#     def stop(self):
#         """Stop autonomous operation"""
#         self.is_running = False
#         print("🛑 Autonomous newsroom stopped")

# # Demo with real-time dashboard
# def run_with_dashboard():
#     import streamlit as st
    
#     st.title("🤖 AUTONOMOUS NEWSROOM - LIVE DEMO")
    
#     # Initialize newsroom
#     if 'newsroom' not in st.session_state:
#         st.session_state.newsroom = AutonomousNewsroom()
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         if st.button("🚀 START AUTONOMOUS MODE"):
#             thread = st.session_state.newsroom.start_autonomous_mode()
#             if thread:
#                 st.success("Autonomous newsroom started!")
#             else:
#                 st.warning("Already running!")
    
#     with col2:
#         if st.button("🛑 STOP"):
#             st.session_state.newsroom.stop()
#             st.success("Stopped!")
    
#     # Show statistics
#     st.subheader("📊 Live Statistics")
#     col3, col4, col5 = st.columns(3)
    
#     with col3:
#         st.metric("Stories Processed", len(st.session_state.newsroom.processed_headlines))
    
#     with col4:
#         st.metric("Articles Published", st.session_state.newsroom.published_count)
    
#     with col5:
#         st.metric("Status", "🟢 ACTIVE" if st.session_state.newsroom.is_running else "🔴 STOPPED")
    
#     # Show recent published articles
#     st.subheader("📰 Recent Publications")
#     try:
#         with open("published_news.txt", "r", encoding="utf-8") as f:
#             recent_articles = f.read()[-2000:]  # Last 2000 chars
#             st.text_area("Recent Articles", recent_articles, height=300)
#     except FileNotFoundError:
#         st.info("No articles published yet.")
    
#     # Auto-refresh every 10 seconds
#     time.sleep(10)
#     st.rerun()

# if __name__ == "__main__":
#     # Choose mode
#     import sys
    
#     if len(sys.argv) > 1 and sys.argv[1] == "dashboard":
#         run_with_dashboard()
#     else:
#         # Command line autonomous mode
#         newsroom = AutonomousNewsroom()
#         try:
#             newsroom.autonomous_pipeline()
#         except KeyboardInterrupt:
#             newsroom.stop()
#             print("👋 Goodbye!")