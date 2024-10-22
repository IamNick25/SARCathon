import pandas as pd
import spacy
from fuzzywuzzy import fuzz  
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher


nlp = spacy.load("en_core_web_md")


faq_data = {
   "Admissions": [
      {
         "question": "What is the process for admission into Saras AI Institute?",
         "answer": "The admission process at Saras AI Institute typically involves submitting the online application form along with necessary details, followed by a quick pre-Enrollment assessment to evaluate your candidature based on your personal traits and basic communication skills in English."
      },
      {
         "question": "Is there an application fee for applying to Saras AI Institute?",
         "answer": "There is no application fee for applying to any program at Saras."
      },
      {
         "question": "What is pre-enrollment assessment test? How do I prepare for it?",
         "answer": "It is a fully online assessment which takes less than 15 minutes. It is designed to evaluate your personal traits and basic English communication skills. You can take it at the time of filling out the application. It does not require any specific preparation."
      },
      {
         "question": "Are there any specific requirements or prerequisites for admission into the programs?",
         "answer": "To be a successful professional in AI, you need to possess basic mathematical proficiency - which can be demonstrated by your math scores in high school or beyond. At Saras, you learn with global peers and faculties and should possess basic communication skills in English. These make up for the basic eligibility criteria."
      },
      {
         "question": "When is the deadline for submitting the application?",
         "answer": "The deadline for submitting applications is 5th August 2024."
      }
   ],
   "Curriculum and Faculty": [
      {
         "question": "What is the curriculum like at Saras AI Institute?",
         "answer": "The curriculum at Saras AI Institute helps impart essential technical as well as human skills. We have designed a role-based curriculum that prepares students for one of these in-demand roles: AI/ML Engineer; Data Scientist; Gen AI Engineer. The curriculum is designed to provide a comprehensive understanding of AI principles and practices, including hands-on projects and real-world applications."
      },
      {
         "question": "What does the program structure look like, and how is the curriculum delivered?",
         "answer": "Each year is divided into 5 semesters which last for 8 weeks each. Our programs feature a mix of recorded and live sessions, allowing for flexibility in learning."
      },
      {
         "question": "Can you provide more details about the role-based curriculum feature and how it benefits students?",
         "answer": "Our role-based curriculum is designed to provide targeted training and develop specialized skills in students that are highly relevant to their desired job-roles from day one."
      },
      {
         "question": "Do you also conduct LIVE sessions?",
         "answer": "Live sessions are conducted regularly to supplement the recorded content and provide opportunities for interactive learning and Q&A sessions. You get to interact with instructors as well as your dedicated coach for any help that you might need."
      },
      {
         "question": "Can I transfer credits earned at other universities to Saras AI Institute?",
         "answer": "Yes, we evaluate the course that you have taken, if it overlaps with our curriculum and is relevant in today's time, we offer the flexibility of transferring credits."
      },
      {
         "question": "Who are the faculty members at Saras AI Institute?",
         "answer": "The faculty at Saras AI Institute consists of industry professionals who bring the most relevant skills and mentorship for the students to help them prepare for exactly what is needed to succeed in the job roles they are preparing for."
      },
      {
         "question": "Can I connect with mentors outside of class?",
         "answer": "Yes, we encourage mentorship and provide opportunities for students to connect with mentors outside of class through live sessions as well as 24x7 mentor support to help resolve your doubts or queries."
      }
   ],
   "Accreditation & Recognition": [
      {
         "question": "Is Saras AI Institute accredited?",
         "answer": "No, we are not accredited yet. This is our first Enrollment cycle and there is a minimum period before an institute can get accredited. However, we do follow the highest standards in terms of the curriculum and pedagogy for our students to become the top AI professionals."
      },
      {
         "question": "Are the degree programs recognised by the government?",
         "answer": "Yes, we are a state-approved degree granting institute based in the United States."
      },
      {
         "question": "Do employers require an accredited degree?",
         "answer": "An accredited degree is not an absolute requirement from employers. We ensure our students are among the most-skilled and ready individuals to crack the best of jobs."
      }
   ],
   "Career Services": [
      {
         "question": "Does Saras AI Institute offer employment support?",
         "answer": "Yes, we provide comprehensive employment support including job placement services, resume building workshops, and interview preparation."
      },
      {
         "question": "Does Saras have partnerships with employers?",
         "answer": "Yes, we have partnered with top global companies to recruit our graduating students."
      },
      {
         "question": "Does the university offer internship placement assistance?",
         "answer": "Yes, we assist students in finding internships by connecting them with potential employers and offering guidance on applications and interviews."
      }
   ],
   "Tuition fee and Scholarships": [
      {
         "question": "Does Saras AI Institute offer any scholarships for students? How can I apply for them?",
         "answer": "Yes, we offer various scholarships to eligible students based on academic merit, financial need, and other criteria. You can apply for scholarships after you're offered admission. Go ahead with filling out the application to check your eligibility."
      },
      {
         "question": "What are the tuition fees for your courses?",
         "answer": "You can find detailed information and breakdown of the fee on the 'Programs' page on the website."
      },
      {
         "question": "Are there any payment plans or options available for tuition fees?",
         "answer": "Yes, we offer flexible payment plans to help students manage their tuition fees. At Saras AI Institute, you can pay your annual tuition fees in 5 installments, before the commencement of every semester."
      },
      {
         "question": "Can I avail financial aid?",
         "answer": "You currently can't get federal aid for Saras AI Institute's programs. However, we are partnering with lenders who can help facilitate a loan to help pay the tuition."
      }
   ]
}

