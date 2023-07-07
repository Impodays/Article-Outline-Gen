# Article Generator

The Article Generator is a simple GUI application created with Python and tkinter. It allows the user to input certain parameters and generate a customized outline for a article based on those parameters.

## Installation

First, clone this repository:

#IMPORTANT NOTICE
You need to use own API to use the program. You get API by signing up to openAI. Then you should add API to your working environment. DO NOT SHARE YOUR API WITH ANYONE.

Make sure that you have Python and tkinter installed. 

## Usage

To start the application, simply run:


The user interface has the following inputs:

- `h2 headings, h3 headings, h4 headings`: These are Spinboxes where you input the number of each type of heading you want in the outline.
- `voice tone, writing style, language`: These are Comboboxes where you can select the tone, style, and language of the outline.
- `Blog post title`: This is a Text widget where you can input the title of the article or content.
- `Custom Prompts`: This is a Text widget where you can input any custom prompts for the outline.

Clicking the "Generate" button will generate the outline based on the input parameters. The generated outline will be displayed in the `Post outline` field.

You can then click the "Save" button to save the generated outline as a text file.

## Future Work

The current implementation only generate outline of the article. It uses GPT 3.5 API. Complete article generating function will implement in the future. Also we intent to add API choose function,
so user will be able to choose which API to use (ex gpt 3.5 turbo, gpt 4, gpt 3.5 tubo 16k....)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


