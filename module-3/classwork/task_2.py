text = "текст — это связная последовательность слов и предложений, объединённых общей темой и смыслом, записанная на материальном носителе и служащая для передачи информации, мыслей и чувств?"
text.split(".")
s = [x.strip() for x in text.split(".") if x.strip()]
text_normalized = ". " .join(x.capitalize() for x in s) + "."
print(text)

count = sum(c.isdigit() for c in text)
print(count)

punctuation_count = sum(1 for c in text if c in ".,")
print(punctuation_count)

exclamation_count = text.count("?")
print(exclamation_count)
