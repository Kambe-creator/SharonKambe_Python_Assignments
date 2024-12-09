# Dictionary for language translations
translations = {
    'en': {
        'welcome': "Welcome to the File Handling Program!",
        'choose_lang': "Choose your language: (en: English, fr: Français, es: Español): ",
        'file_read': "Enter the name of the file to read: ",
        'file_write': "Enter the name of the file to write the modified content: ",
        'original_content': "Original Content:",
        'modified_success': "Modified content written to",
        'try_again': "Attempt complete. Try again if necessary.",
        'file_not_found': "Error: The file does not exist. Please try again.",
        'permission_denied': "Error: Permission denied for the file. Please check the file permissions.",
        'unexpected_error': "An unexpected error occurred:",
        'exit': "Exiting the program. Goodbye!"
    },
    'fr': {
        'welcome': "Bienvenue dans le programme de gestion des fichiers!",
        'choose_lang': "Choisissez votre langue : (en : Anglais, fr : Français, es : Espagnol) : ",
        'file_read': "Entrez le nom du fichier à lire : ",
        'file_write': "Entrez le nom du fichier pour écrire le contenu modifié : ",
        'original_content': "Contenu original :",
        'modified_success': "Contenu modifié écrit dans",
        'try_again': "Tentative terminée. Réessayez si nécessaire.",
        'file_not_found': "Erreur : Le fichier n'existe pas. Veuillez réessayer.",
        'permission_denied': "Erreur : Permission refusée pour le fichier. Veuillez vérifier les autorisations.",
        'unexpected_error': "Une erreur inattendue s'est produite :",
        'exit': "Quitter le programme. Au revoir!"
    },
    'es': {
        'welcome': "¡Bienvenido al programa de manejo de archivos!",
        'choose_lang': "Elige tu idioma: (en: Inglés, fr: Francés, es: Español): ",
        'file_read': "Introduce el nombre del archivo para leer: ",
        'file_write': "Introduce el nombre del archivo para escribir el contenido modificado: ",
        'original_content': "Contenido original:",
        'modified_success': "Contenido modificado escrito en",
        'try_again': "Intento completado. Inténtalo de nuevo si es necesario.",
        'file_not_found': "Error: El archivo no existe. Por favor, inténtalo de nuevo.",
        'permission_denied': "Error: Permiso denegado para el archivo. Por favor, verifica los permisos.",
        'unexpected_error': "Ocurrió un error inesperado:",
        'exit': "Saliendo del programa. ¡Adiós!"
    }
}

# Function to choose a language
def choose_language():
    lang = input(translations['en']['choose_lang']).lower()
    return lang if lang in translations else 'en'

# Function to handle file reading
def read_file(lang):
    while True:
        try:
            filename = input(translations[lang]['file_read'])
            with open(filename, 'r') as file:
                content = file.read()
                print(f"\n{translations[lang]['original_content']}\n", content)
            return content
        except FileNotFoundError:
            print(translations[lang]['file_not_found'])
        except PermissionError:
            print(translations[lang]['permission_denied'])
        except Exception as e:
            print(f"{translations[lang]['unexpected_error']} {e}")
        finally:
            print(translations[lang]['try_again'])

# Function to handle file writing
def write_file(content, lang):
    try:
        output_file = input(translations[lang]['file_write'])
        modified_content = content.upper()  # Example modification: Convert to uppercase
        with open(output_file, 'w') as file:
            file.write(modified_content)
        print(f"{translations[lang]['modified_success']} {output_file}!")
    except Exception as e:
        print(f"{translations[lang]['unexpected_error']} {e}")

# Main function
def main():
    lang = choose_language()
    print(translations[lang]['welcome'])
    content = read_file(lang)
    if content:
        write_file(content, lang)
    print(translations[lang]['exit'])

if __name__ == "__main__":
    main()
