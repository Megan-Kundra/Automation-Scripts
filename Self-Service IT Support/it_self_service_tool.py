import csv
import os

def generate_knowledgebase(csv_file_path, output_dir="knowledgebase"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    faq_data = {}

    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                category = row['category'].strip()
                question = row['question'].strip()
                answer = row['answer'].strip()
                faq_data.setdefault(category, []).append((question, answer))
    except FileNotFoundError:
        print(f"❌ File not found: {csv_file_path}")
        return
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return

    for category, faqs in faq_data.items():
        filename = f"{category.replace(' ', '_').lower()}.md"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# {category} FAQs\n\n")
            for q, a in faqs:
                md_file.write(f"## Q: {q}\n")
                md_file.write(f"A: {a}\n\n")

    print(f"✅ Markdown files generated in: {output_dir}")

# Example usage:
csv_path = input("Enter the full path to your FAQ CSV file: ")
generate_knowledgebase(csv_path)
