from src.document_summarization.document_summarization import get_text_summarization, print_summary

toy_text = """
Elephants are large mammals of the family Elephantidae and the order Proboscidea. 
Two species are traditionally recognised, the African elephant and the Asian elephant. 
Elephants are scattered throughout sub-Saharan Africa, South Asia, and Southeast Asia. 
Male African elephants are the largest extant terrestrial animals. 
All elephants have a long trunk used for many purposes, particularly breathing, lifting water and grasping objects. 
Their incisors grow into tusks, which can serve as weapons and as tools for moving objects and digging. 
Elephants' large ear flaps help to control their body temperature. 
Their pillar-like legs can carry their great weight. 
African elephants have larger ears and concave backs while Asian elephants have smaller ears and convex or level backs.
"""

summary = get_text_summarization(text=toy_text, method='gensim')
print "===== Text Summarization via Gensim implementation of TextRank  ====="
print_summary(summary=summary)
print

summary = get_text_summarization(text=toy_text, method='lsa')
print "===== Text Summarization via LSA ====="
print_summary(summary=summary)
print

summary = get_text_summarization(text=toy_text, method='text_rank')
print "===== Text Summarization via TextRank ====="
print_summary(summary=summary)