# Convert the dictionary into a dataframe
rows = []
for category, faqs in faq_data.items():
    for faq in faqs:
        rows.append([category, faq["question"], faq["answer"]])

# Create a DataFrame
df = pd.DataFrame(rows, columns=["Category", "question", "answer"])

# Fuzzy match function
def fuzzy_match_query(query, df, threshold=60):
    best_question = None
    best_answer = None
    best_score = 0

    # Iterate through all FAQ entries
    for i, row in df.iterrows():
        # Compare the similarity using fuzzy matching
        score = fuzz.ratio(query.lower(), row['question'].lower())

        # If a better match is found, update the best score, question, and answer
        if score > best_score:
            best_score = score
            best_question = row['question']
            best_answer = row['answer']
            best_category=row[0]
    # Return the best match if the score exceeds the threshold
    if best_score >= threshold:
        return best_question, best_answer, best_score, best_category
    else:
        return None, None, best_score, None


# Main function to handle FAQ response
def generate_answer(query, df, threshold=60):
    # Perform fuzzy matching
    best_question, best_answer, best_score, best_category = fuzzy_match_query(query, df, threshold=threshold)
    
    # If a match is found with a score between 65-100, return the question and answer
    if best_question:
        if 65 <= best_score <= 100:
            print(f"Found match with a score of {best_score}% similarity.")
            return best_answer,best_category
        else:
            return "No relevant FAQs found", ""
    else:
        return "No relevant FAQs found", ""


# Example query with some variations
#query = "What is the process for admission?"
#
## Get the best FAQ response
#best_question, best_answer = faq_response(query, df)
#
#print("Best Match Question:", best_question)
#print("Answer:", best_answer)

def save_to_file():
    query=query_text.get("1.0", "end-1c").strip()  # Get query from the textbox

    if query:
        answer,category=generate_answer(query,df,threshold=60) #Generate the answer
        new_row={"Category":category,"question":query,"answer":answer}
        df.loc[len(df)]=new_row
        # Enable the answer box, insert the answer, then disable it again
        answer_text.config(state="normal")  # Enable the answer box for editing
        answer_text.delete("1.0", "end")  # Clear the previous content
        answer_text.insert("1.0", answer)  # Display the new answer
        answer_text.config(state="disabled")  # Make answer text box read-only

        # Save the query and answer to a file
        with open("queries_answers.txt", "a") as file:
            file.write(f"Query: {query}\nAnswer: {answer}\n{'-' * 40}\n")

        messagebox.showinfo("Saved", "Query and Answer saved to file!")
        query_text.delete("1.0", "end")  # Clear the query textbox after saving
    else:
        messagebox.showwarning("Input Error", "Please enter a query.")

# Create the main window
root = tk.Tk()
root.title("Query Answering Interface")

# Query Label
tk.Label(root, text="Enter your Query:").grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Query Textbox
query_text = tk.Text(root, height=5, width=50)
query_text.grid(row=1, column=0, padx=10, pady=5)

# Answer Label
tk.Label(root, text="Generated Answer:").grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Answer Textbox (non-editable by default)
answer_text = tk.Text(root, height=5, width=50)
answer_text.grid(row=3, column=0, padx=10, pady=5)
answer_text.config(state="disabled")  # Make answer text box read-only

# Save Button
save_button = tk.Button(root, text="Get Answer and Save", command=save_to_file)
save_button.grid(row=4, column=0, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
