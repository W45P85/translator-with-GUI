<pre style="background-color: transparent; border: none;">
  _____                         _         _               
 |_   _|_ __  __ _  _ __   ___ | |  __ _ | |_  ___   _ __ 
   | | | '__|/ _` || '_ \ / __|| | / _` || __|/ _ \ | '__|
   | | | |  | (_| || | | |\__ \| || (_| || |_| (_) || |   
   |_| |_|   \__,_||_| |_||___/|_| \__,_| \__|\___/ |_|   
                                                          
<p>Translate nearly every language to nearly every other language. :-)</p>
</pre>


<img src="/img/doc/1.PNG" width="800">


This project is a simple text translator with a graphical user interface (GUI) built using Python and the Tkinter module.

## Features

- Translation of text between different languages.
- Selection of source and target languages via dropdown menus.
- Display of country flags alongside language selection options.
- User-friendly interface with modern design.

## Prerequisites

To run this project, you need Python and the Tkinter module. You can download Python from the official website: [python.org](https://www.python.org/downloads/)

## Installation

1. Clone the repository:

  ```
    git clone https://github.com/W45P85/translator-with-GUI
  ```

2. Navigate to the project directory:

  ```
    cd translator-with-GUI
  ```

3. Run the application:

  ```
    python translator.py
  ```


## How the App Works
The Translator with GUI application allows users to translate text from one language 
to another through a simple and intuitive interface. Below, we provide an explanation 
of the main components of the application, focusing on the part of the code that 
handles the translation process.

### Main Components
- Language Selection: Users can select the source and target languages from dropdown menus.
- Text Input and Output: Users input the text to be translated in the source text box and view the translated text in the target text box.
- Translation Button: A button that initiates the translation process when clicked.

### The translation process
The core translation functionality is handled by the 'translate_now' function. This function is triggered when the 'Translate' button is clicked.

Here is the relevant part of the code with detailed explanations:

```
  def translate_now():
      try:
          # Get the text from the source text box
          text_ = text1.get(1.0, END).strip()
          
          # Get the selected languages from the dropdown menus
          c3 = combo1.get()
          c4 = combo2.get()

          # Find the language codes
          src_lang = language.get(c3, None)
          dest_lang = language.get(c4, None)

          print("Source language:", src_lang)
          print("Destination language:", dest_lang)

          # Check if text and language selections are valid
          if text_ and src_lang and dest_lang:
              # Initialize the Translator object with the selected languages
              translator = Translator(from_lang=src_lang, to_lang=dest_lang)
              
              # Translate the text
              translated_text = translator.translate(text_)
              
              if translated_text:
                  # Display the translated text in the target text box
                  print("Translated text:", translated_text)
                  text2.delete(1.0, END)
                  text2.insert(END, translated_text)
              else:
                  # Handle the case where translation fails
                  messagebox.showerror("Translation Error", "The translation could not be performed.")
                  print("Translation failed")
          else:
              # Handle invalid input or language selections
              messagebox.showwarning("Input Error", "Please enter text to be translated and select the correct languages.")
      except Exception as e:
          # Handle any other errors that occur during the translation process
          messagebox.showerror("Translation Error", f"Please try again. Error: {e}")
          print("Error occurred:", e)
```

#### Explanation
1. Text Retrieval: The function starts by retrieving the text from the source text box (text1) and stripping any leading or trailing whitespace.
```
  text_ = text1.get(1.0, END).strip()
```

2. Language Selection: It then gets the selected source and target languages from the dropdown menus (combo1 and combo2).
```
  c3 = combo1.get()
  c4 = combo2.get()
```

3. Language Code Lookup: The selected language names are used to look up their corresponding language codes from the language dictionary.
```
  src_lang = language.get(c3, None)
  dest_lang = language.get(c4, None)
```

4. Validation: The function checks if there is text to translate and if the language selections are valid. If any of these checks fail, it shows an error or warning message.
```
  if text_ and src_lang and dest_lang:
    # Proceed with translation
```

5. Translation: If the input is valid, it initializes the Translator object with the source and target languages, then performs the translation.
```
  translator = Translator(from_lang=src_lang, to_lang=dest_lang)
  translated_text = translator.translate(text_)
```

6. Display Translation: If the translation is successful, the translated text is displayed in the target text box (text2). If the translation fails or an error occurs, appropriate error messages are shown.
```
  if translated_text:
    text2.delete(1.0, END)
    text2.insert(END, translated_text)
  else:
    messagebox.showerror("Translation Error", "The translation could not be performed.")
```

## User Interface
The user interface includes dropdown menus for language selection, text boxes for input and output, and a translate button. Additionally, country flags are displayed next to the language selection dropdowns for a better user experience.
