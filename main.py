from rouge import Rouge


def read_summary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def compute_rouge(human_summary, llm_summary):
    rouge = Rouge()
    scores = rouge.get_scores(human_summary, llm_summary)
    return scores

if __name__ == "__main__":
    human_summary = read_summary("manual/Sprat.txt")
    llm_summary = read_summary("llm/GPT3.5/CoT_Sprat3.txt")

 

    rouge_scores = compute_rouge(human_summary, llm_summary)
    print("ROUGE Scores:", rouge_scores)



