from deep_translator import GoogleTranslator

def translate_dialog(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    translated_lines = []
    translator = GoogleTranslator(source='en', target='tr')

    for line in lines:
        line = line.strip()
        if line:
            translated_text = translator.translate(line)
            translated_lines.append(f"{line}\n{translated_text}\n")

    with open("translated_dialog.txt", "w", encoding="utf-8") as output_file:
        output_file.writelines(translated_lines)

translate_dialog("dialog.txt")
