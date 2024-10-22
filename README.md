# FAQ Module Project Documentation
Overview:
This project contains a dataset of FAQs for the Saras AI Institute, organized by different categories such as Admissions, Curriculum and Faculty, Accreditation & Recognition, Career Services, and Tuition Fee and Scholarships. The dataset provides information to prospective students about the institute, its programs, services, and general inquiries.
Libraries to Install:
•	 Pandas
•	 Nltk
•	 String
•	 Spacy
•	 Python -m spacy download en_core_web_md
•	 Tkinter
•	 Tkinter supporting framework and environment
•	Fuzzywuzzy
# Usage:
This model can be used to submit any query in a given text box, and the model will return the best suitable answer to the corresponding question from the dataset.
Troubleshooting:
The known issue is that the model provides an answer even if the best possible similarity score is low. For example, if the best possible similarity score is 0.3, the model will still return that answer.

# Code Work:
This whole process is done by fuzzy. In this a best score is given for a query after passing it through all the sentences and checking the similarities. If the best score is above a thresholder value, then it gives the relevant answer to the query.
The relevant answer is shown in an output box. After that the question and the answer gets added to the dataset, where it self-learns itself (the self-learning will be only till that time when the window is open as soon as the window closes the datsaet is back to it’s original one )
